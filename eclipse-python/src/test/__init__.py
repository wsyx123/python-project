import re
res=r"t[io]p"
st="top tip tqp twp tep"
print(re.findall(res, st))

s="hello world,hello boy"
r=r"^hello"
e=r"boy$"
print(re.findall(r,s ))
print(re.findall(e, s))

# \d 匹配任何十进制数，相当于【0-9】
# \D 匹配任何非数字字符，相当于【^0-9】
num=r"^010-\d{8}"
number="010-12345678"
print(re.findall(num,number))

# * 匹配前一个字符重复0次或多次
# + 匹配前一个字符至少一次，或多次
# ？匹配一次或0次

