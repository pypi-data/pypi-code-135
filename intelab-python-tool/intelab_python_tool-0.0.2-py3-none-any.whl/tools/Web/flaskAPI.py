from datetime import datetime
import os
from intelab_python_tool.tools.log import log
from flask import Flask, jsonify
from flask.views import MethodView
from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess

"""
使用方法如下：
    >> 该方法用来制作接口给后端数据

    from intelab_python_tool.tools.Web.flaskAPI import app

    @app.route('/index': 页面地址, method = ['post'])
    def give_data():
        ...

    app.run(host=..., port=..., *args, **kwargs)
"""

data_bytes = {"monitor-log": 0}
check_times = 0
error_times = 0
TIMEZONE = 'Asia/Shanghai'


def start_scheduler(monitor_log_path: str, service_name: str, minutes: int):

    scheduler = BlockingScheduler(
        {'apscheduler.timezone': TIMEZONE}
    )

    scheduler.add_job(service_control_task(monitor_log_path, service_name), 'interval', minutes=minutes)
    scheduler.start()


def service_control_task(monitor_log_path: str, service_name: str):

    global data_bytes

    MC = MinitorClient(monitor_log_path, service_name, data_bytes)
    data_bytes = MC.run()


class MinitorClient:
    global data_bytes, check_times, error_times

    def __init__(self, monitor_log_path: str, service_name: str, old_data_bytes):
        self.service_name = service_name
        self.log_path = monitor_log_path
        self.time = datetime.now().strftime("%Y-%m-%d")
        self.old_data_bytes = old_data_bytes
        self.hour = datetime.now().hour

    def run(self):
        global data_bytes, check_times, error_times

        new_data_bytes = os.stat(f"{self.log_path}" + f"{self.time}").st_size
        log.info('主监控日志文件变化前大小为{}，变化后大小为{}'.format(self.old_data_bytes, new_data_bytes))

        if new_data_bytes != self.old_data_bytes['monitor_log']:
            check_times = 0
        else:
            check_times += 1

        log.info(f'主监控日志check_times为{check_times}')
        if check_times > 3:
            log.info(f'check_times大于3，重启服务')
            self.restart_service()
            check_times = 0
            error_times += 1
        else:
            error_times = 0

        hour_str = f"{self.hour}" if self.hour > 9 else f"0{self.hour}"
        log_check = os.system(f"cat {self.log_path}" + f"{self.time} | grep {self.time}T{hour_str}")
        log.info(f"执行shell: cat {self.log_path}" + f"{self.time} | grep {self.time}T{hour_str}")

        if log_check != 0:
            log.info(f"{self.time}T{hour_str} 无法在日志文件中查询到，请及时查看处理")
            self.send_alarm2developer(f"{self.time}T{hour_str} 无法在日志文件中查询到，请及时查看处理")
            self.restart_service()
            check_times = 0

        return new_data_bytes

    def restart_service(self) -> None:
        service_name = self.service_name
        log.info(f"正在重启{service_name}服务")
        res = os.system(f"supervisorctl restart {service_name}")
        if res == 0:
            log.info(f"重启{service_name}完成")
        else:
            self.send_alarm2developer(f"重启{service_name}失败，请开发人员介入查看")

    @staticmethod
    def send_alarm2developer(msg: str, ding_talk_function) -> None:
        log.info('警告已发送至开发者')
        ding_talk_function(msg)


class ServiceHealthRemind(MethodView):
    global error_times

    def get(self):

        global error_times

        if error_times >= 3:
            response = {'msg': '算法服务重启三次仍无法正常运行，请相关运维人员检查服务配置或网络', 'code': 400,
                        'data': 0}
        else:
            response = {'msg': '服务正常', 'code': 200, 'data': 0}
        return jsonify(response)

    def post(self):
        global error_times

        if error_times >= 3:
            response = {'msg': '算法服务重启三次仍无法正常运行，请相关运维人员检查服务配置或网络', 'code': 400,
                        'data': 0}
        else:
            response = {'msg': '服务正常', 'code': 200, 'data': 0}
        return jsonify(response)


def app_run(host, port):
    app = Flask(__name__)

    app.add_url_rule('/api/ai/service_monitor', view_func=ServiceHealthRemind.as_view('service_health'))
    app.run(host=host, port=port)


