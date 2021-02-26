class code:
    def __init__(self, output_file):
        self.output = open(output_file, 'w')

    def address(self, address):
        # Convert integer address to 16-bit binary
        bin_address = bin(address)[2:]
        bin_address_16bit = bin_address.zfill(16)
        self.output.write(str(bin_address_16bit)+'\n')

    def comp(self, command):
        start = '111'
        a = '0'

        if command.find('M') != -1:
            a = '1'

        if command == '0':
            c = '101010'
        if command == '1':
            c = '111111'
        if command == '-1':
            c = '111010'
        if command == 'D':
            c = '001100'
        if command == 'A' or command == 'M':
            c = '110000'
        if command == '!D':
            c = '001101'
        if command == '!A' or command == '!M':
            c = '110001'
        if command == '-D':
            c = '001111'
        if command == '-A' or command == '-M':
            c = '110011'
        if command == 'D+1':
            c = '011111'
        if command == 'A+1' or command == 'M+1':
            c = '110111'
        if command == 'D-1':
            c = '001110'
        if command == 'A-1' or command == 'M-1':
            c = '110010'
        if command == 'D+A' or command == 'D+M':
            c = '000010'
        if command == 'D-A' or command == 'D-M':
            c = '010011'
        if command == 'A-D' or command == 'M-D':
            c = '000111'
        if command == 'D&A' or command == 'D&M':
            c = '000000'
        if command == 'D|A' or command == 'D|M':
            c = '010101'

        self.output.write(start+a+c)


    def dest(self, command):
        if command is None:
            d = '000'
        if command == 'M':
            d = '001'
        if command == 'D':
            d = '010'
        if command == 'MD':
            d = '011'
        if command == 'A':
            d = '100'
        if command == 'AM':
            d = '101'
        if command == 'AD':
            d = '110'
        if command == 'AMD':
            d = '111'

        self.output.write(d)


    def jump(self, command):
        if command is None:
            j = '000'
        if command == 'JGT':
            j = '001'
        if command == 'JEQ':
            j = '010'
        if command == 'JGE':
            j = '011'
        if command == 'JLT':
            j = '100'
        if command == 'JNE':
            j = '101'
        if command == 'JLE':
            j = '110'
        if command == 'JMP':
            j = '111'

        self.output.write(j+'\n')
