#!/bin/python3.9

import sys
from dataclasses import dataclass


@dataclass
class Iris:
    irisType: str
    sLen: float
    sWid: float
    pLen: float
    pWid: float

    def __init__(self, iris_type, s_len, s_wid, p_len, p_wid):
        self.irisType = iris_type
        self.sLen = s_len
        self.sWid = s_wid
        self.pLen = p_len
        self.pWid = p_wid


def readData(in_file):
    iris_list = []
    reading = False
    with open(in_file) as file:
        for line in file:
            if "@DATA" in line:
                reading = True
                continue
            if reading:
                fields = line.split(',')
                if "Iris-setosa" in fields[4]:
                    iris_type = "setosa"
                elif "Iris-virginica" in fields[4]:
                    iris_type = "virginica"
                elif "Iris-versicolor" in fields[4]:
                    iris_type = "versicolor"
                else:
                    iris_type = "unknown"
                iris_list.append(
                    Iris(iris_type, float(fields[0]), float(fields[1]), float(fields[2]), float(fields[3])))
    return iris_list


def procNumField(iris_list, field):
    vals = []
    for iris in iris_list:
        if field == 1:
            vals.append(iris.sLen)
        elif field == 2:
            vals.append(iris.sWid)
        elif field == 3:
            vals.append(iris.pLen)
        elif field == 4:
            vals.append(iris.pWid)
        else:
            print(f"Field {field} is invalid")
            exit(1)
    field_min = min(vals)
    field_max = max(vals)
    field_avg = round(sum(vals) / len(vals), 3)
    return field_min, field_max, field_avg


def countIrisTypes(iris_list):
    set_count = 0
    vir_count = 0
    ver_count = 0
    for iris in iris_list:
        iris_type = iris.irisType
        if iris_type == "setosa":
            set_count += 1
        elif iris_type == "virginica":
            vir_count += 1
        elif iris_type == "versicolor":
            ver_count += 1
    return set_count, vir_count, ver_count


def main(args):
    if len(args) != 2:
        print(f"Incorrect number of arguments. Expected 2, got {len(args)}")
        exit(1)

    iris_list = readData(args[1])

    field_min, field_max, field_avg = procNumField(iris_list, 1)
    print(f"Sepal Length: min = {field_min}, max = {field_max}, average = {field_avg}")
    field_min, field_max, field_avg = procNumField(iris_list, 2)
    print(f"Sepal Width: min = {field_min}, max = {field_max}, average = {field_avg}")
    field_min, field_max, field_avg = procNumField(iris_list, 3)
    print(f"Petal Length: min = {field_min}, max = {field_max}, average = {field_avg}")
    field_min, field_max, field_avg = procNumField(iris_list, 4)
    print(f"Petal Width: min = {field_min}, max = {field_max}, average = {field_avg}")

    num_set, num_vir, num_ver = countIrisTypes(iris_list)
    print(f"Iris Types: Iris Steosa = {num_set}, Iris Versicolor = {num_ver}, Iris Virginica = {num_vir}")


if __name__ == '__main__':
    main(sys.argv)
