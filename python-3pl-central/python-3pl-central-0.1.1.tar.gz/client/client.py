from .tpl import TPLClient


def get_client(
    BASE_URL,
    AUTH_PATH,
    CLIENT_ID,
    CLIENT_SECRET,
    TPL_KEY,
    GRANT_TYPE,
    USER_LOGIN_ID,
    SESSION=None,
    VERIFY_SSL=True,
):
    client = TPLClient(
        BASE_URL,
        AUTH_PATH,
        CLIENT_ID,
        CLIENT_SECRET,
        TPL_KEY,
        GRANT_TYPE,
        USER_LOGIN_ID,
        SESSION,
        VERIFY_SSL,
    )

    return client
