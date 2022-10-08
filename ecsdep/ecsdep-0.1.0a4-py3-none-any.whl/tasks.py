import os
import json

class AttrDict (dict):
	def __init__(self, *args, **kwargs):
		super(AttrDict, self).__init__(*args, **kwargs)
		self.__dict__ = self

	def delta (self, k, delta = 1):
		self.set (k, self.get (k) + delta)


class Tasks:
    def __init__ (self, d, current_stage, tag):
        self.d = d
        self.current_stage = current_stage
        self.tag = tag
        self.out_json = None
        self.load_balancers = []
        self.loggings = []
        self.generate_tasks ()

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

        try:
            devices = opts.deploy ["resources"]["reservations"]["devices"]
        except KeyError:
            pass
        else:
            for device in devices:
                if "gpu" in device.get ("capabilities", []):
                    task.resourceRequirements = [{"type": "GPU", "value": device ["count"]}]

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

    def set_port_mapping (self, task, opts):
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
                self.load_balancers.append ((opts.container_name, target))
            task.portMappings.append (dict (containerPort = target, hostPort = 0, protocol = protocol))

    def set_loggings (self, task, opts, region, cluster_name, service_name, container_name):
        service_name_suffix = '' if self.current_stage == 'production' else ('-' + self.current_stage)
        if not ("logging" in opts and opts.logging.get ("x-ecs-driver") == "awslogs"):
            return
        self.loggings.append (container_name)
        task.logConfiguration = {
            "logDriver": "awslogs",
            "options": {
                "awslogs-group": "/ecs/{}/{}{}/{}".format (cluster_name, service_name, service_name_suffix, container_name),
                "awslogs-stream-prefix": "ecs",
                "awslogs-region": "{}".format (region)
            }
        }

    def generate_tasks (self):
        terraform = self.d ["x-terraform"]
        services = self.d ["services"]
        secrets = self.d ["secrets"]

        tasks = []
        for service_name, opts in services.items ():
            opts = AttrDict (opts)
            if "deploy" not in opts:
                continue
            assert service_name == opts.container_name
            task = AttrDict ()

            task.name = opts.container_name
            task.image = opts.image.replace (':latest', '') + f':{self.tag}'
            task.repositoryCredentials = {"credentialsParameter": opts ['x-ecs-pull_credentials']}
            task.essential = opts.get ("x-ecs-essential", False)
            task.mountPoints = []

            self.set_environment (task, opts, secrets)
            self.set_resources (task, opts)
            self.set_healthcheck (task, opts)
            self.set_depends_on (task, opts, services)
            self.set_port_mapping (task, opts)
            self.set_loggings (task, opts, terraform ["region"], self.d ["x-ecs-cluster"]['name'], self.d ["x-ecs-service-config"]['name'], opts.container_name)

            tasks.append (task)

        with open (os.path.expanduser ("~/.ecsdep/task-def/tasks.json"), "w") as f:
            out_json = json.dumps (tasks, indent = 2)
            f.write (out_json)

        assert len (self.load_balancers) <= 1
        self.out_json = out_json