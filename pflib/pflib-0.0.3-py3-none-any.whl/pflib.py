import re
import socket
import logging

import urllib3


pfver = "0.0.3"


class metric:
    def __init__(self, name_metric: str, type_metric: str, help_metric: str, script_name: str) -> None:
        res = re.match(r"[a-zA-Z_][a-zA-Z0-9_]*", name_metric)
        if not res:
            logging.error(f"Name metric - {name_metric} incorrect.")
            return False
        self.name = str(name_metric)
        self.type = str(type_metric)
        self.help = str(help_metric)
        self.label = []
        self.pushgateway_host = "netdata-master"
        self.pushgateway_port = 9091
        self.script_name = script_name
        self.hostname = socket.gethostname()
        self.pushgateway_url_path = f"/metrics/job/{self.script_name}/source/{self.hostname}"
        self.pushgateway_url = f"http://{self.pushgateway_host}:{self.pushgateway_port}{self.pushgateway_url_path}"
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'User-Agent': f'pflib/{pfver}'
        }

    def __str__(self) -> str:
        labels = []
        if metric.validate_metric(self):
            for obj in self.label:
                label_str = self.name + '{' + f'script_name="{self.script_name}",'
                for label in obj[0]:
                    label_str += f'{label}="{obj[0][label]},"'
                label_str = label_str[:-2] + '"} ' + str(obj[1])
                labels.append(label_str)
            metrics = f"""# HELP {self.name} {self.help}
# TYPE {self.name} {self.type}"""
            for i in labels:
                metrics += f"\n{i}"
            return metrics
        logging.error(f"Validate metric - {self.name} is not True.")
        return "Error"

    def added_label(self, label: dict, value) -> bool:
        type_access = ["gauge", "counter", "histogram", "summary"]
        value = str(value)
        if not (self.type in type_access):
            list_type = ""
            for i in type_access:
                list_type += f"{i},"
            logging.error(f"Type {self.type} does not belong to: {list_type[:-1]}.")
            return False
        if not (value.isdecimal()):
            logging.error("Value is not decimal.")
            return False
        for i in label:
            res = re.match(r"[a-zA-Z_][a-zA-Z0-9_]*", i)
            if not res:
                logging.error(f"Label name - {i} incorrect.")
                return False
        self.label.append([label, value])
        return True

    def validate_metric(self) -> bool:
        for i in self.label:
            obj = i[0]
            value = str(i[1])
            try:
                test = i[2]
                logging.error(f"Validate metric is fail. Label - {i[2]}")
                return False
            except:
                pass
            if isinstance(obj, dict):
                for e in obj:
                    res = re.match(r"[a-zA-Z_][a-zA-Z0-9_]*", e)
                    if not res:
                        logging.error(f"Label name - {e} incorrect.")
                        return False
            if not (value.isdecimal()):
                logging.error(f"Value - {value} is not decimal")
            return True

    def send(self) -> bool:
        metrics = metric.__str__(self)
        logging.debug(metrics)
        metrics = metrics + "\n"
        http = urllib3.PoolManager()
        request = http.request('POST', self.pushgateway_url, headers=self.headers, body=metrics)
        if request.status != 200:
            logging.error(f"Error send metrics. Status code - {request.status}.")
            logging.error(f'Error is {request.data}.')
            logging.error(metrics)
            return False
        else:
            logging.info("Successful send metric.")
            return True
