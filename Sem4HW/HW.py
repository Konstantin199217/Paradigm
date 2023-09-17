from math import sqrt

'''
Написать скрипт для расчета корреляции Пирсона между
двумя случайными величинами (двумя массивами).

'''
def pirson(mylist_x, mylist_y):
    if len(mylist_x) != len(mylist_y):
        return None
    else:
        n = len(mylist_x)
        sum_x = sum(mylist_x) # сумма х
        sum_y = sum(mylist_y) # сумма y
        sum_x_squared = 0
        sum_y_squared = 0
        for i in range(len(mylist_x)):
            sum_x_squared += mylist_x[i]*mylist_x[i]    # сумма квадратов х
            sum_y_squared += mylist_y[i]*mylist_y[i]    # сумма квадратов у

        sum_xy = 0                                      # последовательная сумма произведений
        for i in range(len(mylist_x)):
            sum_xy += mylist_x[i]*mylist_y[i]


        chislitel = n *sum_xy - sum_x*sum_y
        znamenatel = sqrt((n*sum_x_squared-sum_x**2)*(n*sum_y_squared-sum_y**2))
        if znamenatel == 0:
            r_xy = 0
        else: r_xy = chislitel/znamenatel
        return r_xy


mylist1 = [1,2,3,5,8,9,10]
mylist2 = [8,8,7,4,2,1]
print(pirson(mylist1,mylist2))