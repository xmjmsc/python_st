import os

files = os.listdir('.')
for filename in files:
    portion = os.path.splitext(filename)
    if portion[1] == ".gjf":
    #if portion[1] == ".gjf" or portion[1] == ".in":
        newname = portion[0] + ".in"
        os.rename(filename, newname)
        with open('gau16.sh', 'r', encoding="utf-8") as f1:
            text = f1.readlines()
            text[15] = 'jobname=' + portion[0] + '\n'
        with open('gau16.sh', 'w', encoding="utf-8") as f1:
            f1.writelines(text)
        print(os.system("bsub <gau16.sh"))

# if portion[1] == ".gjf":
# 	newname = portion[0] + ".in"
# 	os.rename(filename,newname)
# f1 = open('gau16.sh', "r" ,encoding="utf-8")
# lines = f1.readlines()
# lines[15] = "jobname="+portion[0]+"\n"
# f2 = open('gau16.sh', "w" ,encoding="utf-8")
# f2.writelines(lines)
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
