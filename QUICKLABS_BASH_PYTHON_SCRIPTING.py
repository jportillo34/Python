Edit Files using Substrings

ls -l ~/data/jane_* | cut -d' ' -f9 | cut -d'/' -f5





student@dba4f9c56f53:~/scripts$ cat oldFiles.txt
/home/student/data/jane_contact_07292018.csv
/home/student/data/jane_profile_07272018.doc



drwxrwxrwx 2 student student 4096 Jul 22 18:45 .
drwxr-xr-x 1 student student 4096 Jul 22 17:56 ..
-rwxr-xr-x 1 student student  290 Jul 22 18:45 changeJane.py
-rw-r--r-- 1 student student   90 Jul 22 18:08 files
-rwxr-xr-x 1 student student  225 Jul 22 18:30 findJane.sh
-rw-r--r-- 1 student student   90 Jul 22 18:30 oldFiles.txt
student@dba4f9c56f53:~/scripts$ 
student@dba4f9c56f53:~/scripts$ cat findJane.sh
#!/bin/bash

# Create the file.
> oldFiles.txt

files=`ls -l ~/data/jane_* | cut -d' ' -f9 | cut -d'/' -f5`

for file in $files
do
   if test -e ~/data/$file; then
        echo "/home/student/data/$file" >> oldFiles.txt
   fi
done


student@dba4f9c56f53:~/scripts$ cat changeJane.py
#!/usr/bin/env python3

import sys
import subprocess

with open(sys.argv[1], "r") as file:
        lines = file.readlines()
        for line in lines:
                old_name = line.strip()
                new_name = old_name.replace("jane", "jdoe")
                #print(new_name)
                subprocess.run(["mv", old_name, new_name])
        file.close()



student@dba4f9c56f53:~/scripts$ ls ~/data
janez_profile_11042019.doc  kwood_profile_04022017.doc
jdoe_contact_07292018.csv   list.txt
jdoe_profile_07272018.doc   pchow_pic_05162019.jpg
kwood_pic_04032017.jpg