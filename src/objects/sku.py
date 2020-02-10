from src.db import flaskorm as orm
from src.common import exceptions as ex

class Sku():

    def __init__(self):
        pass

    def get_all(self):
        resp_data = {"SKU": []}
        db_data = orm.get_all_sku()
        for data in db_data:
            resp_data["SKU"].append({"id": data.id,
                                     "product_name": data.product_name})
        return resp_data

    def post(self, payload):
        sku_id = payload["id"]
        product_name = payload["product_name"]
        sku_obj = orm.get_sku_by_id(sku_id)
        if sku_obj:
            raise ex.SkuDuplicateEntry()
        if orm.get_sku_by_name(product_name):
            raise ex.SkuProductExists()
        orm.create_sku(sku_id, product_name)
        return

    def delete(self, payload):
        sku_id = payload["id"]
        if not orm.get_sku_by_id(sku_id):
            raise ex.SkuNotFound()
        check_sku_exists = orm.get_storage_by_skuid(sku_id)
        if check_sku_exists:
            raise ex.SkuIDExistsInStorage()
        orm.delete_sku(sku_id)
        return

    def update(self, payload):
        sku_id = payload["id"]
        product_name = payload["product_name"]
        if not orm.get_sku_by_id(sku_id):
            raise ex.SkuNotFound()
        if orm.get_sku_by_name(product_name):
            raise ex.SkuProductExists()
        orm.update_sku(sku_id, product_name)
        return