# [pwn/50] homework

## problem
```
nc hackme.inndy.tw 7701
```
[Source Code](https://hackme.inndy.tw/static/pwn-easy.c), Index out bound, Return Address

## Solution

```
$ checksec homework
[*] '/home/vagrant/pwn/CTF/hackme_inndy/pwn/homework/homework'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
```

* Finding the vulnerability

The program(homework) can read/modify/sum an array of arr (len = 10). I played for a while ,and discovered it doesn't check the index, so you can input a number is greater than 9, and read/write memory outside the array of length 10.

> In the beginning, I thought I need to overflow the string inputed when the program starts before reading the src.
> And I just opened a gdb, trying to crash the program by inputing string "AAA..."
> And then I found the buffer is a global variable
> `char name[1024];`

* Thinking a explit

So far, we've got a 1 byte arbitrary read/write in memory after the array. The first thing come into my mind is write the return address, so we could get control of eip.

The program has a unused function called "call_me_maybe()", and it spawns a shell. I just use the address of that function.

Here comes with the problem: How do i get the relative offset of the return address to the array?

```c=
int arr[10], i, v, act;
```

Dragging the elf into IDA, quickly looking at the beginning of `run_program()`, I get these informations:

1. Size of stack inside `run_program()` is `0x48`
2. `arr[]` begin at `ebp - 0x34`

So we can calculate the the index of arr which will write the return address.

`0x34 / 4 = 013 = index of ebp`

So the index of return address is `14`

```
           +---------+
           |         |   arr[14] = return address
ebp + 4    +---------+
           |         |   arr[13] = old ebp
ebp        +---------+
           |         |   arr[12]
ebp - 4    +---------+
           |         |
  .             .
  .             .
  .             .
           |         |
           +---------+
           |         |   arr[0]
ebp - 0x34 +---------+
  .
  .
  .
ebp - 0x48 +---------+
```
