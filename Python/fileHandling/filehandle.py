# f=open("myfile.txt", "r")
# print(f)
# print(f.read())
# f.close()
'''
x=open("myfile.txt", "w")
x.write("Hello!\nHow are you.\nThank you.")
x.close()
'''
'''
y=open("myfile.txt")
print(y.read())
y.seek(8)
print(y.tell())
print(y.read())
print(y.tell())
y.close()
'''
# z=open("myfile1.txt",'a')
# z.write("\nThis is appended")
# z.close()
p=open('myfile.txt')
# r=p.readline()
# for i in r:
#     print(i)
r=p.readlines()
print(r)
p.close()
