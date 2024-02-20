def age_assignment(*args, **kwargs):
    output = []
    for key, value in kwargs.items():
        for i in args:
            if i.startswith(key):
                output.append(f"{i} is {value} years old.")

    return "\n".join(sorted(output))


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))