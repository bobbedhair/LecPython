#coding: cp949
#Lec20-1125: NumPy1

import numpy as np

#��� �����
data=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(data)
print(data.T)
print(np.ones((3,2)))
print(np.zeros((3,2)))
print(np.eye((3)))
print(np.diag([1,2,3,4]))

#����� ũ��
print(data.ndim)    #n����
print(data.shape)   #n by n
print(len(data))    #1�� �迭�� ũ��

#����� ��������
data=np.array([[1,2,3],[4,5,6],[7,8,9.]])
print(data.dtype)   #��� ��Ұ� ����.

#�������� ����
data=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(data.astype(np.float))
data=np.array(['1','2','3'])
print(data.astype(np.int))

#�������� ����
data=np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=float)
print(data)
data=np.array([1,2,3], dtype=complex)
print(data)

#���� �����Ͽ� ��� �迭 �����
print(np.arange(10))            #0 1 ... 9
print(np.arange(10,1,-1))       #10 9 ... 2
print(np.arange(10,1,-1)[:, np.newaxis])    #�� ����(10 9 ... 2)
print(np.arange(2,8,dtype=np.float))        #2. 3. ... 7.
print(np.arange(35).reshape(5,7))           #0~34�� 5x7 �迭��

#������ ���� �迭?
print(np.linspace(1., 4., 6))   #����, ��, num-points(1.  1.6  2.2  2.8  3.4  4.)
print(np.linspace(1., 4., 6, endpoint=False))   #1.  1.5  2.  2.5  3.  3.5

#���� ����
data=np.random.rand(4)      #[0,1]
print(data)
data=np.random.randn(4)     #Gaussian
print(data)

#�迭�� �ε���/�����̽�
data = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
print(data[0])
print(data[-1])
print(data[0:2])
print(data[:2])
print(data[1:4:2])
print(data[::-1])
print(data[2][0])
print(data[2,0])
print(data[1:4:2, ::3])

#�ε��� �迭
x=np.arange(10,1,-1)
print(x)
print(x[np.array([3,3,1,8])])       #�ش� �ε����� �� ���
print(x[np.array([[1,1],[2,3]])])   #2���� �迭�� ���

y=np.arange(35).reshape(5,7)
print(y)
print(y[np.array([0,2,4])])     #0,2,4�� ���
b=y>20
print(y[b])                   #20���� ū �� ���

#boolean mask?
data=np.array([[0,10,20,30,40,50]]).T 
a=np.array([0,1,2,3,4,5]) 
data=data+a
print(data)

mask=np.array(np.array([1,0,1,0,0,1], dtype=bool))
print(data[mask, 2])

mask1=np.array([0,1,2,3,4])
mask2=np.array([1,2,3,4,5])
print(data[mask1, mask2])

