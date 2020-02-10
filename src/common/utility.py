from flask import Response
from src.db import flaskorm as orm
import json
import operator

def make_response(resp_obj, status_code):
    """
    
    :param resp_obj: response data
    status_code: success HTTP status code
    :return: response object to user
    """

    return Response(status=status_code, response=json.dumps(resp_obj),
                    mimetype='application/json')


def _req_payload_parser(request_payload):
    """
    Parse the request payload received as json
    """
    try:
        req_payload = request_payload.get_json()
    except Exception:
        return Response(status=209)
    return req_payload


def check_invalid_payload(static_payload, req_payload):
    """

    :param static_payload: Hardcoded data input
    :param req_payload: New Payload Request
    :return: True/False
    """
    invalid_payload = set(static_payload) - set(req_payload)
    if invalid_payload:
        return invalid_payload

    return False

def calc_available_stock(storage_obj):
    """
    
    :param storage_obj: list of storage obj to calculate availabel stocks
    :return: 
    """

    total_count = 0
    for obj_count in storage_obj:
        total_count += obj_count.stock

    return total_count

def compute_picks(storage_obj, ele):
    """
    
    :param ele: {skuid: "", stock: ""}
    :return: 
    """

    order_dict = dict()
    final_list = list()
    for storage in storage_obj:
        order_dict.update({storage.id: storage.stock})
    sorted_order_list = sorted(order_dict.items(), key=operator.itemgetter(1))
    for list_ele in sorted_order_list:
        response_dict = dict()
        if ele["quantity"] <= list_ele[1]:
            response_dict.update({"id":list_ele[0],
                                  "quantity": ele["quantity"]})
            updated_stock = list_ele[1] - ele["quantity"]
            orm.update_storage(updated_stock, list_ele[0], ele["sku"])
            final_list.append(response_dict)
            break
        else:
            if list_ele[1] != 0:
                response_dict.update({"id": list_ele[0],
                                      "quantity": list_ele[1]})
                updated_stock = 0
                ele["quantity"] -= list_ele[1]
                orm.update_storage(updated_stock, list_ele[0], ele["sku"])
                final_list.append(response_dict)

    return final_list
