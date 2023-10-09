# 简单验证身份证号是否合法
import re
card = input('请输入待验证的身份证号：')
pattern = re.compile(
    r'^[1-9]\d{5}(18|19|20)\d{2}(0[1-9]|1[0-2])(([0-2][1-9])|10|20|(3[0-1]))\d{3}[\dX]$')
result = pattern.search(card)
print(result)
