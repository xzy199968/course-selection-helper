脚本可以列出所有不冲突的选课方案，依据课程事件信息和一些选课前提。

# 功能
1. 将感兴趣的课程信息写入本地的课程信息库文件 (database.py, class Database)
2. 给它你一定要选的课，它可以告诉你所有可能的选课方案 (selection.py, class Selection)

# 不幸的消息
非常抱歉，我没有实现命令行或者图形界面交互功能，所以需要用户自己完成一些脚本写作。（主要是懒啦！） \
不过别担心！我会提供一个详细的使用说明的，而且主程序文件里也有样例代码啦！

 

# 使用说明
##1. 打开 main.py
##2. 将 'local_url' 设置为你的文件路径
##3. 修改课程资料库
  在<code>d = db.Database(local_url)</code>后面酌情写下以下命令
  - <code>d.rm_all()</code>\
    清空资料库
  - <code>d.add_course('高数', [['周二', 3], ['周三', 4]])</code>\
  增加"高数"课，时间在周二3节和周三4节
  - <code>d.rm_course('高数')</code>\
  去掉"高数"课
  - <code>print(d.get_courses())</code>\
  在终端输出所有的课程信息
  - <code>d.save()</code>\
  保存这个数据库
  
 ##4. 得到所有的方案
 所有的方案都被放在了一个叫"s.schemes()"的list，\
 使用语句
<code>print([sc for sc in s.schemes()])</code>，你就可以看到所有的方案了！

下面的例子提供给有一点点点编程基础的同学们，可以实现脚本强大的高级功能。
<pre><code>print([sc for sc in s.schemes() if len(sc) >= 5
       if not (('地空数算' in sc) and ('计算方法' in sc))
       if ('高数' in sc) ^ ('生院高数' in sc)
       if '热学' in sc
       if '电线' not in sc]
      )
</code></pre>

这个例子中，终端会输出满足以下条件的方案：
1. 所有课程数量不小于5
2. 同时不包含'地空数算'和'计算方法'
3. 不同时包含'高数'和'生院高数'
4. 不包含'电线'
