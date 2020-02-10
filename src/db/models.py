"""
Creates database tables.
"""
from sqlalchemy.dialects.mysql import BIGINT

from src import DB as db

class SKU(db.Model):
    """
    Class to handle SKU details.
    """

    __tablename__ = 'SKU'
    id = db.Column(db.String(100), primary_key=True)
    product_name = db.Column('product_name', db.String(100))

    def __init__(self, product_name, id):
        self.product_name = product_name
        self.id = id


    def __repr__(self):
        return '<SKU %r>' % (self.id)

class STORAGE(db.Model):
    """
    Class to handle Storage details.
    """
    __tablename__ = 'STORAGE'
    store_id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(100))
    stock =  db.Column(db.BIGINT)
    sku = db.Column('sku', db.String(100), db.ForeignKey('SKU.id',
                                                  ondelete='CASCADE'),
                    primary_key=True)

    def __init__(self, stock, id, sku):
        self.stock = stock
        self.id = id
        self.sku = sku



    def __repr__(self):
        return '<STORAGE %r>' % (self.sku)

class ORDER_TABLE(db.Model):
    """
    Class to handle Orders
    """
    __tablename__ = 'ORDER_TABLE'

    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100))



    def __init__(self, customer_name):
        self.customer_name = customer_name

    def __repr__(self):
        return '<ORDER_TABLE %r>' % (self.id)

class ORDER_LINE(db.Model):
    """
    Class to handle Order Lines
    """
    __tablename__ = 'ORDER_LINE'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('ORDER_TABLE.id'))
    sku = db.Column('sku', db.String(100), db.ForeignKey('SKU.id'))
    quantity = db.Column(db.BIGINT)

    def __init__(self, sku, order_id, quantity):
        self.sku = sku
        self.order_id = order_id
        self.quantity = quantity

    def __repr__(self):
        return '<ORDER_LINE %r>' % (self.sku)
