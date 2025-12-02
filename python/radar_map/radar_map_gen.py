# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

zhfont1  =   matplotlib.font_manager.FontProperties(fname="SourceHanSerifSC-Regular.otf")

results  =   [{"大学英语": 87, "高等数学": 79, "体育": 95, "计算机基础": 92, "程序设计": 85},
                {"大学英语": 80, "高等数学": 90, "体育": 91, "计算机基础": 85, "程序设计": 88}]
data_length =   len(results[0])
# 将极坐标系根据数据长度进行等分，endpoint=False表示不包含终点值
angles   =   np.linspace(0,2*np.pi,data_length,endpoint=False)
labels  =   [*results[0]]
score   =   [[v for v in result.values()] for result in results]

# 使雷达图封闭，concatenate连接两个数组
score_a =   np.concatenate((score[0],[score[0][0]]))
score_b =   np.concatenate((score[1],[score[1][0]]))

angles  =   np.concatenate((angles,[angles[0]]))
labels  =   np.concatenate((labels,[labels[0]]))

# 设置图形大小
fig     =   plt.figure(figsize=(8,6),dpi=100)
# 创建极坐标系
# 111: 表示1行1列的第1个子图
# polar=True: 设置为极坐标系
ax      =   plt.subplot(111,polar=True)

# 绘制雷达图
ax.plot(angles,score_a,color='g')
ax.plot(angles,score_b,color='b')

# 设置雷达图中每一项的标签显示
# 设置极坐标图的角度刻度网格线和对应的标签文本
# angles*180/np.pi：将弧度转换为角度（0-360度）
# labels：对应每个角度的标签文本（字符串列表）
ax.set_thetagrids(angles*180/np.pi,labels,fontproperties=zhfont1)


# 设置雷达图的坐标刻度范围
# 0：径向坐标的最小值（中心点）
#100：径向坐标的最大值（最外圈）
ax.set_rlim(0,100)

# 去掉坐标系
plt.axis('off')

# 设置雷达图的坐标值显示角度，相对于起始角度的偏移量
# ax.set_rlabel_position(0)
ax.set_title("计算机专业大一", fontproperties=zhfont1)
plt.legend(["上学期","下学期"],prop=zhfont1)

plt.show()

