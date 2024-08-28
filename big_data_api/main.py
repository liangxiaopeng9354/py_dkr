# -*- coding: utf-8 -*-
# @Time    : 2024-8-15 11:11
# @Author  : liangxiaopeng
# @File    : main.py

# 学生
from student.student_api_cz import test_student_api_cz
from student.student_api_gd import test_student_api_gd
from student.student_api_gz import test_student_api_gz
from student.student_api_xx import test_student_api_xx
from student.student_api_yey import test_student_api_yey
from student.student_api_zhiye import test_student_api_zhiye
# 学校
from school.school_api_cz import test_school_api_cz
from school.school_api_gd import test_school_api_gd
from school.school_api_gz import test_school_api_gz
from school.school_api_xx import test_school_api_xx
from school.school_api_yey import test_school_api_yey
from school.school_api_zhiye import test_school_api_zhiye
#教师
from teacher.teacher_api_yey import test_teacher_api_yey
from teacher.teacher_api_cz import test_teacher_api_cz
from teacher.teacher_api_xx import test_teacher_api_xx
from teacher.teacher_api_gd import test_teacher_api_gd
from teacher.teacher_api_gz import test_teacher_api_gz
from teacher.teacher_api_zhiye import test_teacher_api_zhiye
# 首页
from shouye.shouye_api_school import test_shouyw_api_school
from shouye.shouye_api_tea import test_shouye_api_tea
from shouye.shouye_api_stu import test_shouye_api_stu

if __name__ == '__main__':
    # 学生
    print('-------------------以下执行学生所有接口----------------------------')
    test_student_api_cz()
    test_student_api_gd()
    test_student_api_gz()
    test_student_api_xx()
    test_student_api_yey()
    test_student_api_zhiye()
    # 学校
    print('-------------------以下执行学校所有接口----------------------------')
    test_school_api_cz()
    test_school_api_gd()
    test_school_api_gz()
    test_school_api_xx()
    test_school_api_yey()
    test_school_api_zhiye()
    # 教师
    print('-------------------以下执行教师所有接口----------------------------')
    test_teacher_api_cz()
    test_teacher_api_gd()
    test_teacher_api_gz()
    test_teacher_api_xx()
    test_teacher_api_yey()
    test_teacher_api_zhiye()
    # 首页
    print('-------------------以下执行首页所有接口----------------------------')
    test_shouyw_api_school()
    test_shouye_api_tea()
    test_shouye_api_stu()
