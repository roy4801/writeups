# [100] ROP2

## Problem

```
nc hackme.inndy.tw 7703
```
**ROPgadget** not working anymore

## Solution

```
[*] '/home/vagrant/pwn/CTF/hackme_inndy/pwn/rop2/rop2'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
```

Firstly, the problem said ROPgadget is not working. I thought the ROPgadget is unusable. After struggling for a while, I realized that it's ROP chain functionality of `ROPgadget`unusable. You can still use ROPgadget to rip off the binary to get gadgets.

The exe has NX enabled. So we cannot just use ret2shellcode. But it has no PIE, so we can read "/bin/sh" to a address in data section.

And execve("/bin/sh", NULL, NULL) to get a shell.
