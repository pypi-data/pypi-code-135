from loko_client.business.base_client import OrchestratorClient


class FSClient(OrchestratorClient):

    def ls(self, path: str):
        r = self.u.files[path].get()
        return r.json()['items']

    def read(self, path: str, mode='rb'):
        r = self.u.files[path].get()
        if mode=='rb':
            return r.content
        return r.content.decode()

    def update(self, path: str, body: bytes=None):
        r = self.u.files[path].post(data=body)
        return r.text

    def save(self, path: str, body: bytes=None):
        if body:
            r = self.u.files[path].post(data=body)
        else:
            r = self.u.files[path].post()
        return r.text

    def delete(self, path: str):
        r = self.u.files[path].delete()
        return r.text

    def copy(self, path: str, new_path: str):
        r = self.u.copy[path].post(json=dict(path=new_path))
        return r.text

    def move(self, path: str, new_path: str):
        r = self.u.files[path].patch(json=dict(path=new_path))
        return r.text



if __name__ == '__main__':
    fsclient = FSClient()
    print(fsclient.ls('data/data/datasets'))
    content = fsclient.read('data/data/datasets/titanic.csv', mode='rb')
    print(content.decode())
    ### save file ###
    print(fsclient.save('data/data/test/test.csv', content))
    print(fsclient.save('data/data/test2/test.csv', content))
    ### save dir ###
    print(fsclient.save('data/data/test3'))
    ### delete dir ###
    print(fsclient.delete('data/data/test2/'))
    ### delete file ###
    print(fsclient.delete('data/data/test/test.csv'))
    ### copy file in existing directory ###
    print(fsclient.save('data/data/test3/test.csv', content))
    print(fsclient.copy('data/data/test3/test.csv', 'data/data/test3/test2.csv'))
    ### move file in existing directory ###
    print(fsclient.move('data/data/test3/test.csv', 'data/data/test.csv'))
    ### update ###
    print(fsclient.update('data/data/test.csv', 'hello'.encode()))
