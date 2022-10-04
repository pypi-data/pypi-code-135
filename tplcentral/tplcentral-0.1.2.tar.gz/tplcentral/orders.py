import json
from .client import get_client


def get_packages(api_client, order_id: int):
    return api_client.get(f"orders/{order_id}/packages")

# orders?pgsiz={{pgsiz}}&pgnum={{pgnum}}&rql={{RQLparams}}&sort={{seeSort}}&detail={{specifyDetailType}}&itemdetail={{specifyItemDetailType}}&markforlistid={{markforlistid}}&skulist={{enterSKUName(s)}}&skucontains={{enterSkuContains}}
def get_orders(api_client, pgsiz: int = 100, pgnum: int = 1):
    return api_client.get(f"orders?pgsiz={pgsiz}&pgnum={pgnum}")


# https://developer.3plcentral.com/?version=latest#b630ace1-e5ac-4d87-89fd-7139537d4222
def get_single_order(api_client, order_id: int):
    return api_client.get(f"orders/{order_id}?detail=all&itemdetail=all")

def get_order_by_invoice_number(api_client, ref: str):
    invoice_query = (f"orders?detail=all&itemdetail=all&rql=invoiceNumber=={ref}")
    
    result, headers = api_client.get(invoice_query)
    
    return result["ResourceList"]
    

def get_tracking_numbers(api_client, order_id: int):
    order, headers = get_single_order(api_client, order_id)
    saved_element = next(filter(lambda element: element["Name"] == "SmallParcelReturnTrackingNumbers", order["SavedElements"]), None)
    
    
    return_tracking_number = saved_element["Value"].split("|")[1] if saved_element else None
    outbound_tracking_number = order["RoutingInfo"]["TrackingNumber"] if "RoutingInfo" in order and "TrackingNumber" in order["RoutingInfo"] else None

    return {
        "outbound": outbound_tracking_number,
        "return": return_tracking_number
    }

# https://developer.3plcentral.com/?version=latest#b630ace1-e5ac-4d87-89fd-7139537d4222
def get_etag_for_order(api_client, order_id: int):
    order, headers = get_single_order(api_client, order_id)

    return headers["ETag"]


# https://developer.3plcentral.com/#d40d2679-5aa2-4080-8e85-78e3b38daedf
def create_order(
    customer_id: int,
    facility_id: int,
    reference_num: str,
    billing_code: str,
    invoice_number: str,
    is_insurance: bool,
    requires_delivery_conf: bool,
    carrier: str,
    routing_info_mode: str,
    routing_info_account: str,
    ship_point_zip: str,
    person_name: str,
    address_line_1: str,
    city: str,
    state: str,
    zip: str,
    country: str,
    item_identifier_sku: str,
    item_quantity: float,
    api_client,
    email_address: str = "",
    address_line_2: str = "",
    phone_number: str = "",
    company_name: str = "",
):
    post_data = {
        "customerIdentifier": {
            "id": customer_id,
        },
        "facilityIdentifier": {
            "id": facility_id,
        },
        "referenceNum": reference_num,
        "billingCode": billing_code,
        "invoiceNumber": invoice_number,
        "routingInfo": {
            "isInsurance": is_insurance,
            "requiresDeliveryConf": requires_delivery_conf,
            "carrier": "United States Postal Service",
            "mode": routing_info_mode,
            "account": routing_info_account,
            "shipPointZip": ship_point_zip,
        },
        "shipTo": {
            "companyName": company_name,
            "name": person_name,
            "address1": address_line_1,
            **({"address2": address_line_2} if address_line_2 else {}),
            "city": city,
            "state": state,
            "zip": zip,
            "country": country,
            "phoneNumber": phone_number,
            "emailAddress": email_address,
        },
        # "_embedded": {  # Required Node; not all properties are required, see below marked as required.
        #     "http://api.3plCentral.com/rels/orders/item": [
        #         {
        #             "itemIdentifier": {  # Required Node; Acceptable to only send "sku" or "id"
        #                 "sku": item_identifier_sku,
        #             },
        #             "qty": item_quantity,  # Required
        #         }
        #     ]
        # },
        "orderItems": [
            {"itemIdentifier": {"sku": item_identifier_sku}, "qty": item_quantity}
        ],
    }

    print(f"Creating new order with the following data: {post_data}")

    return api_client.post("orders", post_data)


# https://developer.3plcentral.com/#c2536c33-2927-4b11-a5b0-cbb2945a3a34
def cancel_order(api_client, order_id: int, reason: str = "Customer Cancelled"):
    # you first have to fetch an Order's ETag to pass to the cancel operation
    etag = get_etag_for_order(api_client, order_id)

    post_data = {"reason": reason}
    add_headers = {"If-Match": etag}

    return api_client.post(
        f"orders/{order_id}/canceler", post_data, add_headers=add_headers
    )
