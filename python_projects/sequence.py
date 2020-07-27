# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 14:24:22 2020

@author: username
"""

class sequence():
    numbers = []
    
    def __init__(self,numbers):
        self.numbers = numbers
        
    def arithmetic(self):
        N = len(self.numbers)
        s_N = self.numbers[0] + (N-1)*(self.numbers[1]-self.numbers[0])
        
        if s_N == self.numbers[N-1]:
            print("arithmetic series increasing by {}".format(self.numbers[1]-self.numbers[0]))
    
    def geometric(self):
        N = len(self.numbers)
        s_N = self.numbers[0]*(self.numbers[1]/self.numbers[0])**(N-1)
        
        
        if s_N == self.numbers[N-1]:
            print("geometric series increasing by {}".format(self.numbers[1]/self.numbers[0]))
        
    def fibonacci(self):
        old=self.numbers[0]
        new=self.numbers[1]
        N = len(self.numbers)-2
        for i in range(0,N):
            next_term = old+new
            old=new
            new=next_term
            
     
        if old == self.numbers[N] and new == self.numbers[N+1]:
            print("fibonacci")
  
            
            
    def quadratic(self):
        s_1 = self.numbers[0]
        s_2 = self.numbers[1]
        s_3 = self.numbers[2]
        
        a = 1/2*s_1 - s_2 +1/2*s_3
        b = -5/2*s_1+4*s_2-3/2*s_3
        c = 3*s_1 - 3*s_2 + s_3
        N = len(self.numbers)
        
        series = []
        count=0
        for i in range(1,N+1):
            series.append(int( a*i**2 + b*i + c))
           
            if series[i-1] == self.numbers[i-1]:
                count+=1
        
        if count == N:
            print("quadratic with coeffs. {}, {}, {}".format(a,b,c))
         
test= [ 96, 48, 12, 2, 4, 16]




test_sequence= sequence(test)
odd = sequence(test[::2])
even = sequence(test[1::2])


try:
    test_sequence.arithmetic()
    odd.arithmetic()
    even.arithmetic()
except:
    pass
try:
    test_sequence.geometric()
    odd.geometric()
    even.geometric()
except:
    pass
try:
    test_sequence.fibonacci()
    odd.fibonacci()
    even.fibonacci()
except:
    pass
try:
    test_sequence.quadratic()
   # odd.quadratic()
   # even.quadratic()
except:
    pass
#now need to test for mixed series, make subsets