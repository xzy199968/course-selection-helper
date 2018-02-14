# -*- coding: UTF-8 -*-

# Accept the timetable of all course,and store it into a local file as a dictionary.


class Database:
    def __init__(self, url):
        self.url = url

        with open(url, 'r') as fo:
            text = fo.read()
            if text is '':
                self.courses = {}
            else:
                self.courses = eval(text)

    def get_courses(self):
        return self.courses

    # Course info is given by its name and a corresponding list: time_list
    # time_list = [[day1, time1], [day2, time2] ... ]
    def add_course(self, name, time_list):
        self.courses[name] = time_list

    # Pass the name to delete the course
    def rm_course(self, name):
        try:
            del self.courses[name]
        except KeyError:
            print(name, ' doesn\'t exist!')

    def rm_all(self):
        if input('Are you sure to remove all courses in database?(Y to confirm)') == 'Y':
            self.courses = {}

    def save(self):
        try:
            with open(self.url, 'r+') as fo:
                fo.truncate()
                fo.write(str(self.courses))
        except:
            print('Saving failed!')


if __name__ == '__main__':
    local_url = "/Users/royes/PycharmProjects/course selection helper/data"
    d = Database(local_url)
    d.add_course('数算', [['周三', 1], ['周三', 2]])
    d.add_course('数理', [['周四', 11], ['周五', 12]])
    d.rm_course('数算')
    d.save()
    input('>')
    d.add_course('计概', [['周一', 7]])
    d.add_course('力学', [['周三', 1], ['周六', 7]])
    d.rm_course('计概')
    d.save()
    input('>')
    d.rm_all()
    d.save()
    input('>')
