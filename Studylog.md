# Python

## BIF [![Python 内置函数](http://www.runoob.com/images/up.gif) Python 内置函数](http://www.runoob.com/python/python-built-in-functions.html)

###isinstance()判断类型

```python
isinstance(names,datatype)
#第一个参数提供对象名，第二个参数提供所判断的数据类型
#返回值为True/False
```

### len()长度

```python
返回某个数据对象的长度，或集合的项数
```

### print()输出内容

```python
print(内容, end='', file=fileObjectName)
#end=''关闭在输入中自动包含换行（默认会在输入末尾插入换行符，关了就没啦）
#file= 文件对象名称(默认输出到屏幕)
```

### split()分割数据

```python
split('spliter',number)#返回number+1个数组
for each_line in file:
    (Array1, Array2) = each_line.split(',', 1) #多重赋值
#spliter为分隔依据，如果一行有和number数目不一样的spliter数，从左向右优先级降低
#number为1的时候分两段
```

### open()打开文件（转换为文件对象）

```python
fileObject = open("file.txt","w") #返回文件对象，按行保存数据
#参数1 为文件名字符串
#参数2 （1）"w"以写的方式访问,"wb"二进制模式访问（2）"r"以读的方式访问，"wr"二进制模式访问
```

### help()获取help

```python
查看python所有的modules：help("modules")

单看python所有的modules中包含指定字符串的modules： help("modules yourstr")

查看python中常见的topics： help("topics")

查看python标准库中的module：import os.path + help("os.path")

查看python内置的类型：help("list")

查看python类型的成员方法：help("str.find") 

查看python内置函数：help("open")
```



### sorted()

#### 描述

**sorted()** 函数对所有可迭代的对象进行排序操作。

> **sort 与 sorted 区别：**
>
> sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
>
> list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。

#### 语法

sorted 语法：

```
sorted(iterable[, cmp[, key[, reverse]]])
```

参数说明：

- iterable -- 可迭代对象。
- cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
- key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
- reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。

#### 返回值

返回重新排序的列表。

#### 实例

以下实例展示了 sorted 的使用方法：



# Method



## Python strip()方法

[![Python 字符串](http://www.runoob.com/images/up.gif) Python 字符串](http://www.runoob.com/python/python-string.html)

------

### 描述

Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）。

### 语法

strip()方法语法：

```
str.strip([chars]);
```

### 参数

- chars -- 移除字符串头尾指定的字符。

### 返回值

返回移除字符串头尾指定的字符生成的新字符串。

### 实例

以下实例展示了strip()函数的使用方法：

```
#!/usr/bin/python

str = "0000000this is string example....wow!!!0000000";
print str.strip( '0' );
```

以上实例输出结果如下：

```
this is string example....wow!!!
```





### Python List pop()方法

[![Python 列表](http://www.runoob.com/images/up.gif) Python 列表](http://www.runoob.com/python/python-lists.html)

------

#### 描述

pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。

#### 语法

pop()方法语法：

```
list.pop(obj=list[-1])
```

#### 参数

- obj -- 可选参数，要移除列表元素的对象。

#### 返回值

该方法返回从列表中移除的元素对象。

#### 实例

以下实例展示了 pop()函数的使用方法：

```
#!/usr/bin/python

aList = [123, 'xyz', 'zara', 'abc'];

print "A List : ", aList.pop();
print "B List : ", aList.pop(2);
```

以上实例输出结果如下：

```
A List :  abc
B List :  zara
```

----

### 关键字

```
pass 
```

------

## fragmented 

- Python中字符串一旦创建就不可变，想要改变只能自身赋值替换。python变量只是引用，数据对象才包含数据。


### 不可变类型



-----


## Chapter1

### 列表

#####bullet points

- 列表是一个Python对象，有很多方法
- 列表可以存混合类型数据，是一个逻辑集合
- ​

#### 字面赋值

`name = ["string", intager, float]`

----

####方法

```python
name.insert(下标，内容)
```

-----

### 迭代

#### for循环处理列表

```python
for each_item in suite:
    print(each_item)
```

----

###控制

```python
if condition:
    "true"组
else:
    "false"组
```



----

### 函数

#### 创建

```python
def name(形参):
    code fence
```



#### 递归

嵌套太深则需要很多重复代码处理，这时可以创建自身调用的函数实现递归。

```python
#print_lol()
#1.0.0    实现打印列表中每一项的功能。
#1.1.0    增加一个可选参数level,每一次迭代就多输出一个"/t"
#1.1.1    增加一个可选参数indent,控制缩进开关
def print_lol(listName, indent=false, level=0):
    for each_itme in listName:
        if isinstance(listName,list):
            print_lol(each_item,level+1)
        else:
            if indent:
                for each_tab in range(level):
                    print("/t",end='')
            print(each_item)
```



----

## Chapter2
###模块
#### 发布模块

####模块的命名空间

```python
import nester
nester.print_lol(cast)#模块名.函数名  区别于 对象名.方法名 
```

```python
from nester import print_lol
print_lol(cast)  #当前空间的所有print_lol都是nester下的
```



------

##Chapter3：从文件输入和异常

### 处理异常

异常出现时，控制台会有一个traceback

####用try/except/finally机制处理

```python
try:
    code might crush
except:
    recovery
finally:
    file.close()
#执行顺序 try -> except -> finally
```

#### 用try with open/except处理

       ```python
try:
    with open("file_name1","r") as inputFile1, open("file_name2","r") as inputFile2:
    #用with处理会自动关闭文件流
        for e_l in inputFile:
            ......
except IOError as err:
    prin("File error:" + str(err))

       ```



###从文件输入

从文本文件向程序读入数据时，通过文件对象，一次到达**一个数据行**。

```python
the_file = open("sketch.txt")   #the_file是文件对象
for each_line in the_file:
    print(each_line,end="")  #逐行迭代,行后自带换行，所以去掉print中的换行
the_file.close()
```

-----

## Chapter4:数据持久储存

## pickle

保存数据为二进制

```python
import pickle
	...
with open("mydata.pickle", "wb") as mysavedata:
    pickle.dump([1, 2,"three"], mysavedata)
    ...
with open("mydata.pickle", "rb") as myrestoredata:
    a_list = pickle.load(myrestoredata)
```



----

## Chapter5:处理数据

### 列表推导

```python
#list comprehension
new_list = [functions(t) for t in old_list ]
#list dict set fileObject 都行
```

-----

## Chapter6：定制数据对象

###Python3 字典

字典是另一种可变容器模型，且可存储任意类型对象。

字典的每个键值(key=>value)对用冒号(**:**)分割，每个对之间用逗号(**,**)分割，整个字典包括在花括号(**{})**中 ,格式如下所示：

```
d = {key1 : value1, key2 : value2 }
```

键必须是唯一的，但值则不必。

值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。

一个简单的字典实例：

```
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
```

也可如此创建字典：

```
dict1 = { 'abc': 456 };
dict2 = { 'abc': 123, 98.6: 37 };
```

------

#### 访问字典里的值

把相应的键放入熟悉的方括弧，如下实例:

```
#!/usr/bin/python3

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
```

以上实例输出结果：

```
dict['Name']:  Runoob
dict['Age']:  7
```

如果用字典里没有的键访问数据，会输出错误如下：

```
#!/usr/bin/python3
 
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'};
 
print ("dict['Alice']: ", dict['Alice'])
```

以上实例输出结果：

```
Traceback (most recent call last):
  File "test.py", line 5, in <module>
    print ("dict['Alice']: ", dict['Alice'])
KeyError: 'Alice'
```

------

#### 修改字典

向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:

```
#!/usr/bin/python3

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8;               # 更新 Age
dict['School'] = "菜鸟教程"  # 添加信息


print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
```

以上实例输出结果：

```
dict['Age']:  8
dict['School']:  菜鸟教程
```

------

#### 删除字典元素

能删单一的元素也能清空字典，清空只需一项操作。

显示删除一个字典用del命令，如下实例：

```
#!/usr/bin/python3

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

del dict['Name'] # 删除键 'Name'
dict.clear()     # 删除字典
del dict         # 删除字典

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
```

但这会引发一个异常，因为用执行 del 操作后字典不再存在：

```
Traceback (most recent call last):
  File "test.py", line 9, in <module>
    print ("dict['Age']: ", dict['Age'])
TypeError: 'type' object is not subscriptable
```

**注：**del() 方法后面也会讨论。

##### 字典键的特性

字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。

两个重要的点需要记住：

1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：

```
#!/usr/bin/python3

dict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}

print ("dict['Name']: ", dict['Name'])
```

以上实例输出结果：

```
dict['Name']:  小菜鸟
```

2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：

```
#!/usr/bin/python3

dict = {['Name']: 'Runoob', 'Age': 7}

print ("dict['Name']: ", dict['Name'])
```

以上实例输出结果：

```
Traceback (most recent call last):
  File "test.py", line 3, in <module>
    dict = {['Name']: 'Runoob', 'Age': 7}
TypeError: unhashable type: 'list'
```

------

#### 字典内置函数&方法

Python字典包含了以下内置函数：

| 序号   | 函数及描述                                   | 实例                                       |
| ---- | --------------------------------------- | ---------------------------------------- |
| 1    | len(dict)计算字典元素个数，即键的总数。                | `>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}>>> len(dict)3` |
| 2    | str(dict)输出字典，以可打印的字符串表示。               | `>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}>>> str(dict)"{'Name': 'Runoob', 'Class': 'First', 'Age': 7}"` |
| 3    | type(variable)返回输入的变量类型，如果变量是字典就返回字典类型。 | `>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}>>> type(dict)<class 'dict'>` |

Python字典包含了以下内置方法：

| 序号   | 函数及描述                                    |
| ---- | ---------------------------------------- |
| 1    | [radiansdict.clear()](http://www.runoob.com/python3/python3-att-dictionary-clear.html)删除字典内所有元素 |
| 2    | [radiansdict.copy()](http://www.runoob.com/python3/python3-att-dictionary-copy.html)返回一个字典的浅复制 |
| 3    | [radiansdict.fromkeys()](http://www.runoob.com/python3/python3-att-dictionary-fromkeys.html)创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值 |
| 4    | [radiansdict.get(key, default=None)](http://www.runoob.com/python3/python3-att-dictionary-get.html)返回指定键的值，如果值不在字典中返回default值 |
| 5    | [key in dict](http://www.runoob.com/python3/python3-att-dictionary-in.html)如果键在字典dict里返回true，否则返回false |
| 6    | [radiansdict.items()](http://www.runoob.com/python3/python3-att-dictionary-items.html)以列表返回可遍历的(键, 值) 元组数组 |
| 7    | [radiansdict.keys()](http://www.runoob.com/python3/python3-att-dictionary-keys.html)以列表返回一个字典所有的键 |
| 8    | [radiansdict.setdefault(key, default=None)](http://www.runoob.com/python3/python3-att-dictionary-setdefault.html)和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default |
| 9    | [radiansdict.update(dict2)](http://www.runoob.com/python3/python3-att-dictionary-update.html)把字典dict2的键/值对更新到dict里 |
| 10   | [radiansdict.values()](http://www.runoob.com/python3/python3-att-dictionary-values.html)以列表返回字典中的所有值 |
| 11   | [pop(key[,default\])](http://www.runoob.com/python3/python3-att-dictionary-pop.html)删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。 |
| 12   | [popitem()](http://www.runoob.com/python3/python3-att-dictionary-popitem.html)随机返回并删除字典中的一对键和值(一般删除末尾对)。 |



##

