import os


def create_apps():
    count = input("Nechta app yaratilsin: ")
    if not count.isdigit():
        print("Sonda kiriting")
        create_apps()
    for i in range(int(count)):
        name = input('appni nomini kiriting: ')
        os.system(f"python manage.py startapp {name}")
        print(f"{name} app yaratildi")

create_apps()

# exams = tasks


# attendances
# general
# lessons
# notices
# subjects