import asyncio
import os
from dotenv import load_dotenv
from influxdb_client.client.influxdb_client_async import InfluxDBClientAsync
from price_service import fetch_prices, save_prices
import tibber

load_dotenv()

TIBBER_TOKEN = os.getenv("TIBBER_TOKEN")

INFLUX_BUCKET = "tibber"
INFLUX_ORG = os.getEnv("INFLUX_ORG")
INFLUX_TOKEN = os.getenv("INFLUX_TOKEN")
INFLUX_URL = os.getenv("INFLUX_URL")


async def main():

    tibber_client = tibber.Tibber(TIBBER_TOKEN)
    prices = await fetch_prices(tibber_client)
    await tibber_client.close_connection()

    async with InfluxDBClientAsync(
        url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG
    ) as influx_client:
        await save_prices(
            prices, client=influx_client, bucket=INFLUX_BUCKET, org=INFLUX_ORG
        )


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
