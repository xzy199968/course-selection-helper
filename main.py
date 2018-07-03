# -*- coding: UTF-8 -*-
import database as db
import selection as sl


local_url = "/Users/royes/PycharmProjects/course selection helper/data"
d = db.Database(local_url)

# Do changes to database
'''
d.rm_all()
d.add_course('高数', [['周二', 3], ['周二', 4], ['周五', 1], ['周五', 2]])
print(d.get_courses())
d.save()
input('>')
'''

s = sl.Selection(d)

'''
print([sc for sc in s.schemes()
'''


