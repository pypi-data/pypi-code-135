from . import crawler_processor_pb2_grpc as importStub

class ProcessorService(object):

    def __init__(self, router):
        self.connector = router.get_connection(ProcessorService, importStub.ProcessorStub)

    def ProcessMessage(self, request, timeout=None, properties=None):
        return self.connector.create_request('ProcessMessage', request, timeout, properties)