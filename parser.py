class parser:
    def __init__(self, input_file):
        all_input = open(input_file).read()

        input = []
        lines = 0

        for line in all_input.splitlines():
            # Remove commented lines and whitespace lines
            if line.startswith('//') or len(line)<1:
                continue

            # Retain actual input code and count number of lines
            else:
                input.append(line)
                lines += 1

        self.lines = lines
        self.input = input

        # Initialize line iterator to 0, and ROM iterator to 0
        # Note that labels (XXX) don't get translated and stored in the program
        self.current_line = 0
        self.current_command = None

    def hasMoreCommands(self):
        if self.current_line < self.lines:
            return True
        else:
            return False

    def advance(self):
        command = self.input[self.current_line]

        # Remove any in-line comments
        findComment = command.find('//')
        if findComment != -1:
            self.current_command = command[:findComment].lstrip()
        else:
            self.current_command = command.lstrip()

        self.current_line += 1

    def commandType(self, command):
        if command.startswith('@'):
            return 'A_COMMAND'
        elif command.startswith('('):
            return 'L_COMMAND'
        else:
            return 'C_COMMAND'

    def symbol(self, command, type):
        if type == 'A_COMMAND':
            return command[1:]
        if type == 'L_COMMAND':
            return command[1:-1]

    def dest(self, command):
        findEqual = command.find('=')
        if findEqual != -1:
            return command[:findEqual]
        else:
            return None

    def comp(self, command):
        findEqual = command.find('=')
        findSemi = command.find(';')
        if findEqual != -1 and findSemi != -1:
            return command[findEqual+1:findSemi]
        elif findEqual == -1:
            return command[:findSemi]
        else:
            return command[findEqual+1:]

    def jump(self, command):
        findSemi = command.find(';')
        if findSemi != -1:
            return command[findSemi+1:].strip()
        else:
            return None
