import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    host="localhost",
    database="fleet_erp",
    user="postgres",
    password="1234"
)

cursor = conn.cursor()

# 模拟修复日志
logs = [
    ("L0001", "inventory", "FIX_NEGATIVE_STOCK", "python_auto"),
    ("L0002", "bom", "FIX_ZERO_QTY", "python_auto"),
    ("L0003", "parts", "FIX_NULL_NAME", "python_auto"),
]

for log in logs:
    cursor.execute("""
        INSERT INTO change_logs(log_id, table_name, action, user_id, timestamp)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        log[0],
        log[1],
        log[2],
        log[3],
        datetime.now()
    ))

conn.commit()
cursor.close()
conn.close()

print("CHANGE LOGS CREATED")