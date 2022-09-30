from ..logger import Logger
from ruamel.yaml import YAML
from pkg_resources import resource_filename
from ..deployment_helper import _execute_script,_check_file_exists

def _get_cluster_name(kubeconfig_path):
    logger = Logger.get_instance()
    try:
        with open(kubeconfig_path,'r') as fp:
            kubeconfig_details = YAML().load(fp)
        return kubeconfig_details['clusters'][0]['name']
    except Exception as e:
        logger.error(e)
        raise


def _ecr_kyma_deploy(databricks_config,databricks_config_path):
    logger = Logger.get_instance()
    try:
        cluster_name=_get_cluster_name(databricks_config['KUBECONFIG_PATH'])
        num_replicas=str(databricks_config['NUM_REPLICAS']) if 'NUM_REPLICAS' in databricks_config else "1"
        ecr_kyma_deploy_script_path = resource_filename(__name__, "ecr_kyma_deploy.sh")
        deploy_result=_execute_script(['bash',ecr_kyma_deploy_script_path,databricks_config["SERVICE_NAME"],databricks_config["PROFILE_NAME"],num_replicas,databricks_config["KUBECONFIG_PATH"],databricks_config["MODEL_URI"],databricks_config_path])
        if deploy_result==0:
            endpoint_url=" https://"+databricks_config['SERVICE_NAME']+"."+cluster_name+"/invocations"
            logger.info("The inference endpoint is:  {}".format(endpoint_url))
            return endpoint_url
        else:
            raise Exception("Deployment to kyma failed. Refer the deployment logs for more details.")

    except Exception as e:
        logger.error(e)
        raise