"""
Set configurations required for the application.
"""

import os

MYSQL_DATABASE_PASSWORD = "<PASSWORD>"
DB_SERVER_IP = "<DB SERVER IP>"
MYSQL_DATABASE_USER = '<DB USERNAME>'
MYSQL_DATABASE_DB = 'whmdb'
SQLALCHEMY_DATABASE_URI = 'mysql://root:' + MYSQL_DATABASE_PASSWORD + '@' \
                          + DB_SERVER_IP + '/' + MYSQL_DATABASE_DB
