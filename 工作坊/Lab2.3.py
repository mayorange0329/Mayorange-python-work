import csv

# �G�����
table = [
    ['�m�W', '����', '�魫'],
    ['�O���R', 175, 60],
    ['���F��', 165, 57]
]

with open('d:\python\output.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)

  # �g�J�G�����
  writer.writerows(table)