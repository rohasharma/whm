from src.db import flaskorm as orm
from src.common import exceptions as ex
from src.common import utility

class Oder():

    def __init__(self):
        pass

    def get_all(self):
        db_data = orm.get_all_order()
        resp_data = list()
        for data in db_data:
            resp_data.append({"id": data.id,
                              "customer_name": data.customer_name})
        return resp_data

    def get_user(self, name):
        db_data = orm.get_order_by_name(name)
        if not db_data:
            raise ex.OrderNotFound()
        resp_data = list()
        order_line_obj = orm.get_order_line_by_id(db_data.id)
        for order_line in order_line_obj:
            resp_data.append({"sku": order_line.sku,
                              "quantity": order_line.quantity})

        resp_obj = {"customer_name": name,
                    "lines": resp_data}

        return resp_obj


    def post(self, payload):
        customer_name = payload["customer_name"]
        lines = payload["lines"]
        order_id = orm.create_order(customer_name)
        order_line = OrderLine(order_id)
        order_line_list = order_line.post(lines)
        return order_line_list

    def put(self, payload):
        customer_name = payload["customer_name"]
        lines = payload["lines"]
        order_details = orm.get_order_by_name(customer_name)
        if not order_details:
            raise ex.OrderNotFound()
        order_line = OrderLine(order_details.id)
        order_line_list = order_line.put(lines)
        return order_line_list




class OrderLine():

    def __init__(self, order_id):
        self.order_id = order_id


    def post(self, lines):
        order_line_list = list()
        for ele in lines:
            if not orm.get_sku_by_id(ele["sku"]):
                raise ex.SkuNotFound()
            storage_list = orm.get_storage_by_skuid(ele["sku"], all=True)
            total_available_stock = utility.calc_available_stock(storage_list)
            if ele["quantity"] > total_available_stock:
                raise ex.OutOfStockRequest()
            orm.create_orderline(self.order_id, ele)
            order_line_list.extend(utility.compute_picks(storage_list, ele))
        return order_line_list

    def put(self, lines):
        order_line_list = list()
        for ele in lines:
            if not orm.get_sku_by_id(ele["sku"]):
                raise ex.SkuNotFound()
        for ele in lines:
            order_line_obj = orm.get_order_by_sku_id(ele["sku"], self.order_id)
            old_quantity = order_line_obj.quantity  # 30
            new_quantity = ele["quantity"]  # 20
            diff_stock_dict = {"add_storage": None,
                          "dec_storage": None}
            if old_quantity <= new_quantity:
                diff_stock_dict["dec_storage"] = new_quantity - old_quantity # 10
            else:
                diff_stock_dict["add_storage"] = old_quantity - new_quantity
            storage_list = orm.get_storage_by_skuid(ele["sku"], all=True)
            total_available_stock = utility.calc_available_stock(
                storage_list)
            if diff_stock_dict["dec_storage"] > total_available_stock:
                raise ex.OutOfStockRequest()
            order_line_list.extend(utility.update_orderline(self.order_id,
                                                            ele,
                                                            diff_stock_dict))

        return order_line_list

