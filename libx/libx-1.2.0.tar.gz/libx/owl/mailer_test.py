# Import this somewhere to test
def main() -> None:
    subj = "testies"
    content = "hola amigo"
    msg = f"Subject: {subj}\n\n{content}"

    # 586 is used for tls
    server = SMTP("smtp.gmail.com", 587)
    sender = Sender(uname="lmistprox@gmail.com", passwd="thsxpkfcyezyltjb")
    recipient = Recipient(uname="louaimisto@gmail.com")

    mailargs = MailArgs(sender=sender, recipient=recipient, subj=subj, content=msg)

    sendmail(server, mailargs)
    exit(0)
