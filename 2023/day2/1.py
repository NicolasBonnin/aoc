input_file = open('resources/input.txt', 'r')

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

game_id_total_value = 0

def get_number_from_string(string):
    return [int(s) for s in string.split() if s.isdigit()][0]

def source_dice_hand(hand):
    for dice in hand.split(','):
        quantity = get_number_from_string(dice)
        if ("red" in dice):
            if quantity > MAX_RED:
                return True
        elif ("green" in dice):
            if quantity > MAX_GREEN:
                return True
        elif ("blue" in dice):
            if quantity > MAX_BLUE:
                return True
    return False


for game in input_file.readlines():
    game_id = get_number_from_string(game.split(':')[0].strip())
    game_values = game.split(':')[1].strip().split(';')
    impossible = False
    for hand in game_values:
        if source_dice_hand(hand):
            impossible = True
            break
    game_id_total_value += 0 if impossible else game_id

print(game_id_total_value)