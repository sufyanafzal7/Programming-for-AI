import numpy as np


# a = np.array([1,2,3])
# print(type(a), a.shape)
# a[0] = 5
# print(a)



# b = np.array([[1,2,3],[4,5,6]])
# print(b)
# print(b.shape)



# c = np.zeros((3,2))
# print(c)



# d = np.ones((2,1))
# print(d)



# e = np.full((2,3),7)
# print(e)



# f = np.eye(2,4)
# print(f)



# g = np.random.random((4,4))
# print(g)



# h = np.arange(3,50,4)
# print(h)



# i = np.linspace(0.,1.,num = 10)
# print(i)



# j = np.array([1,2,3])
# k = np.array([4,5,6])
# print(np.vstack((j,k)))



# l = np.array([1,2,3,4])
# m = np.array([5,6,7,8])
# print(np.hstack((l,m)))



# n = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# o = n[:2,1:3]
# print(o)
# print(n[0,1])
# o[0,0] = 57
# print(n[0,1])
# rowR1 = n[1,:]
# print(rowR1, rowR1.shape)
# rowR2 = n[1:3,:]
# print(rowR2, rowR2.shape)
# colR1 = n[:,1]
# print(colR1,colR1.shape)
# colR2 = n[:,1:2]
# print(colR2, colR2.shape)



# p = np.array([[1,2,3],[4,5,6]])
# boolIndex = (p>2)
# print(boolIndex)



# q = np.random.random(100000000)
# print(q)
# r = q.sum
# print(r)


# error
# s = np.array([[1,2],[4,5]], dtype = np.float64)
# t = np.array([[7,8],[10,11]], dtype = np.float64)
# print(s+t)
# print(np.sum(s,t))
# print(s-t)
# print(np.subtract(s,t))
# print(s*t)
# print(np.multiply(s,t))
# print(s/t)
# print(np.divide(s,t))
# print(np.sqrt(s))

# print(s.dot(t))
# print(np.dot(s,t))
# print(s @ t)

# print(np.min(s))
# print(np.max(t))
# print(np.sum(s))




# u = np.array([[1,2,3],[4,5,6]])
# print(u.T) #Transpose





a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([[9,8,7],[6,5,4],[3,2,1]])
print("\n 2 Dimentinal: \n")
print("Dot Product(2D): \n", a.dot(b))
print("\nInner Product(2D): \n",np.inner(a,b))
print("\nOuter Product(2D): \n",np.outer(a,b))
print("\nCross Product(2D): \n",np.cross(a,b))
c = np.array([1,2,3])
d = np.array([3,2,1])
print("\n\n")
print("-"*40)
print("#"*40)
print("-"*40)
print("\n\n\n 1 Dimentinal: \n")
print("\nDot Product(1D): \n", np.dot(c,d))
print("\nInner Product(1D): \n",np.inner(c,d))
print("\nOuter Product(1D): \n",np.outer(c,d))
print("\nCross Product(1D): \n",np.cross(c,d))










