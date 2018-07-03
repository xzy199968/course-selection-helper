# -*- coding: UTF-8 -*-


class Selection:
    def __init__(self, database, preconds=[]):
        self.pcds = preconds
        self.db = database

    def add_precond(self, name):
        if name in self.db.get_courses() and \
                self.is_possible(self.pcds + [name]):
            self.pcds.append(name)
        else:
            print('Impossible appending!')

    def rm_precond(self, name):
        self.pcds.remove(name)

    def cr_preconds(self):
        self.pcds = []

    def schemes(self):
        cz2s = [cz for cz in self.db.get_courses() if cz not in self.pcds]
        schemes = [scheme for scheme in power_sets(cz2s)
                   if self.is_possible(self.pcds + scheme)]
        return schemes

    def is_possible(self, cz_names):
        for day in ['周一', '周二', '周三', '周四', '周五', '周六', '周日']:
            for time in range(1, 13):
                czs = [name for name in cz_names
                       if [day, time] in self.db.get_courses()[name]]
                if len(czs) > 1:
                    return False
        return True


def power_sets(items):
        # the power set of the empty set has one element, the empty set
        result = [[]]
        for x in items:
            result.extend([subset + [x] for subset in result])
        return result

if __name__ == '__main__':
    import database as db
    d = db.Database(url="/Users/royes/PycharmProjects/course selection helper/data")