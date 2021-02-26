#################################
# Run in command line
# ex: >>> python main.py Pong.asm
#################################

import sys
import parser
import code
import symboltable

parser = parser.parser(sys.argv[1]) # .asm input file from command line
code = code.code(sys.argv[1].split('.')[0]+'.hack') # .hack output file
symboltable = symboltable.symboltable()

############
# First pass
############

current_ROM = 0

while parser.hasMoreCommands():

    parser.advance()
    commandType = parser.commandType(parser.current_command)

    if commandType == 'A_COMMAND' or commandType == 'C_COMMAND':
        current_ROM += 1

    if commandType == 'L_COMMAND':
        # Get symbol
        symbol = parser.symbol(parser.current_command,commandType)

        # Add L-Command symbol and next ROM line
        symboltable.add_entry(symbol,current_ROM)


############
# Second pass
############

# Reset parser iterators
parser.current_line = 0
parser.current_command = None

while parser.hasMoreCommands():
    parser.advance()

    commandType = parser.commandType(parser.current_command)

    if commandType == 'A_COMMAND':
        symbol = parser.symbol(parser.current_command,commandType)

        try: # See if address is a decimal
            code.address(int(symbol))
        except: # Handle the symbol
            if symboltable.contains(symbol):
                address = symboltable.get_address(symbol)
                code.address(int(address))
            else:
                address = symboltable.add_entry(symbol)
                code.address(int(address))

    if commandType == 'C_COMMAND':
        comp = parser.comp(parser.current_command)
        code.comp(comp)

        dest = parser.dest(parser.current_command)
        code.dest(dest)

        jump = parser.jump(parser.current_command)
        code.jump(jump)
