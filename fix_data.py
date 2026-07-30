import pandas as pd

# 读取数据
parts = pd.read_csv("data/parts.csv")
bom = pd.read_csv("data/bom.csv")
inventory = pd.read_csv("data/inventory.csv")

# =====================
# 修库存错误
# =====================

inventory.loc[
    inventory["stock"] < 0,
    "stock"
] = 0

# =====================
# 修BOM错误
# =====================

bom.loc[
    bom["qty"] <= 0,
    "qty"
] = 1

# =====================
# 修Part名称缺失
# =====================

parts["name"] = parts["name"].fillna(
    "UNKNOWN_PART"
)

# 保存修复结果
parts.to_csv(
    "data/parts_fixed.csv",
    index=False
)

bom.to_csv(
    "data/bom_fixed.csv",
    index=False
)

inventory.to_csv(
    "data/inventory_fixed.csv",
    index=False
)

print("DATA FIXED SUCCESSFULLY")