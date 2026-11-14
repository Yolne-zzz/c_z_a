import random
import string


def generate_password(length):
    # 定义密码包含的字符：大小写字母 + 数字 + 标点符号
    characters = string.ascii_letters + string.digits + string.punctuation

    # 使用列表推导式（一种简写循环）从字符中随机挑选
    # 如果你不理解推导式，也可以写成：
    # password = ""
    # for i in range(length):
    #     password += random.choice(characters)

    password = ''.join(random.choice(characters) for i in range(length))

    return password

# 主程序
try:
    user_length = int(input("请输入你想要生成的密码长度（建议8位以上）: "))
    if user_length < 4:
        print("密码太短不安全，请至少输入4位。")
    else:
        new_password = generate_password(user_length)
        print(f"为你生成的随机密码是: {new_password}")
except ValueError:
    print("请输入有效的数字！")