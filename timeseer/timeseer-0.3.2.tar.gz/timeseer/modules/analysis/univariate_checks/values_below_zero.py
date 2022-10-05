"""This check looks for values < 0, which are unexpected for certain series types.

<p>This check identifies whether there are values < 0 in the given time frame.</p>
<p><img src='../static/images/reporting/limits_lower.svg'></p>
<p class="scoring-explanation">The score of this check is calculated based on the count of all
points where the corresponding value is lower than 0.
Imagine that 100 points are analyzed in a given time-frame
and there are 10 points whose value is lower than 0.
The score for this check in that case would be
90% = 1 - 10 / 100. Which means that 90% of all points lie above 0.</p>
<div class="ts-check-impact">
<p>
Negative values in certain circumstances are an indication of sensor failure. This might mean the
sensor needs to be recalibrated.
</p>
</div>
"""

import pandas as pd

from pandas.api.types import is_string_dtype

from timeseer import AnalysisInput, AnalysisResult, DataType, EventFrame
from timeseer.analysis.utils import (
    event_frames_from_dataframe,
    process_open_intervals,
    handle_open_intervals,
)

_CHECK_NAME = "Values below zero"
_EVENT_FRAME_NAME = "Values below zero"

META = {
    "checks": [
        {
            "name": _CHECK_NAME,
            "event_frames": [_EVENT_FRAME_NAME],
        }
    ],
    "conditions": [
        {
            "min_series": 1,
            "min_data_points": 1,
            "data_type": [DataType.FLOAT32, DataType.FLOAT64],
        }
    ],
    "signature": "univariate",
}


def _get_intervals(outliers, df, event_type):
    outliers = pd.Series(data=outliers, index=df.index).fillna(False)
    outlier_grp = (outliers != outliers.shift().bfill()).cumsum()
    outlier_intervals = (
        df.assign(outlier_grp=outlier_grp)[outliers]
        .reset_index()
        .groupby(["outlier_grp"])
        .agg(start_date=("ts", "first"), end_date=("ts", "last"))
    )
    outlier_intervals["type"] = event_type
    return outlier_intervals


def _get_active_points(df: pd.DataFrame):
    return df["value"] < 0


def _clean_dataframe(df: pd.DataFrame):
    return df[~df.index.duplicated(keep="first")].dropna().sort_index()


def _run_limit_check(
    analysis_input: AnalysisInput,
) -> list[EventFrame]:
    df = analysis_input.data
    df = _clean_dataframe(df)

    active_points = _get_active_points(df)
    intervals = _get_intervals(active_points, df, _EVENT_FRAME_NAME)
    intervals = handle_open_intervals(df, intervals)

    frames = event_frames_from_dataframe(process_open_intervals(intervals))

    return list(frames)


def _is_valid_input(
    analysis_input: AnalysisInput, median_archival_step: list[float]
) -> tuple[str, bool]:
    if median_archival_step is None or len(median_archival_step) == 0:
        return "No median archival step", False
    if len(_clean_dataframe(analysis_input.data)) == 0:
        return "No data", False
    if is_string_dtype(analysis_input.data["value"]):
        return "Can not be a string", False
    return "OK", True


# pylint: disable=missing-function-docstring
def run(analysis_input: AnalysisInput) -> AnalysisResult:
    median_archival_step = [
        statistic.result
        for statistic in analysis_input.statistics
        if statistic.name == "Archival time median"
    ]
    message, is_ok = _is_valid_input(analysis_input, median_archival_step)
    if not is_ok:
        return AnalysisResult(condition_message=message)

    frames = _run_limit_check(analysis_input)
    return AnalysisResult(
        event_frames=frames, last_analyzed_point=analysis_input.data.index[-1]
    )
