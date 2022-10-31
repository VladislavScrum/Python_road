from dependence import cls, load
import road_calculator
import road_grade
import road_lists
import road_range

load()
cls()
user_name = input('Введите своё имя для продолжения: ')

def menu():
    while True:
        cls()
        print('============================')
        print('Здравствуйте ', user_name, '! Вас приветствует компания Roadmap!', sep='')
        print('============================')
        print('1) Змеинный калькулятор (Змеинный - потому что Python)')
        print('2) Программа расчёта успеваемости пользователей')
        print('3) Программа сложения списков')
        print('4) Программа демонстрирующая возможности среза списков')
        print('5) Выход')
        print('============================')
        choice = input('Сделайте свой выбор: ')

        while True:
            if choice == '1':
                road_calculator.calculator()
                break
            elif choice == '2':
                road_grade.grade()
                break
            elif choice == '3':
                road_lists.road_3()
                break
            elif choice == '4':
                road_range.counter()
                break
            elif choice == '5':
                cls()
                print('============================================================')
                print('Надеюсь вы остались довольны работой программы. До свидания.')
                print('============================================================')
                return False
            else:
                choice = input('Сделайте выбор из меню, введя цифру от 1 до 5: ')
        
menu()