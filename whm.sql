create schema whmdb;
use whmdb;

CREATE TABLE SKU(
                        id VARCHAR(100) NOT NULL,
                        product_name VARCHAR(100),
                        PRIMARY KEY ( id )
);

CREATE TABLE STORAGE(
                        store_id INT NOT NULL AUTO_INCREMENT,
                        id VARCHAR(100) NOT NULL,
                        stock bigint,
                        sku VARCHAR(100),
                        PRIMARY KEY (store_id),
                        FOREIGN KEY (sku) REFERENCES SKU(id) ON DELETE CASCADE
);

CREATE TABLE ORDER_TABLE(
                        id INT NOT NULL AUTO_INCREMENT,
                        customer_name VARCHAR(100) UNIQUE,
                        PRIMARY KEY ( id )
);

CREATE TABLE ORDER_LINE(
                        id INT NOT NULL AUTO_INCREMENT,
                        order_id INT NOT NULL,
                        sku VARCHAR(100),
                        quantity bigint,
                        customer_name VARCHAR(100) UNIQUE,
                        PRIMARY KEY ( id ),
                        FOREIGN KEY (sku) REFERENCES SKU(id)
);
