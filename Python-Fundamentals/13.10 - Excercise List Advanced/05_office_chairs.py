def how_many_chairs(list):
    count = 0
    letter_to_count = "X"
    for item in list:
        letter_count = item.count(letter_to_count)
        count += letter_count
    return count


number_of_rooms = int(input())
free_chairs = 0
is_game_on = True

for room in range(1, number_of_rooms + 1):
    input_data = input().split()
    chairs = how_many_chairs(input_data[0])
    people = int(input_data[1])
    if people > chairs:
        print(f'{abs(chairs - people)} more chairs needed in room {room}')
        is_game_on = False
    else:
        free_chairs += (chairs - people)

if is_game_on:
    print(f'Game On, {free_chairs} free chairs left')



