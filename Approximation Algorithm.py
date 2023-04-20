task_length = float(input("Enter the assigned total task length (in half-hour(s)):"))

portions = { }

#First entered income value should begin with ID no 1 and length of the first portion of work hour should be 0.5h
id = 1
len = 0.5

n = task_length * 2

max_profit = 0

#For all 5 portions assign the decent ID no, length and unit (income per half-hour) of each portion
for i in range (0, int(n)):
    unit = 0

    print("Enter the payment value (in TL) for task portion ID ", id, "having length", len, "hour(s): ")
    income = float(input())

#To calculate the unit, entered hour(s) amount it multiplied by 2 because each hour has 2 half. Then the matching portion of income is divided to it.
    unit = income / (len * 2)

#Create dictionary where keys are length of the portion, unit value of the portion, ID of the portion. And where value is the income that the portion brings.
    portions[(unit, id, len)] = income
 
#If current profit is less than the unit, then max_profit should be equal to this unit's value.        
    if (unit >= max_profit):
        max_profit = unit

    id +=  1
    len +=  0.5
    i += 1
        
day = 0

sort_data = sorted(portions.keys(), reverse = True)

#for i in range (0,5):
#    print(sort_data[i][0])

j=0
m=0

print()

#While there is still some amount of time to work:
while(task_length > 0):
    if (task_length >= sort_data[0][2]):                #If remaining time provides to do the task with the most profitable choice  
        task_length = task_length - sort_data[m][2]     #Recalculate the remaining time by subtracting the time it takes for the best choice
        day += 1                                        #Since this will be the work of 1 day, increment the day count.
        print("On Day ", day ,"do task portion with ID ", sort_data[m][1])

    elif (task_length < sort_data[j][2]):     
        if (m < n ) and (task_length >= sort_data[m+1][2]):
            task_length = task_length - sort_data[m+1][2]
            day += 1
            print("On Day ", day ,"do task portion with ID ", sort_data[m+1][1])
            j += 1    
        else:
            m = m + 1   

    else:    
        j += 1

print("\nThe most profitable completion of the assigned task takes", day ,"day(s).")
