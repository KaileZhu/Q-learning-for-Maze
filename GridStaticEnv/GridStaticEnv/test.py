# -*- coding:utf-8 -*-
import os

# os.path.dirname(__file__)返回的是.py文件的目录
path1 = os.path.dirname(__file__)
print(path1)

# os.path.abspath(__file__)返回的是.py文件的绝对路径（完整路径）
path2 = os.path.abspath(__file__)
print(path2)

# 组合使用
path3 = os.path.dirname(os.path.abspath(__file__))
print(path3)

# os.path.join()拼接路径
path4 = os.path.join(os.path.dirname(os.path.abspath(__file__)), '001.py')
print(path4)
