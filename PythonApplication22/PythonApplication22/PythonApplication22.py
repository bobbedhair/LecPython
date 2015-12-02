#coding: cp949
#Lec22-1202: NumPy2 
  
import numpy as np
from matplotlib import pyplot as plt

#city ������ �Ÿ� ���ϱ�
mileposts=np.array([0,198,303,736,871,1175,1475,1544,1913,2448])
distance_array=np.abs(mileposts-mileposts[:, np.newaxis])
print(distance_array)

#�׸���/��Ʈ��ũ ��� �Ÿ� ���?
x=np.arange(5)
y=np.arange(5)[:, np.newaxis]
distance=np.sqrt(x**2 + y**2)
print(distance)

plt.pcolor(distance)
plt.colorbar()
plt.show()

x,y=np.ogrid[0:5, 0:5]
print(x+y)
x,y=np.mgrid[0:5, 0:5]
print(x, y)

#Flattening
a=np.array([[1,2,3],[4,5,6]])
print(a.ravel())
print(a.T)
print(a.T.ravel())

#Reshaping
b=a.ravel()
print(b)
b=b.reshape((2,3))  #b.reshape((2,-1))
print(b)

#Resizing
a=np.arange(4)
a.resize((8,))   #0 1 2 3 0 0 0 0
print(a)

#Sorting data
a = np.array([[4, 3, 5], [1, 2, 1]])
b=np.sort(a, axis=1)    #a.sort(axis=1)
print(b)

a = np.array([4, 3, 1, 2])
j=np.argsort(a)     #sort�� ����� �ε��� ��ȯ?
print(a)
print(j)
j_max=np.argmax(a)  #�ִ밪�� �ε���
print(j_max)
j_min=np.argmin(a)  #�ּҰ��� �ε���
print(j_min)

#Polynomials
p=np.poly1d([3,2,-1])
print(p(0))
print(p.roots)
print(p.order)
p=np.polynomial.Polynomial([-1,2,3])
print(p)

x=np.linspace(0,1,20)
y=np.cos(x)+0.3*np.random.rand(20)
p=np.poly1d(np.polyfit(x,y,3))
t=np.linspace(0,1,200)
plt.plot(x,y,'o',t,p(t),'-')
plt.show()

x = np.linspace(-1, 1, 2000)
y = np.cos(x) + 0.3*np.random.rand(2000)
p=np.polynomial.Chebyshev.fit(x,y,90)
t=np.linspace(-1,1,200)
plt.plot(x,y,'r.')
plt.plot(t,p(t),'k-',lw=3)
plt.show()

#�̹��� �ε�
img=plt.imread('Penguins.png')
print(img.shape)    #����ũ��, ����ũ��, rgb+@
print(img.dtype)
plt.imshow(img)    #�����̹���
plt.show()

subimg = img[:188, :250] #�߸� �̹���
plt.imshow(subimg)
plt.show()

