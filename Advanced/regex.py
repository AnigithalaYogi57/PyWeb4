import re
'''
data = "abcabdefgcab"
ptn = input("Enter pattern to check:")
# m = re.match(ptn, data)
# m = re.fullmatch(ptn, data)
# m = re.search(ptn,data)
print(m)
if m:
    print("Match is available")
    print("match start index:",m.start(),"match end index:",m.end(), 'match:',m.group())
else:
    print("Match is not available")
'''
'''
data1="a7b9c5kz"
ptn = input("Enter pattern to check:")
m=re.findall(ptn,data1)
print(m)
for i in m:
    print(i)
'''
'''
data1="a7b9c5kz"
ptn = input("Enter pattern to check:")
# m=re.sub(ptn, "#", data1)
m = re.subn(ptn, "#", data1)
print(m)
print("no. of replacements are:",m[1])
'''
'''
l = re.split(',','sunny,bunny,chinny,vinny')
print(l)

l = re.split('\.', 'www.pythonorg.com')
print(l)

p= re.compile("[a-z]")
print(p)

# itr = re.finditer("[a-z]", "a7b9cde5k8z")
itr = re.finditer("[cd]", "a7b9cde5k8z")

for m in itr:
    print(m.start(),'-------',m.end(),'-------',m.group())
'''
'''
s="Learning Python is Very Easy"
# res=re.search("^Learn",s)
res=re.search("Easy$",s)

if res != None:
    # print("Target String starts with Learn")
    print("Target String ends with Easy")

else:
    print("Target String not starts with Learn")
'''

f = open('rawdata.txt', 'r')

d = f.read()

# print(d)
# ptn = "[6-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]"
ptn = "[6-9]\d{9}"
r = re.findall(ptn, d)
print(r)
match=re.findall("[a-zA-Z0-9_.]+@\w+[.]com",d)
print(match)