import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

alert_dir = "C:\\Users\\kelle\\OneDrive\\Documents\\TradeIdeasPro"

log_file_pos_file = Path(__file__).parent / ".window_log_pos.json"
log_file_pos = (
    json.loads(log_file_pos_file.read_text()) if log_file_pos_file.is_file() else {}
)

window_headers = {
    "Alerts": [
        "TimeStamp",
        "Type",
        "Time",
        "Symbol",
        "Description",
        "Price",
        "Relative Volume",
        "Volume Today",
        "Change from the Close",
        "Volume 1 Minute",
        "Volume 5 Minute",
        "Volume Today",
        "Count",
    ]
}


def read_new_alerts(window_name: str) -> List[Dict[str, Any]]:
    """Parse the log file from the TI desktop app."""
    today = datetime.today().strftime("%Y%m%d")
    path = f"{alert_dir}\\alertlogging.{window_name}.{today}.csv"
    pos = log_file_pos.get(window_name, 0)
    with open(path, "r") as f:
        f.seek(pos)
        # iterate through existing lines.
        lines = f.readlines()
    log_file_pos[window_name] = f.tell()
    log_file_pos_file.write_text(json.dumps(log_file_pos))
    header = window_headers[window_name]
    lines = [dict(zip(header, l.strip().split(","))) for l in lines]
    for l in lines:
        l["TimeStamp"] = datetime.strptime(l["TimeStamp"], "%Y-%m-%d %H:%M:%S")
    return lines
