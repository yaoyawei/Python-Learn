f = open('E:\\Farmer\\Python-Test\\Python-Learn\\testfiles\\test.txt', 'w')

#f.read()
f.write('Hello, world!!!!')
f.close()


# StringIO和BytesIO
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

# 
