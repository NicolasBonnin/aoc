input_file = open('resources/input.txt', 'r')

#467..114..
#...*......
#..35..633.
#......#...
#617*......
#.....+.58.
#..592.....
#......755.
#...$.*....
#.664.598..



# agrego linea 1 en vacio para la primera vuelta
# lineas 1 2 y 3
# miro linea 2 y tomo el primer numero, leo la posicion que ocupa
# si el primer nro tiene un symbol a la derecha o a la izquierda, lo anoto
# sino busco en la linea 2 y linea 3, para ver si hay symbol abajo o arriba + a la derecha o izquierda (rango [x-1, y+1]), si tiene lo anoto
# ejemplo 114: tiene las posiciones 6-8. Tengo que buscar en (linea 1: 5 o 9) o (linea 2: 5 o 9) o (linea 3: 5 o 9)

# una vez pasada la linea, cargo las proximas 3. Linea 2 pasa a ser linea 1, linea 3 pasa a ser linea 2, proxima linea pasa a ser linea 3

def char_is_symbol(char):
    return char == '*' or char == '+' or char == '$' or char == '#'

def has_symbol_above_or_below(line, pos1, pos2):
    for i in range(pos1-1, pos2+1):
        if char_is_symbol(line[i]):
            return True
    return False

def has_symbol_in_same_line(line, pos1, pos2):
    if char_is_symbol(line[pos1-1]) | char_is_symbol(line[pos2+1]):
        return True

def has_symbol_adjacent(line_pre, line_act, line_next, pos1, pos2):
    if has_symbol_in_same_line(line_act, pos1, pos2):
        return True
    if has_symbol_above_or_below(line_pre, pos1, pos2):
        return True
    if has_symbol_above_or_below(line_next, pos1, pos2):
        return True

def get_number_from_string(string):
    return [int(s) for s in string.split() if s.isdigit()][0]

lines = []
for line in input_file.readlines():
    lines.append(line)

line_pre = ''
line_act = ''
line_next = ''
total_value = 0
length = len(lines)
for i in range(0, length):
    line_act = lines[i]
    if i > 0:
        line_pre = lines[i-1]
    if i < length - 1:
        line_next = lines[i+1]
    pos1 = -1
    pos2 = -1
    for j in range(0, len(line_act)):
        if line_act[j].isdigit():
            if pos1 == -1:
                pos1 = j
            else:
                pos2 = j
                break
        if char_is_symbol(line_act[j]):
            if has_symbol_adjacent(line_pre, line_act, line_next, j-1, j+1):
                print('Linea: ' + str(i) + ' Posicion: ' + str(j))
                break
    line_pre = line_act
    line_act = line_next
    line_next = ''
