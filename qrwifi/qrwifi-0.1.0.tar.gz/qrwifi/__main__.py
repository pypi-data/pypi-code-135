import qrcode
import subprocess
import sys


def main():
    pass


if sys.platform == "darwin":
    try:
        ssid = (
            subprocess.check_output(
                "/System/Library/PrivateFrameworks/Apple80211.framework"
                "/Versions/Current/Resources/airport"
                " -I | sed -n 's/ *SSID: //p'",
                shell=True,
            )
            .decode()
            .strip()
        )

        auth = (
            subprocess.check_output(
                "/System/Library/PrivateFrameworks/Apple80211.framework"
                "/Versions/Current/Resources/airport"
                " -I | sed -n 's/ *link auth: //p'",
                shell=True,
            )
            .decode()
            .strip()
            .lower()
        )
        if "wpa" in auth:
            auth = "WPA"
        if "wep" in auth:
            auth = "WEP"

        password = (
            subprocess.check_output(
                "sudo security find-generic-password -l"
                f"{ssid} -D 'AirPort network password' -w",
                shell=True,
            )
            .decode()
            .strip()
        )
    except Exception:
        sys.exit(1)
else:
    print("Your OS is not yet supported because I don't know how to get the auth type.")
    print("Please create an issue on Github.")

qr = qrcode.QRCode(version=1, border=4)
qr.add_data(f"WIFI:S:{ssid};T:{auth};P:{password};")
qr.print_ascii(tty=True)
