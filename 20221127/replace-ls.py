import os

with open('gau16.sh', 'r', encoding="utf-8") as f1:
    text = f1.readlines()
    text[15] = 'jobname=\n'
with open('gau16.sh', 'w', encoding="utf-8") as f1:
    f1.writelines(text)





# f1 = open('gau16.sh', "r" ,encoding="utf-8")
# lines1 = f1.readlines()
# lines1[15] = "jobname=cdcsc"+"\n"
# f2 = open('gau16.sh', "w" ,encoding="utf-8")
# print(lines1)
# f2.writelines(lines1)
# print("ok")
# replace_with = "jobname=cdsdcsdvv"
# search = "jobname="
# fd1 = open('gau16.sh','r')
# fd2 = open('gau16.sh', 'w')
# for line in fd1.readlines():
#     if line.find(search) > -1:
#         fd2.write(replace_with)
#     else:
#         fd2.write(line)
# fd1.close()
# fd2.close()
