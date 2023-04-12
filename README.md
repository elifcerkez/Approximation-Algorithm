# Approximation-Algorithm

Remote Worker’s Overtime Plan:

ABC company that you work for makes remote working payment to its employees for each portion the task in varying-half-hour slots basis. For example, if an employee works for 0.5 hour to complete a portion of an assigned task then ABC pays 100 TL; for its 1 hour portion 500 TL; for 1.5 hours portion 800 TL etc. (see Figure 1 below). Notice that the payment amount is a strictly increasing function of work-hours.

Assume that your employer assigns you a task that requires total 𝑁 hour(s) of overtime work for its completion. According to the rules & regulations of the ABC company:
“For each day, you are allowed to complete only one portion of the task in only one overtime working slot. Once you complete a portion of the task your wage is paid, immediately.”

For example, if you plan to work for 2.5 hours today, you can’t realize it in two consecutive overtime working slots of 1 hour + 1.5 hours on the same day but instead, you can do it today either in one single 2.5 hours slot or in two (or more) separate (not necessarily consecutive) days.

Your aim is to generate a most profitable plan on daily basis to complete the given 𝑁 hours length task assigned to you and to compute how many days it takes to complete the assigned task.

SAMPLE INPUT:
Enter the assigned total task length (in half-hour(s)): 2.5
Enter the payment value (in TL) for task portion ID 1 having length 0.5 hour(s): 100 Enter the payment value (in TL) for task portion ID 2 having length 1 hour(s): 500 Enter the payment value (in TL) for task portion ID 3 having length 1.5 hour(s): 800 Enter the payment value (in TL) for task portion ID 4 having length 2 hour(s): 900 Enter the payment value (in TL) for task portion ID 5 having length 2.5 hour(s): 1000

A SAMPLE OUTPUT:
On Day 1 do task portion with ID 3
On Day 2 do task portion with ID 2
The most profitable completion of the assigned task takes 2 day(s).



