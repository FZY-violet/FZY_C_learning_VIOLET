current_number = 0
while current_number < 1000:
    current_number += 1#步长为一
    if current_number % 2 == 0:#被2整除的余数
        continue#如果可以被2整除那么此项便忽略余下的代码，下一项返回初始。
    print(current_number)