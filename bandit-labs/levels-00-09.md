# Level 00->01
* The goal of this is to introduce how to login to a server using ssh
* password is `bandit0`
* Cat a file called readme, use this for the next level

```sh
ssh -l bandit0 bandit.labs.overthewire.org -p 2220
```

Once logged in, you should see this in the terminal:

```sh
       
Welcome to OverTheWire!

If you find any problems, please report them to Steven or morla on
irc.overthewire.org.

--[ Playing the games ]--

  This machine might hold several wargames. 
  If you are playing "somegame", then:

    * USERNAMES are somegame0, somegame1, ...
    * Most LEVELS are stored in /somegame/.
    * PASSWORDS for each level are stored in /etc/somegame_pass/.

  Write-access to homedirectories is disabled. It is advised to create a
  working directory with a hard-to-guess name in /tmp/.  You can use the
  command "mktemp -d" in order to generate a random and hard to guess
  directory in /tmp/.  Read-access to both /tmp/ and /proc/ is disabled
  so that users can not snoop on eachother. Files and directories with 
  easily guessable or short names will be periodically deleted!
	
  Please play nice:
      
    * don't leave orphan processes running
    * don't leave exploit-files laying around
    * don't annoy other players
    * don't post passwords or spoilers
    * again, DONT POST SPOILERS! 
      This includes writeups of your solution on your blog or website!

--[ Tips ]--

  This machine has a 64bit processor and many security-features enabled
  by default, although ASLR has been switched off.  The following
  compiler flags might be interesting:

    -m32                    compile for 32bit
    -fno-stack-protector    disable ProPolice
    -Wl,-z,norelro          disable relro 

  In addition, the execstack tool can be used to flag the stack as
  executable on ELF binaries.

  Finally, network-access is limited for most levels by a local
  firewall.

--[ Tools ]--

 For your convenience we have installed a few usefull tools which you can find
 in the following locations:

    * pwndbg (https://github.com/pwndbg/pwndbg) in /usr/local/pwndbg/
    * peda (https://github.com/longld/peda.git) in /usr/local/peda/
    * gdbinit (https://github.com/gdbinit/Gdbinit) in /usr/local/gdbinit/
    * pwntools (https://github.com/Gallopsled/pwntools)
    * radare2 (http://www.radare.org/)
    * checksec.sh (http://www.trapkit.de/tools/checksec.html) in /usr/local/bin/checksec.sh

--[ More information ]--

  For more information regarding individual wargames, visit
  http://www.overthewire.org/wargames/

  For support, questions or comments, contact us through IRC on
  irc.overthewire.org #wargames.

  Enjoy your stay!

bandit0@bandit:~$ 
bandit0@bandit:~$ cat readme
boJ9jbbUNNfktd78OOpsqOltutMc3MY1
```

# Level 01->02
https://overthewire.org/wargames/bandit/bandit2.html

```
ssh -l bandit1 bandit.labs.overthewire.org -p 2220

password:
boJ9jbbUNNfktd78OOpsqOltutMc3MY1
```

* The password for the next level is in a file called `-`
* this is tricky because you can't just do a `cat -`
* I used `vi .` to edit files in a directory to get the next level
* Or use `cat ./-`

```
found:
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```

# Level 02->03
https://overthewire.org/wargames/bandit/bandit3.html

## Login
```sh
ssh -l bandit2 bandit.labs.overthewire.org -p 2220

password:
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```

* There are spaces in this filename.
* So escape the spaces with '\' or use vi

```
found:
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```

# Level 03-04
https://overthewire.org/wargames/bandit/bandit4.html


## Login
```sh
ssh -l bandit3 bandit.labs.overthewire.org -p 2220

password:
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```

* It is a hidden file in `inhere/`
* Solution: 

```
ls -al ./inehere/
cat ./inhere/.hidden

password:
pIwrPrtPN36QITSp3EQaw936yaFoFgAB
```

# Level 04-05
https://overthewire.org/wargames/bandit/bandit5.html

## Login
```sh
ssh -l bandit4 bandit.labs.overthewire.org -p 2220

password:
pIwrPrtPN36QITSp3EQaw936yaFoFgAB
```


The password for the next level is stored in the only human-readable file in the inhere directory. 

Tip: if your terminal is messed up, try the “reset” command.

```sh
bandit4@bandit:~/inhere$ cat ./*
����������~%	C[�걱>��| ����U"7�w���H��ê�Q����(���#����T�v��(�ִ�����A*�
2J�Ş؇_�y7��.A��u��#���w$N?c�-��Db3��=���=<�W�����ht�Z��!��{�U
                                                                     �+��pm���;��:D��^��@�gl�Q���@�%@���ZP*E��1�V���̫*����koReBOKuIDDepwhWk7jZC0RTdopnAYKh
FPn�
      '�U���M��/u
                 XS

```
