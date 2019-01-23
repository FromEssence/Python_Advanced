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
   - 
4. 时间加减法
   - timedelta()方法
      ``` python
         today = datetime.datetime.now()
         yestoday = today - datetime.timedelta(days=1)
         oneHourAgo = today - datetime.timedelta(hours=1)
      ```
