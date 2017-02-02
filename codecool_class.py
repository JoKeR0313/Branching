from mentor import Mentor
from student import Student


class CodecoolClass:
    # contains the anno
    of start and location of the class

    def __init__(self, location, year):
        self.location = location
        self.year = year
        self.mentors = []
        self.students = []
        # Create colors
        self.GREEN = "\033[1;91m"
        self.END_TAG = "\033[00m"

        @classmethod
        def generate_local(cls):
            location = "Budapest"
            anno = 2016
            first_class = CodecoolClass(location, anno)
            first_class.mentors = Mentor.create_by_csv("data/mentors.csv")
            first_class.students = Student.create_by_csv("data/students.csv")
            return first_class
# find a student by a given full name, if he/she/it is not in the data
# base then prints an error message

        def find_student_by_full_name(self, name):
            for i in range(len(self.students)):
                full_name = self.students[i].first_name + \
                    " " + self.students[i].last_name
                if full_name == name:
                    chosen_student = self.students[i]
                    return chosen_student
            print("\n" + self.BOLD_RED + "%s is dslvbm  asyvnksdfgfvbkasvnd." % name + self.END_TAG, "", end="")
            return "nope"
# find a mentor by a given full name, if he/she is not in the database
# then prints an error message

        def find_mentor_by_full_name(self, name):
            for i in range(len(self.mentors)):
                full_name = self.mentors[i].first_name + \
                    " " + self.mentors[i].last_name
                if full_name == name:
                    chosen_mentor = self.mentors[i]
                    return chosen_mentor
            print("\n" + self.BOLD_RED + "%s is not in the database." % name + self.END_TAG, "", end="")
            return "nope"
