from matplotlib import pyplot as plt
from matplotlib import style

# x = [2, 3, 4]
# y = [5, 6, 7]

# plt.plot(x, y)

# plt.xlabel('X')
# plt.ylabel('Y')

# plt.show()

#--------------------

style.use('ggplot') # 背景特效
# style.use('bmh')
# style.use('classic')
# style.use('dark_background')
# style.use('fivethirtyeight')
# style.use('ggplot')
# style.use('grayscale')
# style.use('seaborn-colorblind')

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [18, 21, 4, 3, 45, 17, 16, 5, 6]

x2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y2 = [16, 19, 5, 4, 44, 18, 17, 6, 8]

#plot 曲線圖

plt.subplot(211)
#linewidth=6 控制線圖粗細 marker='o'轉折點放一個圈圈 linestyle='-' label='Turth Value'顯示說明圖示的線(細節說明)
plt.plot(x, y, linewidth=3,color='b', label='Turth Value') 
plt.plot(x2, y2, linewidth=3, marker='o', color='r', linestyle='-', label='Prediction')
plt.legend() #強制顯示出細節說明

#subplot 合併兩個圖
#bar 柱狀圖
plt.subplot(212)
plt.bar(x, y, align='center', label='Turth Value')
plt.bar(x2, y2, align='center', label='Prediction')

plt.ylabel('Y')
plt.xlabel('X')

plt.legend()
plt.show()