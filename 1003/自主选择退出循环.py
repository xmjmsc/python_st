qwhile = "\n请输入内容："
qwhile += "\n请输入'退出'退出程序："
message = ""
while message != '退出':
    message = input(qwhile)
    if message != '退出':
        print(message)
