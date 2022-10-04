import requests

class Powerbrain:
    def __init__(self, url, verify_ssl=False):
        self.session = requests.Session()
        self.base_url = url
        self.verify_ssl = verify_ssl
        self.meta = None
    
    def connect(self):
        self.meta = self.session.get(f'{self.base_url}/cnf?cmd=get_params').json()
        self.max_total_evse_power = self.meta['max_total_evse_power']
        self.version = self.meta['version']
        if 'dev_meta' in self.meta:
            self.device_names = self.meta['dev_meta']
        else:
            self.device_names = self.session.get(f'{self.base_url}/cnf?cmd=get_dev_types').json()
    
    def get_dev_info(self, get_raw_response=False):
        response = self.session.get(f'{self.base_url}/cnf?cmd=get_dev_info').json()
        if get_raw_response:
            return response
        devices = {}
        output = {}
        if 'devices' in response:
            for raw_device in response['devices']:
                dev_id = raw_device['dev_id']
                dev_type = raw_device['dev_type']
                raw_device['dev_type_label'] = self.device_names[dev_type]
                # Attach might not be set at all
                if not 'attach' in raw_device:
                    raw_device['attach'] = None
                devices[dev_id] = raw_device
        
        # Link attached devices
        for dev_id in devices:
            attached_id = devices[dev_id]['attach']
            if attached_id is not None:
                if attached_id in devices:
                    devices[dev_id]['attached_device'] = devices[attached_id]
                else:
                    devices[dev_id]['attached_device'] = None
                    devices[dev_id]['attach'] = None
            else:
                devices[dev_id]['attach'] = None
                
        
        # Copy all dict keys except for devices
        for key in response:
            if key != 'devices':
                output[key] = response[key]
        output['devices'] = devices
        
        return output