from flask import request
from src import WHM as whm
from src.objects import sku
from src.common import utility


@whm.route('/sku', methods=["GET", "POST", "PUT", "DELETE"])
def sku_controller():
    """
    API to get all customers. 
    """

    post_payload_list = ["id", "product_name"]
    delete_payload_list = ["id"]
    sku_obj = sku.Sku()

    if request.method == "GET":
        try:
            resp_data = sku_obj.get_all()
            return utility.make_response(resp_data, "200")
        except Exception as e:
            return utility.make_response({"message": e.message}, "409")

    if request.method == "POST":
        payload_obj = utility._req_payload_parser(request)
        req_payload_list = list()
        if payload_obj:
            req_payload_list = payload_obj.keys()
            invalid_payload = utility.check_invalid_payload(post_payload_list,
                                                    req_payload_list)
            if invalid_payload:
                msg = "Invalid payload {}".format(invalid_payload)
                return utility.make_response({"message": msg}, 400)

            try:
                sku_obj.post(payload_obj)
                msg = "Created SKU Entry"
                return utility.make_response({"message":msg}, "201")
            except Exception as e:
                return utility.make_response({"message": e.message}, "409")

    if request.method == "DELETE":
        payload_obj = utility._req_payload_parser(request)
        req_payload_list = list()
        if payload_obj:
            req_payload_list = payload_obj.keys()
            invalid_payload = utility.check_invalid_payload(delete_payload_list,
                                                    req_payload_list)
            if invalid_payload:
                msg = "Invalid payload {}".format(invalid_payload)
                return utility.make_response({"message": msg}, 400)
            try:
                sku_obj.delete(payload_obj)
                msg = "Deleted SKU Successfully"
                return utility.make_response({"message": msg}, "200")
            except Exception as e:
                return utility.make_response({"message": e.message}, "409")

    if request.method == "PUT":
        payload_obj = utility._req_payload_parser(request)
        req_payload_list = list()
        if payload_obj:
            req_payload_list = payload_obj.keys()
            invalid_payload = utility.check_invalid_payload(post_payload_list,
                                                    req_payload_list)
            if invalid_payload:
                msg = "Invalid payload {}".format(invalid_payload)
                return utility.make_response({"message": msg}, 400)

            try:
                sku_obj.update(payload_obj)
                msg = "Updated SKU {} Successfully".format(payload_obj["product_name"])
                return utility.make_response({"message": msg}, "200")
            except Exception as e:
                return utility.make_response({"message": e.message}, "409")