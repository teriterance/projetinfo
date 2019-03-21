import numpy as np
import math

class Domino(list):
    
    def __init__(self, num1, num2, color = 0):
        '''initialazation of domino like two linked values of number,
        after we will introduce the concept of color'''
        if (num1 <= 6 and num1>= 0) and (num2 >= 0 and num2 <= 6):
            self.__Value = [num1, num2]
        else:
            print("the value must be betwen 0 and 6")
        self.__Color = color #give a default value 0  to color

    def __str__(self):
        '''use str 2 to print in scree a domino'''
        return str2()

    @property
    def get_Value(self):
        ''' this function allow to get the values of different domino'''
        return self.__Value
    
    def nb_point(self):
        '''this fucntion return the nuber off point of the domino value directly sum of num1 and num2'''
        return sum(self.Value)
    
    def str2(self):
        '''convert the domino to the console version of then'''
        return str([[str(self.__Value[0])],[str(self.__Value[1])]])
