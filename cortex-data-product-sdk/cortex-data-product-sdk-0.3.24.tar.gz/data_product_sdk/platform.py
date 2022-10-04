from data_product_sdk.aws.dynamodb import AwsDynamoDb
from data_product_sdk.databricks.spark import DatabricksSpark
from pyspark.sql import SparkSession
from typing import List


class Platform:
    def __init__(self, table_name: str) -> None:
        self.aws_dynamodb = AwsDynamoDb(table_name=table_name)
        self.databricks_spark = DatabricksSpark()

    def bronze_to_silver(self):
        pass

    def landing_to_bronze(
        self,
        *,
        application_name: str,
        key: str,
        partition_columns: List[str] = None,
        read_options: dict = None,
        spark_session: SparkSession = None,
        write_options: dict = None,
    ):
        schema = self.aws_dynamodb.get_item(key=key)
        if partition_columns is None:
            partition_columns = list()
        if spark_session is None:
            spark_session = self.databricks_spark.get_spark_session(
                application_name=application_name
            )
        data_frame = self.databricks_spark.read_data(
            data_path=schema["data_path"],
            data_type=schema["data_type"],
            read_options=read_options,
            spark_session=spark_session,
        )
        self.databricks_spark.write_table(
            catalog_name=schema["catalog_name"],
            checkpoint_location="",
            data_frame=data_frame,
            database_name=schema["database_name"],
            partition_columns=partition_columns,
            table_name=schema["table_name"],
            write_options=write_options,
        )
        if "table_modifiers" in schema:
            self.databricks_spark.set_table_modifiers(
                catalog_name=schema["catalog_name"],
                database_name=schema["database_name"],
                spark_session=spark_session,
                table_modifiers=schema["table_modifiers"],
                table_name=schema["table_name"],
            )
        if "table_owner" in schema:
            self.databricks_spark.set_table_owner(
                catalog_name=schema["catalog_name"],
                database_name=schema["database_name"],
                spark_session=spark_session,
                table_name=schema["table_name"],
                table_owner=schema["table_owner"],
            )
        if "table_properties" in schema:
            self.databricks_spark.set_properties(
                catalog_name=schema["catalog_name"],
                database_name=schema["database_name"],
                spark_session=spark_session,
                table_name=schema["table_name"],
                table_properties=schema["table_properties"],
            )
        if "table_selectors" in schema:
            self.databricks_spark.set_table_selectors(
                catalog_name=schema["catalog_name"],
                database_name=schema["database_name"],
                spark_session=spark_session,
                table_name=schema["table_name"],
                table_selectors=schema["table_selectors"],
            )

    def silver_to_gold(self):
        pass
