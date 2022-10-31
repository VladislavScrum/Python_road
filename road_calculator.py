from dependence import cls
import time
import random

def calculator():

    cls()
    print('================================================')
    print('Вас приветствует программа - Змеиный калькулятор')
    print('================================================')
    input('Нажмите Enter для продолжения...')
    cls()
    time.sleep(1)

    while True:
        cls()
        print('=======================================') 
        print('                 Меню:                 ')
        print('=======================================')        
        print('1) Сложение')
        print('2) Вычитание')
        print('3) Умножение')
        print('4) Деление')
        print('5) Целочисленно деление')
        print('6) Остаток от деления')
        print('7) Выход')
        print('=======================================')
        
        try:
            choice = int(input('Сделайте свой выбор: '))  
            cls()    
        except ValueError:
            print('Цифры, цифры, мне нужны цифры!')
            time.sleep(3)
            print('Давай по новой, и в этот раз чтоб без глупостей!')
            time.sleep(3)
            continue
        if choice >0 and choice <7:
            try:
                a = int(input('Введите первое число: '))
                b = int(input('Введите второе число: '))
                cls()    
            except ValueError:
                print('Цифры, цифры, мне нужны цифры!')
                time.sleep(3)
                print('Давай по новой, и в этот раз чтоб без глупостей!')
                time.sleep(3)
                continue
            if choice == 1:          
                print('Проводим вычисления...')
                time.sleep(random.randint(2,4))
                print('Уже почти...')
                time.sleep(random.randint(2,4))
                print('Итак, если сложить ', a, ' и ', b, ', получится: ', a+b, sep='')
                time.sleep(3)
            elif choice == 2:
                print('Вычисления займут какое-то время...')
                time.sleep(random.randint(2,4))
                print('Минутку...')
                time.sleep(random.randint(2,4))
                print('Получилось!')
                time.sleep(2)
                print('Если отнять ', b, ' от ', a, ', то получится: ', a-b, sep='')
                time.sleep(3)
            elif choice == 3:
                print('Сейчас посчитаем...')
                time.sleep(random.randint(2,4))
                print('Как же это...')
                time.sleep(random.randint(2,4))
                print('Так, ну вроде если ', a, ' умножить на ', b, ', то получится: ', a*b, sep='') 
                time.sleep(3)   
            elif choice == 4:
                print('Python проводит вычисления, никому не двигаться!')
                time.sleep(random.randint(2,4))
                print('Цифры на стол чтобы я их видел!')
                time.sleep(random.randint(2,4))
                print('Если ', a, ' разделить на ', b, ', то получится: ', a/b, sep='')
                time.sleep(3)
            elif choice == 5:
                print('Ох и задачка...')
                time.sleep(random.randint(2,4))
                print('Змеи такого не знают...')
                time.sleep(random.randint(2,4))
                print('Но я думаю что ', b, ' помещается в ', a, ', ', a//b, ' раз(а), так что ответ ', a//b, sep='')
                time.sleep(3)
            elif choice == 6:
                print('Так ну если', a, 'разделить на', b, 'потом...')
                time.sleep(random.randint(2,4))
                print('Угу... это туда, это сюда...', a%b, 'в уме.')
                time.sleep(random.randint(2,4))
                print('Итак, остаток от деления ', a, ' на ', b, ', это: ', a%b, sep='')
                time.sleep(3)
            cls()
            while choice not in ('Y','y'):
                choice = input('Еще будем что-то считать? (Y/N): ')
                if choice in ('Y','y'):
                    continue
                elif choice in ('N','n'):
                    cls()
                    print('=======================================================================')
                    print('Спасибо что воспользовались услугами змеиного калькулятора. Досвидания!')
                    print('=======================================================================')
                    time.sleep(2)
                    cls()
                    return
                else:
                    print('Не не, давай мне или Y или N, по другому я не понимаю. :Р')
                

                
        elif choice == 7:
            cls()
            print('=======================================================================')
            print('Спасибо что воспользовались услугами Змеиного калькулятора. Досвидания!')
            print('=======================================================================')
            time.sleep(2)
            cls()
            break
        else:
            cls()
            print('Пожалуйста будьте благоразумны, ведёте себя как тестировщик!')
            print('Сделайте выбор из меню, указав цифру от 1 до 7, всё просто.')
            time.sleep(4)
            print('Давайте попробуем еще раз.')
            time.sleep(2)
            cls()