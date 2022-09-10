"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
def strings_checker(string1, string2):
  
    if type(string1) != str or type(string2) != str:
      return print("0")

    elif string1 == string2:
      return print("1")

    elif len(string1) > len(string2):
      return print("2")

    elif string1 != string2 and string2 == 'learn':
      return print("3")

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    strings_checker('hello', 123)
    strings_checker('hello', 'hello')
    strings_checker('hellolololo', 'hello')
    strings_checker('hello', 'learn')

    return
    
if __name__ == "__main__":
    main()
