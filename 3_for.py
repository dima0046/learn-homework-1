"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
def count_average(list):
    scores_sum_all = 0
    len_all = 0

    for item in list:
      scores_sum = 0
      
      for score in item["items_sold"]:
        scores_sum += score
        scores_avg = scores_sum / len(item["items_sold"])
      
      print(f"Суммарное количество продаж для {item['product']}: {round(scores_sum, 2)}")
      print(f"Среднее количество продаж для {item['product']}: {round(scores_avg, 2)}" )
      
      scores_sum_all += scores_sum
      len_all += len(item["items_sold"])
    
    print(f"Суммарное количество всех продаж {scores_sum_all}")
    print(f"Среднее количество всех продаж {scores_sum_all / len_all}")
    
    return

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    list =   [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]

    count_average(list)

    return
    
if __name__ == "__main__":
    main()
