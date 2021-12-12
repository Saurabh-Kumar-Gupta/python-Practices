# Author -- Saurabh Kumar Gupta                                                                                            Date -- 13 dec 2021

# This Python File shows how list comprehensions can save you a lot of time and frustations with the creation of lists. 

# 1. Making a list that goes from 0 to 150 in one line

print([i for i in range(15)])


# 2. Doing math with your comprehensions. 
print("\n \n N0.2 Doing math with List comprehensions \n \n")

print([i*10 for i in range(1,11)])            # every element will be multiplied by 10 



#3. Making it even more intresting by having a conditional statement. 
print("\n \n NO.3 using a conditional statement to have more control over the comprehensions \n \n")

print([i for i in range(10,210) if i%10 == 0])    # every element will be tested against the specific condition you put. 
