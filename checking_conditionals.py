""" In this task, you will implement a check using the if … else structure you learned earlier.
You are required to create a program that uses this conditional.

At your school, the front gate is locked at night for safety.
You often need to study late on campus. There is sometimes a night guard on duty who can let you in .
You want to be able to check if you can access the school campus at a particular time.

The current hour of the day is given in the range 0, 1, 2 … 23 and the guard’s presence is indicated by with a True/False boolean.

If the hour is from 7 to 17, you do not need the guard to be there as the gate is open
If the hour is before 7 or after 17, the guard must be there to let you in

Using predefined variables for the hour of the day and whether the guard is present or not, write an if statement to print out whether you can get in .

Example start:
hour = 4
guard = True

Example output:
'You're in !'

Make use of the if statement structure to implement the program.
 """
current_hour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

hour = float(input("What time is it? "))
# if the hour is between 7 to 17
if hour >= 7 and hour <= 17:
    print("You are in!")
# if the hour is before 7am
elif hour < 7:
    print("The guard must be there to let you in")
# if the hour is after 17
elif hour > 17:
    print("The guard must be there to let you in")
