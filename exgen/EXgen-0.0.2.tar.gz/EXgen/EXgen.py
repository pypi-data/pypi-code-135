import os 
from typing import Callable, Dict, Any, List
import EXgen.util.expression_handler as eh
import yaml
import shutil
import re

######## CONST DEFS #########

TASK_SPLIT_TOKEN = "%END-PART"
EX_GROUP_TOKEN = "INSERT-GROUP"
EX_NUM_TOKEN = "INSERT-EX-NUM"
EX_NAME_TOKEN = "INSERT-EX-NAME"
TASKS_TOKEN = "INSERT-TASKS"
FIG_INSERT_TOKEN = "FIGPATH"
SOLUTION_TOKEN = "INSERT-SOLUTION"
TOKEN_PREFIX_LEN = len("INSERT-")

TASK_KEYS_LIST = ["netlist", 
                  "var_defs",
                  "solution_gen_type"]

#############################
######## EXgen class ########

class EXgen:
    def __init__(self, setup_file: str) -> None:
        
        # get setup info : 
        self.meta_data = self._read_yaml(setup_file)
        
        # initialize variables : 
        self._init_vars()

        # initialize function maps : 
        self._init_solution_gen_map()
        self._init_units_map()
        self._init_lcapy_maps()

        # initialize paths and dirs :
        self._init_paths_and_dirs()

        # initialize tex templates : 
        self._init_tex_templates()

        # make task list containing tasks : 
        self._make_tasks_list()


    def _init_vars(self) -> None:
        
        self.course = self.meta_data["course"]
        self.session_id = str(self.meta_data["session_id"])
        self.session = self.meta_data["session_name"]
        self.groups = self.meta_data["groups"]
        self.n_tasks = self.meta_data["n_tasks"]
        self.fig_dir_path = self.meta_data["figure_path"]
        self.generate_solution_files = self.meta_data["generate_solution_files"]

        self.templates_figures_dir = __file__[:-8] + "templates/figures/"
        self.main_tex_template_file = self.meta_data["template"] + "_template.tex"
        self.template_file = __file__[:-8] + "templates/" + self.main_tex_template_file
        self.tasks_tex_template_file = self.meta_data["tasks_template"]

    def _init_paths_and_dirs(self) -> None:
        
        if not os.path.exists(self.fig_dir_path):
            os.mkdir(self.fig_dir_path)

    def _init_units_map(self) -> None:
        self.units_map = {'U': 'V', 'V': 'V', 
                          'I': 'A', 
                          'R': '\Omega'}

    def _init_lcapy_maps(self) -> None:
        self.lcapy_symbol_map = {'U': 'V', 
                                 'R': 'R',
                                 'I': 'I',
                                 'C': 'C',
                                 'L': 'L'}

    def _init_solution_gen_map(self) -> None:
        self.solution_gen_map = {"list-results": self._list_results_tex,}

    def _make_tasks_list(self) -> None:

        self.tasks = []

        for i_task in range(self.n_tasks):
            task_keys = [key + f"_t{i_task+1}" for key in TASK_KEYS_LIST]
            self.tasks.append({key[:-3]:self.meta_data[key] for key in task_keys})

            self.tasks[i_task]["inserts"] = self._get_inserts_for_task(i_task)
            self.tasks[i_task]["solution_gen_fun"] = self.solution_gen_map[self.tasks[i_task]["solution_gen_type"]]
            
            self.tasks[i_task]["schematic_path"] = self._get_schematic_path(self.tasks[i_task]["inserts"])
            
    def _get_schematic_path(self, inserts: Dict[str, str]) -> str:
        
        for key, val in inserts.items():
            if FIG_INSERT_TOKEN in key:
                return val

    def _get_inserts_for_task(self, i_task: int) -> Dict[str, str]:
        
        inserts_list = re.findall("(INSERT-[\w.-]*)\s", self.tasks_tex_list[i_task])

        return {key: self._get_insert_value(key) for key in inserts_list}

    def _get_insert_value(self, key: str) -> str:
        
        key_part = key.split('-')[1] 

        if FIG_INSERT_TOKEN in key_part:
            key_out = f"{self.fig_dir_path}/figure_{key_part[len(FIG_INSERT_TOKEN):]}.pdf"
        elif SOLUTION_TOKEN in key:
            key_out = SOLUTION_TOKEN[TOKEN_PREFIX_LEN:]
        else:
            key_out = self.lcapy_symbol_map[key_part[0]] + key_part[1:]

        return key_out

    def _generate_document_for_group(self, group: str) -> None:

        # fill template with meta data 
        tex_content = self._fill_meta_data(group)
        tex_tasks = ''
        tex_solved_tasks = ''

        # add tasks : 
        for i_task, task in enumerate(self.tasks):
            
            # solve task and get results : 
            task["result"] = eh.solve(task, draw=True)

            task["result"][SOLUTION_TOKEN[TOKEN_PREFIX_LEN:]] = task["solution_gen_fun"](task)

            # write task to template : 
            tex_task, tex_solved_task = self._write_task(task, i_task)

            tex_tasks += tex_task
            tex_solved_tasks += tex_solved_task

        tex_tasks = self._update_if_biomed(tex_tasks, group)
        tex_solved_tasks = self._update_if_biomed(tex_solved_tasks, group)

        tex_content_tasks = tex_content.replace(TASKS_TOKEN, tex_tasks)
        tex_content_solution = tex_content.replace(TASKS_TOKEN, tex_solved_tasks)

        self._tex_to_pdf(tex_content_tasks, group, clean=True)
    
        if self.generate_solution_files:
            self._tex_to_pdf(tex_content_solution, group, clean=True, is_solution=True)

    
    def generate(self) -> None:

        for group in self.groups:
            self._generate_document_for_group(group)

        self._clean_templates()

    #####################################
    ######## Tex - functions : ##########

    def _init_tex_templates(self) -> None:

        shutil.copytree(self.templates_figures_dir, "./figures/", symlinks=False, ignore=None, copy_function=shutil.copy2, ignore_dangling_symlinks=False, dirs_exist_ok=True)
        shutil.copy(self.template_file, "./")

        self.main_tex = self._read_tex(self.main_tex_template_file)
        self.tasks_tex_list = self._read_tex(self.tasks_tex_template_file).split(TASK_SPLIT_TOKEN)

    def _fill_meta_data(self, group: str) -> str:

        tex_str = self.main_tex

        tex_str = tex_str.replace(EX_GROUP_TOKEN, group)
        tex_str = tex_str.replace(EX_NUM_TOKEN, self.session_id)
        tex_str = tex_str.replace(EX_NAME_TOKEN, self.session)

        return tex_str

    def _write_task(self, task: Dict[str, Any], i_task: int) -> str:
        
        tex_task = self.tasks_tex_list[i_task]
        tex_task_solution = self.tasks_tex_list[i_task]

        corrected_res_keys = [x.replace('V', 'U') for x in task["result"].keys()]
        corrected_res_keys.remove(SOLUTION_TOKEN[TOKEN_PREFIX_LEN:])

        for key, val in task["inserts"].items():

            if key[TOKEN_PREFIX_LEN:] in corrected_res_keys:
                tex_task = tex_task.replace(key, str(task["result"][val]))
            elif FIG_INSERT_TOKEN in key:
                tex_task = tex_task.replace(key, val)

        solution_key = task["inserts"][SOLUTION_TOKEN]
        tex_task_solution = tex_task.replace(SOLUTION_TOKEN, task["result"][solution_key])
        tex_task = tex_task.replace(SOLUTION_TOKEN, '')

        return tex_task, tex_task_solution        

    def _tex_to_pdf(self, tex_content: str, group: str, clean: bool=False, is_solution: bool=False) -> None:
        
        ext = "_solution" if is_solution else ''

        tex_filename = self.course.replace(' ', '_') + '_' + self.session_id + f"_{group}{ext}.tex"
        fid = open(tex_filename, 'w') 
        fid.write(tex_content)
        fid.close()

        os.system(f"pdflatex {tex_filename}")

        if clean:
            os.remove(f"{tex_filename[:-4]}.aux")
            os.remove(f"{tex_filename[:-4]}.log")
            os.remove(f"{tex_filename[:-4]}.tex")

    def _list_results_tex(self, task: Dict[str, Any]) -> str:
        template = "Solution : \\ \n \\begin{itemize}\n INSERT \n \end{itemize}"

        items = ''
        for key, val in task["result"].items():
            unit_id = key.replace("V", "U")
            items += "\item $" + unit_id[0] + "_{" + unit_id[1:] + "} = " + str(val) + ' ' + self.units_map[key[0]] + "$ \n"

        return template.replace("INSERT", items)

    def _update_if_biomed(self, tex: str, group: str) -> str:
        
        if "BME" in group:
            tex = tex.replace("%INSERT-BME", '')
        else : 
            tex = tex.replace("%INSERT-NOTBME", '')

        return tex
    #####################################
    ######## Utility functions ##########

    def _clean_templates(self) -> None:
        shutil.rmtree("./figures/")
        shutil.rmtree(self.fig_dir_path )
        os.remove(self.main_tex_template_file)

    def _read_tex(self, fname: str) -> str:
        
        fid = open(fname)
        contents = fid.read()
        fid.close()

        return contents

    def _read_yaml(self, fpath: str) -> Dict[str, Any]:
    
        with open(fpath) as f:
            contents = yaml.load(f, Loader=yaml.FullLoader)

        return contents
    
    #####################################

# def main() -> None:
#     myGen = EXgen("UE1_config.yaml")
#     myGen.generate()
#     print("finished")

# if __name__ == "__main__":
#     main()
    