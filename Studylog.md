# Python

## BIF

###isinstance()判断类型

```python
isinstance(names,datatype)
//第一个参数提供对象名，第二个参数提供所判断的数据类型
//返回值为True/False
```

### len()长度

```python
返回某个数据对象的长度，或集合的项数
```

### print()输出内容

```python
print(内容,end='')
//end=''关闭在输入中自动包含换行（默认会在输入末尾插入换行符，关了就没啦）
```





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
//print_lol()
//1.0.0    实现打印列表中每一项的功能。
//1.1.0    增加一个可选参数level,每一次迭代就多输出一个"/t"
//1.1.1    增加一个可选参数indent,控制缩进开关
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
nester.print_lol(cast)//模块名.函数名  区别于 对象名.方法名 
```

```python
from nester import print_lol
print_lol(cast)  //当前空间的所有print_lol都是nester下的
```







