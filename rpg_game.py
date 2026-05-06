import random
import time

def バトル(勇者名, レベル):
    print(f"\n=== ⚔️ {勇者名}の戦い（レベル {レベル}） ===")
    
    hp = 80 + レベル * 12
    mp = 25 + レベル * 6
    atk = 14 + レベル * 2
    
    敵一覧 = [
        {"名前": "スライム", "HP": 40, "攻撃力": 8, "経験値": 30},
        {"名前": "ゴブリン", "HP": 60, "攻撃力": 12, "経験値": 50},
        {"名前": "ドラゴン", "HP": 130, "攻撃力": 22, "経験値": 90}
    ]
    敵 = random.choice(敵一覧)
    敵hp = 敵["HP"]
    敵atk = 敵["攻撃力"]
    
    print(f"【{敵['名前']}】が現れた！ 戦闘開始！")
    
    while hp > 0 and 敵hp > 0:
        print(f"\n{勇者名} HP:{hp} MP:{mp}   |   {敵['名前']} HP:{敵hp}")
        print("1. 攻撃   2. 防御   3. 魔法攻撃 (MP消費)   4. 逃げる")
        選択 = input("行動を選択 (1〜4): ").strip()
        
        if 選択 == "1":
            ダメージ = atk + random.randint(-5, 7)
            敵hp -= max(1, ダメージ)
            print(f"お前は{敵['名前']}を攻撃！ {ダメージ}ダメージを与えた！")
        elif 選択 == "2":
            print("防御の構え！ 次の敵の攻撃が軽減される。")
            敵atk = max(3, 敵atk - 7)
        elif 選択 == "3":
            if mp >= 8:
                mp -= 8
                ダメージ = 28 + random.randint(-4, 9)
                敵hp -= max(1, ダメージ)
                print(f"魔法を唾いた！ {ダメージ}ダメージ！")
            else:
                print("MPが足りない...")
                continue
        elif 選択 == "4":
            print("賢く逃げ出した...")
            return False, 0
        else:
            print("無効な入力！")
            continue
        
        if 敵hp <= 0:
            break
        
        time.sleep(0.5)
        ed = 敵atk + random.randint(-2, 4)
        hp -= max(1, ed)
        print(f"{敵['名前']}の反撃！ {ed}ダメージを受けた！")
    
    if hp > 0:
        獲得exp = 敵["経験値"] + random.randint(5, 20)
        print(f"\n🎉 勝利！ {獲得exp}経験値を獲得！")
        return True, 獲得exp
    else:
        print("\n💀 敗北... 旅はここで終わった。")
        return False, 0

def main():
    print("🌟 勇者のお前 ～魔王城への道～ 🌟")
    print("お前は小さな村の勇者。魔王を倒す旅に出発する！")
    
    名前 = input("\n勇者の名前を入力 (デフォルト: 勇者): ").strip() or "勇者"
    exp = 0
    lv = 1
    勝利数 = 0
    
    while True:
        print(f"\n=== ステータス ===")
        print(f"名前: {名前}　レベル: {lv}　経験値: {exp}　勝利: {勝利数}")
        print("\n1. 戦闘する")
        print("2. ステータスを見る")
        print("3. 村で休む")
        print("4. 旅を終える")
        
        選 = input("\n選択: ").strip()
        
        if 選 == "1":
            勝ち, 得exp = バトル(名前, lv)
            if 勝ち:
                exp += 得exp
                勝利数 += 1
                if exp >= lv * 70:
                    lv += 1
                    print(f"\n✨ レベルアップ！ レベル {lv} になった！")
        elif 選 == "2":
            print(f"レベル {lv} / 経験値 {exp} / 勝利数 {勝利数}")
        elif 選 == "3":
            print("村でしっかり休んだ。体力が回復した！")
        elif 選 == "4":
            print("\n「また来てくれ、勇者よ」")
            break
        else:
            print("無効な選択。")
    
    print("\nプレイありがとう！ また魔王に挑みに来てね！")

if __name__ == "__main__":
    main()