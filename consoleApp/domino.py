import numpy as np
import math

class Domino(list):
    
    def __init__(self, num1, num2, color = 0):
        '''initialazation of domino like two linked values of number,
        after we will introduce the concept of color'''
        if (num1 <= 6 and num1>= 0) and (num2 >= 0 and num2 <= 6):
            self.append(num1)
            self.append(num2)
        else:
            print("the value must be betwen 0 and 6")
        self.__Color = color #give a default value 0  to color

    @property
    def get_Value(self):
        ''' this function allow to get the values of different domino'''
        return self
    
    def nb_point(self):
        '''this fucntion return the nuber off point of the domino value directly sum of num1 and num2'''
        return sum(self)
