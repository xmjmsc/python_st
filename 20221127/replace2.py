import os

files = os.listdir('.')
for filename in files:
    with open('gau16.sh', 'r', encoding="utf-8") as f1:
        text = f1.readlines()
        text[0] = '%nprocshared=20\n'
        text[1] = '%mem=10GB\n'
        text[2] = '#p bp86/def2svp opt=(TS,calcfc,noeigentest) freq scrf=(smd,solvent=PentylEthanoate) EmpiricalDispersion=GD3BJ iop(1/8=4)\n'
    with open('gau16.sh', 'w', encoding="utf-8") as f1:
        f1.writelines(text)








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
