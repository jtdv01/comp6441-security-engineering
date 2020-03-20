# Level 21->22

https://overthewire.org/wargames/bandit/bandit22.html

## Login
```sh
ssh -l bandit21 bandit.labs.overthewire.org -p 2220
gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr
```

## Level Goal

A program is running automatically at regular intervals from cron, the time-based job scheduler.

Look in /etc/cron.d/ for the configuration and see what command is being executed.
Commands you may need to solve this level

cron, crontab, crontab(5) (use “man 5 crontab” to access this)

```sh
bandit21@bandit:~$ cat /etc/cron.d/cronjob_bandit22
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null

bandit21@bandit:~$ cat /usr/bin/cronjob_bandit22.sh
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv

bandit21@bandit:~$ file /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
/tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv: ASCII text

bandit21@bandit:~$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
```

# Level 22->23

https://overthewire.org/wargames/bandit/bandit23.html

## Login
```sh
ssh -l bandit22 bandit.labs.overthewire.org -p 2220
Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
```

## Level Goal

A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. If you are having problems understanding what it does, try executing it to see the debug information it prints.
Commands you may need to solve this level

cron, crontab, crontab(5) (use “man 5 crontab” to access this)


```sh
bandit22@bandit:~$ ls /etc/cron.d
atop  cronjob_bandit22  cronjob_bandit23  cronjob_bandit24
bandit22@bandit:~$ cat /etc/cron.d/cronjob_bandit23
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
bandit22@bandit:~$ cat /usr/bin/cronjob_bandit23.sh
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget

```

```
bandit22@bandit:~$ myname=bandit23
bandit22@bandit:~$ mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)
bandit22@bandit:~$ echo "${mytarget}"
8ca319486bfbbc3663ea0fbe813
bandit22@bandit:~$ cat /tmp/$mytarget
jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
```

# Level 23->24

https://overthewire.org/wargames/bandit/bandit24.html

## Login
```sh
ssh -l bandit23 bandit.labs.overthewire.org -p 2220
jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
```

A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!

NOTE 2: Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…


```sh
bandit23@bandit:~$ cat /usr/bin/cronjob_bandit24.sh
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
	echo "Handling $i"
	timeout -s 9 60 ./$i
	rm -f ./$i
    fi
done


bandit23@bandit:~$ cat /tmp/copy.sh
cat /etc/bandit_pass/bandit24 > /tmp/out.txt
bandit23@bandit:~$ ls -al /tmp/copy.sh
-rwxrwxrwx 1 bandit23 root 45 Mar 20 12:14 /tmp/copy.sh
bandit23@bandit:~$ ls /tmp/out_dir
bandit23@bandit:~$ cat /etc/cron.d/cronjob_bandit24 
@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
bandit23@bandit:~$ ls -al /tmp/copy.sh
-rwxrwxrwx 1 bandit23 root 45 Mar 20 12:14 /tmp/copy.sh
bandit23@bandit:~$ ls /tmp/out_dir
bandit23@bandit:~$ mkdir /tmp/out^C


```

UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
