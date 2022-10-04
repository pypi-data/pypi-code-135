from ruamel.yaml import YAML

def write_config(config_dict, yaml_path):
    with open(yaml_path, "w") as f:
        yaml = YAML()
        yaml.dump(config_dict, f)

def read_config(yaml_path):
    with open(yaml_path, "r") as f:
        yaml = YAML()
        return yaml.load(f)

def get_rtsp(cfg, channel):
    return "rtsp://"\
        f"{cfg['server_ip']}"\
        ":"\
        f"{cfg['port']}"\
        "/user="\
        f"{cfg['user_name']}"\
        "&password="\
        f"{cfg['password']}"\
        "&channel="\
        f"{channel}"\
        "&stream=0"
    
def create_template_config():
    """
    This creates the template for config.yaml.
    """
    yaml_str = '''
# Project path (edit when moving around)
    project_path:

# RTSP url (edit where needed)
    server_ip:
    port: 
    user_name:
    password:
    channels:

# Default directories (do not edit)
    image_recordings:
    logs:
    water_recordings:
    '''
    yaml = YAML()
    cfg = yaml.load(yaml_str)
    return cfg
