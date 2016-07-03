
class Student(object):
    def __init__(self, name, USN, semester,subject,resultClass = None, totalMarks = None):
        self.name = name
        self.usn = USN
        self.semester = semester
        self.subject = subject
        self.resultClass = resultClass
        self.totalMarks = totalMarks


class Subject(object):
    def __init__(self, name, internalMarks, externalMarks, subjectCode, totalMarks=None, result=None, theory=None):
        self.name = name
        self.internalMarks = internalMarks
        self.externalMarks = externalMarks
        self.totalMarks = totalMarks
        self.subjectCode = subjectCode
        self.result = result
        self.theory = theory
