import re


# 1行にするときに使用する
def oneline(element_list: list, path: str):
    num_list = list()
    for element in element_list:
        num_list.append((element)[0])
    with open(path + "-oneline.csv", "w", encoding="utf-8") as f:
        f.write(",".join(num_list))


# 学部/学科の名称を変更する
def rename(element_list: list, path: str):
    for element in element_list:
        if (element[2] == "P院"):
            element[2] = "T"
        elif (element[2] == "T院"):
            element[2] = "Y"
        elif (element[2] == "AC専攻"):
            element[2] = "ac"
        elif (element[2] == "EDM専攻"):
            element[2] = "edm"
        elif (element[2] == "KVU専攻"):
            element[2] = "kvu"
        elif (element[2] == "T部（共通）"):
            element[2] = "Q"
        else:
            element[2] = re.match(r"\w", element[2]).group()
    with open(path + ".csv", "w", encoding="utf-8") as f:
        for element in element_list:
            f.write(",".join(element))
            f.write("\n")


# インポートされたcsvをリストに変換する
def convert_list(path: str):
    element_list = list()
    with open(path + "-original.csv", "r", encoding="utf-8") as f:
        for line in f:
            element = line.strip().split(",")
            element_list.append(element)
    return element_list


# 学部/学科ごとにcsvを抽出する
def extract(year: str, element_list: list):
    num_list = list()

    for i in range(len(element_list)-1):
        num_list.append((element_list[i])[0])
        if ((element_list[i])[2] != (element_list[i+1])[2]):
            with open("./timetable/" + year + "/csv/" + (str(element_list[i][2])) + "-official.csv", "w", encoding="utf-8") as f:
                f.write(",".join(num_list))
            num_list.clear()
    num_list.append((element_list[i+1])[0])
    with open("./timetable/" + year + "/csv/" + (str(element_list[i][2])) + "-official.csv", "w", encoding="utf-8") as f:
        f.write(",".join(num_list))


def main():
    year = "2022"
    omiya = "./timetable/" + year + "/omiya"
    # umeda = "./timetable/" + year + "/umeda"
    # hirakata = "./timetable" + year + "/hirakata"

    for campus in [omiya]:
        element_list = convert_list(campus)
        # oneline(element_list, campus)
        # rename(element_list, campus)
        extract(year, element_list)


if __name__ == "__main__":
    main()
