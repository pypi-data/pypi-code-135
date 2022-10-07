def API_factory(service_type):
    if service_type == 'graph':
        from . microsoft.GraphAPI import GraphAPI
        return GraphAPI()
    if service_type == 'azure':
        from . microsoft.AzureAPI import AzureAPI

