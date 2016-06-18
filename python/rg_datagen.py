import names as names_lib
import pickle
from classes import Student
from classes import Subject
from random import randint
import jsonpickle as jpk

# Names generation and saving
# names=[]
# for i in range(0, 120):
#     names.append(names_lib.get_first_name())
#
# with open('/Users/prathyushsp/Data/rg/names.pickle', 'wb') as pkl_file:
#     pickle.dump(names, pkl_file, protocol=3)

# Load names
with open('/Users/prathyushsp/Data/rg/names.pickle','rb') as pkl_file:
    names = pickle.load(pkl_file)

usn_list = []
usn_string = "4MH11EC"
sem_subjects = []
subject_code_list = []
semester = 1

# Generate USN
for i in range(0, 120):
    if i < 10:
        usn_list.append(usn_string + "00" + str(i))
    elif i<100:
        usn_list.append(usn_string + "0" + str(i))
    else:
        usn_list.append(usn_string + str(i))

# Generate Subject Code
for i in range(1,9):
    subject_code_list.append("10EC"+str(semester)+str(i))

# Generate Subject Names
for i in range(1,9):
    sem_subjects.append("Sem"+str(semester)+"Subject"+str(i))

student_list = []
result_class = "PASS"
student_total_marks = 0
student_final_marks = 125*8
pass_per = 0.35
second_class_per = 0.5
first_class_per = 0.6
fcd_per = 0.7

for i in range(0,120):
    result_class = "PASS"
    subject_list = []
    student_total_marks = 0
    for j in range(0,8):
        subject = Subject(sem_subjects[j], randint(0,100), randint(0,35), subject_code_list[j])
        subject.totalMarks = subject.internalMarks + subject.externalMarks
        student_total_marks += subject.totalMarks
        if subject.totalMarks < 35:
            subject.result = "FAIL"
            result_class = "FAIL"
        else:
            subject.result = "PASS"
        subject_list.append(subject)
    if result_class == "PASS":
        if  (pass_per * student_final_marks) <= student_total_marks < (student_final_marks * second_class_per):
            result_class = "PASS"
        elif (student_final_marks * second_class_per) <= student_total_marks < (student_final_marks * first_class_per):
            result_class = "SECOND CLASS"
        elif (student_final_marks * first_class_per) <= student_total_marks < (student_final_marks * fcd_per):
            result_class = "FIRST CLASS"
        else:
            result_class = "FIRST CLASS WITH DISTINCTION"
    student = Student(names[i], usn_list[i], semester, subject_list, result_class, student_total_marks)
    print(jpk.dumps(student, unpicklable=False))
