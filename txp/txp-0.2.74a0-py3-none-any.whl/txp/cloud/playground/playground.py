# import json
# from google.oauth2 import service_account
# import google.cloud.firestore as firestore
# from google.cloud import bigquery
# from txp.common.utils import firestore_utils
# import datetime
# from txp.common.utils import reports_utils, bigquery_utils
#
# credentials_path = "../../common/credentials/pub_sub_to_bigquery_credentials.json"
# with open(credentials_path, 'r') as file:
#     credentials_str = file.read().replace('\n', '')
#
# json_dict_service_account = json.loads(credentials_str, strict=False)
# credentials = service_account.Credentials.from_service_account_info(json_dict_service_account)
# firestore_db = firestore.Client(credentials=credentials, project=credentials.project_id)
# bigquery_db = bigquery.Client(credentials=credentials, project=credentials.project_id)
#
# w = reports_utils.get_available_reports(firestore_db, bigquery_db, "tranxpert-mvp.reports_test.sections",
#                                       "labshowroom-001",
#                                       datetime.datetime.strptime("2022-08-15 18:00:00.0+0000",
#                                                                  '%Y-%m-%d %H:%M:%S.%f%z'))
#
# print(w)
#


#bigquery_utils.get_last_task_prediction_for_asset("labshowroom-001", "ml_events_and_states.states", "Showroom_Fridge", 10, bigquery_db)


#
# transitions_path = "./transitions_states.json"
# with open(transitions_path, 'r') as file:
#     transitions = file.read().replace('\n', '')
# transitions = json.loads(transitions, strict=False)
#
#
# bigquery_db.insert_rows_json("tranxpert-mvp.reports_test.sections", [transitions])
#
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../../common/credentials/pub_sub_to_bigquery_credentials.json"
from google.api_core.exceptions import AlreadyExists
from google.cloud.pubsublite import AdminClient, Topic
from google.cloud.pubsublite.types import (
    CloudRegion,
    CloudZone,
    ReservationPath,
    TopicPath,
)
from google.protobuf.duration_pb2 import Duration

project_number = 977520001763
cloud_region = "us-west4"
zone_id = "a"
topic_id = "test-topic"
reservation_id = "test-reservation"
num_partitions = 1
regional = True

cloud_region = CloudRegion(cloud_region)
reservation_path = ReservationPath(project_number, cloud_region, reservation_id)

topic_path = None
if regional:
    #  A regional topic.
    topic_path = TopicPath(project_number, cloud_region, topic_id)
else:
    #  A zonal topic
    topic_path = TopicPath(
        project_number, CloudZone(cloud_region, zone_id), topic_id
    )

topic = Topic(
    name=str(topic_path),
    partition_config=Topic.PartitionConfig(
        # A topic must have at least one partition.
        count=num_partitions,
        # Set throughput capacity per partition in MiB/s.
        capacity=Topic.PartitionConfig.Capacity(
            # Set publish throughput capacity per partition to 4 MiB/s. Must be >= 4 and <= 16.
            publish_mib_per_sec=4,
            # Set subscribe throughput capacity per partition to 4 MiB/s. Must be >= 4 and <= 32.
            subscribe_mib_per_sec=8,
        ),
    ),
    retention_config=Topic.RetentionConfig(
        # Set storage per partition to 30 GiB. This must be in the range 30 GiB-10TiB.
        # If the number of byptes stored in any of the topic's partitions grows beyond
        # this value, older messages will be dropped to make room for newer ones,
        # regardless of the value of `period`.
        per_partition_bytes=30 * 1024 * 1024 * 1024,
        # Allow messages to be retained for 7 days.
        period=Duration(seconds=60 * 60 * 24 * 7),
    ),
    reservation_config=Topic.ReservationConfig(
        throughput_reservation=str(reservation_path),
    ),
)

client = AdminClient(cloud_region)
try:
    response = client.create_topic(topic)
    if regional:
        print(f"{response.name} (regional topic) created successfully.")
    else:
        print(f"{response.name} (zonal topic) created successfully.")
except AlreadyExists:
    print(f"{topic_path} already exists.")
