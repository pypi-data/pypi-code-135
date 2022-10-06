"""
Send emails.
"""


from email.message import EmailMessage
from smtplib import SMTP, SMTPAuthenticationError

# Life on the edge.
from .interface import *

__all__ = ["sendmail"]


def sendmail(server: SMTP, mailargs: MailArgs) -> None:
    # ughh, https://stackoverflow.com/questions/54785148/destructuring-dicts-and-objects-in-python
    # sender, recipient, subj, content = mailargs
    m = mailargs
    try:
        server.starttls()
        server.login(m.sender.uname, m.sender.passwd)
        obj = EmailMessage()
        del obj["Subject"]
        obj["Subject"] = "py roolz"
        res = server.sendmail(m.sender.uname, m.recipient.uname, obj.as_string())
        if res == {}:
            # which I think is the case...
            server.quit()
            print(f"sent.")
            exit(0)
        else:
            print(res)
            exit(2)
    except SMTPAuthenticationError as _:
        print(f"incorrect creds for {m.sender.uname}")
        exit(1)


def get_msg_object(mailargs: MailArgs) -> None:
    """
    Constructs a message object.
    From, To, Subject
    """
    pass
