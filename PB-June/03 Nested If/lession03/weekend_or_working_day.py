#user input
day = input()

user_output = ''

#logic
if day == "Monday":
    user_output = "Working day"
elif day == "Tuesday":
    user_output = "Working day"
elif day == "Wednesday":
    user_output = "Working day"
elif day == "Thursday":
    user_output = "Working day"
elif day == "Friday":
    user_output = "Working day"
elif day == "Saturday":
    user_output = "Weekend"
elif day == "Sunday":
    user_output = "Weekend"
else:
    user_output = "Error"

#user output
print(user_output)