// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

    @SCREEN
    D=A
    @addr
    M=D
    @8192
    D=A
    @n
    M=D

(INFINITELOOP)
    @KBD
    D=M
    @SET
    D;JEQ
    D=-1
    
(SET)
    @set
    M=D
    @i
    M=0
(WB)
    @i
    D=M
    @n
    D=D-M
    @INFINITELOOP    //if i == n, then the screen is set
    D;JEQ
    
    @i
    D=M
    @addr
    A=M+D
    D=A
    @temp
    M=D
    
    @set
    D=M
    @temp
    A=M   
    M=D              //RAM[addr+i] = 0 or -1
    
    @i
    M=M+1
    @WB
    0;JMP