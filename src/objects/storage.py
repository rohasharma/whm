from src.db import flaskorm as orm
from src.common import exceptions as ex

class Storage():

    def __init__(self):
        pass

    def get_all(self):
        resp_data = {"STORAGES": []}
        db_data = orm.get_all_storage()
        for data in db_data:
            resp_data["STORAGES"].append({"id": data.id,
                                          "stock": data.stock,
                                          "sku": data.sku})
        return resp_data

    def post(self, payload):
        for ele in payload:
            sku_id = ele["sku"]
            id = ele["id"]
            stock = ele["stock"]
            check_sku = orm.get_sku_by_id(id=sku_id)
            if not check_sku:
              raise ex.SkuNotRegistered()
            check_sku_storage = orm.get_storage_by_sid_skuid(id, sku_id)
            if check_sku_storage:
                raise ex.SkuStorageExists()
            orm.create_storage(stock, id, sku_id)
        return

    def update(self, payload):
        sku_id = payload["sku"]
        id = payload["id"]
        stock = payload["stock"]
        if not orm.get_sku_by_id(sku_id):
            raise ex.SkuNotFound()
        if not orm.get_storage_by_id(id):
            raise ex.StorageNotFound()
        check_sku_storage = orm.get_storage_by_sid_skuid(id, sku_id)
        if not check_sku_storage:
            raise ex.SkuStorageNotExists()
        if check_sku_storage.stock == stock:
            raise ex.SkuQuantityIsSame()
        orm.update_storage(stock, id, sku_id)
        return

    def delete(self, payload):
        id = payload["id"]
        sku_id = payload["sku"]
        storage_check = orm.get_storage_by_sid_skuid(id, sku_id)
        if not storage_check:
            raise ex.StorageNotFound()
        if storage_check.stock != 0:
                raise ex.ProductAvailable()
        orm.delete_storage(id, sku_id)



