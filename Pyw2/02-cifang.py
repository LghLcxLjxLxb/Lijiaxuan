# 求2的10次方，20次方，30次方，40次方，50次方，观察其增长趋势
for i in range(10, 51, 10):
    print('2的{0}次方为{1}'.format(i, 2**i))

# 2的10次方为1024
# 2的20次方为1048576
# 2的30次方为1073741824
# 2的40次方为1099511627776
# 2的50次方为1125899906842624
# 由此可见，增长得很快
