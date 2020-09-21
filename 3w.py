#!/usr/bin/env python
# coding: utf-8

# **Упражнение 1:** создайте произвольный текстовый файл с несколькими строками произвольного текста. Выведите в консоль строки файла, удалив лишние пробелы в начале и конце строк, если они есть. \

# In[2]:


with open("file_1task", "w") as file:
    file.write("dfddfdsfs\n" + "fdfdfdf")
with open("file_1task", "r") as file:
    for line in file:
        print(line.strip())


# **Упражнение 2:** запишите в новый файл содержимое списка строк (каждую строку с новой строки) без использования цикла.
# 

# In[2]:


def write_array(arr, file_name):
    arr = map(lambda x : x+'\n', arr)
    file_name.writelines(arr)
    
list1 = ["abc", "bca", "cda"]
with open("file_2task", "w") as file:
    write_array(list1, file)
with open("file_2task", "r") as file:
    for line in file:
        print(line.strip())


# **Упражнение 3:** Вам дана в архиве **main.zip** файловая структура, состоящая из директорий и файлов.
# 
# Вам необходимо распаковать этот архив (средствами языка python), и затем найти в данной в файловой структуре все директории, в которых есть хотя бы один файл с расширением “.py”.
# 
# Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.

# In[4]:


import zipfile
with zipfile.ZipFile("main.zip", 'r') as zip_ref:
    zip_ref.extractall("main_contents")


# In[24]:


import os
from pathlib import Path
p = Path("main_contents")
files = list(p.glob('**/*.py'))
out = set()
for path in files:
    out.add(path.parts[-2])
out_list = list(out)
out_list.sort()
with open("file_3task", "w") as file3:
    write_array(out_list, file3)
with open("file_3task", "r") as file3:
    for line in file3:
        print(line.strip())


# # 4
# Загрузить 1.json из папки w3/ и открыть его в питоне. Добавить внутрь "GlossEntry" свойство {"week": 3} и сохранить результат в файл 1.json двумя способами:
# 
#     через json.dumps()
#     через json.dump()
# 

# In[27]:


import json
with open("1.json", "r") as file:
    data = json.load(file)
    data_initial = data.copy()
    print(json.dumps(data, indent=4, sort_keys=True))
    to_add = {"week": 3}
    temp = data["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"]
    temp["week"] = 3
# with open("1.json", "w") as file:
#     json.dump(data, file, indent=4)
with open("1.json", "w") as file:
    file.write(json.dumps(data, indent=4))
with open("1.json", "r") as file:
    data1 = json.load(file)
    print(json.dumps(data1, indent=4, sort_keys=True))


# # 5
# Посмотреть на 1.json не в питоне. Увидеть, что все данные немного отличаются от питоновских (булевы переменные стали с маленькой буквы, None превратился в null). Это связано с тем, что JSON изначально создавался для JavaScript и поэтому имеет такие же названия.

# In[1]:


from IPython.display import Image
Image(filename='screen1.png')


# # 6
# Загрузить table.csv из папки w3/ и открыть его в питоне. Считать содержимое в массив. Добавить в массив строку из повторяющихся чисел -200 в середину файла и сохранить массив в CSV-файл с именем middle_row.csv.

# In[73]:


import csv
def read_my_csv(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
read_my_csv("table.csv")


# In[108]:


import pandas as pd
import numpy as np
df = pd.read_csv('table.csv', sep=';', header=None)
df_out = pd.DataFrame(np.insert(df.values, int(len(df)/2), values=[-200, -200, -200, -200], axis=0))
df_out.to_csv('middle_row.csv', index=False, header=0)


# [Pandas Documentation](https://pandas.pydata.org/docs/user_guide/index.html#user-guide) \
# [Про атрибут axis у numpy](https://www.sharpsightlabs.com/blog/numpy-axes-explained/)

# Проверяем корректную запись в файл:

# In[109]:


read_my_csv("middle_row.csv")


# # 7
# Загрузить table.csv из папки w3/ и открыть его в питоне. Считать содержимое в массив. Добавить колонку (!) с именем my_col и значениями на каждом ряду True. Сохранить полученный массив в CSV-файл с именем new_col.csv.

# In[110]:


df2 = pd.read_csv('table.csv', sep=';', header=0)
df2['my_col'] = [True for i in range(len(df2))]
df2.to_csv('new_col.csv', index=False)
read_my_csv("new_col.csv")


# # 8
# Создать код, который выбрасывает ZeroDivisionError. Обернуть его в try/except и вывести "Делим на ноль" в случае деления на ноль.

# In[111]:


try:
    k = 1 / 0
except ZeroDivisionError:
    print("Делим на ноль")


# # 9
# Создать код, который может выбросить ValueError (это может быть попытка привести к int "плохую" строку). Окружить код try/except и добавить finally блок, где вывести "Дошел до finally". Попробовать запустить программу нормально (без выбрасывания исключения) и с исключением. В обоих случаях должен выполняться код из finally.

# In[123]:


try:
    int("abc")
except ValueError:
    print("You are trying to make a number from a text you dumb-ass fuck")
finally:
    print("\"finally\" block executed")


# In[124]:


try:
    int("3")
except ValueError:
    print("You are trying to make a number from a text you dumb-ass fuck")
finally:
    print("\"finally\" block executed")


# # 10
# Создать свое исключение (название любое). Написать код, который выбрасывает его с неким сообщением. Не перехватывайте это исключение в коде - цель задания заключается в том, чтобы увидеть, как он отображается в консоли.

# In[136]:


class NumberIsTooLow(Exception):
    def __init__(self, number):
        self.number = number
        self.message = "You have entered: " + str(number) + " - " + "This number is too low"
        super().__init__(self.message)

number = 7
if (number < 10):
    raise NumberIsTooLow(number)


# ## Объяснение про super()

# [Python's super() documentation](https://docs.python.org/3/library/functions.html#super)

# In[1]:


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


# Here, you’ve used **super()** to call the **\_\_init\_\_()** of the Rectangle class, allowing you to use it in the Square class without repeating code. Below, the core functionality remains after making changes:

# In[2]:


square = Square(4)
square.area()


# # 11
# Написать код, который вызывает функции в порядке a() -> b() -> c(), а в функцию c заложите raise ValueError('my exception') (функции a, b, c надо самому объявить). Посмотрите на стек-трейс - видно ли, где из трех функций появилась ошибка? Сделайте скриншот, залейте в репозиторий и будьте готовы ответить на вопросы по чтению stack trace.

# In[139]:


def a():
    print("Function a executed")
def b():
    print("Function b executed")
def c():
    int("abc")
    print("Function c executed")
a()
b()
c()


# In[141]:


from IPython.display import Image
Image(filename='tracestack.jpg')

