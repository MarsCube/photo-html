import os
import shutil


def content(text, filename):
    with open(filename, 'a',encoding='utf-8') as f:   # .txt可以不自己新建,代码会自动新建
        f.write("{}\n".format(text))    # 此时不需在第2行中的转为字符串

def getaa(path,filename):
    get_name = os.listdir(path)
    name = (os.path.splitext(get_name[0]))[0]
    name = name.replace("Brochure_", "")
    name = name.replace("_1", "")
    for i in get_name:
        if not os.path.exists(filename +"\\"+name+ "\img"):
            os.makedirs(filename +"\\"+name+ "\img")
        shutil.copy((path+'\\'+i),(filename +"\\"+name+ "\img"))
    a = '<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0" /><title>郑州冉码</title><link rel="stylesheet" type="text/css" href="../../Css/index.css"><script language="javascript" src="../../Js/index.js"></script></head><body>'
    b='<img class="imag" src="img\\'
    c = r'">'
    d = "</body>\n</html>"
    filename += ("\\"+name+"\index.html")
    content(a,filename)
    for i in range(len(get_name)):
        get_name[i] = b + get_name[i] + c
    for i in get_name:
        content(i, filename)
    content(d,filename)


# path = input("请输入文件夹地址：")
# filename = input("请输入目的地：")
# name=input("请输入图片名字：")


j = 1
for i in range(19):
    w = r'C:\Users\DJM\Desktop\cy'
    q = r"D:\git_code\wx.github.io\Cy"
    path = w
    filename=q
    if not i == 10:
        path += ("\\" + str(i))
        getaa(path, filename)
        print("完成第" + str(j) + "条。")
        j += 1
        



