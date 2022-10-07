class BaseAPI:
    '''
    Each manufacturer's API offers different methods. In order to
    know which methods are available at execution time, dictionaries
    of available API calls must be offered by the "methods" variable.
    For example:

    >> obj.methods

    [
        {
            'method_name': 'get_user_data',
            'method': self.get_user_data,
            'format': 'json'
        },
        {
            'method_name': 'get_usage_report',
            'method': self.get_usage_report,
            'format': 'csv'
        }
    ]
    
    the "self.methods" class variable must list all the methods which
    retrieve data fom API calls, as well as their return format. Its
    format is as follows:
    [
        {
            'method_name': <method name as string>,
            'method': <pointer to method>,
            'format': <format as string>
        }
        ...
    ]

    the "methods" variable must be instanced within a bound method,
    so that each entry may be properly bound and thus, callable.
    '''
    def methods(self):
        pass

    '''
    The "required_info" variable holds a list of data needed
    for connection. This list contains tuples representing the
    information's name and its type, respectively. For example:

    >> obj.required_info

    [
        ("username", "str"),
        ("password", "str"),
        ("id", "int")
    ]

    After a call to required_info yields this data, the object's
    user knows how to properly call the connect method:

    obj.connect(username="some_username",
                password="some_password",
                id=42)
    '''
    required_info = []


    def connect(self, **kwargs):
        '''
        The "connect" method is responsible for authenticating the API
        and should be implemented accordingly for each specific
        manufacturer. Arguments must be the data required for 
        authentication i.e. credentials or key files. The authentication
        process' result should be stored withing the object, so that
        ideally each object stays authenticated as long as it exists.
        '''
        pass


