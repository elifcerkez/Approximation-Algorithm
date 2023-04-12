task_length = float(input("Enter the assigned total task length (in half-hour(s)):"))

portions = { }

id = 1
len = 0.5

n = task_length * 2

max_profit = 0

for i in range (0, int(n)):
    unit = 0

    print("Enter the payment value (in TL) for task portion ID ", id, "having length", len, "hour(s): ")
    income = float(input())

    unit = income / (len * 2)

    portions[(unit, id, len)] = income
 
    if (unit >= max_profit):
        max_profit = unit

    id +=  1
    len +=  0.5
    i += 1
        
day = 0

sort_data = sorted(portions.keys(), reverse = True)

j=0
m=0

print()
while(task_length > 0):
    if (task_length >= sort_data[0][2]):               
        task_length = task_length - sort_data[m][2]     
        day += 1                                        
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
