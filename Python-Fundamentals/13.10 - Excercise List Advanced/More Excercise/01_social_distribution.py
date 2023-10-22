population = [int(x) for x in input().split(', ')]
minimum_wealth = int(input())

# You should distribute the wealth so that no part of the population has less than the minimum wealth.
# To do that, you should always take wealth from the wealthiest part of the population.


average = sum(population) / len(population)
if average < minimum_wealth:
    print('No equal distribution possible')
else:
    for index, number in enumerate(population):
        if number < minimum_wealth:
            to_be_added = (minimum_wealth - number)
            population[index] += (minimum_wealth - number)
            welthiest = max(population)
            index_of_welthies = population.index(welthiest)
            population[index_of_welthies] -= to_be_added

    print(population)