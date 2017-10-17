# try:
#     f = open('../data/text', 'r')
#     print(f.read())
#
# except:
#     IOError

# finally:
# if f:
# f.close()

# 等价,会close file
# with open('../data/text', 'r') as file:
    # print(file.read())

with open('../data/text', 'r', encoding='utf-8') as file:
    for line in file:
        #末尾带有换行
        print(line.strip())

import os

print(os.name)
print(os.uname())
print(os.path.abspath('.'))
# os.mkdir('test')
# os.rmdir('test')

try:
    i = 10 / 0
except ZeroDivisionError as error:
    print(error)
finally:
    print('finally')



