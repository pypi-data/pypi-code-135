import ctypes
import platform
from fnmatch import fnmatch
import importlib
import io
import os
import re
import sys
import textwrap
from jinja2 import Environment,PackageLoader,FileSystemLoader,PrefixLoader
import jinja2
from jinja2 import ext


class PythonExtension(ext.Extension):
    # a set of names that trigger the extension.
    tags = {'py'}

    def __init__(self, environment: Environment):
        super().__init__(environment)

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        body = parser.parse_statements(['name:endpy'], drop_needle=True)
        return jinja2.nodes.CallBlock(self.call_method('_exec_python',
                                                       [jinja2.nodes.ContextReference(),
                                                        jinja2.nodes.DerivedContextReference(),
                                                        jinja2.nodes.Const(lineno),
                                                        jinja2.nodes.Const(parser.filename)]),
                                      [], [], body).set_lineno(lineno)

    def _exec_python(self, ctx, derived_ctx, lineno, filename, caller):
        # Remove access indentation
        # ctx=derived_ctx
        code = textwrap.dedent(caller())
        # Compile the code.
        compiled_code = compile("\n" * (lineno - 1) + code, filename or "string template", "exec")

        # Create string io to capture stdio and replace it.
        # Sometimes one may need to stream stdout to the file
        sout = io.StringIO()
        stdout = sys.stdout
        # sys.stdout = sout
        # print(ctx.parent.keys(), ctx.vars.keys())
        try:
            # print(filename)
            derived_ctx.parent["__name__"]=os.path.basename(filename).split(".")[0]
            derived_ctx.parent["__package__"] = os.path.dirname(filename.replace('\\','/').strip('./').strip('/')).replace('/','.')
            # Execute the code with the derived context parents as global and context vars as locals.
            # print("derived:",derived_ctx.parent.keys(),derived_ctx.vars.keys(),derived_ctx.get_exported().keys())
            # print("ctx:",ctx.parent.keys(),ctx.vars.keys(),ctx.get_exported().keys())
            exec(compiled_code, derived_ctx.parent, ctx.vars) #

            ## Set all variable names as exported vars,
            ctx.exported_vars=set(ctx.vars.keys())
            # print("ctx:", ctx.parent.keys(), ctx.vars.keys(), ctx.get_exported().keys())
        except Exception:
            raise
        finally:
            # Restore stdout whether the code crashed or not.
            sys.stdout = stdout

        # Get a set of all names in the code.
        code_names = set(compiled_code.co_names)

        # The the frame in the jinja generated python code.
        caller_frame = sys._getframe(2)
        var_name_regex = re.compile(r"l_(\d+)_(.+)")
        # Loop through all the locals.
        for local_var_name in caller_frame.f_locals:
            # Look for variables matching the template variable regex.
            match = re.match(var_name_regex, local_var_name)
            if match:
                # Get the variable name.
                var_name = match.group(2)

                # If the variable's name appears in the code and is in the locals.
                if (var_name in code_names) and (var_name in ctx.vars):
                    # Copy the value to the frame's locals.
                    caller_frame.f_locals[local_var_name] = ctx.vars[var_name]
                    # Do some ctypes vodo to make sure the frame locals are actually updated.
                    ctx.exported_vars.add(var_name)
                    ctypes.pythonapi.PyFrame_LocalsToFast(
                        ctypes.py_object(caller_frame),
                        ctypes.c_int(1))

        # Return the captured text.
        return sout.getvalue()


class MyEnvironment(Environment):
    def join_path(self, template, parent):
        template=template.replace('\\','/').replace('//','/')
        if './' in template or '../' in template:
            template=os.path.normpath(os.path.dirname(parent)+"/"+template).replace('\\','/')
            return template
        else:
            return template

def load_yaml(f, **kwargs):
    import yaml
    from importlib import import_module
    g = dict()
    g.update(
        import_module=import_module,
    )
    for func in ['abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr',
                 'classmethod', 'compile', 'complex', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec',
                 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id',
                 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'list', 'locals', 'map', 'max',
                 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'range',
                 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum',
                 'super', 'tuple', 'type', 'vars', 'zip']:
        g[func] = getattr(__builtins__, func)

    class MyUndefined(jinja2.Undefined):
        @classmethod
        def __repr__(self):
            return ""

    Undefined = MyUndefined

    def required(v, name):
        if isinstance(v, Undefined):
            raise jinja2.UndefinedError(name)
        return ""

    g["required"] = required

    singleton_mode=False
    if singleton_mode:
        with open(f, 'r', encoding='utf-8') as f:
            text = f.read()
            text = Environment(extensions=[PythonExtension,
                                           ext.do,
                                           ], undefined=Undefined).from_string(text, globals=g).render(**kwargs)
            return yaml.safe_load(text)
    else:
        # loader = PackageLoader("tasks",".")
        loader = FileSystemLoader(".")
        # print(loader.list_templates())
        f=f.replace('\\','/')
        text = MyEnvironment(loader=loader,extensions=[PythonExtension,
                                ext.do,
                                ], undefined=Undefined).get_template(f,globals=g).render(**kwargs)
        return yaml.safe_load(text)



def load_json(f):
    import json
    with open(f, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_config(arg_file):
    if arg_file.endswith('.yaml') or arg_file.endswith('.yml'):
        cfg = load_yaml(arg_file)
    elif arg_file.endswith('.json'):
        cfg = load_json(arg_file)
    else:
        cfg = load_json(arg_file)
    return cfg


def convert_path_to_module_string(python_file):
    import os
    relpath = os.path.relpath(python_file, os.getcwd())

    def replace_all(s: str, args, target):
        for p in args:
            s = s.replace(p, target)
        return s

    def convert(relpath):
        return replace_all(relpath, ['./', '.\\'], '.').replace('/', '.').replace('\\', '.').replace('.py', '')

    return convert(relpath)


def dict2obj(dic):
    class C:
        pass

    o = C()
    for k, v in dic.items():
        setattr(o, k, v)
    return o


def feed_func(python_file: str, func: str, *config_files: str, as_object=False, **kwargs):
    import sys
    sys.path.append(os.getcwd())
    import importlib
    mod = importlib.import_module(convert_path_to_module_string(python_file))
    params = {}
    for file in config_files:
        params.update(load_config(file))
    params.update(kwargs)
    if as_object:
        return getattr(mod, func)(dict2obj(params))
    else:
        return getattr(mod, func)(**params)


def feed(python_file: str, *config_files: str, **kwargs):
    import sys
    sys.path.append(os.getcwd())
    params = {}
    for file in config_files:
        params.update(load_config(file))
    params.update(kwargs)
    args = []
    for k, v in params.items():
        args.append('--%s=%s' % (k, v))
    args = ' '.join(args)
    os.system(' '.join([sys.executable, python_file, args]))


import os
import time
import threading


class Task:
    def __init__(self, target, name) -> None:
        self.target = target
        self.started = False
        self.finished = False
        self.name = name
        self.on_started = None
        self.on_finished = None

    def set_on_started(self, func):
        self.on_started = func

    def set_on_finished(self, func):
        self.on_finished = func

    def start(self):
        self.started = True
        if self.on_started:
            self.on_started(self)
        start_time = time.time()
        print(("Task %s started." % (self.name)).center(100, "="))
        self.target()
        end_time = time.time()
        print(("Task %s finished. Time used: %.5f" % (self.name, end_time - start_time)).center(100, "="))
        if self.on_finished:
            self.on_finished(self)
        self.finished = True


class BatchTaskRunner:
    def __init__(self, tasks, workers_limit=5, delay=0) -> None:
        self.tasks = tasks
        self.workers_limit = workers_limit
        self.running_workers = 0
        self.delay = delay
        for task in self.tasks:
            assert isinstance(task, Task)
            # task.set_on_started(self.on_task_started)
            task.set_on_finished(self.on_task_finished)

    def on_task_started(self, task: Task):
        self.running_workers += 1

    def on_task_finished(self, task: Task):
        self.running_workers -= 1

    def get_one(self):
        for task in self.tasks:
            if not task.started:
                return task
        return None

    def start_task(self, task):
        self.on_task_started(task)
        thread = threading.Thread(target=task.start)
        thread.start()

    def all_task_finished(self):
        for task in self.tasks:
            if not task.finished:
                return False
        return True

    def exit(self):
        print("All task finished".center(100, "="))

    def run(self):
        while True:
            if self.all_task_finished():
                break
            while self.running_workers < self.workers_limit:
                task = self.get_one()
                if not task:
                    break
                self.start_task(task)
                time.sleep(self.delay)
            time.sleep(5)
        self.exit()


def import_module(python_file):
    import sys
    sys.path.append(os.getcwd())
    import importlib
    mod = importlib.import_module(convert_path_to_module_string(python_file))
    return mod

def get_platform():
    return platform.system().lower()
def generate_env_string(**kwargs):
    if get_platform()=='windows':
        return ' && '.join(['set %s=%s'%(k,v) for k,v in kwargs.items()])+( " && " if len(kwargs) else '')
    else:
        return ' '.join(['%s=%s'%(k,v) for k,v in kwargs.items()])+ ( "  " if len(kwargs) else '')



class Builder:
    @staticmethod
    def build_cmd_task(task:dict, name):
        command = task['command']
        env = task.get('env',{})
        def task():
            os.system(generate_env_string(**env)+command)
        return Task(task, name)

    @staticmethod
    def build_python_task(task:dict, name):
        python_file = task['path']
        args = task.get('args',[])
        kwargs = task.get('kwargs',{})
        func_name= task.get('function',None) or task.get('func',None)
        env=task.get('env',{})
        if func_name:
            module = import_module(python_file)
            func = getattr(module, func_name)
            assert func
            task = lambda: func(*args, **kwargs)
            return Task(task, name)
        else:
            args = ' '.join([str(x) for x in args])
            kwargs_str = []
            for k, v in kwargs.items():
                if isinstance(v, bool):
                    if v:
                        kwargs_str.append('--%s' % (k))
                    else:
                        continue
                else:
                    kwargs_str.append('--%s=%s' % (k, v))
            kwargs = ' '.join(kwargs_str)

            def task():
                os.system(generate_env_string(**env)+f"{sys.executable} {python_file}{' ' + args if args else ''}{' ' + kwargs if kwargs else ''}")
            return Task(task, name)

    @staticmethod
    def build_task(task, name):
        assert isinstance(task, dict)
        task_type = task.get('type', 'python')
        builder_factory = {
            'python': Builder.build_python_task,
            'task-group': Builder.build_task_group,
            'cmd': Builder.build_cmd_task,
        }
        tasks = builder_factory[task_type](task, name)
        if isinstance(tasks, Task):
            tasks = [tasks]
        return tasks

    @staticmethod
    def build_task_group(cfg, name, task_spec=None):
        '''
        task_spec example: 'train-*,test-*'
        '''
        task_dict = cfg.get('tasks')
        # print(task_dict.keys())
        if isinstance(task_dict, (list, tuple, set)):
            task_dict = {str(k): v for k, v in enumerate(task_dict)}
        # print("tasks:",task_dict)
        def search_keys(pattern, candidates):
            if not set([',', '*']).intersection(set(list(pattern))):

                if pattern in candidates:
                    # print(pattern)
                    return [pattern]
                else:
                    return None
            results = []
            if ',' in pattern:
                for p in pattern.split(','):
                    p = p.strip()
                    r = search_keys(p, candidates)
                    if r is not None:
                        results += r
            for cand in candidates:
                if fnmatch(cand, pattern) and not cand in results:
                    results.append(cand)
            return results

        if task_spec:
            keys = search_keys(str(task_spec), list(task_dict.keys()))
            task_dict = {key: task_dict[key] for key in keys}

        task_dict = {f'{name}-{key}': v for key, v in task_dict.items()}
        task_list = []
        for name, t in task_dict.items():
            # print(name)
            task_list += Builder.build_task(t, name)
        return task_list


def run_tasks(config_file, task=None, **kwargs):
    cfg = load_yaml(config_file, **kwargs)
    workers_limit = cfg.get('workers_limit', 1)
    delay = cfg.get('delay', 0)
    tasks = Builder.build_task_group(cfg, cfg.get('name', 'Task'), task)
    BatchTaskRunner(tasks, workers_limit, delay).run()


def job(job_name, *args, **kwargs):
    job_spec = job_name.split('.')
    module = importlib.import_module('.' + job_spec[0], 'jobs')
    job = module
    for spec in job_spec[1:]:
        job = getattr(job, spec)
    job(*args, **kwargs)


class CLI:
    feed_func = staticmethod(feed_func)
    feed = staticmethod(feed)
    tasks = staticmethod(run_tasks)
    run_tasks = staticmethod(run_tasks)

    job = staticmethod(job)


# if __name__ == '__main__':
#     import fire
#
#     fire.Fire(CLI.tasks)
