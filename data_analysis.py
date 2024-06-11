import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 設置中文字體
font_path = "C:/Windows/Fonts/msjh.ttc"  # Windows系統內的SimHei字體
my_font = font_manager.FontProperties(fname=font_path)

# 創建示例數據
data = {"年份": [2020, 2021, 2022], "銷售額": [1000, 1500, 2000]}
df = pd.DataFrame(data)

# 繪製圖表
plt.plot(df["年份"].astype(str), df["銷售額"])
plt.xlabel("年份", fontproperties=my_font)
plt.ylabel("銷售額", fontproperties=my_font)
plt.title("年度銷售額", fontproperties=my_font)
plt.show()
