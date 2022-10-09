import asyncio
import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from time import time
from typing import Sequence, Union

import aioredis
from lxml.html import fromstring
from pyppeteer import launch
from tqdm import tqdm


class TIProWeb:
    def __init__(
        self,
        redis_url: str = "redis://localhost",
        top_lists_file: Union[str, Path] = None,
    ) -> None:
        top_lists_file = (
            Path(top_lists_file)
            if top_lists_file
            else Path(__file__).parent / "top_lists.json"
        )
        self.window_names = json.loads(top_lists_file.read_text())
        self.redis = aioredis.from_url(
            redis_url, encoding="utf-8", decode_responses=True
        )
        self.browser = None
        self.page = None
        self.last_processed_alert = None
        self.today_str = datetime.now().strftime("%Y-%m-%d")

    @classmethod
    async def launch(cls):
        self = cls()
        await self.open_app()
        input("Configure windows and hit enter...")
        return self

    async def run(self):
        while True:
            await self.scrape_top_list()
            await self.scape_alerts()
            asyncio.sleep(1)

    async def open_app(self):
        if self.browser is not None:
            await self.browser.close()
        self.browser = await launch(
            headless=False,
            executablePath="/usr/bin/google-chrome",
            userDataDir="/home/dan/.config/google-chrome/Default",
            args=[
                "--disable-web-security",
                "--no-sandbox",
                "--start-maximized",
            ],
            defaultViewport={},
        )
        pages = await self.browser.pages()
        self.page = pages[0]
        await self.page.goto("https://hadoop.trade-ideas.com/TIProWeb/TIPro.html")
        print("Waiting for sign in...")
        # detect sign in is complete by waiting for path on app page.
        await self.page.waitForXPath('//div[@class="K15MBM-i-b MenuBar"]')
        print("Detected sign in complete.")

    async def scrape_top_list(self):
        root = await self.get_html_parser()
        print("Scraping top lists...")
        for window_name in tqdm(self.window_names):
            window = root.xpath(
                f'//div[@class="K15MBM-s-e"]/div[contains(text(),"{window_name}")]/ancestor::node()[5]/following-sibling::div[@class="K15MBM-n-a"]'
            )
            if not window:
                raise ValueError(f"No window found matching '{window_name}'")
            if len(window) > 1:
                raise ValueError(f"More than one window found matching {window_name}")
            window = window[0]
            column_names = [
                str(e).strip()
                for e in window.xpath(
                    './/div[contains(@class," tigrid-header")]//tbody/tr[@class="K15MBM-gb-h"]/td/div/span/span/text()'
                )
            ]
            # if nothing is at path, that should mean there are no entries in the top list.
            if not column_names:
                print(f"No entries found in window: {window_name}")
                return
            column_names = [c.strip("▲▼ ") for c in column_names]
            symbol_column = self._symbol_column(column_names)
            rows = [
                {
                    column_name: str(value[0])
                    if (value := cell.xpath(".//text()"))
                    else ""
                    for column_name, cell in zip(column_names, row.xpath("./td"))
                }
                for row in window.xpath('.//table[@class="K15MBM-W-f"]/tbody[2]/tr')
            ]
            for row in rows:
                key = f"{self.today_str}::{window_name}-{row[symbol_column]}"
                current = dict(
                    zip(column_names, await self.redis.hmget(key, column_names))
                )
                # update times on top list for existing symbols
                new = {k: v for k, v in row.items() if current[k] != v}
                (
                    time_listed_today,
                    last_list_time_update,
                ) = await self._get_updated_listed_times(key)
                if time_listed_today:
                    new["time_listed_today"] = time_listed_today
                new["last_list_time_update"] = last_list_time_update
                await self.redis.hmset(key, new)
                await self.redis.publish(f"topic::{key}", json.dumps(new))
            # when a symbol is removed from the window, remove last list time update field and set last increment for total day listed time.
            current_symbols = {row[symbol_column] for row in rows}
            last_symbols_key = f"{window_name}-latest-symbols"
            if last_symbols := await self.redis.get(last_symbols_key):
                last_symbols = json.loads(last_symbols)
                removed_symbols = {s for s in last_symbols if s not in current_symbols}
                print(
                    f"{len(removed_symbols)} symbols removed from window {window_name}"
                )
                for symbol in removed_symbols:
                    key = f"{self.today_str}::{window_name}-{symbol}"
                    time_listed_today, _ = await self._get_updated_listed_times(key)
                    await self.redis.hmset(
                        key,
                        {
                            "time_listed_today": time_listed_today,
                            "last_list_time_update": "",
                        },
                    )
            await self.redis.set(last_symbols_key, json.dumps(list(current_symbols)))

    async def scape_alerts(self):
        is_pm = (now := datetime.now()).hour >= 12
        root = await self.get_html_parser()
        symbol_alert_counts = defaultdict(dict)
        last_processed_alert = self.last_processed_alert
        for idx, row in enumerate(
            root.xpath('//tr[contains(@class," alert_rows_1_neutral")]')
        ):
            cells = row.xpath("./td/div")
            alert_time = str(cells[0].xpath(".//text()")[0])
            hour, minute = alert_time.split(":")
            hour, minute = int(hour), int(minute)
            # once we scroll through all the PM alerts, is_pm should be set False. (alerts are time ordered newest to oldest)
            if is_pm := (is_pm and hour <= 12):
                hour += 12
            alert_time = now.replace(hour=hour, minute=minute)
            if idx == 0:
                self.last_processed_alert = alert_time
            if last_processed_alert and alert_time <= last_processed_alert:
                break
            alert_type = Path(
                str(
                    cells[1].xpath(
                        './/img[contains(@src,"https://secure.trade-ideas.com/static/Alerts")]/@src'
                    )
                )
            ).stem
            symbol = str(cells[2].xpath(".//text()")[0])
            alert_count = int(
                str(cells[-1].xpath(".//text()")[0])
                .replace(",", "")
                .replace("K", "000")
                .replace("M", "000000")
            )
            key = f"{self.today_str}::{symbol}-alert-counts"
            prev_alert_count = await self.redis.hget(key, alert_type)
            if not prev_alert_count or alert_count > int(prev_alert_count):
                symbol_alert_counts[symbol][alert_type] = alert_count
                await self.redis.hset(key, alert_type, alert_count)
        if symbol_alert_counts:
            print(f"New alerts for {len(symbol_alert_counts)} symbols.")
            await self.redis.publish(
                "topic::alert-counts", json.dumps(symbol_alert_counts)
            )

    async def get_html_parser(self):
        """Parse the static HTML.
        The DOM is constantly updating, so we need to parse a static snapshot of the HTML rather than work in the DOM directly."""
        html = await self.page.content()
        return fromstring(html)

    async def shutdown(self):
        await self.browser.close()

    async def _get_updated_listed_times(self, key: str):
        last_list_time_update, time_listed_today = await self.redis.hmget(
            key, ["last_list_time_update", "time_listed_today"]
        )
        time_listed_today = time_listed_today or 0
        now = time()
        if last_list_time_update:
            time_listed_today += now - last_list_time_update
        return time_listed_today, now

    def _symbol_column(self, column_names: Sequence[str]):
        for c in ("Symbol", "Sym"):
            if c in column_names:
                return c
        raise ValueError(f"Symbol column not found: {column_names}")


async def run():
    ti = TIProWeb()
    await ti.launch()
    await ti.run()


def run_cmd():
    asyncio.run(run())
