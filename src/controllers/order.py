from flask import request
from src import WHM as whm
from src.objects import order
from src.common import utility


@whm.route('/order', methods=["GET", "POST", "PUT", "DELETE"])
def order_controller():
    """

    API to handle order.
    """

    post_payload_list = ["customer_name", "lines"]
    order_table_obj = order.Oder()
    if request.method == "GET":
        try:
            user = request.args.get('q')
            if user:
                resp_data = order_table_obj.get_user(user)
            else:
                resp_data = order_table_obj.get_all()
            return utility.make_response(resp_data, "200")
        except Exception as e:
            return utility.make_response({"message": e.message}, "409")

    if request.method == "POST":
        payload_obj = utility._req_payload_parser(request)
        if not isinstance(payload_obj["lines"], list):
            msg = "Invalid Payload type for lines. Expected List!"
            return utility.make_response({"message": msg}, "400")
        req_payload_list = list()
        if payload_obj:
            req_payload_list = payload_obj.keys()
            invalid_payload = utility.check_invalid_payload(post_payload_list,
                                                            req_payload_list)
            if invalid_payload:
                msg = "Invalid payload {}".format(invalid_payload)
                return utility.make_response({"message": msg}, 400)
            try:
                resp = order_table_obj.post(payload_obj)
                return utility.make_response(resp, "201")
            except Exception as e:
                return utility.make_response({"message": e.message}, "400")

    if request.method == "PUT":
        payload_obj = utility._req_payload_parser(request)
        if not isinstance(payload_obj["lines"], list):
            msg = "Invalid Payload type for lines. Expected List!"
            return utility.make_response({"message": msg}, "400")
        req_payload_list = list()
        if payload_obj:
            req_payload_list = payload_obj.keys()
            invalid_payload = utility.check_invalid_payload(post_payload_list,
                                                            req_payload_list)
            if invalid_payload:
                msg = "Invalid payload {}".format(invalid_payload)
                return utility.make_response({"message": msg}, 400)
            try:
                resp = order_table_obj.put(payload_obj)
                return utility.make_response(resp, "200")
            except Exception as e:
                return utility.make_response({"message": e.message}, "400")
