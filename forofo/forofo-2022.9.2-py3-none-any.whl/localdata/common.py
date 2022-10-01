from clutter.aws import get_secrets
import pendulum

KST = pendulum.timezone("Asia/Seoul")
UTC = pendulum.timezone("UTC")

try:
    SERVICE_KEYS = get_secrets("prod/localdata/openapi")
except Exception as ex:
    SERVICE_KEYS = None
