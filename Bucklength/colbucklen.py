# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 19:37:41 2022

@author: GoffX
"""
import math

print('''Программа предназначена для определения коэффициента расчетной длины
      \rвнецентренно сжатых железобетонных элементов постоянного прямоугольного
      \rпоперечного сечения с несмещаемыми податливыми заделками на обоих концах,
      \rдопускающими ограниченный поворот.\n
      \rСоотношение длин сторон элемента принимают из условия b/h <= 1, где h - 
      \rсторона сечения элемента параллельная плоскости поворота заделок, т.е. h - 
      \rдлинная сторона, а коэффициент расчетной длины определяется для сечения
      \rс наибольшей жесткостью. phi1 > 0, phi1 >= abs(phi2).''')

while True:
    
    try:
        phi1, phi2 = input('''\nЧерез пробел введите значения углов поворта
                           \rзаделок в минутах: ''').split()
        phi1 = float(phi1)
        phi2 = float(phi2)
                
        if abs(phi1) > 1200 or abs(phi2) > 1200:
            print('''\n!!!ACHTUNG: проверьте расчетную схему или значения углов
                  \rповорота, как минимум один из них превышает по модулю 20
                  \rградусов.''')
                        
        if phi1 <= 0 and phi2 <= 0:
            print('''\n!!!ACHTUNG: как минимум одно из значений угла поворота
                  \rдолжно быть положительным.''')
            1/0 #Для организации обработки исключения
            
        if phi1 < phi2:
            phi1, phi2 = phi2, phi1
            print('''\nВ соответствии с соглашениями была изменена нумерация углов
                  \rповорота (phi1 >= phi2).''')
                  
        if not math.isnan(phi1) and not math.isnan(phi2) and not math.isinf(phi1) and not math.isinf(phi1):
            pass
        else:
            float('str_for_error')
        
        break
    
    except ValueError:
        print('''\n!!!ACHTUNG: значения углов поворота должны быть числовые. Два
              \rчисла через пробел.''')
        
    except ZeroDivisionError:
        pass
    
while True:
    
    try:
        l, b, h = input('\nВведите значения высоты и размеров колонны (l, b, h) в мм: ').split()
        
        l = float(l)
        b = float(b)
        h = float(h)
        
        if  abs(l) != l or abs(b) != b or abs(h) != h:
            print('\n!!!ACHTUNG: все значения должны быть положительными числами.')
            1/0 #Для организации обработки исключения
            
        if h < b:
            print('\n!!!ACHTUNG: значение размера колонны b должно быть меньше h.')
            1/0 #Для организации обработки исключения
            
        break
        
    except ValueError:
        print('\n!!!ACHTUNG: значения размеров должны быть числами.')
    
    except ZeroDivisionError:
        pass

lmbd = l/h

if abs(phi1) == phi1 and abs(phi2) == phi2:
    
    if lmbd <= 25:
        alpha = ((lmbd/40)*((phi2/phi1) - 2) - (lmbd**2/200)*((phi2/phi1) - 1.6))*(b/h)
    else:
        alpha = (lmbd - 16)*(0.43 - 0.27*(phi2/phi1))*(b/h)
        
    if phi1 <= alpha:
        k0 = 0.18*((phi1 - phi2)/alpha) - 0.14*(phi1*phi2/alpha**2) + 0.5
    else:
        k0 = 0.68 - 0.18*(phi2/phi1)
    
    if k0 < 0.5:
        k0 = 0.5
        
else:
    
    if lmbd <= 25:
        alpha = 0.004*lmbd*((lmbd - 0.6)*((abs(phi2)/phi1) + 2) - 10)*(b/h)
    else:
        alpha = 0.28*((lmbd + 4)*(0.2*(abs(phi2)/phi1) + 1) - 14)*(b/h)
        
    if phi1 <= alpha:
        k0 = 0.18*((phi1 - phi2)/alpha) - 0.14*(phi1*phi2/alpha**2) + 0.5
    else:
        alpha1 = 0.5*(phi1 + 0.34*(b/h)*(lmbd - 7.5))
        
        if abs(phi2) <= alpha1:
            k0 = 0.68 - 0.32*(phi2/phi1)
        else:
            k0 = 1
            
print('\nКоэффициент расчетной длины вдоль плоскости, параллельной стороне h: ', 
      round(k0, ndigits=2), '''\nРасчетная длина колонны, в плоскости, параллельной
      \rстороне h, мм: ''', round(k0*l))
      
input('\nНажмите Enter для завершения работы программы.')
        
    