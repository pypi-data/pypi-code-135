from .client import get_client


def get_carriers(api_client):
    return api_client.get("properties/carriers")


if __name__ == "__main__":
    print(get_carriers())
