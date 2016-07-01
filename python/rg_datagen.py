import names as names_lib
from classes import Student
from classes import Subject
from random import randint
import VTU
import jsonpickle as jpk
import os

# Global Variables_
years = 4
_branches = {
    'EC': VTU.EC().EC,
    'CS': VTU.CS().CS,
    'MECH': VTU.MECHANICAL().MECHANICAL,
    'CIVIL': VTU.CIVIL().CIVIL,
    'IS': VTU.IS().IS
}
result_class = "PASS"
student_total_marks = 0
student_final_marks = 125 * 8
pass_per = 0.35
second_class_per = 0.5
first_class_per = 0.6
fcd_per = 0.7

# Year 4 - Branch 5 - Students 120 - Subjects 8
for year in range(4):
    for branch_name, branch_data in _branches.items():
        names = []
        for i in range(0, 120):
            names.append(names_lib.get_first_name())
        usn_list = []
        usn_string = '4MH1'+str(year)+str(branch_name)
        sem_subjects = []
        subject_code_list = []

        # For each Semester
        os.system('mkdir -p /Users/prathyushsp/Development/rg/data/1' + str(year) + '/' + str(branch_name))
        for semester in range(8):
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
                subject_code_list.append('1'+str(year)+str(branch_name)+str(semester+1)+str(i))

            # Generate Subject Names
            for i in range(8):
                sem_subjects.append(_branches[branch_name][i][0][0])

            # Empty Student List
            student_list = []

            # For number of students
            for i in range(0, 120):
                result_class = "PASS"
                subject_list = []
                student_total_marks = 0
                for j in range(0,8):
                    subject = Subject(sem_subjects[j], randint(0, 25), randint(0, 100), subject_code_list[j],
                                      theory='true'if _branches[branch_name][1] == 'theory' else 'false')
                    subject.totalMarks = subject.internalMarks + subject.externalMarks
                    student_total_marks += subject.totalMarks
                    if subject.totalMarks < 35:
                        subject.result = "FAIL"
                        result_class = "FAIL"
                    else:
                        subject.result = "PASS"
                    subject_list.append(subject)
                if result_class == "PASS":
                    if (pass_per * student_final_marks) <= student_total_marks < (student_final_marks * second_class_per):
                        result_class = "PASS"
                    elif (student_final_marks * second_class_per) <= student_total_marks < (student_final_marks * first_class_per):
                        result_class = "SECOND CLASS"
                    elif (student_final_marks * first_class_per) <= student_total_marks < (student_final_marks * fcd_per):
                        result_class = "FIRST CLASS"
                    else:
                        result_class = "FCD"
                student = Student(names[i], usn_list[i], semester+1, subject_list, result_class, student_total_marks)
                student_list.append(student)
            with open('data/1'+str(year)+'/' + str(branch_name)+'/semester'+str(semester+1), 'w') as f:
                f.write(jpk.dumps(student_list, unpicklable=False))
        print("Generating data for 1" + str(year) + " year " + str(branch_name)+' branch')