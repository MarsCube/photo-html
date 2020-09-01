import os
import shutil



def content(text, filename):
    with open(filename, 'a',encoding='utf-8') as f:   # .txt可以不自己新建,代码会自动新建
        f.write("{}\n".format(text))    # 此时不需在第2行中的转为字符串


# path = input("请输入文件夹地址：")
# filename=input("请输入目的地：")
w = r'E:\Code\photo-html\test'
q = r"E:\Code\photo-html\out"
path = w
filename=q

get_name = os.listdir(path)
for i in get_name:
    if not os.path.exists(filename + "\img"):
        os.makedirs(filename+"\img")
    shutil.copy((path+'\\'+i),(filename+"\img"))
a = '<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0" /><title></title><style>img {margin: 20px;box-shadow: 0px 0px 5px grey;}</style></head>'
b='<img src="img\\'
c = r'">'
d = "</body>\n</html>"
filename += "\\index.html"
content(a,filename)
for i in range(len(get_name)):
    get_name[i] = b + get_name[i] + c
for i in get_name:
    content(i, filename)
content(d,filename)

