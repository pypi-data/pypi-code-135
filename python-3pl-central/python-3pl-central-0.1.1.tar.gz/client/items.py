from .client import get_client


def get_items(api_client, customer_id: int):
    return api_client.get(f"customers/{customer_id}/items")


def create_item(
    api_client,
    customer_id: int,
    sku: str,
    inventory_unit_identifier_name: str,
    inventory_unit_id: int,
    description: str,
):
    # Required data for POST
    post_data = {
        "sku": sku,  # Required
        "description": description,  # Required
        "inventoryCategory": "str",
        "options": {  # Required node
            "inventoryUnit": {  # Required node
                "unitIdentifier": {  # Required; Can be specified by "Name" and/or "id"
                    "name": inventory_unit_identifier_name,
                    "id": inventory_unit_id,
                },
            },
        },
    }

    return api_client.post(f"customers/{customer_id}/items", post_data)
