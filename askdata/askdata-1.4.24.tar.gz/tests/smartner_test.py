from askdata.human2query import smartner, smartner_automated_analysis
import time

if __name__ == "__main__":

    # Prod
    # token = ""
    # datasets = [""]
    # language = "en"
    # env = "prod"

    # Dev
    token = ""
    datasets = [""]
    language = "en"
    env = "dev"

    # Usage
    nl = "price by months"

    start = time.time()
    smartquery_list = smartner(nl=nl, token=token, datasets=datasets, language=language, env=env, use_cache=False,
                               response_type="anonymize")
    end = time.time()
    print("smartNER")
    for sq in smartquery_list:
        print(sq)
        print()

    print("Time: ", end-start, "s")
    print()

    suggestions = [["{{dimension.A}} and {{measure.A}}", {"{{measure.A}}": {"code": "DOWNLOAD", "value": "Download", "dataset": "f2c705dd-f63f-475b-95a9-c1ad20f33716-MYSQL-70c82ef8-2cb2-40dd-a92f-b49a80d0a305"}, "{{dimension.A}}": {"code": "WEB SITE", "value": "Web site", "dataset": "f2c705dd-f63f-475b-95a9-c1ad20f33716-MYSQL-70c82ef8-2cb2-40dd-a92f-b49a80d0a305"}}, ["f2c705dd-f63f-475b-95a9-c1ad20f33716-MYSQL-70c82ef8-2cb2-40dd-a92f-b49a80d0a305"]]]

    start = time.time()
    smartquery_list = smartner_automated_analysis(suggestions, token, env="dev", response_type="deanonymize")
    end = time.time()

    print("Automated analysis")
    for sq in smartquery_list:
        print(sq)
        print()

    print("Time: ", end - start, "s")

