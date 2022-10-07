import json
import logging
from typing import Dict, Set, Any
from prometheus_client.parser import text_string_to_metric_families
import requests
from deucalion.strategies.strategy import Strategy


class PrometheusDockerComposeDemo(Strategy):
    def __init__(self):
        self.logger = logging.getLogger('PrometheusDemo')
        self.metrics_path = None
        self.targets: [str] = None

    def get_targets(self):
        self.targets = []

    def get_metrics(self, desired_metrics: Set[str]) -> Dict[str, Any]:
        res = {}
        for target in self.targets:
            try:
                res_dict = {}
                r = requests.get('http://' + target + '/' + self.metrics_path)  # TODO: https ondersteuning
                for family in text_string_to_metric_families(r.text):
                    for sample in family.samples:
                        metric_name = sample[0]  # sample[0] is metric name
                        if metric_name in desired_metrics:
                            labels_string = json.dumps(sample[1])
                            if metric_name not in res_dict:
                                res_dict[metric_name] = {}
                            res_dict[metric_name][labels_string] = sample[2]  # value
                    res[target] = res_dict
            except requests.exceptions.ConnectionError:
                self.logger.error('Could not get metrics from target {}'.format(target))

        return res

    def set_config(self, config_object):
        self.get_targets()
