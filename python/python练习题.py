'''#课堂练习1：
# 定义以下几个变量：name=”小明” length=178   id=1
# 格式化输出：我的名字是小明，身高是178.00cm，学号是001
name='小明'
length=178
id=1
print('我的名字是:%s,身高是:%.2f,学号是:%03d'%(name,length,id)#单引号引用字符串和字符类型，引号外写%（类型名1，2，3）'''
import random

'''# 课堂练习2：
# 定义小数 price、weight、money，输出 苹果单价 9.00 元／斤，购买了 5.00 斤，需要支付 45.00 元
price=9.00
weight=5.00
money=45.00
print('苹果单价%.2f元/斤，购买了%.2f斤，需要支付元%.2f'%(price,weight,money))  # %.nf,n代表小数点后位数，%0nd,不足n，用0补'''
'''#课堂练习3
#定义以下几个变量：name=”小明”，length=178 ，id=1 ，并用f-格式化进行输出
name='小明'
length=178
id=1
print(f'我的名字是{name}，我的身高是{length},我的学号是{id}')'''
'''#课堂练习4
#print('人生苦短，')
#print('我用python')
# 自己运行，并在运行之后修改print结束符的方式修改程序，使的程序的输出为：人生苦短，我用python
print('人生苦短，',end='')#更改换行符用，end=‘'/'/n'/'/t'/'...'
print('我用python')
'''
#课堂练习5
#需求:
#收银员输入苹果的价格,单位:元/斤
#收银员输入用户购买苹果的重量,单位:斤
#计算并输出付款金额
'''PriceApple=input('请输入苹果的价格')
PriceApple=float(PriceApple)             #输入默认类型为字符串，所求为浮点型，需要强制类型转换
WeightApple=input('请输入用户购买苹果的重量')
WeightApple=float(WeightApple)
Count=PriceApple*WeightApple
print('付款金额为：%.2f'%Count)'''
'''#课堂练习题6
#编程实现：
#手动输入分数，如果这个分数大于60分，那么输出“合格”；
score=input('请输入你的成绩')
score=int(score)
if score>=60:
    print('合格')  #双引号和单引号效果相同？
'''
'''#课堂练习7
#代码实现
#输入python成绩python_score和c语言成绩c_score，编写代码判断成绩,要求只要有一门成绩 > 60 分就算合格
python_score=input('请输入python_score成绩：')
python_score=int(python_score)
c_score=input('请输入c_score成绩：')
c_score=int(c_score)
if (c_score>60) or (python_score>60):
    print('合格')'''
'''#课堂练习8
#编程实现：
#手动输入分数，如果这个分数大于90，那么输出“优秀”；
#如果这个分数小于90，那么输出“没拿到优秀，继续加油”；
score=input("请输入你的分数：")
score=int(score)
if score>90:
    print('优秀')
else:
    print('没拿到优秀，继续加油')'''
#课堂练习9
#编程实现：
#用户手动输入一个分数score，判断这个分数如果在90（包含90）以上，那么输出“优秀”；
#如果这个分数在75（包含75）和90之间，那么输出“良好”；
#如果这个分数在60（包含60）以上，那么输出“及格”；
#如果这个分数在60一下，那么输出“不及格”。
'''score=input('请输入你的成绩：')  #一步到位score = int(input('请输入分数'))
score=int(score)
if score>=90:
    print('优秀')
elif (score>=75) and (score<90):
    print('良好')
elif(score>=60) and (score<75):
    print('及格')
else:
    print('不及格')'''
'''#课堂练习10
#编程实现：
#提示用户输入用户名，如果用户名不为“admin”，则提示“用户名错误”，程序停止运行；
#如果用户名是"admin"，然后再提示输入密码：
# 如果密码正是“123456”，则提示“你已经登录系统”；
# 如果用户名不为“123456”，则提示“用户名与密码不匹配”；
account=input('请输入用户名：')
if account=="admin":
    password=input('请输入账户密码')
    if password=='123456':
        print('你已成功登录')
    else:
        print('用户名与密码不匹配')
else:
        print('用户名错误')'''#注意类型，账户名和密码为字符串类型
#课堂练习11
#需求
#1. 输入布尔型变量 has_ticket 表示是否有车票
#2. 输入整型变量 knife_length 表示刀的长度，单位：厘米
#3. 首先检查是否有车票，如果有，才允许进行 安检
#4. 安检时，需要检查刀的长度，判断是否超过 20 厘米
     #果超过 20 厘米，提示刀的长度，不允许上车
     #如果不超过 20 厘米，安检通过
#5. 如果没有车票，不允许进门
'''has_ticket=int(input('请输入是否有车票：0表示没有，1表示有'))
knife_length=int(input('请输入刀的长度，单位：厘米'))
if has_ticket==1:
    if knife_length>20:
        print('刀的长度不允许上车')
    else:
        print('安检通过')
else:
    print('没有车票，不允许进门')
'''
#综合：猜拳游戏
#要求：●从控制台输⼊要出的拳 —— 石头（1）／剪子（2）／布（3）
#●电脑 随机 出拳 —— 先假定电脑只会出⽯头，完成整体代码功能
#●比较胜负
'''player=int(input('请输入想要出的类型：石头：1/剪刀：2/布：3'))
computer = random.randint(1,3)
print(computer)
if (player==3) and (computer==1) or (player==2) and (computer==3) or (player==1) and (computer==2):
    print('你赢了')
elif(player==computer):
    print('你们平局了')
else:
    print('你输了')'''
'''#课堂练习12
#编程实现：
#定义变量a = 2，b = 3 ，用三目运算符实现判断a跟b的大小关系，如果a大于b则返回a的平方；否则返回b；
a=5
b=3
c=a**2 if a>b else b
print(c)'''
'''#课堂练习13
#编程实现：
#在屏幕上打印出一千次的“人生苦短，我用python”。
n=1
while n<=1000:
    print("人生苦短，我用python")
n=n+1
'''
'''#课堂练习14
#编程实现：
#定义变量i = 0，使用while循环，控制条件是i<5，
# 如果条件成立那就输出“人生苦短，我用python”，并且执行 i +=2，
# 请问程序运行结束之后，屏幕中出现几句“人生苦短，我用python”。
i=0
while i<5:
    print('人生苦短，我用python')  #x循环3次
    i+=2  #计数器'''
'''#课堂练习15
#编程实现：
#计算1001-2000的累计和。
i = 1001
sum = 0
while i<2001:
    sum += i
    i+=1
print('1001~2000的累计和为:%d'%sum)'''
'''#课堂练习16
#需求:
#打印所有3位回文数
#121 343 545 前面到后面 后面到前面都一样的数称为回文数
i=100
while i<1000:  #为什么用a，b不行？
    a=i//100
    b=i%10
    if a==b:
        print(i)
        i+=1'''
'''i = 100
while i<1000:
    # 百位
    hundreds = i//100
    # 个位
    single = i%10
    if hundreds==single:
        print(i)
    i+=1'''
'''#课堂练习17
#编程实现：
#用while循环输出1-100的数字，如果这个数字等于88，那就退出循环，停止输出。
i=1
while i<101:
    if i==88:
        break
    else:
        print(i)
        i+=1  #注意使用计数器，否则会进入死循环'''
'''#课堂练习
#编程实现：
#用while循环输出1-100的数字，如果某个数字为偶数，那就停止本次循环不再输出，进入下一层循环。
i=1
while i<101:
    if i%2==0:
        continue
        print(i)
        i+=1'''
'''i = 1
while i<101:
    if i%2==0:
        i+=1  #没有这个会陷入死循环
        continue
    print(i)
    i+=1'''
'''#打印5遍1-10
j=0
while j<5:
    i=1
    while i<11:
        print(i)
        i+=1
        j+=1  #计数器一般放到最后'''#为什么只有1遍？
'''#课堂练习
#编程实现：
#手动输入分数，如果这个分数大于90，那么输出“优秀”；
#如果这个分数小于90，那么输出“没拿到优秀，继续加油”；
score=int(input("请输入你的分数："))
if score > 90:
    print("优秀")
else:
    print("没拿到优秀，继续加油：")
'''
'''#99乘法表原理
#课堂练习
#需求:
#打印字符串'hello world'中除了'w'之外的每一个元素
str = 'hello world'
for ele in str:
    if ele=='w':
        continue
    print(ele)'''
'''#课堂练习
#打印字符串'hello world'中第一个'o'出现之前(不包含第一个'o')的所有元素
str = 'hello world'
for ele in str:
    if ele=='o':
        break
    print(ele)'''
#课堂练习
#需求:
#打印字符串'hello world'中第三个'l'出现之前(不包含第三个'l')的所有元素
'''str='hello world'
count=0
for i in str:
    if i=='l':
        count+=1
        if count==3:
            break
         print(i)'''
'''str = 'hello world'
# 统计出现的l次数
num = 0
for ele in str:
    if ele=='l':
        num+=1
        if num==3:
            break
    print(ele)'''
'''#用while循环输出三次”人生苦短，我用python”，正常结束循环输出”好好学习
i=0
while i<=3:
    print("人生苦短，我用python")
    i+=1
else:
    print("好好学习")'''
'''#课堂练习
#抽签(随机数1-9)3次,如果抽到6说明很幸运,老师原谅,如果三次都没有抽中6就打扫
import random

i = 0
while i<5:
    num = random.randint(1,7)
    if num==2:
        print('老师赦免我了')
        break
    print(f'    正在挨第{i}次惩罚，共需要惩罚5次')
    i+=1
else:
    print('正常被罚完还需要打扫教室，除非被赦免')'''
'''#课堂练习
#编程实现：
#有字符串str = “chuanzhibokehuanyingni!”,请用索引打印出位置为3, 7,15,17的字母
str="chuanzhibokehuanyingni!"#位置不用-1
print(str[3])
print(str[7])
print(str[15])
print(str[17])'''
#课堂练习
#a = "abcdef"
#1> 取出'abc', 该如何切片
#2> 取出'ace', 该如何切片
#3>使用a[5:1:2] 切片的结果是什么
#4>使用a[1:5:2]切片的结果是什么
#5>使用a[::-2]切片的结果是什么
#6>使用a[5:1:-2]切片的结果是什么
'''a = "abcdef"
# 取出'abc'
print(a[:3])
print(a[:5:2])
print(a[5:1:2])
print(a[1:5:2])
print(a[::-2])
print(a[5:1:-2])#位置从0开始'''
'''#课堂练习
#编程实现：
#有字符串str = “beijinghuanyingni!”,请用切片切出'huanyingni'
str="beijinghuanyingni!"
print(str[7:])
print(str[::-1])#字符串逆置
'''
'''#课堂练习
#编程实现：
#有字符串str = “beijing huan ying ni!”,请判断“chuan zhi”是否在str中，如果存在的话，起始下标是多少？
str="beijing huan ying ni!"
a=str.find('chuan zhi')  #字符串序列.index(子串)
if a!=-1:
     print(f'起始下标为{a}')
else:
    print('不存在')'''
'''#课堂练习
#编程实现：
#有列表list1 = [“a”，“b”，“c”，“d”]，执行语句：list2 = “”.join(list1)，那么list2得到的数据是什么？
list1 = 'abcd'
list2 = ' '.join(list1)'''
#编程实现：
#有字符串str = “beijing huan ying ni!”,请判断“chuan zhi”是否在str中，如果存在的话，起始下标是多少？
'''str = 'beijing huan ying ni';
str2='chuan zhi';
a=str.find(str2);
if a!=-1:
    print(f'在，位置是{a}');
else:
    print("不在")'''
#编程实现：
#有列表list1 = [“a”，“b”，“c”，“d”]，执行语句：list2 = “”.join(list1)，那么list2得到的数据是什么？
'''list1 = ["a","b","c","d"]#?
list2 = "".join(list1)
print(list2)
print(type(list1),'---',type(list2))'''
#编程实现：
#有字符串str1 = “ren sheng ku DUAN,  Wo yong pYthon!”,请分别用capitalize()、title()、lower()、upper()对这个字符串进行操作并输出结果
'''str = "ren sheng ku DUAN,Wo yong pYthon!"
print(str.capitalize())#首字母大写
print(str.title())#每个单词首字母大写
print(str.lower())#全部小写
print(str.upper())#全部大写
'''
#编程实现：
#有字符串str1 = “  hello python  ”,请分别用一种方法得到“hello python”这个新字符串。
'''str1=" hello python "
print(str1)
print(str1.strip(" "))
print(str1.rstrip(" ").lstrip(" "))#同时调用，一个字符串两个点'''
#需求:
#用户名和密码格式校验程序
#要求从键盘输入用户名和密码，校验格式是否符合规则，如果不符合，打印出不符合的原因，并提示重新输入
#用户名长度6-20，用户名必须以字母开头
#密码长度至少6位，不能为纯数字，不能有空格
# 校验
'''while True:
    # 输入
    name = input('请输入用户名')
    pwd = input('请输入密码')
    # 校验用户名
    if not(len(name)>=6 and len(name)<=20):
        print('用户名必须在6到20位')
        continue
    if not name[0].isalpha():
        print('用户名必须以字母开头')
        continue
    # 校验密码
    if len(pwd)<6:
        print('密码至少6位')
        continue
    if pwd.isdigit():
        print('密码不能为纯数字')
        continue
    if pwd.find('')!=-1:
        print('密码中不能有空格')
        continue
    break
print('开始登陆')'''
#编程实现：
#定义一个列表list1，列表中的元素有“chao”、“ji”、“ma”、“li”，请判断list1中含有多少个元素，并判断“li”的下标是多少，那么出现了几次？
'''list1=['chao','ji','ma','li']
print(len(list1))
print(list1.index('li'))
print(list1.count('li'))'''
#编程实现：
#定义一个列表list1，列表中的元素有“chao”、“ji”、“ma”、“li”，请判断是否存在“li”这个元素，如果存在，那么出现了几次？
'''list1=['chao','ji','ma','li']
if 'li' in list1:
    a=list.count('li')
    print(f"这个元素存在，出现了{a}次")
else:
    print('不存在')'''
'''1.系统里面有多个用户，用户的信息目前保存在列表里面
    users = ['root','westos']
    passwd = ['123','456']
2.用户登陆(判断用户登陆是否成功）
    1).判断用户是否存在
    2).如果存在
        1).判断用户密码是否正确
        如果正确，登陆成功，退出循环
        如果密码不正确，登录失败,重新登录
    3).如果用户不存在,登录失败,重新登录'''
'''users = ['root','westos']
passwd = ['123','456']
while True:#校验
    # 输入
    name = input('请输入用户名')
    pwd = input('请输入密码')
    # 用户名是否存在
    if name not in users:
        print('用户名不存在,请重新登陆')
        continue
    # 用户名存在
    # 密码是否正确
    i = users.index(name)
    p = passwd[i]
    if pwd!=p:
        print('密码不正确,重新登陆')
        continue
    # 登陆成功
    print('登陆成功')
    break'''
#编程实现：
#定义一个列表alist = [1,2,3]，blist = [3,4,5]，将blist当做一个元素添加到列表alist的末尾，应当怎么实现？
'''alist=[1,2,3]
blist=[3,4,5]
print(alist.append(blist))#前原后加'''#为什么打印不了？
'''编程实现：
定义一个列表alist = [1,2,3]，分别按照如下操作：
1.将['456']添加到alist中；
2.将‘456’添加到alist中；
'''
'''alist=[1,2,3]
alist.append(['456'])
alist.extend(['456'])
alist.append('456')
alist.extend('456')
print(alist)#z直接输出更改后的列表'''
#编程实现：
#定义一个列表alist = [10,13,14,15]，在alist列表下标为3地方插入元素。
'''alist=[10,13,14,15]
alist.insert(3,9)#insert 函数直接写位置
print(alist)'''
#编程实现：
#定义一个列表alist = 【10,13,14,15,16】，删除列表下标为3的数据，然后在下标为3的位置插入100，然后删除最后一个元素，并打印输出alist。
'''alist=[10,13,14,15,16]
del alist[3]
alist.insert(3,100)
alist.pop()#像栈一样，删除最上面的元素
print(alist)'''
#编程实现：
#定义一个列表alist = [10,15,13,14,16]，用copy()方法进行复制得到blist，然后对原来的列表alist进行添加数据操作，然后观察的两个列表的值。
'''alist=[10,15,13,14,16]
blist=alist.copy()
alist.append(9)#添加用append，插入用insert
print(alist)
print(blist)'''#增删数据，对复制出来的列表没有影响
#编程实现：
#定义一个列表alist = 【10,15,13,14,16】，用循环对alist进行遍历
'''alist=[10,15,13,14,16]
i=0
while i<len(alist):
    print(alist[i])
    i+=1'''
'''alist=[10,15,13,14,16]#for 循环不用初值，自增，不用数组，长度
for ele in alist:
    print(ele)'''
#编程实现：
#将6个小球放入3个不同的盒子里，并且每个盒子中至少有一个球，请实现这个功能。
#编程实现：
#定义一个元组 atuple=(1,3,8,4,)，请查找出元素28的下标是多少，并且统计一下atuple这个元组有几个元素。
'''atuple=(1,3,8,4,)
print(atuple.index(8))
print(len(atuple))#长度等于个数'''
#已知字典数据a_dict = {‘name’: ’hong’, ’age’: 20},完成下列需求：
#1.新增数据class:12
#2.尝试获取key为‘school’的数据，如果没有，则指定默认值‘英才中学’
#3.获取a_dict所有的键值信息，在终端输出
'''a_dict={'name':'hong','age':20}
a_dict['class']=12#没有.键用’‘
a_dict['school']='英才中学'
for key in a_dict.keys():
print(key)'''
a_dict = {'name':' hong', 'age': 20}
# 新增数据class:12
'''a_dict['class']=12
# 尝试获取key为‘school’的数据，如果没有，则指定默认值‘英才中学’
if not a_dict.get('school'):
    a_dict['school']='育才小学'
# 获取a_dict所有的键值信息，在终端输出
for key in a_dict.keys():
    print(key)
'''
'''需求:
设计一个程序，实现str.split()方法的替换：
首先输入一个任意长度的字符串
其次输入一个字符，用以分割该字符串，并且分割后的字符串保存到一个列表中
不允许使用str.split()方法
最后打印出该字符串被分割成多少部分、以及这个列表
去掉分割出来的空字符串
如"1234r5678r90r"用r分割，则为["1234","5678","90"]
'''
'''def mySplit(msg,splitStr):
    # 1.定义列表保存结果
    result = []
    # 定义变量保存右边的字符串
    rightStr = msg[:]
    # 2.获取第一个出现的分隔字符串
    index = rightStr.find(splitStr)
    while index!=-1:
        # 3.把这个分隔的字符串前面的部分添加到结果列表中
        # 获取前面部分
        leftStr = rightStr[:index]
        if leftStr:
            # 添加到列表中
            result.append(leftStr)
        # 修改右边的字符串
        rightStr = rightStr[index+len(splitStr):]
        # 继续查找索引
        index = rightStr.find(splitStr)
    if rightStr:
        # 添加最后一部分内容
        result.append(rightStr)
    # 返回结果
    return result
msg=input('请输入一个长字符串')
splitstr=input('请输入分割字符串')
result=mySplit(msg,splitstr)
print(result)
'''
#综合练习 创建学生信息管理系统
'''需求：进入系统显示系统功能界面，功能如下：
1.添加学员
2.删除学员
3.修改学员信息
4.查询学员信息
5.显示所有学员信息
6.退出系统
系统共6个功能，⽤户根据⾃⼰需求选取。'''

'''info=[]

def jiemian():
    print("1.添加学员")
    print("2.删除学员")
    print("3.修改学员信息")
    print("4.查询学员信息")
    print("5.显示所有学员信息")
    print("6.退出系统")

    jiemian()
def main():


num=input("请输入要进行的操作")

if num == '1':
    print('添加学员')
elif num == '2':
    print('删除学员')
elif num == '3':
    print('修改学员信息')
elif num == '4':
    print('查询学员信息')
elif num == '5':
    print('显示所有学员信息')
elif num == '6':
    print('退出系统')
else:
    print('输入错误，请重新输入!!!')

def insert_stu():
        new_name=input("请输入学生姓名")
        new_id=input("请输入学生id")

        info_dict={}

        global info

        for i in info:
            if new_id==i["id"]:
                print("该学生已输入")
                return
            else:
                info_dict={}
                info_dict["id"]=new_id
                info_dict["name"]=new_name #为什么不是大括号？


                info.append(info_dict)  #将字典数据添加到列表

                print(info)

def delete_stu():
    del_id=input("请输入要删除的学生id：")
    global info

    for i in info:
        if del_id == i["id"]:
            info.remove(i)
            print(info)
            break
        else:
            print("该学生信息已删除")

def modify_stu():
    modify_name = input('请输入要修改的学员的姓名：')
    global info

    for i in info:
        if modify_name == i['name']:
            i['id'] = input('请输入新的id：')
            break
    else:
        print('该学员不存在')

    print(info)

def search_stu():
    search_id = input("请输入要查找的学生id：")
    global info

    for i in info:
        if search_id == i['id']:
                print('查找到的学员信息如下：----------')
                print(f"该学员的学号是{i['id']}, 姓名是{i['name']}")
            else:
                print('该学员不存在')


def print_all():  # 显示所有学员信息
    print('学号\t姓名')
    for i in info:
        print(f'{i["id"]}\t{i["name"]}')

def exit_stu():
  if num == '6':
    exit_flag = input('确定要退出吗？yes or no')
    if exit_flag == 'yes':


        main()'''

'''import time
import os

# 定一个列表，用来存储所有的学生信息
info_list = []


def print_menu():  #显示界面
    print("---------------------------")
    print("      学生管理系统      ")
    print(" 1:添加学生")
    print(" 2:删除学生")
    print(" 3:修改学生")
    print(" 4:查询学生")
    print(" 5:显示所有学生")
    print(" 6:退出系统")
    print("---------------------------")


def add_stu():  #添加学生信息

    global info_list

    new_name = input("请输入学生姓名:")
    new_id = input("请输入学生id:")
    new_score = input("请输入学生成绩:")

    for stu_info in info_list:  #stu_info 为列表
        if stu_info['id'] == new_id:
            print("此学生信息已存在,请重新输入")
            return

    # 定义一个字典，用来存储学生
    info = {}

    # 向字典中添加数据
    info["name"] = new_name
    info["id"] = new_id
    info["score"] = new_score

    # 向列表中添加这个字典
    info_list.append(info)


def delete_info():  #删除学生信息

    global info_list

    del_num = int(input("请输入要删除的序号:"))
    if 0 <= del_num < len(info_list):
        del_flag = input("你确定要删除么?yes or no")
        if del_flag == "yes":
            del info_list[del_num]
    else:
        print("输入序号有误,请重新输入")


def modify_info(): #修改学生信息

    global info_list
    modify_num = int(input("请输入要修改的序号:"))
    if 0 <= modify_num < len(info_list):
        print("你要修改的信息是:")
        print("name:%s, id:%s, score:%s" % (info_list[modify_num]['name'],
            info_list[modify_num]['id'],info_list[modify_num]['score']))
        info_list[modify_num]['name'] = input("请输入新的姓名:")
        info_list[modify_num]['tel'] = input("请输入新的id:")
        info_list[modify_num]['qq'] = input("请输入新score:")
    else:
        print("输入序号有误,请重新输入")

def search_info():  #查询学生信息

    search_name = input("请输入要查询的学生姓名:")
    for stu_info in info_list:
        if stu_info['name'] == search_name:
            print("查询到的信息如下:")
            print("name:%s, id:%s, score:%s" % (stu_info['name'],
                stu_info['id'], stu_info['score']))
            break
    else:
        print("没有您要找的信息....")

def print_all_info():  #遍历学生信息

    print("序号\t姓名\t\t手机号\t\tQQ")
    i = 0
    for stu in info_list:
        # temp是一个字典
        print("%d\t%s\t\t%s\t\t%s" % (i, stu['name'], stu['id'], stu['score']))
        i += 1

def main():
    """用来控制整个流程"""
    while True:
        # 1. 打印功能
        print_menu()

        # 2. 获取用户的选择
        num = input("请输入要进行的操作(数字)")

        # 3. 根据用户选择,做相应的事情
        if num == "1":
            # 添加学生
            add_stu()
        elif num == "2":
            # 删除学生
            delete_info
        elif num == "3":
            # 修改学生
            modify_info()
        elif num == "4":
            # 查询学生
            search_info()
        elif num == "5":
            # 遍历所有的信息
            print_all_info()
        elif num == "6":
            # 退出系统
            exit_flag = input("亲,你确定要退出么?~~~~(>_<)~~~~(yes or no) ")
            if exit_flag == "yes":
                break
        else:
            print("输入有误,请重新输入......")


        input("\n\n\n按回车键继续....")
        os.system("clear")  # 调用Linux命令clear完成清屏

# 程序的开始
main()
'''
#课堂练习:
#使用递归求n的阶乘
'''def sum_n(n):  #注意是否是含参函数
    if n==1:
        return 1
        return sum-n(n-1)*n
 a=sum_n(6)
print(a) ''' #为什么无法打印？
#课堂练习 求第n个斐波那契数
#1 1 2 3 5 8 13
'''def Fibonacci(n):
    if n==1 or n==2:
        return 1
    return Fibonacci(n-1)+Fibonacci(n-2)'''
#面向对象
#综合练习1 烤地瓜
#需求主线：
#1.被烤的时间和对应的地瓜状态：
#0-3分钟：生的
#3-5分钟：半生不熟
#5-8分钟：熟的
#超过8分钟：烤糊了
#2.添加的调料：
#用户可以按用户的意愿添加调料

'''class SweetPotato():
    def __init__(self):
        # 被烤的时间
        self.cook_time = 0
        # 地瓜的状态
        self.cook_static = '生的'
        # 调料列表
        self.condiments = []

    def cook(self, time):
        """烤地瓜的方法"""
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_static = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_static = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_static = '熟了'
        elif self.cook_time >= 8:
            self.cook_static = '烤糊了'

    def add_condiments(self, condiment):
        """添加调料"""
        self.condiments.append(condiment)

    def __str__(self):
        return f'这个地瓜烤了{self.cook_time}分钟, 状态是{self.cook_static}, 添加的调料有{self.condiments}'

digua1 = SweetPotato()  #引用类
print(digua1)  #引用完接着打印
digua1.cook(2)  #引用方法：对象.函数（内容）
digua1.add_condiments('酱油')
print(digua1)
digua1.cook(2)
digua1.add_condiments('辣椒孜然')
print(digua1)
digua1.cook(2)
print(digua1)
digua1.cook(2)
print(digua1)'''
#搬家具
#将用于房子剩余面积的家具摆放到房子中
#房子类
#实例属性
#房子地理位置
#房子占地面积
#房子剩余面积
#房子内家具列表

#家具类
#家具名称
#家具占地面积
'''class Home():  #定义类型
    def __init__(self, address, area):  #初始化
        # 地理位置
        self.address = address  #self相当于this
        # 房屋面积
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.furniture = []

    def __str__(self):
        return f'房子坐落于{self.address}, 占地面积{self.area}, 剩余面积{self.free_area}, 家具有{self.furniture}'  #str相当于总结

    def add_furniture(self, item):
        """容纳家具"""
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            # 家具之后，房屋剩余面积 = 之前剩余面积 - 该家具面积
            self.free_area -= item.area
        else:
            print('家具太大，剩余面积不足，无法容纳')

class Furniture():
    def __init__(self, name, area):
        # 家具名字
        self.name = name
        # 家具占地面积
        self.area = area


        def __str__(self):
            return f'房子坐落于{self.address}, 占地面积{self.area}, 剩余面积{self.free_area}, 家具有{self.furniture}'

    def add_furniture(self, item):
        """容纳家具"""
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            # 家具之后，房屋剩余面积 = 之前剩余面积 - 该家具面积
            self.free_area -= item.area
        else:
            print('家具太大，剩余面积不足，无法容纳')

bed = Furniture('双人床', 6)
jia1 = Home('北京', 1200)
print(id(jia1))
print(jia1)
jia1.add_furniture(bed)
print(jia1)
sofa = Furniture('沙发', 10)
jia1.add_furniture(sofa)
print(jia1)
ball = Furniture('篮球场', 1500)
jia1.add_furniture(ball)
print(jia1)
print(id(jia1))
'''
#总结
'''
魔法方法
init() : 初始化
str() :输出对象信息
del() :删除对象时调⽤'''
import requests
url='https://www.itheima.com/about/about.html'
headers=



