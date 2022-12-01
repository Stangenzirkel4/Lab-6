class Employee:
    objectsCount = 0
    bonus = 0.05
    def __init__(self, name, age, salary):
        self._name = name
        self.age = age
        self.salary = salary
        self.worked = 0
        self.teams = []
        Employee.objectsCount = Employee.objectsCount + 1

    #Рассчитываем премию сотрудника
    def calc_bonus(self, workdays):
        return self.salary * self.bonus / workdays * self.worked

    def calc_salary(self, workdays):
        return

    def fire(self):
        print("Работник %s уволен" % (self._name))

    def getname(self):
        return self._name

    def work(self):
        self.worked +=1
        print("Работник %s отработал смену" % self._name)


class SeniorEmployee(Employee):
    bonus = 0.1
    pass

class Manager(Employee):
    bonus = 0.2
    pass

class Team:

    def __init__(self, name, *args):
        self.members = []
        self.teamname = name
        for i in args:
            self.add(i)

    def add(self, other):
        for i in self.members:
            if other == i:
                print('Работник %s уже в команде!' %(other.getname()))
                return
        self.members.append(other)
        print("Работник %s добавлен в команду" %(other.getname()))

    def remove(self, member):
        for i in self.members:
            if member == i:
                self.members.remove(i)
                print('Работник удален из %s' %(self.teamname))
                return True
        print('Работник не найден')
        return False

    def show_members(self):
        print("В команде %s следующие работники:")
        for i in self.members:
            print(i._name)

#Набираем работников
se_001 = SeniorEmployee('Михаил', 35, 40000)
e_001 = Employee('Леонид', 26, 20000)
e_002 = Employee('Виктор', 24, 20000)
m_001 = Manager('Ипполит', 45, 100000)
e_003 = Employee('Прокофий', 21, 20000)
e_004 = Employee('Порфирий', 22, 20000)
se_002 = SeniorEmployee('Арсений', 35, 40000)
e_005 = Employee('Евгений', 25, 20000)
e_006 = Employee('Василий', 24, 20000)

#Собираем команду
team_001 = Team("Отдел кадров",se_001,e_006)
team_001.add(e_005)
e_004.fire()
