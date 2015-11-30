#coding: cp949
#Lec21-1130: Numpy1(행렬의 연산)

import numpy as np
from matplotlib import pyplot as plt

#행렬의 연산 - 각 요소별 연산 수행
data=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(data+2)
print(data-2)
print(data*data)
print(data/3)
print(data**2)
print(data**0.5)
print(data.dot(data))

#비교연산
a=np.array([1,2,3,4])
b=np.array([4,2,2,4])
print(a==b)
print(a>b)

#Array 비교연산
a=np.array([1,2,3,4])
b=np.array([4,2,2,4])
c=np.array([1,2,3,4])
print(np.array_equal(a,b))
print(np.array_equal(a,c))

#논리연산
a=np.array([1,1,0,0], dtype=bool)
b=np.array([1,0,1,0], dtype=bool)
print(np.logical_or(a,b))
print(np.logical_and(a,b))
print(np.all([True, True, False]))
print(np.any([True, True, False]))

#초월함수
a=np.arange(5)
print(np.sin(a))
print(np.log(a))
print(np.exp(a))

#전이행렬
a=np.triu(np.ones((3,3)),1) #상삼각행렬
print(a)
print(a.T)

#Sum
x=np.array([1,2,3,4,])
print(np.sum(x))    #x.sum()
x=np.array([[1,1],[2,2]])
print(x)
print(x.sum(axis=0))
print(x.sum(axis=1))

#최대, 최소
x=np.array([1,3,2])
print(x.min())
print(x.max())
print(x.argmin())   #최소값의 인덱스
print(x.argmax())   #최대값의 인덱스

#통계
x=np.array([1,2,3,1])
y=np.array([[1,2,3],[5,6,1]])
print(x.mean())        #평균값
print(np.median(x))
print(np.median(y, axis=-1))
print(x.std())         #표준편차


#응용
data=np.loadtxt('data.txt')
year, hares, lynxes, carrots = data.T
plt.plot(year, hares, year, lynxes, year, carrots)
plt.show()

#각 필드의 평균, 표준편차 구하기
h_avg=hares.mean()
h_std=hares.std()
l_avg=lynxes.mean()
l_std=lynxes.std()
c_avg=carrots.mean()
c_std=carrots.std()
data=np.array([[h_avg, l_avg, c_avg],[h_std, l_std, c_std]])    
print(data)

#최대값을 갖는 해 구하기
print(year[hares.argmax()])
print(year[lynxes.argmax()])
print(year[carrots.argmax()])


#Broadcasting
data=np.array([[0,10,20,30,40,50]]).T
a=np.array([0,1,2,3,4,5])
data=data+a
print(data)

