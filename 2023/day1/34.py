input_file = open('resources/input.txt', 'r')

calibration_values = input_file.readlines()

def get_first_number(cadena):
    for char in cadena:
        if char.isdigit():
            return char

cajita_de_todo = 0
for cadena in calibration_values:
    cajita_primer_numero = get_first_number(cadena)
    cajita_segundo_numero = get_first_number(cadena[::-1])
    cajita_de_todo = cajita_de_todo + int(cajita_primer_numero + cajita_segundo_numero)

print(cajita_de_todo)