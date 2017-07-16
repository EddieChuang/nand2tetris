import re, SymbolTable

class Parser:
    def __init__(self, f):
        self.file = f
        self.instruction = list()
        self.symbol = list()

    def ignoreComment(self, line):
        pattern = re.compile(r'[^/\n]*')
        match = pattern.search(line)
        return match.group()

    def CInstruction(self, str):
        dest, comp, jump = "null", "0", "null";
        equalPos = str.find("=")
        semicPos = str.find(";")

        #D=D-M;JGT
        if equalPos != -1 and semicPos != -1:
            dest = str[0:equalPos]
            comp = str[equalPos+1:semicPos]
            jump = str[semicPos+1:]
        #D=D-M
        elif equalPos != -1:
            dest = str[0:equalPos]
            comp = str[equalPos+1:]
        #D;JGT
        elif semicPos != -1:
            comp = str[0:semicPos]
            jump = str[semicPos+1:]
        
        return [dest, comp, jump]
    
    def parseVariable(self, symbolTable):
    
        for line in self.file:
            
            match = self.ignoreComment(line)
            match = match.replace(" ", "")
            
            if match == "" or match[0] == "(":
                continue 
            if match[0] == '@':
                self.instruction.append(['@', match[1:]])
                if not(match[1:].isdigit()):
                    symbolTable.setVariable(match[1:])
            else:
                self.instruction.append(self.CInstruction(match));
        return self.instruction, symbolTable
    
    def parseLabel(self):
        i = 0
        symbolTable = SymbolTable.SymbolTable()
        for line in self.file:
            match = self.ignoreComment(line)
            match = match.replace(" ", "")
            if match == "":
                continue

            if match[0] == "(":
                symbolTable.setLabel(match[1:-1], i)
                i -= 1
            i += 1
        self.file.seek(0)
        return symbolTable