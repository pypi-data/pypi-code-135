import argparse
from pyspark.sql import SparkSession

def run():
    parser = argparse.ArgumentParser(description='Stage data for fast ingest.')
    parser.add_argument('--compression_format', required=False)
    parser.add_argument('--data_format', required=False)
    parser.add_argument('--sql_query', required=False)
    parser.add_argument('--stage_destination_uri', required=False)

    parser.add_argument('--csv_delimiter', required=False, default="\x1e")
    parser.add_argument('--csv_null_value', required=False, default='_SISU_NULL')

    # For GCP Cloud Storage.
    parser.add_argument('--service_account_private_key_id', required=False)
    parser.add_argument('--service_account_email', required=False)
    parser.add_argument('--service_account_private_key', required=False)

    # For AWS S3.
    parser.add_argument('--access_key_id', required=False)
    parser.add_argument('--secret_access_key', required=False)

    # Deprecated; to be removed in future version.
    parser.add_argument('--stage_output_bucket', required=False)
    parser.add_argument('--stage_output_prefix', required=False)

    args = parser.parse_args()

    spark = SparkSession.builder.getOrCreate()

    # Deprecated; to be removed in future version.
    if args.stage_output_bucket is not None:
        df = spark.sql(f"""{args.sql_query}""")
        df.write \
            .format("csv") \
            .option("compression", "gzip") \
            .option("nullValue", "_SISU_NULL") \
            .option("delimiter", "\x1e") \
            .mode("overwrite") \
            .save(f"s3a://{args.access_key_id}:{args.secret_access_key}@{args.stage_output_bucket}/{args.stage_output_prefix}")
        return

    url = args.stage_destination_uri

    # AWS S3.
    if args.access_key_id and args.secret_access_key:
        if not url.startswith("s3:"):
            raise ValueError(f"invalid S3 url: {url}")
        url = "s3a:" + url[3:]

        existing_email = spark.conf.get("fs.s3a.access.key", None)
        if existing_email:
            raise ValueError("ERROR")

        # Set job-scoped configuration.
        spark.conf.set("fs.s3a.access.key", args.access_key_id)
        spark.conf.set("fs.s3a.secret.key", args.secret_access_key)

    # GCP Cloud Storage.
    elif args.service_account_private_key_id and \
            args.service_account_private_key and \
            args.service_account_email:

        # Set job-scoped configuration.
        spark.conf.set("fs.gs.auth.service.account.private.key.id", args.service_account_private_key_id)
        spark.conf.set("fs.gs.auth.service.account.email", args.service_account_email)
        spark.conf.set("fs.gs.auth.service.account.private.key", args.service_account_private_key)

    else:
        raise ValueError(f"invalid credentials configuration for url: {url}")

    df = spark.sql(f"""{args.sql_query}""")
    df.write \
        .format(args.data_format) \
        .option("compression", args.compression_format) \
        .option("delimiter", args.csv_delimiter) \
        .option("nullValue", args.csv_null_value) \
        .mode("overwrite") \
        .save(url)
