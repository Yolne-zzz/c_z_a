import random

# 定义出拳选项
choices = ["石头", "剪刀", "布"]

print("--- 欢迎来到石头剪刀布游戏！---")

while True:
    # 获取玩家输入
    user_choice = input("\n请输入 石头/剪刀/布 (输入'退出'结束游戏): ")

    # 退出机制
    if user_choice == "退出":
        print("游戏结束，下次再战！")
        break

    # 防呆设计：防止玩家乱输入
    if user_choice not in choices:
        print("❌ 输入无效，请检查错别字！")
        continue  # 跳过这次循环，重新开始

    # 电脑随机出拳
    computer_choice = random.choice(choices)
    print(f"🤖 电脑出了: {computer_choice}")

    # 判断胜负
    if user_choice == computer_choice:
        print("😐 结果：平局！")

    elif (user_choice == "石头" and computer_choice == "剪刀") or \
            (user_choice == "剪刀" and computer_choice == "布") or \
            (user_choice == "布" and computer_choice == "石头"):
        print("🎉 结果：你赢了！")

    else:
        print("😢 结果：你输了...")