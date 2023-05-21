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

print(ru.NIGHT_TSD)
print(ru.NIGHT_ALL)
print(ru.MORNING_TSD)
print(ru.TSD_DNT_WNT)
print(ru.TSD_CHOIS_DNT_WNT)
ans_tsd = input()

while ans_tsd != '1' or ans_tsd != '2':
  print(ru.ANS_ELSE)
  print(ru.TSD_CHOIS_DNT_WNT)
  ans_tsd = input()
  if ans_tsd == '1' or ans_tsd == '2':
   break
if ans_tsd == '1':
  print(ru.CLASS)
  print(ru.TSD_MTH, name, ru.TSD_MTH_NAME)
  print(ru.TSD_EXS)
  ans_exs = input()
  if ans_exs != 'x1=0,x2=2,x3=5':
    score_2 = random.randint(2, 4)
    print(ru.TSD_EXS_WRG, score_2)
    respect_2 = 0
  if ans_exs == 'x1=0,x2=2,x3=5':
    print(ru.TSD_EXS_RGHT)
    score_2 = 5
    print(ru.TSD_ANS_V)
    print(ru.CHOICE)
    ans_viet = input()
    while ans_viet != '1' or ans_viet != '2':
      print(ru.CHOICE)
      if ans_viet == '1' or ans_viet == '2':
        break
    if ans_viet == '1':
      print(ru.TSD_PRS)
      respect_2 = 1
    elif ans_viet == '2':
      print(ru.TSD_BAD)
      respect_2 = -1
  if hw == '1' and score_2 != 5:
    score_2 += 1
    print(ru.TSD_DN_HW, ru.PLS_HW, score_2)
  elif hw == '2' or score_2 == 5:
    score_2 = score_2
  if score_2 > 3:
    print(ru.TSD_GOOD_SCORE)
  else:
    print(ru.TSD_BAD_SCORE)
elif ans_tsd == '2':
  print(ru.TSD_TRNC)
  score_2 = 2
  respect_2 = 0
print(ru.WED_HW)
print(ru.CHOICE)
hw_2 = input()
if hw_2 != '1' and hw_2 != '2':
  while check:
    print(ru.ANS_ELSE)
    print(ru.CHOICE)
    hw_2 = input()
    if hw_2 == '1' or hw_2 == '2':
      check = False
print(ru.TSD_NIGHT)
print(ru.RSLT)
print(ru.SCORE, score_2)
print(ru.RESPECT, respect_2)
print(ru.NIGHT_ALL)

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

print(ru.THRSD_MRNG)
print(ru.THRSD_WAY)
print(ru.THRSD_CHOISE)
ans_thrsd = input()
while ans_thrsd != '1' and ans_thrsd != '2':
  print(ru.ANS_ELSE)
  print(ru.CHOICE)
  ans_thrsd = input()
  if ans_thrsd == '1' or ans_thrsd == '2':
    break
if ans_thrsd == '1':
  print(ru.THRSD_PTT)
  print(ru.THRSD_PTT_TM)
  print(ru.THRSD_SCORE)
  score_4 = 2
  respect_4 = 0
elif ans_thrsd == '2':
  print(ru.CLASS)
  print(ru.THRSD_MICRO, name)
  if hw_3 == '1':
    print(ru.THRSD_BRD_GD)
    score_4 = 5
    print(ru.THRSD_RESP)
    print(ru.THRSD_RESP_ANS)
    ans_micro = input()
    check = True
    if ans_micro != '1' and ans_micro != '2':
      while check:
        print(ru.ANS_ELSE)
        print(ru.THRSD_RESP_ANS)
        ans_micro = input()
        if ans_micro == '1' or ans_micro == '2':
          check = False
    if ans_micro == '1':
      print(ru.THRSD_ANS_WRG)
      respect_4 = -1
    if ans_micro == '2':
      print(ru.THRSD_ANS_GD)
      respect_4 = 1
  elif hw_3 == '2':
    score_4 = random.randint(2, 3)
    print(ru.THRSD_BRD_BD, score_4)
    print(ru.THRSD_RESP)
    print(ru.THRSD_RESP_ANS)
    ans_micro = input()
    check = True

    if ans_micro != '1' and ans_micro != '2':
      while check:
        print(ru.ANS_ELSE)
        print(ru.THRSD_RESP_ANS)
        ans_micro = input()
        if ans_micro == '1' or ans_micro == '2':
          check = False
    if ans_micro == '1':
      print(ru.THRSD_ANS_WRG)
      respect_4 = -1
    elif ans_micro == '2':
      print(ru.THRSD_ANS_GD)
      respect_4 = 1
  if score_4 > 3:
    print(ru.THRSD_PRS)
  else:
    print(ru.THRSD_BD)
print(ru.THRSD_HW)
print(ru.CHOICE)
hw_4 = input()
while hw_4 != '1' or hw_4 != '2':
  print(ru.ANS_ELSE)
  print(ru.CHOICE)
  hw_3 = input()
  if hw_4 == '1' or hw_4 == '2':
    break
print(ru.THRSD_NGHT)
print(ru.RSLT)
print(ru.SCORE, score_4)
print(ru.RESPECT, respect_4)
print(ru.NIGHT_ALL)

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

print(ru.STRD_MRNG)
print(ru.STRD_BD)
print(ru.STRD_I)
print(ru.STRD_BD_CHOISE)
ans_strd = input()
while ans_strd != '1' or ans_strd != '2':
  print(ru.ANS_ELSE)
  print(ru.STRD_BD_CHOISE)
  ans_strd = input()
  if ans_strd == '1' or ans_strd == '2':
   break
if ans_strd == '1':
  print(ru.STRD_BD_YES)
  print(ru.STRD_TM)
  print(ru.STRD_BD_YES_EV)
  score_6 = 2
  respect_6 = 0
elif ans_strd == '2':
  print(ru.CLASS)
  print(ru.STRD_CLASS)
  hw_dema = random.randint(1, 2)
  if hw_dema == '1':
    if hw_5 == '1':
      print(ru.STRD_HW_GD)
      resrect = 1
    elif hw_5 == '2':
      print(ru.STRD_HW_BD)
      print(ru.STRD_HW_BD_D)
      respect = -1
  print(ru.STRD_BRD, name, ru.STRD_BRD_CONT)
  print(ru.STRD_WNT)
  print(ru.STRD_BRD_CHOISE)
  ans_brd = input()
  while ans_brd != '1':
    print(ru.STRD_BRD_DEMA)
    print(ru.STRD_BRD_CHOISE)
    ans_brd = input()
    if ans_brd == '1':
      break
  print(ru.STRD_EXS)
  print(ru.STRD_EXS_CHOISE)
  ans_exs = input()
  while ans_exs != '2' or ans_exs != '1':
    print(ru.STRD_EXS_CHOISE)
    ans_exs = input()
    if ans_exs == '1' or ans_exs == '2':
      break
  if ans_exs == '1':
    score_6 = random.randint(2, 4)
    print(ru.STRD_EXS_WRG)
  elif ans_exs == '2':
    score_6 = 5
    print(ru.STRD_EXS_GD)

# Result

print(ru.END)
score = (score_1 + score_2 + score_3 + score_4 + score_5 + score_6) / 6
respect = respect_1 + respect_2 + respect_3 + respect_4 + respect_5 + respect_6
if score < 3 and respect < 3:
  print(ru.RES_SCORE, round(score, 2))
  print(ru.RES_RESP, respect)
  print(ru.END_BD)
elif score > 3 or respect >= 3:
  print(ru.RES_SCORE, score)
  print(ru.RES_RESP, respect)
  print(ru.END_GD)
print(ru.END_FNL)