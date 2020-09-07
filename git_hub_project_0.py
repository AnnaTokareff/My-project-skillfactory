import numpy as np
import random

def game_core_v2(number):
    '''Находим середину промежутка, создаем рандомное число и меняем границы нашего промежутка относительно переменной middle_range.
       Функция принимает загаданное число и возвращает число попыток'''
    
    count = 1
    min_num = 1
    max_num = 100
    
    
    while True:         # бесконечный цикл
        count += 1
        middle_range = (min_num + max_num) // 2
        predict = np.random.randint(min_num, max_num+1)
        
        if predict != number:
            
            if number > middle_range:
                min_num = middle_range + 1          # если наше число больше средней границы, сокращаем расстояние от нижней границы
                
            elif number < middle_range:
                max_num = middle_range - 1          # если наше число меньше средней границы, сокращаем расстояние до верхней границы
                
                
        else:
            return(count)   # если число совпало с загаданным, возвращаем кол-во попыток
            
#game_core_v2(16)             
   

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
score_game(game_core_v2)

