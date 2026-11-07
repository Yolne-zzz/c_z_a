import random
secret_number=random.randint(1,100)
guess_count=0
print("欢迎来到猜数字游戏！我心里想了一个1到100之间的数字。")

while True:
    try:
        guess=int(input("请输入你猜的数字："))
        guess_count+=1
        if guess<secret_number:
            print("太小了，再试一次！")
        elif guess>secret_number:
            print("太大了，再试一次！")
        else:
            print(f"恭喜你！猜对了！你一共猜了{guess_count}次。")
            break
    except ValueError:
        print("请输入一个有效的整数")