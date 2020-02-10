"""
Set configurations required for the application.
"""

import os

MYSQL_DATABASE_PASSWORD = "e4fc6a65f379296c804f"
DB_SERVER_IP = "localhost"
MYSQL_DATABASE_USER = 'root'
MYSQL_DATABASE_DB = 'whmdb'
SQLALCHEMY_DATABASE_URI = 'mysql://root:' + MYSQL_DATABASE_PASSWORD + '@' \
                          + DB_SERVER_IP + '/' + MYSQL_DATABASE_DB
