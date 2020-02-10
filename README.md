# whm
Basic Warehouse Management

# How to run the application
```bash
1) Change the values in config.py for DB connection:
  MYSQL_DATABASE_PASSWORD: <Password>
  DB_SERVER_IP: <localhost>
  MYSQL_DATABASE_USER: <DB User>
  MYSQL_DATABASE_DB: <DB Name>
2) Create the Database using whmdb.sql
    mysql -uroot -p<DB Password> -hDB_SERVER_IP < whm.sql
3) run the application:
    python run.py (App will run on PORT 5001 in DEBUG Mode)
```

# Assumptions
Customer Name will be used as a unique identity in the Application (Would have prefered using an email id instead of Cusomter  Name)

Customer Name will be used while placing the Order so that search mapping will become easy.

# Endpoints
## /sku : GET/POST/DELETE/PUT
## GET:
```bash
http://<IP ADDRESS>:5001/sku
  {
    "SKU": [
        {
            "id": "SKU1",
            "product_name": "Laptop"
        },
        {
            "id": "SKU2",
            "product_name": "Charger"
        }
    ]
}
```

## POST:
```bash
  {"id":"def",
"product_name": "table"
}
```
## PUT: Same payload as POST however validation is done to not change SKU ID but product name can be modifed.
## DELETE:
```bash
   {"id":"def"}
This will only delete the SKU if it is not mapped to any Storage. (To Delete a SKU you need to Delete it from the Storage first)
```

## 2) /storage: GET/POST/DELETE/PUT
## GET:
```bash
{
    "STORAGES": [
        {
            "sku": "abc",
            "id": "zzz",
            "stock": 0
        },
        {
            "sku": "abc",
            "id": "yyy",
            "stock": 81
        },
        {
            "sku": "def",
            "id": "xxx",
            "stock": 96
        }
    ]
}
```
## POST:
```bash
[
  {
    "id": "zzz",
    "sku": "abc",
    "stock": 5
  },
  {
    "id": "yyy",
    "sku": "abc",
    "stock": 100
  },
  {
    "id": "xxx",
    "sku": "def",
    "stock": 100
  }
]
```
## PUT:
```bash
{"id":"yyy",
  "sku": "abc",
  "stock": 10
}
```
## DELETE:
```bash
{"sku": "abc", "id":"zzz"} 
  We can only delete the entry from the Storage if stock count is 0 else:
{"sku": "abc", "id":"yyy"}
  {
      "message": "Prodcut available in Storage hence can not delete."
  }
```
## 3) /order: GET and POST
## GET:
```bash
[
    {
        "id": 32,
        "customer_name": "<username1>"
    },
    {
        "id": 31,
        "customer_name": "<username2>"
    },
    {
        "id": 33,
        "customer_name": "<username3>"
    }
]
```
## POST:
```bash
  {
	"customer_name": "Thomas müller",
	"lines": [
    {
      "sku": "abc",
      "quantity": 12
    },
    {
      "sku": "def",
      "quantity": 2
    }
  ]
}
  Response:
  [
    {
        "id": "yyy",
        "quantity": 12
    },
    {
        "id": "xxx",
        "quantity": 2
    }
]
```

## Query Search Parameter
http://<IP ADDR>:5001/order?q=Thomas müller
	
```bash
{
    "lines": [
        {
            "sku": "abc",
            "quantity": 12
        },
        {
            "sku": "def",
            "quantity": 2
        }
    ],
    "customer_name": "Thomas müller"
}
```
