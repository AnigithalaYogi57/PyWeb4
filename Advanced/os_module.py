import os
cwd = os.getcwd()
print('cwd1=',cwd)
os.chdir(os.pardir)
cwd2=os.getcwd()
print("cwd2=",cwd2)

d=os.listdir("Advanced")
for file in d:
    print(file)

os.chdir("databse")

print("cwd3=", os.getcwd())
os.chdir(os.pardir)
try:
    os.makedirs('osdir1/multiple/levels')
except FileExistsError:
    print("Already directories are created.")

fp = open("osdir1/multiple/levels/myfiles",'w')
fp.write("python\nweb\ndevelopment")
fp.close()

os.remove("osdir1/multiple/levels/myfiles")
os.removedirs("osdir1/multiple/levels")
os.chdir("Advanced")

# command = "ipconfig"
command = "dir"

os.system(command)