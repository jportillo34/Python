Study guide: Basic Linux commands
=================================
Basic Linux commands are beneficial to developers when interacting with a Linux operating system through the command line interface. 
They are used when working with files and directories. Typically, they are easy to learn and apply, and provide developers with 
additional commands for more advanced situations. If needed, these commands are also easy to look up on your preferred search engine.

In this reading, you will review basic Linux commands with examples provided along the way.

Managing files and directories

Many applications configure themselves by reading files. They are designed to read and write files in specific directories. 
Because of this, developers need to understand how to move and rename files, change their permissions, and do simple operations 
on their contents. Here are some common commands:

mv is used to move one or more files to a different directory, rename a file, or both at the same time.

Note: Linux is case-sensitive, so mv can also be used to change the case of a filename.

mv myfile.txt dir1/ This command moves a file to the directory.

mv file1.txt file2.txt file3.txt dir1/ This command moves multiple files.


cp is used to copy one or more files. Some examples include:

cp file1.txt file2.txt 

cp file1.txt file2.txt file3.txt dir1/


chmod/chown/chgrp is used to make a file readable to everyone on the system before moving it to a public directory. A common example is:

chmod +r file.html && mv file.html /var/www/html/index.html 


Operating with the content of files

Every programmer will use files for something. Whether it’s for configuration, data, or input and output, programmers work with files 
and need to know how to operate with their contents.

cut is a command that extracts fields from a data file. Two examples are:

cut -f1 -d”,” addressbook.csv This command extracts the first field from a .csv file.

cut -c1-3,5-7,9-12 phones.txt This command extracts only the digits from a list of phone numbers.


sort is a command that sorts the contents of a file. Some examples include:

sort names.txt This command sorts inputs alphabetically.

sort -r names.txt This command sorts inputs in reverse alphabetical order, starting with the letter z. 

sort -n numbers.txt This command treats the inputs as numbers and then sorts them numerically.


Some examples that include combining multiple commands are:

ls -l | cut -w -f5,9 | sort -rn | head -10 This command displays the 10 largest files in the current directory.


cut -f1-2 -d”,” addressbook.csv | sort This command extracts the first and last names from a .csv file and sorts them.

Additional commands
Additional commands that programmers commonly use are:

id  is a command that prints information about the current user. This command is useful if you are getting a permissions denied error 
and think you should be granted access to a file.

$ id

uid=3000(tradel) gid=3000(tradel) groups=3000(tradel),0(root),100(users),545(builtin_users),999(docker)


free is a command that prints information about memory on the current system.

free -h This command prints in human-readable units instead of bytes.

Key takeaways

Basic Linux commands assist developers in different types of tasks related to managing files and directories and working with the 
content of each file. These commands allow developers to work more efficiently and effectively.




Redirections, Pipes, and Signals
================================
Managing streams
These are the redirectors that we can use to take control of the streams of our programs

command > file: redirects standard output, overwrites file

command >> file: redirects standard output, appends to file

command < file: redirects standard input from file

command 2> file: redirects standard error to file

command1 | command2: connects the output of command1 to the input of command2

Operating with processes
These are some commands that are useful to know in Linux when interacting with processes. Not all of them are explained in videos, 
so feel free to investigate them on your own.

ps: lists the processes executing in the current terminal for the current user

ps ax: lists all processes currently executing for all users  

ps e: shows the environment for the processes listed  

kill PID: sends the SIGTERM signal to the process identified by PID

fg: causes a job that was stopped or in the background to return to the foreground

bg: causes a job that was stopped to go to the background

jobs: lists the jobs currently running or stopped

top: shows the processes currently using the most CPU time (press "q" to quit)




SCRIPTS
=======
echo *.py

About this code
When we write star dot py [*.py], the shell turns it into a list containing all filenames that end with py in the current directory. 
We can also put the star at the end of an expression to get a list of all files that start with a certain prefix.

Code output: 

action_deprecation.py areas.py capitalize.py charfreq.py  check_deprecation.py health_checks.py hello.py mycheck.py seconds.py  
stdout_example.py streams.py test.py validations.py


echo c*

About this code
c* allows us to get all the files in the current directory that start with c.

Code output:

capitalize.py charfreq.py check_localhost.sh


echo *

About this code
The star with no prefix or suffix matches all the files in the current directory.

Code output:

(... all the files ...)


echo ?????.py

About this code
The question mark symbol can be used to match exactly one character, instead of any amount of characters.We can repeat it 
as many times as we need. In this example, we can get the Python files with five characters in their name by using five 
question marks together.

Code output:

areas.py hello.py





Review: Conditional execution in Bash
=====================================

cat check_localhost.sh

About this code
Here  we’ll start with the if  keyword, followed by the grep command. This is how we’ll check for success. At the end of the command, we have a semicolon [;], followed by the word then. After that comes the body of the conditional. 

Code output:

#!/bin/bash



if grep "127\.0\.0\.1" /etc/hosts; then
	echo "Everything ok"
else
	echo "ERROR! 127.0.0.1 is not in /etc/hosts"
fi

./check_localhost.sh

Code output:

127.0.0.1	localhost

Everything ok


if test -n "$PATH"; then echo "Your path is not empty"; fi

Code output:

Your path is not empty


if [ -n "$PATH" ]; then echo "Your path is not empty"; fi

Code output:

Your path is not empty





Review: While loops in Bash scripts
===================================

#!/bin/bash

n=1
while [ $n -le 5 ]; do
  echo "Iteration number $n"
  ((n+=1))
done


./while.sh

Code output:

Iteration number 1

Iteration number 2

Iteration number 3

Iteration number 4

Iteration number 5



cat while.sh

 Code output:


#!/usr/bin/env python

import random

value=random.randint(0, 3)

print("Returning: " + str(value))

sys.exit(value)


./random-exit.py
./random-exit.py
./random-exit.py

Code output:

Returning: 3

Returning: 2

Returning: 0



#!/bin/bash

n=0
command=$1
while ! $command && [ $n -le 5 ]; do
        sleep $n
        ((n+=1))
        echo "Retry #$n"
done;

./retry.sh ./random

Code output:

Returning: 3

Retry #1

Returning: 3

Retry #2

Returning: 1

Retry #3

Returning: 3

Retry #4

Returning: 0






Review: For loops in bash scripts
=================================

cat fruits.sh

About this code
Here we're iterating over three different elements that have the names of the fruits.

Code output:

#!/bin/bash

for fruit in peach orange pear; do
        echo "I like $fruit!"
done




./fruits.sh

Code output:

I like peach!

I like orange!

I like pear!



cd old_website/
/old_website$ ls -l


Code output:

total 0

-rw-r--r-- 1 user user 0 May 24 10:19 about.HTM
-rw-r--r-- 1 user user 0 May 24 10:20 contact.HTM
-rw-r--r-- 1 user user 0 May 24 10:20 footer.HTM
-rw-r--r-- 1 user user 0 May 24 10:20 header.HTM
-rw-r--r-- 1 user user 0 May 24 10:19 index.HTM





/old_website$ basename index.HTM .HTM

About this code
This command takes a filename and an extension, and then returns the name without the extension.



#!/bin/bash

for file in *.HTM; do
        name=$(basename "$file" .HTM)
        mv "$file" "$name.html" 
done


#!/bin/bash

for file in *.HTM; do
        name=$(basename "$file" .HTM)
        echo mv "$file" "$name.html" 
done

About this code
The script iterates through all files with the ".HTM" extension in the current directory. For each file, it extracts 
the filename without the extension and generates the new filename with the ".html" extension. Finally, it prints the 
mv command that would rename the original file to the new filename.

Note: This script only prints the mv commands. To actually rename the files, you need to execute the script by running 
chmod +x script.sh && ./script.sh where script.sh is the name of the script file.



/old_website$ chmod +x rename.sh
/old_website$ ./rename.sh


About this code
Here the script gets saved as rename.sh

Code output:

mv about.HTM about.html

mv contact.HTM contact.html

mv footer.HTM footer.html

mv header.HTM header.html

mv index.HTM index.html



/old_website$ ./rename.sh 
/old_website$
/old_website$ ls -l

About this code
These commands won’t print anything. That's expected because these commands don't print anything when they succeed.



ls -l

About this code
ls -l is a command in Linux and Unix systems used to list the contents of a directory in a long format. This format 
provides detailed information about each file

Code output:

total 4

-rw-r--r-- 1 user user  0 May 24 10:19 about.html
-rw-r--r-- 1 user user  0 May 24 10:20 contact.html
-rw-r--r-- 1 user user  0 May 24 10:20 footer.html
-rw-r--r-- 1 user user  0 May 24 10:20 header.html
-rw-r--r-- 1 user user  0 May 24 10:19 index.html
-rwxr-xr-x 1 user user 90 May 24 10:40 rename.sh






Review: Advanced Command Interaction
====================================

tail /var/log/syslog

Code output:

May 24 10:17:01 ubuntu.local CRON[257236]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)

May 24 10:18:41 ubuntu.local rsyslogd: -- MARK --

May 24 10:25:19 ubuntu.local systemd[1]: Reloading.



tail /var/log/syslog | cut -d' ' -f5-

Code output:

CRON[257236]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)

rsyslogd: -- MARK --

systemd[1]: Reloading.



cut -d' ' -f5- /var/log/syslog | sort | uniq -c | sort -nr | head

Code output:

     41 systemd[1]: Starting Network Manager Script Dispatcher Service...

     41 systemd[1]: Started Network Manager Script Dispatcher Service.

     41 systemd[1]: NetworkManager-dispatcher.service: Succeeded.

     41 nm-dispatcher: req:1 'dhcp4-change' [ens3]: start running ordered scripts...

     41 nm-dispatcher: req:1 'dhcp4-change' [ens3]: new request (1 scripts)

     41 dhclient[757]: DHCPREQUEST for 192.168.122.103 on ens3 to 192.168.122.1 port 67 (xid=0x3a5ff7ed)

     41 dhclient[757]: DHCPACK of 192.168.122.103 from 192.168.122.1 (xid=0xedf75f3a)

     41 dbus-daemon[592]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'

     41 dbus-daemon[592]: [system] Activating via systemd: service name='org.freedesktop.nm_dispatcher' unit='dbus-org.freedesktop.nm-dispatcher.service' requested by ':1.15' (uid=0 pid=599 comm="/usr/sbin/NetworkManager --no-daemon " label="unconfined")

      9 systemd[1]: Started Run anacron jobs.



#!/bin/bash

for logfile in /var/log/*log; do
    echo "Processing: $logfile"
    cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done

About this code
This script is written in the Bash scripting language and designed to analyze log files. It analyzes each log file in the 
/var/log directory and displays the top 5 most frequently occurring messages along with their counts.




./toploglines.sh

Code output:

(...)

Processing: /var/log/user.log

     23 system-updater[199481]: DEBUG Command exited with status: 0

     19 system-updater[46682]: DEBUG Command exited with status: 0

     16 system-updater[175060]: DEBUG Command exited with status: 0

     11 /usr/bin/lock: called by /bin/bash for . uid 0, euid 0.

     11 network-manager-dhclient-hooks: Dispatching run of '/etc/dhcp/dhclient-exit-hooks.d/hostname' ...

Processing: /var/log/Xorg.0.log

     87 Printing DDC gathered Modelines:

     87 Modeline "1920x1080"x0.0  141.00  1920 1936 1952 2104  1080 1083 1097 1116 -hsync -vsync (67.0 kHz eP)

     87 EDID vendor "AUO", prod id 5949

     78 vendor "AUO", prod id 5949

     78 DDC gathered Modelines:






Review: Choosing between Bash and Python
========================================

for i in $(cat story.txt); do B=`echo -n "${i:0:1}" | tr "[:lower:]" "[:upper:]"`; echo -n "${B}${i:1} "; done; echo -e "\n"

About this code
This code snippet is written in the Bash scripting language and designed to capitalize the first letter of each word in a text file. 
This script iterates through each line in the story.txt file and capitalizes the first letter of each word. It then prints 
the modified text to the output.



cat capitalize_words.py

Code output:

#!/usr/bin/env python3

import sys

for line in sys.stdin:

    words = line.strip().split()

    print(" ".join([word.capitalize() for word in words]))

About this code
This script takes input from a text file  or from another command, removes the whitespace, splits it into separate words, 
capitalizes the first letter of each word in every line, and prints the modified text to the standard output.

cat story.txt | ./capitalize_words.py

Code output:

Once Upon A Time There Was An Egg Of A Programming Language Called Python





Glossary terms from course 2, module 6
======================================

Bash script: A script that contains multiple commands

Cut: A command that can split and take only bits of each line using spaces

Globs: Characters that create list of files, like the star and question mark 

Pipes: A process of connecting the output of one program to the input of another

Piping: A process of connecting multiple scripts, commands, or other programs together into a data processing pipeline

Redirection: A process of sending a stream to a different destination

Signals: Tokens delivered to running processes to indicate a desired action





IT skills in action reading
===========================
Congratulations! You have gained so much knowledge about using Python to interact with your operating system. 
There are many technical pieces that are included while using regexes in your code, but how would you apply the skills 
you learned in a professional setting?

In this reading, you will review an example of how regular expressions are used in the real world.

Disclaimer: The following scenario is based on a fictitious company called LogicLink Innovations.

Time is ticking
Dakota is a fairly new programmer with his company. He just earned a spot on the project for LogicLink Innovations. 
This is one of the biggest and most credible companies in the industry, so Dakota knows he has to excel on this project 
to help make a name for himself. LogicLink Innovations manages customer data and has hundreds of customer phone numbers 
in its database. The phone numbers are in inconsistent formats. Some are written with dashes, some in parentheses with spaces, 
and some are just digits. Dakota sees this:

123-456-7890

(123) 456-7890

1234567890


Dakota is assigned to take the dataset containing phone numbers and organize the formatting so they are all consistent. 
His manager tells him they need it by the end of the week! There is no way Dakota can work through and edit hundreds of phone numbers. 
There has to be another way.

Search and replace
Dakota remembers reading about how other programmers use regular expressions to make their coding life easier. He knows there 
has to be one that can help him with his dilemma. This can’t be the first time a programmer needs to standardize numbers! 
He decides to craft a regular expression that captures three groups of digits, each of which might be surrounded by non-digit characters.


Using a regex tool and the sample data from above, he eventually comes up with a regex that matches all three samples:

^\D*(\d{3})\D*(\d{3})\D*(\d{4})$


Let’s break down this line of code, piece by piece:

^\D*

This part of the code matches zero or more non-digit characters at the beginning of the string.

(\d{3})

This part of the code captures exactly three digits, which represent the area code.

\D*

This part of the code matches zero or more non-digit characters between the area code and exchange.

(\d{3} ) 

This part of the code captures the three-digit exchange.

\D*       

This part of the code matches zero or more non-digit characters between the exchange and line.

(\d{4})$

This part of the code captures exactly four digits at the end of the string.

    

Now he has three capture groups: area code, exchange, and number. He then substitutes those groups into a new string using backreferences:

(\1) \2-\3


This puts all of the phone numbers into a uniform format.


This regular expression helps Dakota by searching for phone numbers in different formats and replacing them to match the format that 
Dakota’s manager needs: (123) 456-7890. Dakota begins to code.


He writes up a simple Python script to read the dataset from a file and output the corrected phone numbers using his regular expressions:

import re


with open("data/phones.csv", "r") as phones:

 for phone in phones:

   new_phone = re.sub(r"^\D*(\d{3})\D*(\d{3})\D*(\d{4})$", r"(\1) \2-\3", phone)

   print(new_phone)

(123) 456-7890

(123) 456-7890

(123) 456-7890


Success! Dakota gets the project done in a single day and is now the office hero. 

A happy client
By using a regular expression, Dakota expedited the process of collecting, organizing, and providing LogicLink Innovation 
with its customers’ phone numbers, all in the same format. 

