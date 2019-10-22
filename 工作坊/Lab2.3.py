import csv

# 二維表格
table = [
    ['姓名', '身高', '體重'],
    ['令狐沖', 175, 60],
    ['岳靈珊', 165, 57]
]

with open('d:\python\output.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)

  # 寫入二維表格
  writer.writerows(table)