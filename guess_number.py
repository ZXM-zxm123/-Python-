import random
import json
import os


def load_best_scores():
    """从文件加载最高分数记录"""
    if os.path.exists('best_scores.json'):
        with open('best_scores.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {'easy': None, 'medium': None, 'hard': None}


def save_best_scores(best_scores):
    """保存最高分数记录到文件"""
    with open('best_scores.json', 'w', encoding='utf-8') as f:
        json.dump(best_scores, f, ensure_ascii=False, indent=2)


def get_difficulty():
    """让用户选择难度级别"""
    print("\n请选择难度级别：")
    print("1. 简单 (1-50)")
    print("2. 中等 (1-100)")
    print("3. 困难 (1-200)")
    print("0. 退出游戏")
    
    while True:
        choice = input("\n请输入选项 (0-3): ")
        if choice == '0':
            return 'exit'
        elif choice == '1':
            return 'easy', 1, 50
        elif choice == '2':
            return 'medium', 1, 100
        elif choice == '3':
            return 'hard', 1, 200
        else:
            print("无效的选项，请重新输入！")


def get_user_guess(min_num, max_num):
    """获取用户的猜测输入"""
    while True:
        try:
            guess = int(input(f"\n请输入你的猜测 ({min_num}-{max_num}): "))
            if min_num <= guess <= max_num:
                return guess
            else:
                print(f"请输入 {min_num} 到 {max_num} 之间的数字！")
        except ValueError:
            print("请输入有效的整数！")


def play_game(min_num, max_num):
    """进行一轮猜数字游戏"""
    target_number = random.randint(min_num, max_num)
    attempts = 0
    
    print(f"\n游戏开始！我已经想好了一个 {min_num} 到 {max_num} 之间的数字。")
    
    while True:
        guess = get_user_guess(min_num, max_num)
        attempts += 1
        
        if guess < target_number:
            print("太小了！请再试一次。")
        elif guess > target_number:
            print("太大了！请再试一次。")
        else:
            print(f"\n恭喜你！猜对了！")
            print(f"目标数字是: {target_number}")
            print(f"你用了 {attempts} 次猜测。")
            return attempts


def main():
    """主游戏循环"""
    print("=" * 50)
    print("欢迎来到猜数字游戏！")
    print("=" * 50)
    
    best_scores = load_best_scores()
    
    while True:
        result = get_difficulty()
        
        if result == 'exit':
            print("\n感谢游玩！再见！")
            break
        
        difficulty, min_num, max_num = result
        
        # 显示当前难度的最高记录
        current_best = best_scores.get(difficulty)
        if current_best:
            print(f"\n{difficulty}难度的最少猜测次数记录: {current_best} 次")
        else:
            print(f"\n{difficulty}难度还没有记录，你将成为第一个挑战者！")
        
        # 进行游戏
        attempts = play_game(min_num, max_num)
        
        # 检查是否打破记录
        if not current_best or attempts < current_best:
            print(f"\n恭喜！你打破了{difficulty}难度的最少猜测次数记录！")
            print(f"原记录: {current_best if current_best else '无'} 次")
            print(f"新记录: {attempts} 次")
            best_scores[difficulty] = attempts
            save_best_scores(best_scores)
        
        # 询问是否继续游戏
        play_again = input("\n你想继续游戏吗？(y/n): ").lower()
        if play_again != 'y' and play_again != 'yes':
            print("\n感谢游玩！再见！")
            break


if __name__ == "__main__":
    main()
