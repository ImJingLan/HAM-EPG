import json
import sys
import random
import datetime
import os


Question_Num = [1, 30, 50, 80, 0]

Bank_Count = [365, 365, 689, 1066, 1237]

json_list = ['a.json', 'a.json', 'b.json', 'c.json', "all.json"]

Option_Map = {'1': 'A', '2': 'B', '3': 'C', '4': 'D'}

Bank_Map = {'1': 'A', '2': 'B', '3': 'C', '4': 'All', "0": 'Single'}


def mkdir(path):

    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)
    else:
        os.path.exists(path)


def getLastDate():
    return str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))


if __name__ == "__main__":
    print("HAM Examination Questions Picker By Yurik\nWhich Question Bank You Want To Use\n0.Single(Default) 1.Class A  2.Class B  3.Class C  4.ALL(Deving)")
    num = input() or '0'
    num = int(num)

    with open("./Jsons/"+json_list[num], 'r', encoding="utf-8") as f:
        bank = json.load(f)

    if (num == 4):
        Question_Num = input(
            "How Many Questions You Want (Default 30): ") or "30"

        Question_Num = int(Question_Num)

    else:
        Question_Num = Question_Num[num]

    Bank_Count = Bank_Count[num]

    res = random.sample(range(1, Bank_Count+1), Question_Num)

    data = [0]*(Question_Num)

    answer = [0]*(Question_Num)

    for i in range(0, len(res)):
        ans = [bank[res[i]-1]['A'], bank[res[i]-1]['B'],
               bank[res[i]-1]['C'], bank[res[i]-1]['D']]

        random.shuffle(ans)

        data[i] = {"id": i+1, "uid": bank[res[i]-1]['id'], "question": bank[res[i]-1]
                   ['question'], "A": ans[0], "B": ans[1], "C": ans[2], "D": ans[3]}

        correct_ans = 0

        for j in range(0, 4):
            if (ans[j] == bank[res[i]-1]['A']):
                correct_ans = Option_Map[str(j+1)]
                answer[i] = {"id": i+1, "uid": bank[res[i]-1]['id'], "question": bank[res[i]-1]['question'], "option": correct_ans,
                             "content": bank[res[i]-1]['A']}

    mkdir("Papers")

    path = "./Papers/"+getLastDate()+"_"+Bank_Map[str(num)]

    mkdir(path)

    data = {"contestId": int(
        getLastDate()), "contestGroup": Bank_Map[str(num)], "questions": data}

    question_file = open(path+"/Paper.json", "w", encoding="utf-8")

    question_file.write(json.dumps(data, ensure_ascii=False))

    answer = {"contestId": int(
        getLastDate()), "contestGroup": Bank_Map[str(num)], "questions": answer}

    question_file = open(path+"/Answer.json", "w", encoding="utf-8")

    question_file.write(json.dumps(answer, ensure_ascii=False))

    print("The Contest Has Beed Generated in "+path)
