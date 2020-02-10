from flask import request
from src import WHM as whm
from src.objects import storage
from src.common import utility

@whm.route('/storage', methods=["GET", "POST", "PUT", "DELETE"])
def storage_controller():
    """

    API to handle storage operations.
    """

    post_payload_list = ["id", "sku", "stock"]
    delete_payload_list = ["id", "sku"]
    storage_obj = storage.Storage()
    if request.method == "GET":
        try:
            resp_data = storage_obj.get_all()
            return utility.make_response(resp_data, "200")
        except Exception as e:
            return utility.make_response({"message": e.message}, "409")

    if request.method == "POST":
        payload_obj = utility._req_payload_parser(request)
        req_payload_list = list()
        if payload_obj:
            for store_ele in payload_obj: 
                req_payload_list = store_ele.keys()
                invalid_payload = utility.check_invalid_payload(post_payload_list,
                                                                req_payload_list)
                if invalid_payload:
                    msg = "Invalid payload {}".format(invalid_payload)
                    return utility.make_response({"message": msg}, 400)

            try:
                storage_obj.post(payload_obj)
                msg = "Created Storage Entry"
                return utility.make_response({"message": msg}, "201")
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
            storage_obj.update(payload_obj)
            msg = "Updated Storage Entry"
            return utility.make_response({"message": msg}, "200")
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
                storage_obj.delete(payload_obj)
                msg = "Deleted SKU Successfully"
                return utility.make_response({"message": msg}, "200")
            except Exception as e:
                return utility.make_response({"message": e.message}, "409")
