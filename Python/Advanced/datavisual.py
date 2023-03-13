from matplotlib import pyplot as plt
'''
x=[1,2,3,4,5,6,7,8,9,10]
y=[5,6,4,6,7,8,9,14,12,10]

x2=[1,2,3,4,5,6,7,8,9,10]
y2=[7,5,6,4,8,12,13,10,7,8]

plt.plot(x,y, label="india")
plt.plot(x2,y2, label="england")

plt.xlabel('over number')
plt.ylabel('runs')

plt.title('Score comparision')
plt.legend()
plt.show()
'''
plt.bar([1,3,5,7,9],[5,2,7,8,2],label='example1')
plt.bar([2,4,6,8,10],[8,6,2,5,6],label='example2',color='g')
plt.legend()
plt.xlabel("bar number")
plt.ylabel("bar height")
plt.title("mybargraph")
plt.show()