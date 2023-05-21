"""
"Game: Student day"
Group:
Tsvykh Viktoria
Fishchukova Sofia
"""

import ru_local as ru
import random as random

# Monday
name = input(ru.NAME)
print(f'{ru.HELLO} {name}!')
print(ru.GREETING)
print(ru.ESSENCE)
print(ru.SUCCESS)
print(ru.START)
print(ru.CHOICE)
ans = input()
while ans != '1':
    if ans == '2':
        print(ru.ANS_NO)
        while ans != '1':
            print(ru.START)
            print(ru.CHOICE)
            ans = input()
            break
    else:
        print(ru.ANS_ELSE)
        while ans != '1':
            print(ru.START)
            print(ru.CHOICE)
            ans = input()
            break
else:
    if ans == '1':
        print(ru.NIGHT)
        print(ru.NIGHT_ALL)
        print(ru.MND_MORNING)
        print(ru.MND_ROOMMATE)
        print(ru.CHOICE)
        ans_rmmate = input()
        check = True
        while ans_rmmate != '2' or ans_rmmate != '1':
            print(ru.ANS_ELSE)
            print(ru.MND_ROOMMATE)
            print(ru.CHOICE)
            ans_rmmate = input()
            if ans_rmmate == '1':
                print(ru.MND_TIME)
                print(ru.MND_PE_NO)
                score_1 = 2
                respect_1 = 0
                print(ru.HW)
                print(ru.CHOICE)
                hw = input()
                check = True
                while check:
                    print(ru.ANS_ELSE)
                    print(ru.CHOICE)
                    hw = input()
                    if hw == '1' or hw == '2':
                        check = False
                if hw == '1':
                    print(ru.SCORE, score_1)
                    print(ru.RESPECT, respect_1)
                    break
                if hw == '2':
                    print(ru.SCORE, score_1)
                    print(ru.RESPECT, respect_1)
                    break

            elif ans_rmmate == '2':
                print(ru.CLASS)
                print(ru.MND_PE_YES)
                print(ru.MND_PE)
                print(ru.MND_PE_CHOICE)
                pe_choice = input()
                check = True

                if pe_choice != '1' and pe_choice != '2':
                    while check:
                        print(ru.ANS_ELSE)
                        print(ru.MND_PE_CHOICE)
                        pe_choice = input()
                        if pe_choice == '1' or pe_choice == '2':
                            check = False
                if pe_choice == '1':
                    score_1 = random.randint(2, 5)
                    if score_1 <= 3:
                        print(ru.MND_BAD_SCORE)
                        respect_1 = 1
                    elif score_1 > 3:
                        print(ru.MND_GOOD_SCORE)
                        respect_1 = 1
                elif pe_choice == '2':
                    score_1 = 2
                    print(ru.MND_PE_LIE)
                    respect_1 = -1
                print(ru.HW)
                print(ru.CHOICE)
                hw = input()
                check = True
                while check:
                    print(ru.ANS_ELSE)
                    print(ru.CHOICE)
                    hw = input()
                    if hw == '1' or hw == '2':
                        check = False
                if hw == '1' or hw == '2':
                    print(ru.SCORE, score_1)
                    print(ru.RESPECT, respect_1)
                    break

# Tuesday

# Wednesday
print(ru.WED_MRNG)
print(ru.WED_RMMT)
print(ru.WED_RMMT_QSTN)
print(ru.WED_RMMT_CHOICE)
wed_rmmt_choice = input()

if wed_rmmt_choice == '2':
    print(ru.WED_RMMT_NO)
    score_3 = 2
    respect_3 = 0
    print(ru.WED_HW, ru.WED_HW_MICRO)
    print(ru.CHOICE)
    hw_3 = input()
    check = True
    if hw_3 != '1' and hw_3 != '2':
        while check:
            print(ru.ANS_ELSE)
            print(ru.CHOICE)
            hw_3 = input()
            if hw_3 == '1' or hw_3 == '2':
                check = False
    if hw_3 == '1' or hw_3 == '2':
        print(ru.WED_NIGHT)
        print(ru.RSLT)
        print(ru.SCORE, score_3)
        print(ru.RESPECT, respect_3)
        print(ru.NIGHT_ALL)

if wed_rmmt_choice == '1':
    print(ru.WED_RMMT_YES)
    print(ru.WED_ENG)
    print(ru.WED_ENG_1)
    print(ru.WED_ENG_2)
    print(ru.CHOICE)
    wed_eng_2 = input()
    check = True

    if wed_eng_2 != '1' and wed_eng_2 !='2':
        while check:
        print(ru.ANS_ELSE)
        print(ru.CHOICE)
        if wed_eng_2 == '1' or wed_eng_2 == '2':
            check = False

    if wed_eng_2 == '1':
        print(ru.WED_ENG_LIE)
        score_3 = 2
        respect_3 = 0
        print(ru.WED_NIGHT)
        print(ru.RSLT)
        print(ru.SCORE, score_3)
        print(ru.RESPECT, respect_3)
        print(ru.NIGHT_ALL)
    if wed_eng_2 == '2':
        print(ru.WED_ENG_TASK)
        print(ru.WED_ENG_TASK_1)
        print(ru.WED_ENG_TASK_ANS)
        wed_eng_task_ans = input()
        check = True

        if wed_eng_task_ans != '1' and wed_eng_task_ans != '2':
            while check:
                print(ru.ANS_ELSE)
                wed_eng_task_ans = input()
        if wed_eng_task_ans == '1' or wed_eng_task_ans == '2':
          check = False

        if wed_eng_task_ans == '1':
            score_3 = 5
            respect_3 = 1
            print(ru.WED_HW, ru.WED_HW_MICRO)
            print(ru.CHOICE)
            hw_3 = input()
            check = True

            if hw_3 != '1' and hw_3 != '2':
                while check:
                  print(ru.ANS_ELSE)
                  print(ru.CHOICE)
                  hw_3 = input()
                  if hw_3 == '1' or hw_3 == '2':
                    check = False

                  if hw_3 == '1' or hw_3 == '2':
                    if hw_2 == '1' and score_3 != 5:
                      score_3 += 1
                      respect_3 = 1
                      print(ru.WED_NIGHT)
                      print(ru.RSLT)
                      print(ru.SCORE, score_3)
                      print(ru.RESPECT, respect_3)
                      print(ru.NIGHT_ALL)
                    if hw_2 == '2':
                      print(ru.WED_NIGHT)
                      print(ru.RSLT)
                      print(ru.SCORE, score_3)
                      print(ru.RESPECT, respect_3)
                      print(ru.NIGHT_ALL)


        if wed_eng_task_ans == '2':
            score_3 = random.randint(2, 4)
            respect_3 = 1
            print(ru.WED_HW, ru.WED_HW_MICRO)
            print(ru.CHOICE)
            hw_3 = input()
            check = True

            if hw_3 != '1' and hw_3 != '2':
                while check:
                  print(ru.ANS_ELSE)
                  print(ru.CHOICE)
                  hw_3 = input()
                  if hw_3 == '1' or hw_3 == '2':
                    check = False

            if hw_3 == '1' or hw_3 == '2':
                if hw_2 == '1' and score_3 != 5:
                    score_3 += 1
                    respect_3 = 1
                    print(ru.WED_NIGHT)
                    print(ru.RSLT)
                    print(ru.SCORE, score_3)
                    print(ru.RESPECT, respect_3)
                    print(ru.NIGHT_ALL)
                if hw_2 == '2':
                    print(ru.WED_NIGHT)
                    print(ru.RSLT)
                    print(ru.SCORE, score_3)
                    print(ru.RESPECT, respect_3)
                    print(ru.NIGHT_ALL)

# Thursday

# Friday
print(ru.FR_MRNG)
print(ru.FR_QSNT)
print(ru.CHOICE)
fr_ans = input()
check = True
if fr_ans != '1' and fr_ans != '2':
    while check:
        print(ru.FR_QSNT)
        print(ru.CHOICE)
        fr_ans = input()
        if fr_ans == '1' or fr_ans == '2':
            check = False

if fr_ans == '1':
    print(ru.FR_QSNT_YES)
    score_5 = 2
    respect_5 = 0
    print(ru.HW)
    print(ru.CHOICE)
    hw = input()
    check = True
    if hw != '1' and hw != '2':
        while check:
            print(ru.ANS_ELSE)
            print(ru.CHOICE)
            hw = input()
            if hw == '1' or hw == '2':
                check = False
    if hw == '1':
        print(ru.SCORE, score_5)
        print(ru.RESPECT, respect_5)
    if hw == '2':
        print(ru.SCORE, score_5)
        print(ru.RESPECT, respect_5)

if fr_ans == '2':
    print(ru.FR_QSNT_NO)
    print(ru.FR_TASK)
    print(ru.FR_TASK_1)
    print(ru.FR_ANS)
    ans_test = input()
    check = True

    if ans_test != '1' and ans_test != '2':
        while check:
            print(ru.ANS_ELSE)
            print(ru.FR_TASK_1)
            print(ru.FR_ANS)
            ans_test = input()
            if ans_test == '1' or ans_test == '2':
                check = False

    if ans_test == '1':
        score_5 = 5
        respect_5 = 0
        print(ru.HW)
        print(ru.CHOICE)
        hw_5 = input()
        check = True

        if hw_5 != '1' and hw_5 != '2':
            while check:
                print(ru.ANS_ELSE)
                print(ru.CHOICE)
                hw_5 = input()
                if hw_5 == '1' and hw_5 == '2':
                    check = False
        if hw_5 == '1' or hw_5 == '2':
            if hw_4 == '1' and score_5 != 5:
                score_5 += 1
                respect_5 = 0
                print(ru.FR_NIGHT)
                print(ru.RSLT)
                print(ru.SCORE, score_5)
                print(ru.RESPECT, respect_5)

    if ans_test == '2':
        score_5 = random.randint(2, 4)
        print(ru.FR_ANS_BAD)
        respect_5 = 0
        print(ru.HW)
        print(ru.CHOICE)
        hw_5 = input()
        check = True

        if hw_5 != '1' and hw_5 != '2':
            while check:
                print(ru.ANS_ELSE)
                print(ru.CHOICE)
                hw_5 = input()
                if hw_5 == '1' and hw_5 == '2':
                    check = False

        if hw_5 == '1' or hw_5 == '2':
            if hw_4 == '1' and score_5 != 5:
                score_5 += 1
                respect_5 = 0
                print(ru.FR_NIGHT)
                print(ru.RSLT)
                print(ru.SCORE, score_5)
                print(ru.RESPECT, respect_5)
            if hw_4 == '2':
                print(ru.FR_NIGHT)
                print(ru.RSLT)
                print(ru.SCORE, score_5)
                print(ru.RESPECT, respect_5)
# Saturday

# Result
