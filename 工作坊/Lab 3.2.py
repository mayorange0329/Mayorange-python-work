import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
ironman = np.linspace(-10,10,100)
plt.style.use('bmh')
fig = plt.figure() #�w�q�@�ӹϹ����f
ax = plt.axes() #�e�W���
plt.plot(ironman, np.sin(ironman), '.', ironman, np.cos(ironman), '--') #�w�qx,y�M�Ϫ��˦� ���


