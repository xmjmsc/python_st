current_number = 0 
#输出10以内的奇数
while current_number < 10: 
    current_number += 1 
    if current_number % 2 == 0: 
        continue
    #执行continue，直接忽略下面的代码，返回循环的开头

    print(current_number) 