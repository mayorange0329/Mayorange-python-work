import csv

# 開啟 CSV 檔案
with open('d:\python\iris.csv', newline='') as csvfile:

# 讀取 CSV 檔案內容
rows = csv.reader(csvfile)

# 以迴圈輸出每一列
for row in rows:
    print(row)