import csv
with open('d:\python\output.csv', 'w', newline='') as csvfile:
  # �w�q���
  fieldnames = ['�m�W', '����', '�魫']

  # �N dictionary �g�J CSV ��
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

  # �g�J�Ĥ@�C�����W��
  writer.writeheader()

  # �g�J���
  writer.writerow({'�m�W': '�O���R', '����': 175, '�魫': 60})
  writer.writerow({'�m�W': '���F��', '����': 165, '�魫': 57})