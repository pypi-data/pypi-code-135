from data_product_sdk.databricks.checkpoint import DatabricksCheckpoint
from data_product_sdk.databricks.spark import DatabricksSpark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType
from typing import List


class Platform:
    def __init__(self) -> None:
        self.databricks_checkpoint = DatabricksCheckpoint()
        self.databricks_spark = DatabricksSpark()

    def bronze_to_silver(self):
        pass

    def landing_to_bronze(
        self,
        *,
        application_name: str,
        catalog_name: str,
        data_pack_name: str,
        data_path: str,
        database_name: str,
        dataset_name: str,
        data_type: str,
        partition_columns: List[str] = None,
        read_options: dict = None,
        schema: StructType,
        spark_session: SparkSession = None,
        table_name: str,
        write_options: dict = None,
    ):
        if partition_columns is None:
            partition_columns = list()
        if spark_session is None:
            spark_session = self.databricks_spark.get_spark_session(
                application_name=application_name
            )
        data_frame = self.databricks_spark.read_data(
            data_path=data_path,
            data_type=data_type,
            read_options=read_options,
            schema=schema,
            spark_session=spark_session,
        )
        data_frame = self.databricks_spark.rename_invalid_columns(data_frame=data_frame)
        checkpoint_location = self.databricks_checkpoint.get_checkpoint_location(
            bucket_name="",
            data_pack_name=data_pack_name,
            dataset_name=dataset_name,
            table_name=table_name,
        )
        self.databricks_spark.write_table(
            catalog_name=catalog_name,
            checkpoint_location=checkpoint_location,
            data_frame=data_frame,
            database_name=database_name,
            partition_columns=partition_columns,
            table_name=table_name,
            write_options=write_options,
        )
        return data_frame

    def silver_to_gold(self):
        pass
