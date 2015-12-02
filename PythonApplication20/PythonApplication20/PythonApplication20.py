#coding: cp949
#Lec20-1125: NumPy1

import numpy as np

#행렬 만들기
data=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(data)
print(data.T)
print(np.ones((3,2)))
print(np.zeros((3,2)))
print(np.eye((3)))
print(np.diag([1,2,3,4]))

#행렬의 크기
print(data.ndim)    #n차원
print(data.shape)   #n by n
print(len(data))    #1차 배열의 크기

#행렬의 데이터형
data=np.array([[1,2,3],[4,5,6],[7,8,9.]])
print(data.dtype)   #모든 요소가 같다.

#데이터형 변경
data=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(data.astype(np.float))
data=np.array(['1','2','3'])
print(data.astype(np.int))

#데이터형 지정
data=np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=float)
print(data)
data=np.array([1,2,3], dtype=complex)
print(data)

#범위 지정하여 등간격 배열 만들기
print(np.arange(10))            #0 1 ... 9
print(np.arange(10,1,-1))       #10 9 ... 2
print(np.arange(10,1,-1)[:, np.newaxis])    #행 증가(10 9 ... 2)
print(np.arange(2,8,dtype=np.float))        #2. 3. ... 7.
print(np.arange(35).reshape(5,7))           #0~34를 5x7 배열로

#지정된 수의 배열?
print(np.linspace(1., 4., 6))   #시작, 끝, num-points(1.  1.6  2.2  2.8  3.4  4.)
print(np.linspace(1., 4., 6, endpoint=False))   #1.  1.5  2.  2.5  3.  3.5

#난수 생성
data=np.random.rand(4)      #[0,1]
print(data)
data=np.random.randn(4)     #Gaussian
print(data)

#배열의 인덱스/슬라이싱
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

#인덱스 배열
x=np.arange(10,1,-1)
print(x)
print(x[np.array([3,3,1,8])])       #해당 인덱스의 값 출력
print(x[np.array([[1,1],[2,3]])])   #2차원 배열로 출력

y=np.arange(35).reshape(5,7)
print(y)
print(y[np.array([0,2,4])])     #0,2,4행 출력
b=y>20
print(y[b])                   #20보다 큰 값 출력

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

