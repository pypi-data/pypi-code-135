# Mobile Verification Toolkit (MVT)
# Copyright (c) 2021-2022 Claudio Guarnieri.
# Use of this software is governed by the MVT License 1.1 that can be found at
#   https://license.mvt.re/1.1/

import logging
from typing import Optional

from mvt.android.parsers import parse_dumpsys_battery_history

from .base import BugReportModule


class BatteryHistory(BugReportModule):
    """This module extracts records from battery daily updates."""

    def __init__(
        self,
        file_path: Optional[str] = None,
        target_path: Optional[str] = None,
        results_path: Optional[str] = None,
        fast_mode: Optional[bool] = False,
        log: logging.Logger = logging.getLogger(__name__),
        results: Optional[list] = None
    ) -> None:
        super().__init__(file_path=file_path, target_path=target_path,
                         results_path=results_path, fast_mode=fast_mode,
                         log=log, results=results)

    def check_indicators(self) -> None:
        if not self.indicators:
            return

        for result in self.results:
            ioc = self.indicators.check_app_id(result["package_name"])
            if ioc:
                result["matched_indicator"] = ioc
                self.detected.append(result)
                continue

    def run(self) -> None:
        content = self._get_dumpstate_file()
        if not content:
            self.log.error("Unable to find dumpstate file. "
                           "Did you provide a valid bug report archive?")
            return

        lines = []
        in_history = False
        for line in content.decode(errors="ignore").splitlines():
            if line.strip().startswith("Battery History "):
                lines.append(line)
                in_history = True
                continue

            if not in_history:
                continue

            if line.strip() == "":
                break

            lines.append(line)

        self.results = parse_dumpsys_battery_history("\n".join(lines))

        self.log.info("Extracted a total of %d battery history records",
                      len(self.results))
