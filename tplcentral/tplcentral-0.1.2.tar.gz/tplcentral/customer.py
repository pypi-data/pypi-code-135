from client.client import get_client


def get_customer(customer_id: int, api_client):
    return api_client.get(f"customers/{customer_id}")
