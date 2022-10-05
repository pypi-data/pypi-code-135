from trojsdk.client import TrojClient
from trojsdk.core.data_utils import load_json_from_disk
from pathlib import Path
from trojsdk.core.client_utils import TrojJobHandler
import logging


def test_sdk_fail():
    # config = load_json_from_disk(Path("./trojsdk/configs/testing_config.json"))
    config = load_json_from_disk(Path("./trojsdk/configs/s3_test/s3_classification_config.json"))
    
    docker_metadata = {
        "docker_image_url": "trojai/troj-engine-base-tabular:tabular-shawn-latest",
        "docker_secret_name": "trojaicreds"
    }

    tjh = TrojJobHandler()
    response = tjh.post_job_to_endpoint(config, docker_metadata)

    res = tjh.client.get_job_status("invalid-jeb-name2")
    assert res["data"]["status"] == "fail"


def test_sdk_pass_tabular():
    # config = load_json_from_disk(Path("./trojsdk/configs/testing_config.json"))
    config = load_json_from_disk(Path("./trojsdk/configs/s3_test/s3_classification_config.json"))
    
    docker_metadata = {
        "docker_image_url": "trojai/troj-engine-base-tabular:b4e7733771d798ce18b6421d009c11fb3a6b5eef",
        "docker_secret_name": "trojaicreds"
    }

    tjh = TrojJobHandler()
    response = tjh.post_job_to_endpoint(config, docker_metadata)
    import time
    time.sleep(1)
    logging.info("Config posted to endpoint: " + config["auth_config"]["api_endpoint"])
    logging.info("Response: " + str(response))
    print(str(response))

    res2 = tjh.check_job_status(response)
    print(res2)

    assert res2["data"]["status"] == "success"
