import csv
# �}�ҿ�X�� CSV �ɮ�
with open('d:\python\output.csv', 'w', newline='') as csvfile:
  # �إ� CSV �ɼg�J��
  writer = csv.writer(csvfile)

  # �g�J�@�C���
  writer.writerow(['�m�W', '����', '�魫'])

  # �g�J�t�~�X�C���
  writer.writerow(['�O���R', 175, 60])
  writer.writerow(['���F��', 165, 57])