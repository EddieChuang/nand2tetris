compTable = dict({"0":"101010", "1":"111111", "-1":"111010", "D":"001100",
                  "A":"110000", "M":"110000", "!D":"001101", "!A":"110001",
                  "!M":"110001", "-D":"001111", "-A":"110011", "-M":"110011",
                  "D+1":"011111", "A+1":"110111", "M+1":"110111", "D-1":"001110",
                  "A-1":"110010", "M-1":"110010", "D+A":"000010", "D+M":"000010",
                  "D-A":"010011", "D-M":"010011", "A-D":"000111", "M-D":"000111",
                  "D&A":"000000", "D&M":"000000", "D|A":"010101", "D|M":"010101"
                    })
                    
destTable = dict({"null":"000", "M":"001", "D":"010", "MD":"011",
                  "A":"100", "AM":"101", "AD":"110", "AMD":"111"})

jumpTable = dict({"null":"000", "JGT":"001", "JEQ":"010", "JGE":"011",
                  "JLT":"100", "JNE":"101", "JLE":"110", "JMP":"111"})

                  

def encode(instruction, symbolTable):
    
    instruction_bin = list()
    for inst in instruction:
        binary = ""
        if inst[0] == '@':
            binary += "0"
            if inst[1].isdigit():
                binary += format(int(inst[1]), '015b')
            else:
                binary += symbolTable.get(inst[1])
        else:
            if (inst[1].find('M') != -1):
                binary += "1111"
            else:
                binary += "1110"
            binary += compTable[inst[1]] + destTable[inst[0]] + jumpTable[inst[2]]
        instruction_bin.append(binary)
    
    return instruction_bin
        
            
