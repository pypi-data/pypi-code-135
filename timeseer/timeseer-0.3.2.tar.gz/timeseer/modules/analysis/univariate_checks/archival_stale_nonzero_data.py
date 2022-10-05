"""There is no change in the non-zero data for a period longer than expected based on history.

<p> This check identifies periods time where the
exact same value has been consistently recorded for a sensor. These could be indications of issues with
connectivity or offline sensors.</p>
<p><img src='../static/images/reporting/stale_data.svg'></p>
<p class="scoring-explanation">The score for this check is based on the total amount of time
where there seems to be staleness relative to the total time range of the analysis.</p>
<div class="ts-check-impact">
<p>
A series that does not put out any new measurements might be faulty or could indicate a network failure.
Failing to detect this could lead to wrong process operation when attempting to obtain a particular
interval of operation.
</p>
</div>
"""

from datetime import datetime, timedelta

import jsonpickle
import numpy as np
import pandas as pd

from timeseer import AnalysisInput, AnalysisResult, EventFrame, ModuleParameterType

from timeseer.analysis.utils import (
    event_frames_from_dataframe,
    process_open_intervals,
    handle_open_intervals,
    get_cutoff_for_sketch,
)

_CHECK_NAME = "Stale non-zero data (distribution)"

META = {
    "checks": [
        {
            "name": _CHECK_NAME,
            "event_frames": [_CHECK_NAME],
        }
    ],
    "conditions": [
        {
            "min_series": 1,
            "min_weeks": 3,
            "min_data_points": 2,
        }
    ],
    "parameters": [
        {
            "name": "percentile",
            "type": ModuleParameterType.FLOAT64,
            "range": {
                "lower": 0,
                "upper": 1,
            },
            "default": 0.75,
            "helpText": "Percentile sets the upper limit of the range for calculating the IQR for stale non-zero data.",
        },
        {
            "name": "scale",
            "type": ModuleParameterType.FLOAT64,
            "range": {
                "lower": 0,
            },
            "default": 3,
            "helpText": "Scale sets the factor for considering a non-zero stale data frame an anomaly.",
        },
    ],
    "signature": "univariate",
}


def _get_last_analyzed_point(df, intervals):
    if len(intervals) == 0:
        return df.index[-1]

    if intervals.iloc[-1]["end_date"] < df.index[-1]:
        return intervals.iloc[-1]["end_date"]

    return intervals.iloc[-1]["start_date"]


def _is_frame_long_enough(frame, df, delta):
    end_date = frame.end_date
    if frame.end_date is None:
        end_date = df.index[-1]

    return (
        end_date.replace(tzinfo=None) - frame.start_date.replace(tzinfo=None)
    ) > timedelta(seconds=delta)


def _filter_stale_event_frames(all_frames, df, delta):
    filter_iterator = filter(lambda x: _is_frame_long_enough(x, df, delta), all_frames)
    return filter_iterator


def _get_intervals(active_points, df, event_type):
    interval_grp = (active_points != active_points.shift().bfill()).cumsum()
    active_points[active_points.isna()] = 0
    active_points = np.array(active_points, dtype=bool)
    intervals = (
        df.assign(interval_grp=interval_grp)[active_points]
        .reset_index()
        .groupby(["interval_grp"])
        .agg(start_date=("ts", "first"), end_date=("ts", "last"))
    )
    intervals["type"] = event_type
    return intervals


def _clean_dataframe(df: pd.DataFrame):
    return df[~df.index.duplicated(keep="first")].sort_index()


def _run_stale_data_check(
    analysis_input, median_archival_step, stale_sketch
) -> tuple[list[EventFrame], datetime]:
    df = _clean_dataframe(analysis_input.data)

    df_copy = df.copy()
    df_copy["shifted_forward"] = df_copy["value"].shift()
    df_copy["shifted_backward"] = df_copy["value"].shift(-1)
    active_points = (
        (df_copy["shifted_forward"] == df_copy["value"])
        | (df_copy["shifted_backward"] == df_copy["value"])
    ) & (df_copy["value"] != 0)

    intervals = _get_intervals(active_points, df, _CHECK_NAME)
    intervals = handle_open_intervals(df, intervals)

    delta = max(
        get_cutoff_for_sketch(stale_sketch, analysis_input), 2 * median_archival_step
    )
    frames = _filter_stale_event_frames(
        event_frames_from_dataframe(process_open_intervals(intervals)), df, delta
    )
    last_analyzed_point = _get_last_analyzed_point(df, intervals)

    return frames, last_analyzed_point


def _get_relevant_statistic(analysis_input: AnalysisInput, stat_name: str):
    statistics = [
        statistic.result
        for statistic in analysis_input.statistics
        if statistic.name == stat_name
    ]
    if statistics is None or len(statistics) == 0:
        return None
    return statistics[0]


# pylint: disable=missing-function-docstring
def run(analysis_input: AnalysisInput) -> AnalysisResult:
    median_archival_step = _get_relevant_statistic(
        analysis_input, "Archival time median"
    )
    json_stale_nonzero_sketch = _get_relevant_statistic(
        analysis_input, "Stale Non-zero Sketch"
    )
    if median_archival_step is None:
        return AnalysisResult(condition_message="No median archival step")
    if json_stale_nonzero_sketch is None:
        return AnalysisResult(condition_message="No stale non-zero sketch")
    stale_sketch = jsonpickle.decode(json_stale_nonzero_sketch)

    frames, last_analyzed_point = _run_stale_data_check(
        analysis_input, median_archival_step, stale_sketch
    )
    return AnalysisResult(
        event_frames=list(frames), last_analyzed_point=last_analyzed_point
    )
