import csv

# �}�� CSV �ɮ�
with open('d:\python\iris.csv', newline='') as csvfile:

# Ū�� CSV �ɮפ��e
rows = csv.reader(csvfile)

# �H�j���X�C�@�C
for row in rows:
    print(row)