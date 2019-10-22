plt.style.use('bmh')
fig = plt.figure()
ax = plt.axes()
plt.plot(ironman, np.sin(ironman), '.') #定義x,y和圖的樣式
plt.xlim(-15, 15)
plt.ylim(-1.5, 1.5)
plt.title("Sine curve y=sin(x)")
plt.xlabel("x")
plt.ylabel("sin(x)")