import random

def get_user_choice():
    print("请选择: 剪刀(0), 石头(1), 布(2)")
    while True:
        try:
            choice = int(input("请输入你的选择: "))
            if choice in [0, 1, 2]:
                return choice
            else:
                print("无效输入，请输入 0, 1 或 2.")
        except ValueError:
            print("无效输入，请输入数字 0, 1 或 2.")

def get_computer_choice():
    return random.randint(0, 2)

def determine_winner(user, computer):
    if user == computer:
        return "平局!"
    elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
        return "你赢了!"
    else:
        return "你输了!"

def main():
    choices = ["剪刀", "石头", "布"]
    print("欢迎来到剪刀石布游戏!")
    
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"你选择了: {choices[user_choice]}")
    print(f"电脑选择了: {choices[computer_choice]}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()