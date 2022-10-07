import json
import time
from datetime import datetime
from typing import List, Optional

from rich import markup
from rich.console import Console
from rich.table import Table

from client.model.rule_catalog_asset_dto import RuleCatalogAssetDto
from client.model.rule_info_dto import RuleInfoDto
from client.model.rule_run_dto import RuleRunDto
from sifflet.constants import (
    OutputType,
    DEFAULT_PAGE_SIZE,
    DEFAULT_PAGE_NUM,
    DEFAULT_TIMEOUT_MINUTES,
    StatusSuccess,
    StatusRunning,
    StatusError,
)
from sifflet.errors import exception_handler, SiffletRuntimeError, SiffletRunRuleFail
from sifflet.logger import logger
from sifflet.rules.api import RulesApi
from sifflet.utils import show_table


class RulesService:
    def __init__(
        self,
        sifflet_config,
        output_type: str = OutputType.TABLE.value,
        page_size=DEFAULT_PAGE_SIZE,
        page_num=DEFAULT_PAGE_NUM,
    ):
        self.api_rules = RulesApi(sifflet_config)
        self.output_type = OutputType(output_type)
        self.page_size = page_size
        self.page_num = page_num

        self.console = Console()

    @exception_handler
    def show_rules(self, filter_name: str):
        """Display rules in a table"""
        rules, total_count = self.api_rules.fetch_rules(filter_name, page_size=self.page_size, page_num=self.page_num)

        if rules:
            rules_cleaned = [
                {
                    "id": rule.get("id"),
                    "name": self._escape_markup(rule.get("name")),
                    "datasource_type": rule.get("datasource_type"),
                    "dataset_name": rule.get("dataset_name"),
                    "platform": rule.get("source_platform"),
                    "last_run_status": self._get_last_run_status(rule),
                    "last_run": self._get_last_run_timestamp(rule),
                }
                for rule in rules
            ]
            if self.output_type == OutputType.TABLE:
                table = Table()
                table.add_column("ID", no_wrap=True)
                table.add_column("Name", no_wrap=True)
                table.add_column("Datasource Type")
                table.add_column("Dataset")
                table.add_column("Platform")
                table.add_column("Last run status", justify="right")
                table.add_column("Last run date")
                for val in rules_cleaned:
                    table.add_row(*val.values())
                self.console.print(table)

                if len(rules) < int(total_count):
                    if self.page_num == 0:
                        self.console.print(f"Showing first {len(rules)} rules out of {total_count} rules")
                    else:
                        self.console.print(f"Showing {len(rules)} rules out of {total_count} rules")
            else:
                self.console.print_json(json.dumps(rules_cleaned))
        elif filter_name:
            logger.info(f"No rule found for search filter: [bold]{filter_name}[/]")
        else:
            logger.info("No rule found")

    @staticmethod
    def _get_last_run_timestamp(rule: RuleCatalogAssetDto) -> str:
        if rule.get("last_run_status") and rule.get("last_run_status").timestamp:
            return str(datetime.fromtimestamp(rule.get("last_run_status").timestamp / 1000))
        else:
            return ""

    def _get_last_run_status(self, rule: RuleCatalogAssetDto) -> str:
        if rule.get("last_run_status") and rule.get("last_run_status").status:
            return self._format_status(rule.get("last_run_status").status)
        else:
            return ""

    @exception_handler
    def run_rules(self, rule_ids: List[str]) -> List[RuleRunDto]:
        rule_runs: List[RuleRunDto] = []
        for rule_id in rule_ids:
            logger.info(f"Triggering rule {rule_id} ...")
            rule_run: RuleRunDto = self.api_rules.run_rule(rule_id)
            rule_runs.append(rule_run)
            logger.info(f"Rule {rule_id} triggered, waiting for result...")
        return rule_runs

    @exception_handler
    def wait_rule_runs(
        self,
        rule_runs: List[RuleRunDto],
        timeout: Optional[int] = 60 * DEFAULT_TIMEOUT_MINUTES,
        wait_time: int = 2,
        error_on_rule_fail: bool = True,
    ):
        start = time.monotonic()
        rule_run_fail: List[RuleRunDto] = []

        for rule_run in rule_runs:
            rule_run_result: RuleRunDto = self._wait_run(
                rule_run=rule_run, timeout=timeout, start=start, wait_time=wait_time
            )
            if rule_run_result.get("status") in StatusSuccess.list():
                logger.info(f"Rule success, id = '{rule_run.rule_id}'")
            else:
                logger.error(
                    f"Rule failed, id = '{rule_run.get('id')}', status = '{rule_run_result.get('status')}',"
                    f" result = '{self._format_result_message(rule_run_result.get('result'))}'",
                    extra={"markup": False},
                )
                rule_run_fail.append(rule_run)

        if rule_run_fail:
            details_fail = [{"id": rf.rule_id, "name": self._build_rule_name(rf.rule_id)} for rf in rule_run_fail]
            if error_on_rule_fail:
                raise SiffletRunRuleFail(f"The following rules are on fail: {details_fail}")
            else:
                logger.error(
                    f"The following rules are on fail: {details_fail}. "
                    f"Mark task SUCCESS as params error_on_rule_fail is False.",
                    extra={"markup": False},
                )

    def _build_rule_name(self, rule_id):
        rule_overview: RuleInfoDto = self.api_rules.info_rule(rule_id=rule_id)
        return (
            f"[{rule_overview.get('datasource_name')}][{rule_overview.get('dataset_name')}]"
            f"{rule_overview.get('name')}"
        )

    @exception_handler
    def _wait_run(self, rule_run: RuleRunDto, timeout=None, start=None, wait_time=None):
        while True:
            if timeout and start + timeout < time.monotonic():
                raise SiffletRuntimeError(f"Timeout: Sifflet rule run {rule_run} not started after {timeout}s")

            time.sleep(wait_time)
            try:
                rule_run_result: RuleRunDto = self.get_status_rule_run(
                    rule_id=rule_run.get("rule_id"), rule_run_id=rule_run.get("id")
                )
            except SiffletRuntimeError as err:
                logger.warning("Retrying... Sifflet API returned an error when waiting for rule run status: %s", err)
                continue

            run_status = rule_run_result.get("status")
            if run_status in StatusRunning.list():
                continue
            if run_status in StatusSuccess.list() or run_status in StatusError.list():
                return rule_run_result
            raise SiffletRuntimeError(
                f"Encountered unexpected status `{rule_run_result.get('status')}` for rule run `{rule_run}`"
            )

    def get_status_rule_run(self, rule_id: str, rule_run_id: str) -> RuleRunDto:
        rule_run_dto: RuleRunDto = self.api_rules.status_rule_run(rule_id=rule_id, run_id=rule_run_id)
        logger.debug(f"Rules status = {rule_run_dto.get('status')}")
        return rule_run_dto

    def show_run_history(self, rule_id: str):
        rule_info: RuleInfoDto = self.api_rules.info_rule(rule_id=rule_id)

        rule_runs, total_count = self.api_rules.rule_runs(rule_id, page_size=self.page_size, page=self.page_num)
        if rule_runs:
            rules_runs_cleaned = [
                {
                    "status": self._format_status(rule_run.get("status", default="")),
                    "start_date": str(datetime.fromtimestamp(rule_run.get("start_date", default=0) / 1000)),
                    "end_date": str(datetime.fromtimestamp(rule_run.get("end_date", default=0) / 1000)),
                    "type": self._escape_markup(rule_run.get("type")),
                    "result": self._escape_markup(rule_run.get("result")),
                }
                for rule_run in rule_runs
            ]
            table_title = (
                f"Rule name: [{rule_info.get('datasource_name')}]"
                f"[{rule_info.get('dataset_name')}]{rule_info.get('name')}"
            )
            if self.output_type == OutputType.TABLE:
                show_table(rules_runs_cleaned, title=table_title)
            else:
                self.console.print(rules_runs_cleaned)
            if len(rule_runs) < int(total_count):
                if self.page_num == 0:
                    self.console.print(f"Showing first {len(rule_runs)} runs out of {total_count} runs")
                else:
                    self.console.print(f"Showing {len(rule_runs)} runs out of {total_count} runs")

    def _escape_markup(self, value: str):
        return markup.escape(value) if self.output_type == OutputType.TABLE else value

    def _format_status(self, status: str) -> str:
        result = status
        if self.output_type == OutputType.TABLE:
            if status in StatusError.__members__:
                result = f"[bold red]{status}[/bold red]"
            elif status in StatusSuccess.__members__:
                result = f"[bold green]{status}[/bold green]"

        return result

    @staticmethod
    def _format_result_message(rule_run_result):
        return str(rule_run_result).strip().replace("\n", " ")
