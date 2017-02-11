def find_person(name):

    students = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

    while students:

        sudent_name = students.pop()
        if sudent_name == name:
            print('Есть такое имя')
            break
    else:
        print('Нет в списке')
user_say = input('Напишите имя: ')
find_person(user_say)