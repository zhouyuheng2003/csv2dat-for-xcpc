import csv
problemNumber = 12 #题目数量
csvFilePath = 'content.csv'  # csv路径
contestName = "The 19th Heilongjiang Provincial Collegiate Programming Contest"
contestLength = 300 #比赛时长（单位分钟）
problems = []
teams = []
submissions = []

def gen_problems():
    for i in range (0,problemNumber):
        problems.append( f"@p {chr(ord('A')+i)},{chr(ord('A')+i)},20,0")

def parse_csv_with_comma_count(file_path):
    data = []  # 存储解析后的数据

    # 打开CSV文件
    with open(file_path, mode='r', encoding='utf-8-sig') as file:
        csv_reader = csv.reader(file)
        
        # 逐行读取CSV文件
        for line in csv_reader:
            pl = 0
            teamid = 0
            name = ""
            school = ""
            char_to_int_map = {}
            for i in range(0,problemNumber):
                char_to_int_map[chr(ord('A')+i)] = 0
            problemid = 0
            for token in line:
                token = token.replace('\n', '|')
                pl = pl + 1
                if(pl == 1):
                    teamid = token
                if(pl == 2):
                    name =token
                if(pl == 3):
                    school =token
                    teams.append( f"@t {teamid},0,1,\"{school} - {name}\"")
                if(pl > 3):
                    problemchar=chr(ord('A')+problemid)
                    if token.startswith('-'):
                        if(token == '-'):
                            ccc = 1
                        elif token[1:].isdigit():
                            X = int(token[1:])
                            for j in range(0,X):
                                char_to_int_map[problemchar]+=1
                                submissions.append(f"@s {teamid},{problemchar},{char_to_int_map[problemchar]},{j},WA")
                    elif token.startswith('+'):
                        if '|' in token:
                            parts = token[1:].split('|')  # 分割token
                            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                                X = int(parts[0])
                                Y = int(parts[1])
                                for j in range(0,X):
                                    char_to_int_map[problemchar]+=1
                                    submissions.append(f"@s {teamid},{problemchar},{char_to_int_map[problemchar]},{j},WA")
                                char_to_int_map[problemchar]+=1
                                submissions.append(f"@s {teamid},{problemchar},{char_to_int_map[problemchar]},{Y*60},OK")
                    elif token.isdigit():
                        char_to_int_map[problemchar]+=1
                        submissions.append(f"@s {teamid},{problemchar},{char_to_int_map[problemchar]},{int(token)*60},OK")
                    problemid = problemid + 1
#                 print(token, end=",")
    return data

gen_problems()
parsed_data = parse_csv_with_comma_count(csvFilePath)

# 输出解析后的数据
# for row in parsed_data:
#     print(row)

# print("@contest \""+contestName+"\"")
# print("@contlen "+str(contestLength))
# print("@problems "+str(problemNumber))
# print("@teams")
# print("@submissions")
# for row in problems:
#     print(row)
# for row in teams:
#     print(row)
# for row in submissions:
#     print(row)

with open("result.txt", "w", encoding="utf-8") as file:
    file.write("@contest \"" + contestName + "\"\n")
    file.write("@contlen " + str(contestLength) + "\n")
    file.write("@problems " + str(problemNumber) + "\n")
    file.write("@teams\n")
    file.write("@submissions\n")
    for problem in problems:
        file.write(problem)
        file.write("\n")
    for team in teams:
        file.write(team)
        file.write("\n")
    for submission in submissions:
        file.write(submission)
        file.write("\n")

print("内容已成功写入到 result.txt 文件中。")