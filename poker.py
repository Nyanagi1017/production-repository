import random
import time

while (True):
    print('--------------------------------------------------------')
    try:
        # トランプを用意
        marklist = ['♥','♦','♠','☘']
        card = []
        player_score = 0
        CPU_score = 0

        for i in range(4):
            mark = marklist[i]
            for num in range(13):
                card.append([[mark],[num+1]])

        #print(card)


        p1_card_list = []
        p2_card_list = []
        p3_card_list = []
        front_card_list = []

        p1_card_list.append(card.pop(random.randint(0,51)))
        p1_card_list.append(card.pop(random.randint(0,51)))
        print(p1_card_list)

        p2_card_list.append(card.pop(random.randint(0,51)))
        p2_card_list.append(card.pop(random.randint(0,51)))

        p3_card_list.append(card.pop(random.randint(0,51)))
        p3_card_list.append(card.pop(random.randint(0,51)))

        # print(p1_card_list)
        # print(p2_card_list)
        # print(p3_card_list)

        for i in range(3):
            front_card_list.append(card.pop(random.randint(0,51)))
        print(front_card_list)

        p1_first_select = int(input('1:フォールド　2:ベット'))

        if p1_first_select == 1:
            print('フォールド')
            break
        elif p1_first_select == 2:
            front_card_list.append(card.pop(random.randint(0,51)))
            print(front_card_list)
            p1_second_select = int(input('1:フォールド　2:ベット'))
            if p1_second_select == 1:
                print('フォールド')
                break
            elif p1_second_select == 2:
                front_card_list.append(card.pop(random.randint(0,51)))
                print(front_card_list)
                for i in range(5):
                    p1_card_list.append(front_card_list[i])
                print(p1_card_list)
                
                # 5枚選ぶ
                p1_select = []
                for i in range(5):
                    p1_select.append(int(input('カードを選択：')))
                p1_select_card = []
                for i in range(5):
                    p1_select_card.append(p1_card_list[p1_select[i]-1])
                print(p1_select_card)
                
                break
                
    except:
        print('ランダム数値取得エラー')