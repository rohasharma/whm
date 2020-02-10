class WHMException(Exception):
    message = "An unknown exception occurred."
    code = 500

    def __init__(self, message=None, **kwargs):
        self.kwargs = kwargs
        if 'code' not in self.kwargs:
            try:
                self.kwargs['code'] = self.code
            except AttributeError:
                pass
        if message:
            self.message = message

class SkuDuplicateEntry(WHMException):
    code = 409
    message = "SKU with ID already registered."

class SkuProductExists(WHMException):
    code = 409
    message = "Product name already exists with a different SKU ID."

class SkuNotFound(WHMException):
    code = 409
    message = "SKU ID Not Found"

class SkuNotRegistered(WHMException):
    code = 409
    message = "Invalid SKU ID Detected. Register the SKU ID and then proceed."

class SkuStorageExists(WHMException):
    code = 409
    message = "SKU ID Exists with given Storage. " \
              "Use Update to increase/decrease the stock in storage"

class SkuStorageNotExists(WHMException):
    code = 409
    message = "SKU ID Doesn't Exists with given Storage."

class StorageNotFound(WHMException):
    code = 409
    message = "Storage doesn't exists."

class SkuQuantityIsSame(WHMException):
    code = 409
    message = "SKU quantity is same in the storage selected."

class ProductAvailable(WHMException):
    code = 409
    message = "Prodcut available in Storage hence can not delete."

class SkuIDExistsInStorage(WHMException):
    code = 409
    message = "Can not Delete SKU as this SKU is mapped with a storage."

class OutOfStockRequest(WHMException):
    code = 400
    message = "Requested Quantity not available"

class OrderNotFound(WHMException):
    code = 400
    message = "Order Not Found"