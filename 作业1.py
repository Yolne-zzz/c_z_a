def calculate(num1, num2,operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 !=0:
            return num1 / num2
        else:
            return"错误：除数不能为0"
    else:
        return"错误：无效的运算符"
a=float(input("请输入第一个数字："))
b=float(input("请输入第二个数字："))
op=input("请输入运算符(+,-,*,/):")

result=calculate(a,b,op)
print(f"结果是：{result}")