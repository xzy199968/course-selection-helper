# -*- coding: UTF-8 -*-

# Accept the time info of all course,and store it into a local file.
# The info is store

localurl = "/Users/royes/PycharmProjects/course selection helper/data"


# Info is given as name and time_list
# time_list = [[day1, time1], [day2, time2] ... ]
def add_course(name, time_list):
    with open(localurl, "r+") as fo:
        text = fo.read()
        if text == '':
            fo.write(str({name: time_list}))
        else:
            adict = eval(text)
            adict[name] = time_list
            fo.seek(0)
            fo.truncate()
            fo.write(str(adict))


# Pass the name to delete
def rm_course(name):
    with open(localurl, "r+") as fo:
        text = fo.read()
        try:
            adict = eval(text)
            del adict[name]
            fo.seek(0)
            fo.truncate()
            fo.write(str(adict))
        except:
            print('Deletion failed!')


def rm_all():
    if input('Are you sure to remove all courses in database?(Y to confirm)') == 'Y':
        with open(localurl, "r+") as fo:
            fo.truncate()


if __name__ == '__main__':
    add_course('数算', [['周三', 1], ['周三', 2]])
    add_course('数理', [['周四', 11], ['周五', 12]])
    rm_course('数算')
    add_course('计概', [['周一', 7]])
    add_course('力学', [['周三', 1], ['周六', 7]])
    rm_course('计概')
    rm_all()
