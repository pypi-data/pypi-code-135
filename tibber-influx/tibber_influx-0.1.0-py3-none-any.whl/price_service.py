from dotenv import load_dotenv
from dataclasses import dataclass
from enum import Enum
from typing import Sequence
import tibber
from influxdb_client.client.influxdb_client_async import InfluxDBClientAsync

load_dotenv()


@dataclass
class Price:
    time: str
    level: str
    total: float
    unit: str


async def fetch_prices(client: tibber.Tibber) -> Sequence[Price]:
    await client.update_info()
    print(client.name)

    home = client.get_homes()[0]
    await home.update_info()
    print(home.address1)

    await home.update_price_info()

    price_info = []
    for t in home.price_total.keys():
        level = home.price_level[t]
        price = home.price_total[t]

        price_info.append(Price(time=t, level=level, total=price, unit=home.price_unit))

    return price_info


async def save_prices(
    prices: Sequence[Price], bucket: str, org: str, client: InfluxDBClientAsync
):
    write_api = client.write_api()

    success = await write_api.write(
        bucket=bucket,
        org=org,
        record=prices,
        record_measurement_name="price_total",
        record_time_key="time",
        record_tag_keys=[""],
        record_field_keys=["total", "level", "unit"],
    )
    print(f" > success: {success}")
