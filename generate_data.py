import os

print('1. migration\n2. no migration')
migration_db = input('migration db?: ')

if migration_db == '1':
    os.system("python migration_db.py")

os.system("python manage.py generate_groups")
os.system("python manage.py generate_users")
os.system("python manage.py generate_subjects")
os.system("python manage.py generate_additional_tasks")
os.system("python manage.py generate_exams")
os.system("python manage.py generate_payment")
os.system("python manage.py generate_lessons")
os.system("python manage.py generate_student_groups")