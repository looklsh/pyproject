import numpy as np
'''
배열의 기본요소
array = np.array([[1,2,3], [4,5,6]])

print(array.ndim)
print(array.shape)
print(array.dtype)
'''

'''
배열의 개별 단위요소 접근
array1 = np.array([1, 2, 3])
array2 = np.array([[1, 2], [3, 4]])
array3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(array1[-1])
print(array2[0][1])
print(array3[0][1][1])
'''

'''
배열의 블록 단위 요소 접근1
array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for i in array[0]:
    for j in i:
        if j % 2 == 0:
            print(j)
'''

'''
배열의 블록 단위 요소 접근2
array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])

print(array[1:3])
print(array[::2])
print(array[2:, 1::2])
'''

# 배열의 차원변형
# array = np.arange(12)
# reshape1 = array.reshape(2, 3, 2)
# reshape2 = np.reshape(array, (2, -1), order='F')

# print(array)
# print('reshape1:\n', reshape1)
# print('reshape2:\n', reshape2)

'''
배열의 차원 확장
array = np.arange(4)

axis1 = array[np.newaxis]
axis2 = array[:, np.newaxis]
axis3 = array[np.newaxis, :]

print(array)
print(axis1)
print('axis2:\n', axis2)
print('axis3:\n', axis3)
'''

'''
배열의 차원 축소
array = np.arange(12).reshape(3, -1)
flat1 = array.flatten(order='F')
flat2 = array.ravel() # 1차원으로 변형

print(array)
print('flat1:\n', flat1)
print('flat2:\n', flat2)
'''

'''
배열의 병합
array1 = np.arange(6).reshape(2, 3)
array2 = np.arange(6, 12).reshape(2, 3)

merge1 = np.stack([array1, array2], axis=0)
merge2 = np.stack([array1, array2], axis=-1)

print(array1)
print(array2)
print('merge1:\n', merge1)
print('merge2:\n', merge2)
'''

'''
배열의 분리
array = np.arange(10).reshape(2, 5)

detach1 = np.split(array, 2, axis=0)
detach2 = np.split(array, [2, 3], axis=1)


print('array:\n', array)
print('detach1:\n', detach1)
print('detach2:\n', detach2)
'''

'''
관심영역 지정
array = np.zeros((1280, 1920, 3), np.uint8)

x, y, w, h = 100, 100, 300, 300
roi = array[x:x+w, y:y+h]


print(array.shape)
print(roi.shape)
'''

array = np.zeros((1280, 1920, 3), np.uint8)

coi = array[:,:,0]

print(array.shape)
print(coi.shape)