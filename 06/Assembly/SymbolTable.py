buildIn = dict({"R0":"0", "R1":"1", "R2":"2", "R3":"3", "R4":"4", 
                "R5":"5", "R6":"6", "R7":"7", "R8":"8", "R9":"9",
                "R10":"10", "R11":"11", "R12":"12", "R13":"13", "R14":"14", "R15":"15",
                "SP":"0", "LCL":"1", "ARG":"2", "THIS":"3", "THAT":"4", 
                "SCREEN":"16384", "KBD":"24576"})

class SymbolTable:
    def __init__(self):
        self.table = dict()
        self.label = dict()
        self.address = 16
    
    def setVariable(self, symbol):
        if self.table.get(symbol) == None:
            if self.address == 16384 or self.address == 24576:
                self.address += 1            #is  SCREEN or KBD
            if buildIn.get(symbol) != None:  #is  build-in register
                self.table[symbol] = format(int(buildIn[symbol]), '015b')
            else:                            #not build-in register
                self.table[symbol] = format(self.address, '015b')
                self.address += 1

    def setLabel(self, symbol, i):
        self.table[symbol] = format(i, '015b')

    def get(self, symbol):
        return self.table[symbol]