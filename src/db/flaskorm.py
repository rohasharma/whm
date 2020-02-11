import models as mod
from src import DB as db

def get_all_sku():
    """
    
    :return: List of all sku objects
    """
    list_sku = mod.SKU.query.all()

    return list_sku

def get_sku_by_id(id):
    """
    
    :return: sku with specific id
    """
    sku_entry = mod.SKU.query.filter_by(id=id).first()

    return sku_entry

def get_sku_by_name(name):
    """
    
    :return: sku with specific id
    """
    sku_entry = mod.SKU.query.filter_by(product_name=name).first()

    return sku_entry


def create_sku(skuid, name):
    """
    
    :return: 
    """

    sku_entry = mod.SKU(name, skuid)
    db.session.add(sku_entry)
    db.session.commit()

    return

def delete_sku(skuid):
    """
    
    :param skuid: 
    :return: 
    """
    sku_obj = get_sku_by_id(skuid)
    db.session.delete(sku_obj)
    db.session.commit()
    return

def update_sku(skuid, name):
    """
    
    :param skuid: 
    :param name: 
    :return: 
    """
    sku_obj = get_sku_by_id(skuid)
    sku_obj.product_name = name
    db.session.commit()
    return

def get_all_storage():
    """

    :return: List of all storage objects
    """
    list_storage = mod.STORAGE.query.all()

    return list_storage

def get_storage_by_sid_skuid(id, sku_id):
    """
    
    :param id: storage id
    :param sku_id: sku id 
    :return: if sku id is present on that location or not.
    """

    check_storage = mod.STORAGE.query.filter_by(id=id, sku=sku_id).first()
    return check_storage

def get_storage_by_id(id):
    """
    
    :param id: storage id
    :return: storage obj if id found.
    """

    get_storage = mod.STORAGE.query.filter_by(id=id).all()

    return get_storage


def get_storage_by_skuid(sku_id, all=False):
    """

    :param id: storage id
    :return: storage obj if id found.
    """
    if not all:
        get_storage = mod.STORAGE.query.filter_by(sku=sku_id).first()
    else:
        get_storage = mod.STORAGE.query.filter_by(sku=sku_id).all()

    return get_storage

def create_storage(stock, id, sku_id):
    """
    
    :param stock: stock count
    :param id: storage id
    :param sku_id: sku id
    :return: 
    """
    sku_entry = mod.STORAGE(stock, id, sku_id)
    db.session.add(sku_entry)
    db.session.commit()

    return

def update_storage(stock, id, sku_id):
    """
    
    :param stock: stock count
    :param id: storage id
    :param sku_id: sku id
    :return: 
    """

    storage_obj = get_storage_by_sid_skuid(id, sku_id)
    storage_obj.stock = stock
    db.session.commit()

    return

def delete_storage(id, sku_id):
    """
    
    :param stock: stock count
    :param id: storage id
    :param sku_id: sku id
    :return: 
    """
    storage_obj = get_storage_by_sid_skuid(id, sku_id)
    db.session.delete(storage_obj)
    db.session.commit()

    return

def get_all_order():
    """
    
    :return: 
    """
    list_order = mod.ORDER_TABLE.query.all()

    return list_order

def create_order(name):
    """
    
    :param name: customer name
    :return: order_id
    """

    create_order = mod.ORDER_TABLE(customer_name=name)
    db.session.add(create_order)
    db.session.commit()

    return create_order.id

def create_orderline(order_id, ele):
    """
    
    :param order_id: order id
    :param ele: individual order
    :return: 
    """

    create_order_line = mod.ORDER_LINE(ele["sku"], order_id, ele["quantity"])
    db.session.add(create_order_line)
    db.session.commit()

    return

def get_order_line_by_id(order_id):
    """
    
    :param order_id: Order ID of User
    :return: lines of order id
    """

    get_order_line =  mod.ORDER_LINE.query.filter_by(order_id=order_id).all()

    return  get_order_line


def get_order_by_name(name):
    """
    
    :param name: customer name
    :return: 
    """

    get_order = mod.ORDER_TABLE.query.filter_by(customer_name=name).first()

    return get_order

def get_order_by_sku_id(sku_id, order_id):
    """
    
    :param sku_id: 
    :param order_id: 
    :return: 
    """

    get_order_details = mod.ORDER_LINE.query.filter_by(sku=sku_id,
                                                        order_id=order_id).first()

    return get_order_details


def commit_db():
    """

    :return:
    """

    db.session.commit()
