from pydantic import BaseSettings, validator
from ready_logger import get_logger

logger = get_logger("alert-msgs")


class EmailSettings(BaseSettings):
    addr: str
    password: str
    receiver_addr: str
    attachment_max_size_mb: int = 20
    inline_tables_max_rows: int = 2000
    smtp_server: str = "smtp.gmail.com"
    smtp_port: int = 465

    class Config:
        env_prefix = "alert_msgs_email_"

class SlackSettings(BaseSettings):
    webhook: str
    attachment_max_size_mb: int = 20
    inline_tables_max_rows: int = 200

    class Config:
        env_prefix = "alert_msgs_slack_"


class AlertSettings(BaseSettings):
    send_email: bool = False
    alert_slack: bool = False

    class Config:
        env_prefix = "alert_msgs_"
        
    @validator('send_email')
    def check_send_email_set(cls, v):
        if not v:
            logger.warning("Environment variable ALERT_MSGS_SEND_EMAIL is not set. No email alerts will be sent.")
            
    @validator('alert_slack')
    def check_alert_slack_set(cls, v):
        if not v:
            logger.warning("Environment variable ALERT_MSGS_ALERT_SLACK is not set. No Slack alerts will be sent.")


alert_settings = AlertSettings()
