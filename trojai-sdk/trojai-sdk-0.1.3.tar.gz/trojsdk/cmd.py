from pathlib import Path
import logging
from trojsdk.core.data_utils import load_json_from_disk
from trojsdk.core.client_utils import TrojJobHandler

def submit_config(path_to_config, docker_metadata):
    config = load_json_from_disk(Path(path_to_config))
    logging.info("Config loaded")
    tjh = TrojJobHandler()
    response = tjh.post_job_to_endpoint(config, docker_metadata)
    logging.info("Config posted to endpoint")
    logging.info("Response: " + str(response))

def main():
    import argparse
    parser = argparse.ArgumentParser(prog="trojsdk", description="Troj sdk command line utils")
    parser.add_argument(
        "-config", metavar="-c", type=str, help="Path to the config file"
    )
    parser.add_argument(
        "-test", action="store_true", help="Runs test with TrojAI supplied configs"
    )
    # parser.add_argument(
    #     "-endpoint", metavar="-e", type=str, help="Endpoint to post the config to"
    # )
    # parser.add_argument(
    #     "-jobstatus", metavar="-js", type=str, help="Get status of the specified job"
    # )
    args = parser.parse_args()
    config = None
    if args.test:
        docker_metadata = {
            "docker_image_url": "trojai/troj-engine-base-tabular:b4e7733771d798ce18b6421d009c11fb3a6b5eef",
            "docker_secret_name": "trojaicreds"
        }
        import os
        os.chdir(str(Path(__file__).parent.resolve().parents[0]))

        submit_config("./trojsdk/configs/tabular_test/s3_classification_config.json", docker_metadata)
        print("Test finished")
        exit()


    if args.config is not None:
        config = load_json_from_disk(Path(args.config))
        docker_metadata = {
            "docker_image_url": "trojai/troj-engine-base-tabular:b4e7733771d798ce18b6421d009c11fb3a6b5eef",
            "docker_secret_name": "trojaicreds"
        }
        submit_config(config, docker_metadata)

    else:
        print("No config path supplied")
        print("Exiting")




        

    
    






if __name__ == "__main__":
    main()
    