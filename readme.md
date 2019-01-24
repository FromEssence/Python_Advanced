datetime 模块

1. 主要的类
   - datetime.date() 处理日期
   - datetime.time() 处理时间(时分秒、毫秒)
   - datetime.datetime() 日期+时间
   - datetime.timedelta() 处理时间间隔、时间运算
2. 获取当前时间
   - 获取今天日期
     - datetime.date.today()
     - datetime.datetime.now()
   - 修改日期格式
     - strftime()
       - e.g. datetime.date.today().strftime('%Y-%m-%d %H:%M:%S')
     - isoformat()
       - datetime.datetime.now().isoformat()
       
3. 时间戳

4. 时间加减法
   - timedelta()方法
      ``` python
         today = datetime.datetime.now()
         yestoday = today - datetime.timedelta(days=1)
         oneHourAgo = today - datetime.timedelta(hours=1)
      ```

OOP

类的定义与调用

    #类的定义和调用
    class Pen:
        
        def __init__(self): #self指对象实例
            self.width = 1.0
        def sharp(self, wid): #削铅笔
            self.width = wid
    
    myPen = Pen()
    myPen.sharp(0.5)
    print(myPen.width)

特殊方法 (magic method)

1. 基本概念
   在类中实现一些特殊方法，用于方便使用python的一些内置操作
2. 特点
   特殊方法的名称是固定的且都以两个下划线开始和结束
   e.g. Python中的构造器和析构器
       
       __init__(self, [_)
       __del__(self, [_)
3. 算术操作
       
       __add__(self, other) #使用+操作符,左操作数传递给self
       __sub__
       __mul__
       __div__
       __eq__(self,other)   # == 
       __ne__               # !=
       __lt__               # <
       __gt__
       __le__               # <=
       __ge__
4. 字符串操作
       
       __str__(self) # 对象实例转换为字符串时的操作
       __repr__(self)# 返回一个用来表示对象的字符串，官方
       __len__(self) # 返回元素个数、长度等
   
