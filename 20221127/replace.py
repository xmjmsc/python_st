import os

files = os.listdir('.')
for filename in files:
    f1 = open(filename, "r")
    content = f1.read()
    f1.close()
    t = content.replace("%nprocshared=24", "%nprocshared=20")
    with open(filename, "w") as f2:
        f2.write(t)
    f2.close()




# for file in files:
# with open(file,"r",encoding="utf-8") as f:
# 	lines = f.readlines()
# # with open(file,"w",encoding="utf-8") as f_w:
# 	for line in lines:
# 		if "%nprocshared=20" in line:
# 			line = line.replace("%nprocshared=20","%nprocshared=20")
# 	f.write(line)


# for filename in files:
# 	portion = os.path.splitext(filename)
# 	if portion[1] == ".gjf":  
# 		newname = portion[0] + ".in"   
# 		os.rename(filename,newname)
