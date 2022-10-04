from data_product_sdk.databricks.spark import DatabricksSpark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType


class Platform:
    def __init__(self) -> None:
        self.databricks_spark = DatabricksSpark()

    def bronze_to_silver(self):
        pass

    def landing_to_bronze(
        self,
        *,
        application_name: str,
        data_path: str,
        data_type: str,
        read_options: dict = None,
        schema: StructType,
        spark_session: SparkSession = None,
        write_options: dict = None,
    ):
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
        print(data_frame.show())

    def silver_to_gold(self):
        pass
