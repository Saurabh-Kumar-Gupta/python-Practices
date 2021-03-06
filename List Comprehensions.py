# Author -- Saurabh Kumar Gupta                                                                                            Date -- 13 dec 2021

# This Python File shows how list comprehensions can save you a lot of time and frustations with the creation of lists. 

# 1. Making a list that goes from 1 to 15 in one line
print("\n NO.1 - Creating a normal list comprehension which get me values from 1 to 15 in one line. \n")

print([i for i in range(1,16)])              # we can get a whole list with just one line


# 2. Doing math with your comprehensions. 
print("\n \n N0.2 Doing math with List comprehensions \n")

print([i*10 for i in range(1,11)])            # every element will be multiplied by 10 



#3. Making it even more intresting by having a conditional statement. 
print("\n \n NO.3 using a conditional statement to have more control over the comprehensions \n")

print([i for i in range(10,210) if i%10 == 0])    # every element will be tested against the specific condition you put. 


#4. Getting bonanza with the comprehensions and using a function to make the list. 
print("\n \n NO.4 Using a function to create a list for ultimate list customization. \n")        # Function destined list comprehensions 

def Lst_Function(i):     # the function for the facorial
    sum = 1
    for j in range(1, i+1):
        sum = sum*j
    return sum


print([Lst_Function(i) for i in range(1,10)])

s=[]
s=[s[-1] for x in range(1,10) if not s.append(x*s[-1] if s else 1)]
print(s)
