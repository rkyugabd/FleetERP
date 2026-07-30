import pandas as pd
import random

# 1. PARTS
parts = []
for i in range(1, 501):
    parts.append({
        "part_id": f"P{i:04}",
        "name": f"Part_{i}",
        "type": random.choice(["component", "assembly"])
    })

df_parts = pd.DataFrame(parts)

# 2. BOM
bom = []
for i in range(150):
    parent = f"P{random.randint(1, 500):04}"
    for _ in range(random.randint(3, 7)):
        bom.append({
            "parent": parent,
            "component": f"P{random.randint(1, 500):04}",
            "qty": random.randint(1, 5)
        })

df_bom = pd.DataFrame(bom)

# 3. INVENTORY
inventory = []
for i in range(1000):
    inventory.append({
        "part_id": f"P{random.randint(1, 500):04}",
        "warehouse": random.choice(["CA", "US", "UK"]),
        "stock": random.randint(-5, 200)
    })

df_inventory = pd.DataFrame(inventory)

# 4. WORK ORDERS
work_orders = []
for i in range(1000):
    work_orders.append({
        "wo_id": f"WO{i:05}",
        "product": f"P{random.randint(1, 500):04}",
        "qty": random.randint(1, 50),
        "status": random.choice(["OPEN", "DONE", "FAILED"])
    })

df_wo = pd.DataFrame(work_orders)

# 5. SAVE FILES
df_parts.to_csv("data/parts.csv", index=False)
df_bom.to_csv("data/bom.csv", index=False)
df_inventory.to_csv("data/inventory.csv", index=False)
df_wo.to_csv("data/work_orders.csv", index=False)

print("DONE: ERP DATA GENERATED")
import pandas as pd
import random

# =========================
# 1. PART MASTER (500)
# =========================
parts = []
for i in range(1, 501):
    parts.append({
        "part_id": f"P{i:04}",
        "name": f"Part_{i}",
        "type": random.choice(["component", "assembly"])
    })

df_parts = pd.DataFrame(parts)

# =========================
# 2. BOM (150 PRODUCTS)
# =========================
bom = []
for i in range(150):
    parent = f"P{random.randint(1, 500):04}"
    for _ in range(random.randint(3, 8)):
        bom.append({
            "parent": parent,
            "component": f"P{random.randint(1, 500):04}",
            "qty": random.randint(1, 5)
        })

df_bom = pd.DataFrame(bom)

# =========================
# 3. BOO (OPERATIONS)
# =========================
operations = ["Cutting", "Welding", "Painting", "Assembly", "QC"]

boo = []
for i in range(150):
    product = f"P{random.randint(1, 500):04}"
    for step, op in enumerate(operations):
        boo.append({
            "product": product,
            "operation": op,
            "step": step + 1,
            "time_min": random.randint(5, 60)
        })

df_boo = pd.DataFrame(boo)

# =========================
# 4. INVENTORY (1000 + ERRORS)
# =========================
inventory = []
for i in range(1000):
    inventory.append({
        "part_id": f"P{random.randint(1, 500):04}",
        "warehouse": random.choice(["CA", "US", "UK"]),
        "stock": random.randint(-5, 200)  # includes errors
    })

df_inventory = pd.DataFrame(inventory)

# =========================
# 5. WORK ORDERS (1000)
# =========================
work_orders = []
for i in range(1000):
    work_orders.append({
        "wo_id": f"WO{i:05}",
        "product": f"P{random.randint(1, 500):04}",
        "qty": random.randint(1, 50),
        "status": random.choice(["OPEN", "IN_PROGRESS", "COMPLETED", "FAILED"])
    })

df_wo = pd.DataFrame(work_orders)

# =========================
# 6. CHANGE LOG (1000+)
# =========================
logs = []
actions = ["CREATE", "UPDATE", "DELETE"]

for i in range(1200):
    logs.append({
        "log_id": f"L{i:05}",
        "table": random.choice(["BOM", "INVENTORY", "PARTS"]),
        "action": random.choice(actions),
        "user": f"user_{random.randint(1,20)}",
        "timestamp": f"2026-06-{random.randint(1,30)}"
    })

df_logs = pd.DataFrame(logs)

# =========================
# 7. ERROR INJECTION (REAL ERP PROBLEMS)
# =========================

# BOM错误
for i in df_bom.sample(frac=0.1).index:
    df_bom.loc[i, "qty"] = 0

# Inventory错误
for i in df_inventory.sample(frac=0.05).index:
    df_inventory.loc[i, "stock"] = -1

# Parts缺失
df_parts.loc[df_parts.sample(frac=0.03).index, "name"] = None

# =========================
# 8. SAVE FILES
# =========================
df_parts.to_csv("data/parts.csv", index=False)
df_bom.to_csv("data/bom.csv", index=False)
df_boo.to_csv("data/boo.csv", index=False)
df_inventory.to_csv("data/inventory.csv", index=False)
df_wo.to_csv("data/work_orders.csv", index=False)
df_logs.to_csv("data/change_logs.csv", index=False)

print("ERP DATA GENERATED SUCCESSFULLY")