import datetime

class Person(object):
    def __init__(self,name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastname = name.split(' ')[-1]

    def getLastName(self):
        """return self's last name"""
        return self.lastname

    def setBirthday(self,month,day,year):
        """sets self's birthday to birthdate"""
        self.birthday = datetime.date(year,month,day)

    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError("No birthdayte added")
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """returns True if self's name is lexicographically
           less than other's name, and False otherwise"""
        if self.lastname == other.lastname:
            return self.name < other.name
        return self.lastname < other.lastname

    def __str__(self):
        """return self's name"""
        return self.name

class MITPerson(Person):
    nextIdnum = 0 # next ID number to assign

    def __init__(self, name):
        Person.__init__(self, name) #initialize Person attributes
        self.idNum = MITPerson.nextIdnum
        MITPerson.nextIdnum += 1

    def getIdNum(self):
        return self.idNum

    #sorting MIT people uses their ID number, not name
    def __lt__(self, other):
        return self.idNum < other.idNum

    def speak(self,utterance):
        return (self.getLastName() + " says: "+ utterance)

# database of people
p1 = Person('Mark Zuckerberg')
p1.setBirthday(5,14,84)
p2 = Person('Drew Houston')
p2.setBirthday(3,4,83)
p3 = Person('Bill Gates')
p3.setBirthday(10,28,55)
p4 = Person('Andrew Gates')
p5 = Person('Steve Wozniak')

personList = [p1, p2, p3, p4, p5]

personList.sort() #sorts according to def of __lt__ in Person

# database of MIT people
m3 = MITPerson('Mark Zuckerberg')
Person.setBirthday(m3,5,14,84)
m2 = MITPerson('Drew Houston')
Person.setBirthday(m2,3,4,83)
m1 = MITPerson('Bill Gates')
Person.setBirthday(m1,10,28,55)

MITPersonList = [m1, m2, m3]

MITPersonList.sort()

#an important example
a1 = MITPerson('Eric')
a2 = MITPerson('John')
a3 = MITPerson('John')
a4 = Person('John')

print(a1 < a2) #true
print(a1 < a4) #eq to a1.__lt__(a4), lt of MIT,a4 does not have id number so gives error
print(a4<a1) #False, lt of Person, so name comparison


class Student (MITPerson):
    pass


class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self,name)
        self.year = classYear

    def getClass(self):
        return self.year

    def speak(self,utterance):
        return MITPerson.speak(self, "Dude, "+ utterance)


class Grad(Student):
    pass


class TransferStudent(Student):
    pass


def isStudent(obj):
    return isinstance(obj,Student)

# UG students database
s1 = UG('Matt Damon', 2017)
s2 = UG('Ben Affleck', 2017)
s3 = UG('Lin Manuel Mirands', 2018)
s4 = Grad('Leonardo di Caprio')

print(s1)
print(s1.getClass())
print(s1.speak('where is the quiz?'))
print(s2.speak('I have no clue!'))


class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self,name)
        self.department = department

    def speak(self,utterance):
        new = 'In course ' + self.department + ' we say '
        return MITPerson.speak(self,new + utterance )

    def lecture(self, topic):
        return self.speak('it is obvious that ' + topic)

#
#Gradebook example
#
class Grades(object):
    """A mapping from students to a list of grades"""

    def __init__(self):
        """Create empty grade book"""
        self.students = []   #list of Studnet objects
        self.grades = []    # maps idNum -> list of grades
        self.isSorted = True    # true if self.students is sorted

    def addStudnet(self, student):
        """ Assumes: student is of type Student
            Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = {}
        self.isSorted = False

    def addGrade(self, student, grade):
        """Assumes: grade is a float.
           Add grade to the list of grades for student"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')

    def getGrades(self, student):
        """Return a list of grades for student"""
        try:    #return copy of student's grades
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('Student not in grade book')

    def allStudents(self):
        """Return a list of students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        for s in self.students:
            yield s


def gradeReport(course):
    """Assumes: course if of type grades"""
    report = []
    for s in course.allStudents()
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report.append(str(s) + ' \'s mean grade is ' + str(average) )
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
    return '\n'.join(report)