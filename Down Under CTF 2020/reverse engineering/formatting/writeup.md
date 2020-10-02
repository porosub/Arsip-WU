# Reverse Engineering

| Reverse Engineering  |
| ------------- |
| [Formatting (100 pts)](#formatting-100-pts)|

## Formatting (100 pts)

### Soal:
Its really easy, I promise

### Pembahasan:
diberi sebuah file. pertama kita cek file dulu. didapatkan file ELF 64-bit not stripped.
informasi lebih lanjut:
```
formatting: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=bd9f51c1f1535b269a0707054009063f984f6738, for GNU/Linux 3.2.0, not stripped
```
karena deskripsi soal menujukkan itu sangat mudah, kami mencoba dump strings semua yang ada dalam filenya didapatkan:
```
...
...
...
ARAQAPWQA
[]A\A]A^A_
DUCTF{haha its not that easy}
%s%02x%02x%02x%02x%02x%02x%02x%02x}
d1d_You_Just_ltrace_
;*3$"
...
...
...
```
setelah kami lakukan ltrace didapatkan strings d1d_You_Just_ltrace_296faa2990ac. kami inputkan ternyata masih salah.
lalu kami lakukan analisa di gdb, kami breakpoint setelah sprintf. ternyata flag disimpan dalam stack.

<details>
<summary>Flagnya</summary>
DUCTF{d1d_You_Just_ltrace_296faa2990acbc36}
</details>