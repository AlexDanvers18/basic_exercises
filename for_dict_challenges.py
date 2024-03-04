# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]


# count_names = dict()

# for student in students:
#     name = student['first_name']
#     if name not in count_names.keys():
#         count_names.keys() == name
#         count_names[name] = 1
#     else:
#         count_names[name] += 1

# for count_name, count in count_names.items():
#     print(f'{count_name}: {count}')



# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

# count_names = dict()

# for student in students:
#     name = student['first_name']
#     if name not in count_names.keys():
#         count_names.keys() == name
#         count_names[name] = 1
#     else:
#         count_names[name] += 1

# for count_name, count in count_names.items():
#     if count == max(count_names.values()): 
#         print(f'\nСамое частое имя среди учеников: {count_name}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],
    [  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]



# list_students = dict()

# for klass in school_students:
#     for student in klass:
#         name = student['first_name']
#         if name not in list_students.keys():
#             list_students.keys() == name
#             list_students[name] = 1
#         else:
#             list_students[name] += 1


# number_group = 1

# for count_name, count in list_students.items():
#     if count == max(list_students.values()):
#         print(f'\nСамое частое имя среди учеников в {number_group} классе: {count_name}')
#         number_group = int(number_group + 1)




# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': 
     [{'first_name': 'Маша'}, 
      {'first_name': 'Оля'}
      ]
     },
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]

is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}


# for klass in school:
#     count_female = []
#     count_male = []
#     for student in klass['students']:
#         name = student['first_name']
#         if is_male[name] == True:
#             count_male.append(name)
#         elif is_male[name]== False:
#             count_female.append(name)


#     print(f'\nКласс {klass["class"]}: девочки {len(count_female)}, мальчики {len(count_male)}')       

    

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

dict_classes = {}

for klass in school:
    dict_classes[klass['class']] = {'count_male': 0, 'count_female': 0}
    count_female = 0
    count_male = 0
    for student in klass['students']:
        for name in student.values():
            if is_male[name] == True:
                dict_classes[klass['class']]['count_male'] += 1
            elif is_male[name] == False:
                dict_classes[klass['class']]['count_female'] += 1


max_male = 0
max_female = 0
for klass in dict_classes.keys():
    if max_male < dict_classes[klass]['count_male']:
        max_male = dict_classes[klass]['count_male']
        max_male_class = klass
    if max_female < dict_classes[klass]['count_female']:
        max_female  = dict_classes[klass]['count_female']
        max_female_class = klass
print(f"Больше всего мальчиков в классе {max_male_class}")
print(f"Больше всего девочек в классе {max_female_class}")