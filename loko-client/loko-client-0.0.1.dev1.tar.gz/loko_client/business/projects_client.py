from loko_client.business.base_client import OrchestratorClient
from loko_client.model.projects import Project


class ProjectsClient(OrchestratorClient):

    def all_projects(self):
        r = self.u.projects.get()
        return r.json()

    def get_project(self, id: str):
        r = self.u.projects[id].get()
        return Project(**r.json())

    def running_tasks(self):
        r = self.u.tasks.get()
        return r.json()

    def cancel_all_tasks(self):
        r = self.u.tasks.delete()
        return r.json()

    def cancel_task(self, uid: str):
        r = self.u.tasks[uid].delete()
        return r.json()

    def trigger(self, project_id: str, component_id: str):
        r = self.u.projects[project_id].trigger.post(json=dict(id=component_id))
        return r.json()

    def deploy(self, project_id: str):
        r = self.u.deploy[project_id].get()
        return r.json()

    def undeploy(self, project_id: str):
        r = self.u.undeploy[project_id].get()
        return r.json()


if __name__ == '__main__':
    import time

    tclient = ProjectsClient()
    ### PROJECTS ###
    print(f'ALL PROJECTS: {tclient.all_projects()}')
    print(f'ALL TABS: {tclient.get_project("hello").tabs.all()}')
    nodes_ids = tclient.get_project('hello').tabs.main.nodes.all()
    print(f'ALL NODES: {nodes_ids}')
    res = list(tclient.get_project('hello').tabs.main.nodes.search('data.name', 'HTTP Request'))
    print(f'SEARCH FOR HTTP Request: {res}')
    for node_id in res:
        node = tclient.get_project("hello").tabs.main.nodes[node_id]
        print(node.to_dict())
        print(node.data['name'])
    res = list(tclient.get_project('hello').tabs.main.nodes.search('data.options.values.alias', 'prova'))
    print(f'SEARCH FOR alias=prova: {res}')
    for node_id in res:
        node = tclient.get_project("hello").tabs.main.nodes[node_id]
        print(node.to_dict())
        print(node.data['options']['values']['alias'])
    ### TASKS ###
    running = tclient.running_tasks()
    print(f'RUNNING: {running}')
    if running:
        print(f'CANCEL: project {running[0]["project"]} - tab {running[0]["graph"]} - uid {running[0]["uid"]}')
        print(tclient.cancel_task(uid=running[0]['uid']))
        print(f'RUNNING: {tclient.running_tasks()}')
    time.sleep(1)
    trigger_id = list(tclient.get_project('hello').tabs.main.nodes.search('data.name', 'Trigger'))[0]
    tclient.trigger('hello', trigger_id)
    print(f'RUNNING: {tclient.running_tasks()}')
    print(tclient.undeploy('hello'))