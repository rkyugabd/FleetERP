import pandas as pd
import psycopg2

# 数据库连接
conn = psycopg2.connect(
    host="localhost",
    database="fleet_erp",
    user="postgres",
    password="1234"
)

cursor = conn.cursor()

# 读取CSV
parts = pd.read_csv("data/parts.csv")
bom = pd.read_csv("data/bom.csv")
inventory = pd.read_csv("data/inventory.csv")
work_orders = pd.read_csv("data/work_orders.csv")

# 导入 parts
for _, row in parts.iterrows():
    cursor.execute(
        """
        INSERT INTO parts(part_id,name,type)
        VALUES(%s,%s,%s)
        """,
        (row["part_id"], row["name"], row["type"])
    )

# 导入 bom
for _, row in bom.iterrows():
    cursor.execute(
        """
        INSERT INTO bom(parent,component,qty)
        VALUES(%s,%s,%s)
        """,
        (row["parent"], row["component"], row["qty"])
    )

# 导入 inventory
for _, row in inventory.iterrows():
    cursor.execute(
        """
        INSERT INTO inventory(part_id,warehouse,stock)
        VALUES(%s,%s,%s)
        """,
        (row["part_id"], row["warehouse"], row["stock"])
    )

# 导入 work_orders
for _, row in work_orders.iterrows():
    cursor.execute(
        """
        INSERT INTO work_orders(wo_id,product,qty,status)
        VALUES(%s,%s,%s,%s)
        """,
        (row["wo_id"], row["product"], row["qty"], row["status"])
    )

conn.commit()

cursor.close()
conn.close()

print("DATA LOADED SUCCESSFULLY")