import os
import yaml
import subprocess
import sys
import re
from .tasks import Tasks

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
            terraform_region = terraform ["region"],
            state_backend_s3_bucket = state_backend ["bucket"],
            state_backend_s3_region = state_backend.get ("region", terraform ["region"]),
            state_backend_s3_key_prefix = state_backend ["key-prefix"],
        )
        feed_data.update (n)

    def generate_tasks (self, current_stage, tag):
        return Tasks (self.d, current_stage, tag)

    def generate_service_declares (self, current_stage, tag):
        out_tfs = {}
        cluster = self.d ["x-ecs-cluster"]
        terraform = self.d ["x-terraform"]
        service = self.d ["x-ecs-service-config"]
        stages = service ["stages"]

        tasks = self.generate_tasks (current_stage, tag)
        out_tfs [f"tasks.json"] = tasks.out_json

        loggings = self.to_tflist (tasks.loggings)
        if tasks.load_balancers:
            load_balancer = "[" + self.to_tfdict (dict (
                name = tasks.load_balancers [0][0],
                port = tasks.load_balancers [0][1]
            )) + "]"
        else:
            load_balancer = "[]"

        workspaces = {}
        for workspace, vars in stages.items ():
            service_stage = vars ["env-service-stage"]
            vars ["service_name"] = service ["name"] + ("" if service_stage == 'production' else ("-" + service_stage))
            vars ["task_definition_name"] = service ["name"] + ("" if service_stage == 'production' else ("-" + service_stage)) + "-task"
            task_definition_name = "ecsdep"
            workspaces [workspace] = self.to_tfdict (vars, 4)
        stages = self.to_tfdict (workspaces)

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