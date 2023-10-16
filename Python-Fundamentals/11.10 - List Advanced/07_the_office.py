def check_employee_hapiness():
    happiness_list = list(map(int, input().split()))
    happiness_factor = int(input())

    improved_happines = [happiness * happiness_factor for happiness in happiness_list]

    average_happiness = sum(improved_happines) / len(improved_happines)
    happy_count = sum(happiness >= average_happiness for happiness in improved_happines)
    total_count = len(improved_happines)

    message = 'happy' if happy_count >= total_count / 2 else 'not happy'

    result = f'Score: {happy_count}/{total_count}. Employees are {message}!'

    return result

print(check_employee_hapiness())

