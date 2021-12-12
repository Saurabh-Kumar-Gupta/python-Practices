# Author -- Saurabh Kumar Gupta                                                                                            Date -- 13 dec 2021

# This Python File shows how list comprehensions can save you a lot of time and frustations with the creation of lists. 

# 1. Making a list that goes from 0 to 150 in one line, and printing it in another. 

list1 = [i for i in range(151)]
print(list1)

# 2. Doing math with your comprehensions. 
print("\n \n N0.2 Doing math with List comprehensions \n \n")

list2 = [i*10 for i in range(1,101)]            # every element will be multiplied by 10 
print(list2)