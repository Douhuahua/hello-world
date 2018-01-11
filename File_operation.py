#encoding=utf-8

import os

from os.path import getatime, getctime, getmtime, getsize
import datetime
file="F:\\1.txt"
#获取文件最近访问时间
print("访问时间:%s"%datetime.datetime.fromtimestamp(getatime(file)))

#获取文件的创建时间
print("创建时间：%s"%datetime.datetime.fromtimestamp(getctime(file)))

#返回最近文件修改时间
print("修改时间：%s"%datetime.datetime.fromtimestamp(getmtime(file)))

#返回文件大小,以字节为单位
print("文件大小为：%sB"%getsize(file))

#返回文件的路径文件名
print("文件路径%s,文件名%s"%os.path.split(file))
#返回文件名
print("文件名：%s"%os.path.basename(file))
#返回文件名以及后缀
print("文件名称：%s,文件类型:%s"%os.path.splitext(file))

#判断路径是否存在
path="F:\\python_tensorFlow\\"
print(os.path.exists(path))

#获取当前工作目录，此时可以增加文件或删除该路径中的文件
#获取当前工作目录
os.getcwd()
#切换当前路径到其他地方
os.chdir("E:\\test\\")
#可以获取更改后的路径
os.getcwd()
print(os.getcwd())

#判断文件是否存在，并抛出异常
try:
    data=open('missing.txt')
    print(data.readline(),end='')
except IOError as err:
    print('file error:'+str(err))
finally:
    #locals()为局部变量函数，返回一个key/value的字典
    if 'data' in locals():
        data.close()



os.chdir('F:\\')
content=open('1.txt','r')
context=[]
for eachline in content:
    context.append(eachline)
try:
    with open('2.txt','w') as txtfile:
        for j in context:
            txtfile.writelines(j)
        #下一行代码不能写入时不能换行，使用writelines()可以实现换行
        #print(context,file=txtfile)
except IOError as err:
    print('file error:'+str(err))
 
   
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,\
          ["Graham Chapman",\
           ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
#列表多层镶嵌，使用print_lol()
def print_lol(the_list):
    try:
        for i in the_list:
            #内核函数isinstance(),用来判断对象的类型；isinstance(object,class_or_turple)
            if isinstance(i,list):
                print_lol(i)
            else:
                print(i)
    except TypeError as err:
        print("Error information:"+str(err))
print_lol(movies)


import pickle
t1=('this is a string', 42, [1, 2, 3], None)
print(t1)
p1=pickle.dumps(t1)
print(p1)
t2=pickle.loads(p1)
print(t2)





