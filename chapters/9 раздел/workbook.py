from colorama import Back, Style
def draw_lattice(integer):
    lattice = []
    cell = '___|'
    for row in range(0, integer):
        r = []
        if row == (integer - 1):
            cell = '   |'
        for column in range(0, integer):
            if column == (integer - 1):
                r.append(Back.YELLOW + cell[:-1] + Style.RESET_ALL)
                break
            r.append(Back.YELLOW + cell + Style.RESET_ALL)
        lattice.append(r)
    return lattice
def show_lattice(lattice):
    for el in lattice:
        print(*el, sep = '')
def step(player, lattice, row, column):
    cell = lattice[row - 1][column - 1]
    string = f'_{player}_' if row != len(lattice) else f' {player} '
    color_cell = (Back.BLUE if player == 'X' else Back.GREEN) + (string)
    lattice[row - 1][column - 1] = cell.replace('___', color_cell).replace('   ', color_cell)
    return lattice
def count_x_o(lattice):
    return ''.join(sum(lattice, [])).count('X') + ''.join(sum(lattice, [])).count('O')
def tic_tac_toe(integer):
    lattice = draw_lattice(integer)
    show_lattice(lattice)
    while count_x_o(lattice) < (integer ** 2):
        value = f'{'X' if (count_x_o(lattice) % 2) == 0 else 'O'}'
        row = int(input(f'Какая строка для {value}? '))
        if row > len(lattice):
            print(f'Номер строки должен быть меньше {integer}')
            continue
        column = int(input(f'Какой столбец для {value}? '))
        if column > len(lattice):
            print(f'Номер столбца должен быть меньше {integer}')
            continue
        
        lattice = step(value, lattice, row, column)
        show_lattice(lattice)
tic_tac_toe(3)
