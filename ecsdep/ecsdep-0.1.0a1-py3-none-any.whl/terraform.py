import os
import yaml
import subprocess
import sys
import json
import re

class AttrDict (dict):
	def __init__(self, *args, **kwargs):
		super(AttrDict, self).__init__(*args, **kwargs)
		self.__dict__ = self

	def delta (self, k, delta = 1):
		self.set (k, self.get (k) + delta)

class Terraform:
    def __init__ (self, data, disable_terrform = False):
        self.disable_terrform = disable_terrform
        self.d = self.render (data)
        self.check_terraform ()

    ENV_RE = re.compile (r"(\$(?:([_a-zA-Z0-9]+)|\{([_a-zA-Z0-9]+)\}))")
    def render (self, data):
        for target, n1, n2 in self.ENV_RE.findall (data):
            value = os.getenv (n1 or n2, "")
            data = data.replace (target, value)
        return yaml.load (data, Loader=yaml.FullLoader)

    def init_terraform (self):
        copy = os.path.expanduser ("~/.ecsdep")
        if not os.path.exists (copy):
            local = os.path.join (os.path.abspath (os.path.join (os.path.dirname (__file__), 'templates')))
            os.symlink (local, copy)
            print ("[INFO] symbolic link created")

        if not os.path.exists (os.path.expanduser ("~/.ecsdep/ecs-cluster/.terraform")):
            self.run_command ("cd ~/.ecsdep/ecs-cluster && terraform init")

    def check_terraform (self):
        assert self.d ["version"][0] == "3", "docker-compose version shoud be over 3"
        assert "x-terraform" in self.d, "root x-terraform required"
        assert self.d ["x-terraform"]["provider"] == "aws", "x-terraform.provider should be aws"
        self.init_terraform ()

    def to_tfdict (self, d, indent = 2):
        s = ["{"]
        for k, v in d.items ():
            k = k.replace ("-", "_")
            if isinstance (v, list):
                v = self.to_tflist (v)
            elif isinstance (v, str):
                if v.find ("\n") == -1:
                    v = repr (v).replace ("'", '"')
            s.append ("{}{} = {}".format (" " * indent * 2, k, v))
        s.append ("%s}" % (" " * indent))
        return "\n".join (s)

    def to_tflist (self, d):
        return str (d).replace ("'", '"')

    def run_command (self, command, use_system = False, ignore_error = None):
        class Result:
            def __init__ (self, returncode):
                self.returncode = returncode
                self.stderr = b''
                self.stdout = b''

        print (f"[RUN] {command}")
        if self.disable_terrform:
            return Result (0)

        cwd = os.getcwd ()
        try:
            if use_system:
                returncode = os.system (command)
                p = Result (returncode)
            else:
                p = subprocess.run (command, capture_output = True, shell = True)
        finally:
            os.chdir (cwd)

        if p.returncode != 0:
            stderr = p.stderr.decode ("utf8")
            exit = True
            if ignore_error:
                for ig in ignore_error:
                    if ig in stderr:
                        # print (f"[IGNORED] {p.returncode}: {command}")
                        exit = False
                        break
            if exit:
                print (stderr)
                print ('─────')
                print (f"[ERROR] Exit with {p.returncode}: {command}")
                sys.exit (p.returncode)
        return p

    def create_cluster (self, dryrun = True):
        self.run_command ("cd /root/.ecsdep/ecs-cluster && terraform plan")
        if not dryrun:
            self.run_command ("cd /root/.ecsdep/ecs-cluster && terraform apply -auto-approve", use_system = True)

    def remove_cluster (self):
        self.run_command ("cd /root/.ecsdep/ecs-cluster && terraform destroy -auto-approve", use_system = True)

    def select_workspace (self, stage):
        stages = self.d ["x-ecs-service-config"]["stages"]
        workspace = None
        for _workspace, vars in stages.items ():
            if vars ["env-service-stage"] == stage:
                workspace = _workspace
        assert workspace, f"workspace not exist"
        self.run_command (
            f"cd /root/.ecsdep/task-def && terraform workspace new {workspace}",
            ignore_error = ["already exists"]
        )
        self.run_command (f"cd /root/.ecsdep/task-def && terraform workspace select {workspace}")

    def deploy_service (self, stage, dryrun = True):
        workspace = self.select_workspace (stage)
        self.run_command ("cd /root/.ecsdep/task-def && terraform plan")
        if not dryrun:
            self.run_command ("cd /root/.ecsdep/task-def && terraform apply -auto-approve", use_system = True)

    def remove_service (self, stage):
        workspace = self.select_workspace (stage)
        self.run_command ("cd /root/.ecsdep/task-def && terraform destroy -auto-approve", use_system = True)

    def set_terraform_vars (self, feed_data):
        terraform = self.d ["x-terraform"]
        state_backend = terraform ["state-backend"]
        n = dict (
            state_backend_s3_bucket = state_backend ["bucket"],
            state_backend_s3_region = state_backend ["region"],
            state_backend_s3_key_prefix = state_backend ["key-prefix"],
            terraform_region = terraform ["region"]
        )
        feed_data.update (n)

    def set_environment (self, task, opts, secrets):
        if "environment" not in opts and not secrets:
            return
        task.environment = []
        task.secrets = []

        if isinstance (opts.environment, list):
            _env = {}
            for ln in opts.environment:
                k, v = ln.split ("=")
                _env [k] = v
        else:
            _env = opts.environment

        for k, v in _env.items ():
            if k in secrets:
                task.secrets.append (dict (name = k, valueFrom = secrets [k]['name']))
            else:
                assert v, f"env {k} is null string"
                task.environment.append (dict (name = k, value = v))

    def set_resources (self, task, opts):
        try:
            reserve_memory = opts.deploy ["resources"]["reservations"]["memory"]
            assert reserve_memory [-1] == "M"
            task.memoryReservation = int (reserve_memory [:-1])
        except KeyError:
            pass

        try:
            limit_memory = opts.deploy ["resources"]["limits"]["memory"]
            assert limit_memory [-1] == "M"
            task.memory = int (limit_memory [:-1])
        except KeyError:
            pass

        try:
            reserve_cpus = opts.deploy ["resources"]["reservations"]["cpus"]
            assert int (reserve_cpus) >= 0
            task.cpu = int (reserve_cpus)
        except KeyError:
            task.cpu = 0

        try:
            reserve_gpus = int (opts.deploy ["resources"]["reservations"]["x-ecs-gpus"])
        except KeyError:
            pass
        else:
            if reserve_gpus:
                task.resourceRequirements = [{"type": "GPU", "value": reserve_gpus}]

    def set_healthcheck (self, task, opts):
        if "healthcheck" not in opts:
            return
        task.healthCheck = {
            "command": opts.healthcheck ["test"]
        }
        if "retries" in opts.healthcheck:
            task.healthCheck ["retries"] = opts.healthcheck ["retries"]
        if "interval" in opts.healthcheck:
            assert opts.healthcheck ["interval"][-1] == "s"
            task.healthCheck ["interval"] = int (opts.healthcheck ["interval"][:-1])

    def set_depends_on (self, task, opts, services):
        task.dependsOn = []
        if "depends_on" not in opts:
            return
        task.links = opts.depends_on
        assert len (opts.depends_on) == len (opts ['x-ecs-wait-conditions'])

        healthycheckers = {}
        for _, _opts in services.items ():
            if "healthcheck" in _opts:
                healthycheckers [_opts ["container_name"]] = True

        for name, condition in zip (opts.depends_on, opts ['x-ecs-wait-conditions']):
            assert condition in ('START', 'HEALTHY', 'COMPLETE', 'SUCCESS')
            if condition == 'HEALTHY':
                assert name in healthycheckers, f"{name} service has not healthcheck"
            task.dependsOn.append ({
                "containerName": name,
                "condition": condition
            })

    def set_port_mapping (self, task, opts, load_balancers):
        task.portMappings = []
        for port in opts ["ports"]:
            protocol = 'tcp'
            published = None
            if isinstance (port, dict):
                target = port.get ("target")
                published = port.get ("published")
                protocol = port.get ("protocol", 'tcp')
            elif isinstance (port, int):
                target = port
            else:
                try:
                    published, target = port.split (":")
                except ValueError:
                    target = port
                target = int (target)

            if published is not None:
                load_balancers.append ((opts.container_name, target))
            task.portMappings.append (dict (containerPort = target, hostPort = 0, protocol = protocol))

    def set_loggings (self, task, opts, loggings, region, cluster_name, service_name, container_name, current_stage):
        service_name_suffix = '' if current_stage == 'production' else ('-' + current_stage)
        if not ("logging" in opts and opts.logging.get ("x-ecs-driver") == "awslogs"):
            return
        loggings.append (container_name)
        task.logConfiguration = {
            "logDriver": "awslogs",
            "options": {
                "awslogs-group": "/ecs/{}/{}{}/{}".format (cluster_name, service_name, service_name_suffix, container_name),
                "awslogs-stream-prefix": "ecs",
                "awslogs-region": "{}".format (region)
            }
        }

    def generate_tasks (self, current_stage, tag):
        terraform = self.d ["x-terraform"]
        services = self.d ["services"]
        secrets = self.d ["secrets"]

        load_balancers = []
        tasks = []
        loggings = []
        for service_name, opts in services.items ():
            opts = AttrDict (opts)
            if "deploy" not in opts:
                continue
            assert service_name == opts.container_name
            task = AttrDict ()

            task.name = opts.container_name
            task.image = opts.image.replace (':latest', '') + f':{tag}'
            task.repositoryCredentials = {"credentialsParameter": opts ['x-ecs-pull_credentials']}
            task.essential = opts.get ("x-ecs-essential", False)
            task.mountPoints = []

            self.set_environment (task, opts, secrets)
            self.set_resources (task, opts)
            self.set_healthcheck (task, opts)
            self.set_depends_on (task, opts, services)
            self.set_port_mapping (task, opts, load_balancers)
            self.set_loggings (task, opts, loggings, terraform ["region"], self.d ["x-ecs-cluster"]['name'], self.d ["x-ecs-service-config"]['name'], opts.container_name, current_stage)

            tasks.append (task)

        with open (os.path.expanduser ("~/.ecsdep/task-def/tasks.json"), "w") as f:
            out_json = json.dumps (tasks, indent = 2)
            f.write (out_json)

        assert len (load_balancers) <= 1
        return out_json, load_balancers, loggings

    def generate_service_declares (self, current_stage, tag):
        out_tfs = {}
        cluster = self.d ["x-ecs-cluster"]
        terraform = self.d ["x-terraform"]
        service = self.d ["x-ecs-service-config"]
        stages = service ["stages"]

        out_json, load_balancer, loggings = self.generate_tasks (current_stage, tag)
        out_tfs [f"tasks.json"] = out_json

        loggings = self.to_tflist (loggings)
        if load_balancer:
            load_balancer = "[" + self.to_tfdict (dict (
                name = load_balancer [0][0],
                port = load_balancer [0][1]
            )) + "]"
        else:
            load_balancer = "[]"

        s = {}
        for workspace, vars in stages.items ():
            service_stage = vars ["env-service-stage"]
            vars ["service_name"] = service ["name"] + ("" if service_stage == 'production' else ("-" + service_stage))
            vars ["task_definition_name"] = service ["name"] + ("" if service_stage == 'production' else ("-" + service_stage)) + "-task"
            task_definition_name = "ecsdep"
            s [workspace] = self.to_tfdict (vars, 4)
        stages = self.to_tfdict (s)

        feed_data = dict (
            cluster_name = cluster ["name"],
            service_name = service ["name"],
            loadbalancing_pathes= self.to_tflist (service.get ("loadbalancing-pathes", ["/*"])),
            awslog_region = terraform ["region"],
            service_auto_scaling = self.to_tfdict (service ["autoscaling"]),
            stages = stages,
            load_balancer = load_balancer,
            loggings = loggings
        )
        self.set_terraform_vars (feed_data)

        with open (os.path.expanduser ("~/.ecsdep/task-def/declares.tfignore")) as f:
            template = f.read ()
            out_tf = template % feed_data

        with open (os.path.expanduser ("~/.ecsdep/task-def/declares.tf"), 'w') as f:
            f.write (out_tf)
            out_tfs [f"declares.tf"] = out_tf
        return out_tfs

    def generate_cluster_declares (self):
        cluster = self.d ["x-ecs-cluster"]
        terraform = self.d ["x-terraform"]
        state_backend = terraform ["state-backend"]
        assert state_backend ["key-prefix"][-1] != "/"

        feed_data = dict (
            cluster_name = cluster ["name"],
            instance_type = cluster ["instance-type"],
            ami = cluster ["ami"],
            s3_cors_hosts = self.to_tflist (cluster ["s3-cors_hosts"]),
            cert_name = cluster ["loadbalancer"]["cert-name"],
            public_key_file = cluster ["public-key_file"],
            cluster_autoscaling = self.to_tfdict (cluster ["autoscaling"]),
            availability_zones = cluster ['availability-zones']
        )
        self.set_terraform_vars (feed_data)
        with open (os.path.expanduser ("~/.ecsdep/ecs-cluster/declares.tfignore")) as f:
            template = f.read ()
            out_tf = template % feed_data
        with open (os.path.expanduser ("~/.ecsdep/ecs-cluster/declares.tf"), 'w') as f:
            f.write (out_tf)

        return out_tf