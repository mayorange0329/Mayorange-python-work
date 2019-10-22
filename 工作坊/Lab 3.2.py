import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
ironman = np.linspace(-10,10,100)
plt.style.use('bmh')
fig = plt.figure() #定義一個圖像窗口
ax = plt.axes() #畫上刻度
plt.plot(ironman, np.sin(ironman), '.', ironman, np.cos(ironman), '--') #定義x,y和圖的樣式 兩條


