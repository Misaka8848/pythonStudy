# Python

## BIF

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





----

## 关键字

```
pass 
```

------

## fragmented 

- Python中字符串一旦创建就不可变，想要改变只能自身赋值替换。python变量只是引用，数据对象才包含数据。




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

