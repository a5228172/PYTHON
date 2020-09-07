mystr = "hello world and itcast and itheima and Python"

# 1. replace() 把and换成he  #** 说明replace函数有返回值，返回值是修改后的字符串
# new_str = mystr.replace('and', 'he')
# new_str = mystr.replace('and', 'he', 1)
# 替换次数如果超出子串出现的次数，表示替换所有这个子串
# new_str = mystr.replace('and', 'he', 10)
# # print(mystr)
# print(new_str)

# ***** 调用了replace函数后，发现原有字符串的数据并没有做到修改，修改后的数据是replace函数的返回值
# --- 说明 字符串是不可变数据类型
# 数据是否可以改变划分为 可变类型 和 不可变类型


# 2. split() -- 分割，返回一个列表, 丢失分割字符
# list1 = mystr.split('and')
# list1 = mystr.split('and', 2)
# print(list1)


# 3. join() -- 合并列表里面的字符串数据为一个大字符串
# mylist = ['aa', 'bb', 'cc']
#
# # aa...bb...cc
# new_str = '...'.join(mylist)
# print(new_str)
# mystr = "hello world and itcast and itheima and Python"

# 1. capitalize() 字符串首字母大写
# new_str = mystr.capitalize()

# 2.title(): 字符串中每个单词首字母大写
# new_str = mystr.title()

# 3. upper()：小写转大写
# new_str = mystr.upper()

# 4. lower(): 大写转小写
# new_str = mystr.lower()
# print(new_str)

mystr = "   hello world and itcast and itheima and Python   "
print(mystr)
# 1. lstrip(): 删除左侧空白字符
# new_str = mystr.lstrip()

# 2. rstrip(): 删除右侧空白字符
# new_str = mystr.rstrip()

# 3.strip()：删除两侧空白字符
new_str = mystr.strip()
print(new_str)
mystr = "hello world and itcast and itheima and Python"

# 1. startswith(): 判断字符串是否以某个子串开头
# print(mystr.startswith('hello'))
# print(mystr.startswith('hel'))
# print(mystr.startswith('hels'))


# 2. endswith(): 判断字符串是否以某个子串结尾
# print(mystr.endswith('Python'))
# print(mystr.endswith('Pythons'))


# 3. isalpha(): 字母
# print(mystr.isalpha())

# 4. isdigit(): 数字
# print(mystr.isdigit())
mystr1 = '12345'
# print(mystr1.isdigit())

# 5. isalnum() : 数字或字母或组合
# print(mystr1.isalnum())
# print(mystr.isalnum())
mystr2 = 'abc123'
# print(mystr2.isalnum())


# 6.isspace(): 空白
# print(mystr.isspace())
mystr3 = '   '
# print(mystr3.isspace())
