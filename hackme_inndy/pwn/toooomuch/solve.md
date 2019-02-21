# [50+100] toooomuch1/2

## Problem

1. Can you pass the game?
2. Get a shell, please.
Tips: Buffer overflow, `0x8048560`, shellcode

```
nc hackme.inndy.tw 7702
```

## Solution

```
[*] '/home/vagrant/pwn/CTF/hackme_inndy/pwn/toooomuch/toooomuch'
    Arch:     i386-32-little
    RELRO:    No RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x8048000)
    RWX:      Has RWX segments
```

Notice that security option of target binary is all off, so it's very easy to exploit it.
I wrote two exploit, one used `ret2shellcode`, the other one used `ret2libc`.

toooomuch is easy, once you disassemble the binary taking a look at `check_passcode`, you could calculate what's the passcode. After entering the passcode, it turn into a guess number game. If you guess the correct number, you can get the first flag.

toooomuch2 is basic bof exploit. I use two method (mentioned above) to develop the exploit.