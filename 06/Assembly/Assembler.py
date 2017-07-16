import Parser, Code, SymbolTable

fin = open('PongL.asm', 'r')
parser = Parser.Parser(fin)

symbolTable = parser.parseLabel()
instruction, symbolTable = parser.parseVariable(symbolTable);
bin = Code.encode(instruction, symbolTable)

fout = open('PongL.hack', 'w')

for b in bin:
    fout.write(b + '\n')