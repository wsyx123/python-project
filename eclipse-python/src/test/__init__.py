import re
res=r"t[io]p"
st="top tip tqp twp tep"
print(re.findall(res, st))

s="hello world,hello boy"
r=r"^hello"
e=r"boy$"
print(re.findall(r,s ))
print(re.findall(e, s))

# \d ƥ���κ�ʮ���������൱�ڡ�0-9��
# \D ƥ���κη������ַ����൱�ڡ�^0-9��
num=r"^010-\d{8}"
number="010-12345678"
print(re.findall(num,number))

# * ƥ��ǰһ���ַ��ظ�0�λ���
# + ƥ��ǰһ���ַ�����һ�Σ�����
# ��ƥ��һ�λ�0��

