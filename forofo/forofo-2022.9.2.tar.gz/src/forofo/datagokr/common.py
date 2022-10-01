from clutter.aws import get_secrets
import pendulum

KST = pendulum.timezone("Asia/Seoul")
UTC = pendulum.timezone("UTC")

try:
    SERVICE_KEY = get_secrets("general/stonring/datagokr")["decoded"]
except Exception as ex:
    SERVICE_KEY = None
