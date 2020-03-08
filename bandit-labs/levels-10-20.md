# Level 10->11
https://overthewire.org/wargames/bandit/bandit11.html
## Login
```sh
ssh -l bandit10 bandit.labs.overthewire.org -p 2220
truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
```

## Level Goal
The password for the next level is stored in the file data.txt, which contains base64 encoded data

Commands you may need to solve this level
grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

```sh
bandit10@bandit:~$ cat data.txt | base64 -d
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
```


# Level 11->12
https://overthewire.org/wargames/bandit/bandit12.html

## Login
```sh
ssh -l bandit11 bandit.labs.overthewire.org -p 2220
IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
```

## Level Goal
The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

Commands you may need to solve this level
grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

Rot13 help: https://stackoverflow.com/questions/5442436/using-rot13-and-tr-command-for-having-an-encrypted-email-address

```sh
bandit11@bandit:~$ cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
```

# Level 12->13
https://overthewire.org/wargames/bandit/bandit13.html

## Login
```sh
ssh -l bandit12 bandit.labs.overthewire.org -p 2220
5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
```

## Level Goal
The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed.

For this level it may be useful to create a directory under /tmp in which you can work using mkdir. 

For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)

Useful resource explaining why this works: https://www.reddit.com/r/HowToHack/comments/2tizto/extracting_a_password_from_a_hex_dump_file/

```sh
$ cp data.txt /tmp/zxcvasdf123
$ cd /tmp/zxcvasdf123
xxd -r data.txt out1.bin
bandit12@bandit:/tmp/zxcvasdf123$ file out1.bin 
out1.bin: gzip compressed data, was "data2.bin", last modified: Tue Oct 16 12:00:23 2018, max compression, from Unix
bandit12@bandit:/tmp/zxcvasdf123$ zcat out1.bin | bzcat | zcat | tar xO | tar xO | bzcat | tar xO | zcat | file -
/dev/stdin: ASCII text

bandit12@bandit:/tmp/zxcvasdf123$ zcat out1.bin | bzcat | zcat | tar xO | tar xO | bzcat | tar xO | zcat 
The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

```


# Level 13->14

https://overthewire.org/wargames/bandit/bandit14.html

## Login
```sh
ssh -l bandit13 bandit.labs.overthewire.org -p 2220
8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
```
## Level Goal
The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14.

For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level.

Note: localhost is a hostname that refers to the machine you are working on

ssh, telnet, nc, openssl, s_client, nmap

```sh
ssh bandit14@localhost -i sshkey.private
```


# Level 14->15

https://overthewire.org/wargames/bandit/bandit15.html

## Level Goal
The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.


```
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e

bandit14@bandit:~$ cat /etc/bandit_pass/bandit14 | nc localhost 30000
Correct!
BfMYroe26WYalil77FoDi9qh59eK5xNr

```

# Level 15->16

https://overthewire.org/wargames/bandit/bandit16.html


## Login
```sh
ssh -l bandit15 bandit.labs.overthewire.org -p 2220
BfMYroe26WYalil77FoDi9qh59eK5xNr
```

## Level Goal
The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL encryption.

Helpful note: Getting “HEARTBEATING” and “Read R BLOCK”? Use -ign_eof and read the “CONNECTED COMMANDS” section in the manpage. Next to ‘R’ and ‘Q’, the ‘B’ command also works in this version of that command…

Create a connection using openssl
```sh
bandit15@bandit:~$ cat /etc/bandit_pass/bandit15 | openssl s_client -connect localhost:30001 -quiet
depth=0 CN = localhost
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = localhost
verify return:1
Correct!
cluFn7wTiGryunymYOu4RcffSxQluehd

```

# Level 16->17

https://overthewire.org/wargames/bandit/bandit17.html


## Login
```sh
ssh -l bandit16 bandit.labs.overthewire.org -p 2220
cluFn7wTiGryunymYOu4RcffSxQluehd
```

Level Goal
The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

Scan ports from 30000-40000
```
nmap -p 31000-32000 localhost

Starting Nmap 7.40 ( https://nmap.org ) at 2020-03-07 05:29 CET
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00024s latency).
Not shown: 996 closed ports
PORT      STATE SERVICE
31046/tcp open  unknown
31518/tcp open  unknown
31691/tcp open  unknown
31790/tcp open  unknown
31960/tcp open  unknown
```

Let's send it to 30001
```sh
cat /etc/bandit_pass/bandit16 | nc localhost 31046

function pass_to_port {
  port=$1
  cat /etc/bandit_pass/bandit16 | nc localhost "${port}"
}
pass_to_port 31046 # echo back the same
pass_to_port 31518 # nothing
pass_to_port 31691 # echo back the same
pass_to_port 31790 # nothing..
pass_to_port 31960 # echo back the same
```

Nothing.... let's check with openssl

```sh
function connect_via_openssl {
    port=$1
    cat /etc/bandit_pass/bandit16 | openssl s_client -connect localhost:"${port}" -quiet
}

connect_via_openssl 31518
connect_via_openssl 31790
```

Ha!

```sh
bandit16@bandit:~$ connect_via_openssl 31790
depth=0 CN = localhost
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = localhost
verify return:1
Correct!
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----
```

save this as ~/pems/bandit17.pem

and `chmod 400 ~/pems/bandit17.pem`



# Level 17->18

https://overthewire.org/wargames/bandit/bandit18.html


## Login
```sh
ssh -l bandit17 bandit.labs.overthewire.org -p 2220 -i ~/pems/bandit17.pem
```

## Level Goal
There are 2 files in the homedirectory: passwords.old and passwords.new.

The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new

NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19

```sh
bandit17@bandit:~$ diff passwords.old passwords.new 
42c42
< hlbSBPAWJmL6WFDb06gpTx1pPButblOA
---
> kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
```

# Level 18 → Level 19

https://overthewire.org/wargames/bandit/bandit19.html

## Level Goal
The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.

Commands you may need to solve this level

ssh, ls, cat

## Login
```sh
ssh -l bandit18 bandit.labs.overthewire.org -p 2220 cat .bashrc
kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
```


Someone created a automatic logout with .bashrc, we can get around it..

```sh
ssh -l bandit18 bandit.labs.overthewire.org -p 2220 cat readme
kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd


This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password: 
IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
```

# Level 19->20

## Login
```sh
ssh -l bandit19 bandit.labs.overthewire.org -p 2220
IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
```

## Level Goal
To gain access to the next level, you should use the setuid binary in the homedirectory.

Execute it without arguments to find out how to use it.

The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

## Helpful Reading Material
setuid on Wikipedia


Bandit19 doesn't own this.
```sh
bandit19@bandit:~$ ./bandit20-do 
Run a command as another user.
  Example: ./bandit20-do id
  
bandit19@bandit:~$ ls -al
total 28
drwxr-xr-x  2 root     root     4096 Oct 16  2018 .
drwxr-xr-x 41 root     root     4096 Oct 16  2018 ..
-rwsr-x---  1 bandit20 bandit19 7296 Oct 16  2018 bandit20-do
-rw-r--r--  1 root     root      220 May 15  2017 .bash_logout
-rw-r--r--  1 root     root     3526 May 15  2017 .bashrc
-rw-r--r--  1 root     root      675 May 15  2017 .profile

# It executes commands as bandit20
bandit19@bandit:~$ ./bandit20-do whoami
bandit20

bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20
GbKksEFF4yrVs6il55v6gwY5aVje5f0j
```

# Level 20->21

## Login
```sh
ssh -l bandit20 bandit.labs.overthewire.org -p 2220
GbKksEFF4yrVs6il55v6gwY5aVje5f0j
```

## Level Goal

There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

NOTE: Try connecting to your own network daemon to see if it works as you think
Commands you may need to solve this level

ssh, nc, cat, bash, screen, tmux, Unix ‘job control’ (bg, fg, jobs, &, CTRL-Z, …)

 This is about learning how to run background processes using CtrlZ, bg, jobs

```sh
bandit20@bandit:~$ ls
suconnect
bandit20@bandit:~$ nc -l 8080
^Z
[1]+  Stopped                 nc -l 8080
bandit20@bandit:~$ bg %1
[1]+ nc -l 8080 &
bandit20@bandit:~$ ./suconnect 8080
Could not connect
bandit20@bandit:~$ kill %1

bandit20@bandit:~$ nc -lvp 8080
listening on [any] 8080 ...
^Z[1]   Exit 1                  nc -l 8080

[2]+  Stopped                 nc -lvp 8080
bandit20@bandit:~$ jobs
[2]+  Stopped                 nc -lvp 8080
bandit20@bandit:~$ bg %2
[2]+ nc -lvp 8080 &
bandit20@bandit:~$ ./suconnect 8080
connect to [127.0.0.1] from localhost [127.0.0.1] 43354
^C
bandit20@bandit:~$ cat /etc/^C
[2]+  Done                    nc -lvp 8080
bandit20@bandit:~$ jobs
bandit20@bandit:~$ cat /etc/bandit_pass/bandit20 | nc -lvp 8080
listening on [any] 8080 ...
^Z
[1]+  Stopped                 cat /etc/bandit_pass/bandit20 | nc -lvp 8080
bandit20@bandit:~$ bg %1
[1]+ cat /etc/bandit_pass/bandit20 | nc -lvp 8080 &
bandit20@bandit:~$ nc "hey" localhost 8080
hey: forward host lookup failed: No address associated with name
bandit20@bandit:~$ echo "hey" | nc  localhost 8080
connect to [127.0.0.1] from localhost [127.0.0.1] 43364
GbKksEFF4yrVs6il55v6gwY5aVje5f0j
hey
^C
[1]+  Done                    cat /etc/bandit_pass/bandit20 | nc -lvp 8080
bandit20@bandit:~$ cat /etc/bandit_pass/bandit20 | nc -lvp 8080 &
[1] 16384
bandit20@bandit:~$ listening on [any] 8080 ...

bandit20@bandit:~$ jobs
[1]+  Running                 cat /etc/bandit_pass/bandit20 | nc -lvp 8080 &
bandit20@bandit:~$ ./suconnect 8080
connect to [127.0.0.1] from localhost [127.0.0.1] 43366
Read: GbKksEFF4yrVs6il55v6gwY5aVje5f0j
Password matches, sending next password
gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr
[1]+  Done                    cat /etc/bandit_pass/bandit20 | nc -lvp 8080
```


