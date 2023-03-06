# -*- coding: utf-8 -*-
# @Author  : zhouxin
# @Time    : 2023/3/6 19:04
# @File    : aaaaa.py
# @annotation    :


class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)