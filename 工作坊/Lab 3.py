import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
ironman = np.linspace(-10,10,100)
fig = plt.figure() #定義一個圖像窗口
plt.plot(ironman, np.sin(ironman), '.') #定義x,y和圖的樣式