import csv

# �}�� CSV �ɮ�
with open('d:\python\iris.csv', newline='') as csvfile:
   
  # Ū�� CSV �ɤ��e�A�N�C�@�C�ন�@�� dictionary
  rows = csv.DictReader(csvfile)

  # �H�j���X���w���
  for row in rows:
    print(row['sepal_length'], row['species'])