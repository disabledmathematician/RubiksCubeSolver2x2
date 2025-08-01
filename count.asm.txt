	includelib	kernel32.lib
ExitProcess	proto
	.code
; Charles Truscott Watters
; Managing to write a Fibonacci in a few bytes, not a lot of experience with EFLAGS and JMP/JCC
fib proc;
	ADD RAX, RBX;
	XCHG RAX, RBX;
	int 3;
	INC RCX;
	CMP RCX, 9;
	JNE fib;
fib endp
	
main	proc;
	MOV RAX, 1;
	MOV RBX, 2;
	MOV RCX, 2;
	jmp fib;
	mov RCX, 78;
	call ExitProcess;
main	endp
	end

0, 1
1, 1
1, 2
2, 3

