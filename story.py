from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student

codecool_bp = CodecoolClass.generate_local()
mentor_kálmán = codecool_bp.find_mentor_by_full_name("Kálmán Szabó")
mentor_kálmán.ask_random_q(codecool_bp)
mentor_kálmán.bad_jokes(codecool_bp)
print()
stud_kolin = codecool_bp.find_student_by_full_name("Kolin Brokk")
print("Kolin energiaszintje: ", stud_kolin.mood_level)
mentor_kálmán.bfa(stud_kolin)
print()
print("Kolin kedve: ", stud_kolin.mood_level)
print("Kálmán energiaszintje: ", mentor_kálmán.energy_level)
stud_kolin.private_mentoring(mentor_kálmán)
print("Kolin energiaszintje: ", stud_kolin.energy_level)
print("Kálmán energiaszintje: ", mentor_kálmán.energy_level)
print("Kolin kedve: ", stud_kolin.mood_level)
mentor_kálmán.drink_coffee()
print("Kálmán energiaszintje: ", mentor_kálmán.energy_level)
