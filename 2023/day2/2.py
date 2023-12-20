input_file = open('resources/input.txt', 'r')

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def get_number_from_string(string):
    return [int(s) for s in string.split() if s.isdigit()][0]

def source_game_values(game_values):
    max_red = 1
    max_green = 1
    max_blue = 1
    for hand in game_values:
        for dice in hand.split(','):
            quantity = get_number_from_string(dice)
            if ("red" in dice):
                if quantity > max_red:
                    max_red = quantity
            elif ("green" in dice):
                if quantity > max_green:
                    max_green = quantity
            elif ("blue" in dice):
                if quantity > max_blue:
                    max_blue = quantity
    return [max_red, max_green, max_blue]


total_cubes = 0
for game in input_file.readlines():
    game_id = get_number_from_string(game.split(':')[0].strip())
    game_values = game.split(':')[1].strip().split(';')
    impossible = False
    cubes_quantity = source_game_values(game_values)
    total_cubes += int(cubes_quantity[0]) * int(cubes_quantity[1]) * int(cubes_quantity[2])

print(total_cubes)