#coding: cp949
#Lec23-1207: Matplotlib

import numpy as np
from matplotlib import pyplot as plt

plt.plot([1,2,3,4])     #y축
plt.show()

plt.plot([1,2,3,4], [1,4,9,16])     #x축, y축
plt.show()

plt.plot([1,2,3,4], [1,4,9,16])
plt.plot([1,2,3,4], [1,4,9,16], 'o')    #circle marker 추가
plt.show()

t=np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')     #Line style
plt.show()

X=np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S=np.cos(X), np.sin(X)
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-", label="sine")
plt.legend(loc='upper left')    #라벨의 위치
plt.show()


#구간 나누기
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1=np.arange(0.0, 5.0, 0.1)
t2=np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)    #행,열
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()


#Spine(축 옮기기)
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0.3))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0.4))
plt.show()


#Contour Plots(등고선 그리기)
def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n=256
x=np.linspace(-3,3,n)
y=np.linspace(-3,3,n)
X,Y=np.meshgrid(x,y)

plt.axes([0.025, 0.025, 0.95, 0.95])
plt.contourf(X, Y, f(X,Y), 8, alpha=.75, cmap=plt.cm.hot)
C=plt.contour(X, Y, f(X,Y), 8, colors='black', linewidth=.5)
plt.clabel(C, inline=1, fontsize=10)
plt.xticks(())
plt.yticks(())
plt.show()


#Imshow
def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3 ) * np.exp(-x ** 2 - y ** 2)

n = 10
x = np.linspace(-3, 3, 3.5 * n)
y = np.linspace(-3, 3, 3.0 * n)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.axes([0.025, 0.025, 0.95, 0.95])
plt.imshow(Z, interpolation='nearest', cmap='bone', origin='lower')
plt.colorbar(shrink=.92)
plt.xticks(())
plt.yticks(())
plt.show()