import pickle
import pandas as pd

# 读取 pkl 文件
pkl_file_path = ""  # 请替换为您的 pkl 文件路径
with open(pkl_file_path, 'rb') as file:
    data = pickle.load(file)
# 设置显示选项
pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('display.max_rows', 10)  # 显示前10行
pd.set_option('display.width', None)  # 自动调整显示宽度

# 假设数据是可以转换为 DataFrame 的，例如列表或字典
df = pd.DataFrame(data)

# 输出列名
print("列名：")
print(data.columns)
    
    # 输出前五行
print("\n前五行数据：")
print(data.head())
