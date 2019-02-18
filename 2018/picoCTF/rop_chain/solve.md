# [pwn/350] rop chain

## problem

Can you exploit the following [program](https://2018shell1.picoctf.com/static/51c2b076860b7628c8d751424e923504/rop) and get the flag? You can findi the program in /problems/rop-chain_2_d25a17cfdcfdaa45844798dd74d03a47 on the shell server? [Source](https://2018shell1.picoctf.com/static/51c2b076860b7628c8d751424e923504/rop.c).

## solution

```
[*] '/home/vagrant/pwn/CTF/picoCTF/2018/pwn/rop_chain/rop'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
```

If you call functions with correct order:

1. `win_func1();`
2. `win_func2(0xBAAAAAAD);`
3. `flag(0xDEADBAAD);`

Then you get the flag.

Notice that don't touch `push ebp` or you can only enter a function with parameters twice.

If you insist to `ret` to `push ebp`, stack will look like this:
```
    [ arg_f2 ]
    [ arg_f1 ] ; arg_f1 but return addr for func2(arg_f2)
	[ ret  ] ; func2
	[ ret  ] ; func1(arg_f1)
	[ AAAA ]
	[ AAAA ]
	[ AAAA ]
```

You cannot jump to other places after ret to `func2`