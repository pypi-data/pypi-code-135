class Movie:

    def __init__(self, did_sdk, base_url, location, **kwargs):
        """
        Initialize 
        """
        super(Movie, self)
        self.did_sdk = did_sdk
        self.base_url = base_url

     
        self.location = location
    
    def get(self, params=None, data=None,object_type = "movie", object_id=None, headers=None, auth=None, profile_id=None, domain_id=None, domain_action=None):
        return self.did_sdk.request(
            'get',
            self.base_url,
            object_type,
            object_id,     
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            profile_id=profile_id,
            domain_id=domain_id,
            domain_action=domain_action
        )
        
