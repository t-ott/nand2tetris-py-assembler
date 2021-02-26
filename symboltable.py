class symboltable():
    def __init__(self):
        # Retain decimal ROM / RAM addresses as values, symbols as keys
        self.table = {'SP':'0',
                      'LCL':'1',
                      'ARG':'2',
                      'THIS':'3',
                      'THAT':'4',
                      'SCREEN':'16384',
                      'KBD':'24576'}

        # Add R0-R15
        for i in range(16):
            self.table['R'+str(i)] = str(i)

        # Initialize next_RAM address
        # Note that program should not exceed RAM address 16383
        self.next_RAM = 16

    def add_entry(self, symbol, current_ROM=None):
        # current_ROM arg is not supplied when putting in variable
        if current_ROM is None:
            self.table[symbol] = str(self.next_RAM)
            self.next_RAM += 1
            return self.next_RAM - 1
        else:
            self.table[symbol] = str(current_ROM)

    def contains(self, symbol):
        if symbol in self.table:
            return True
        else:
            return False

    def get_address(self, symbol):
        return self.table.get(symbol)
