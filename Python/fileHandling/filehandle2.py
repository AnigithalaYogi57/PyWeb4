# reverse a word, last line of last word of a file
'''
f = open('myfile.txt')
last_line = f.readlines()[-1]
words = last_line.split()
last_word = words[-1]
print(last_word[::-1])
f.close()
'''
# f = open('myfile.txt')
# print(f.readlines()[-1].split()[-1][::-1])
# f.close()

y = open('myfile.txt')
oupt = y.readline().split()
oupt.reverse()
res = " ".join(oupt)
print(res)
y.close()