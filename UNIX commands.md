>## adduser
To install adduser tool use the following commands as per your Linux distribution.
- `$sudo apt-get install adduser`
    1. To add a new user(Only Root can add user)
        - `sudo adduser username`
    ![adduser info](../../Pictures/adduser comand.png)
    2. To add a user with a different shell.
       - `sudo adduser username --shell /bin/sh`
       ![add user diff shell](https://media.geeksforgeeks.org/wp-content/uploads/20200614204812/2-To-add-a-user-with-a-different-shell..png)
    3. To add a new user with a different configuration file.
      - `adduser username --conf custom_config.conf`
      ![add user diff conf](https://media.geeksforgeeks.org/wp-content/uploads/20200614204839/3-To-add-a-new-user-with-a-different-configuration-file..png)
    4. To add a user with different home directory.
      - `sudo adduser username --home /home/manav/`
      ![add user diff home dir](https://media.geeksforgeeks.org/wp-content/uploads/20200614204859/4-To-add-a-user-with-different-home-directory.png)
    5. To get the version of the adduser command.
      - `adduser --version`
      ![add user version](https://media.geeksforgeeks.org/wp-content/uploads/20200614204918/5-To-gee-the-version-of-the-adduser-command..png)
    6.  To display the help section of the adduser command
      - `adduser -h`
        ![add user help](https://media.geeksforgeeks.org/wp-content/uploads/20200614204935/6-To-display-the-help-section-of-the-adduser-command.png)
>## addgroup
To install addgroup tool use the following commands as per your Linux distribution.
- `$sudo apt-get install addgroup`
1. To add a new group
  `sudo addgroup groupname`
     - ![addgroup info](../../Pictures/addgroup.png)
2. To add a new group with specified group id
`sudo addgroup groupname --gid 12345`
![addgroup gid](https://media.geeksforgeeks.org/wp-content/uploads/20200614222223/2-To-add-a-new-group-with-specified-group-id.png)
This command will add a new group with the specified group id.
3. To create a group with a specific shell
`sudo addgroup groupname --shell /bin/sh`
![addgroup gid](https://media.geeksforgeeks.org/wp-content/uploads/20200614222249/3-To-create-a-group-with-a-specific-shell.png)
This command will allocate the /bin/sh shell to the newly create group.
4. To enter verbose mode
`sudo addgroup groupname --debug`
This command will execute the command in the verbose mode that means it will print all details of the tasks it is executing.
5. To display help related to addgroup command.
`addgroup --help`
This command will display the help section of the addgroup command.
6. To display version
`addgroup --version`
This command will display the version details of the addgroup command.
>## cat
1.  To view a single file 
   - ` cat file_name.extension`
   Output
   ![cat info](../../Pictures/view cat.png)
2. To view multiple files 
   - `cat file1 file2`
  ![cat info](../../Pictures/view mulfile cat.png)
3. To view contents of a file preceding with line numbers. 
   - `$cat -n filename` 
   - ![cat info](../../Pictures/view file with line nos cat.png)
4. Create a file 
- ` cat > newfile`
![cat info](../../Pictures/createnewfile cat.png)

5.  Copy the contents of one file to another file.
`$cat [filename-whose-contents-is-to-be-copied] > [destination-filename]`
![copy command](../../Pictures/cat copy.png)
6. Cat command can suppress repeated empty lines in output 
`cat -s oldfile.txt`
![removes empty lines command](../../Pictures/removeMTlineCat.png)
7.  Cat command can append the contents of one file to the end of another file. 
`cat file1 >> file2`
![appends contents](../../Pictures/append cat.png)
8. Cat command can display content in reverse order using tac command. 
`tac filename`
![reverse me print karega](../../Pictures/reversecat(tac).png)
9. Cat command can highlight the end of line. 
`cat -E "filename"`
![highlighting the EOL](../../Pictures/highlightEOLcat.png)
10. If you want to use the -v, -E and -T option together, then instead of writing -vET in the command, you can just use the -A command line option. 
`cat -A "filename"`
![instead of -VET](../../Pictures/instead of-VET or A cat.png)
11. Cat command to open dashed files. 
`$cat -- "-dashfile"`
Will display the content of -dashfile
12.  Cat command if the file has a lot of content and can’t fit in the terminal. 
`$cat "filename" | more`
Will show that much content, which could fit in terminal and will ask to show more.
#### Works like normal Cat command for viewing more content

13.  Cat command to merge the contents of multiple files. 
`$cat "filename1" "filename2" "filename3" > "merged_filename"`
![merging file using cat](../../Pictures/mergeusing Cat.png)
* Will merge the contents of file in respective order and will insert that content in "merged_filename".
14. Cat command to display the content of all text files in the folder. 
`$cat *.txt`
![ek specific extension ka sab fike ka content](../../Pictures/all(specExt)contentCat.png)
15. Cat command to write in an already existing file. 
`$cat >> geeks.txt
The newly added text.`
![isi file me content append karega](../../Pictures/append in ExistingCat.png)
>## cd
- To move inside a subdirectory : to move inside a subdirectory in linux we use
`$ cd [directory_name]` 
- command is used to change directory to the root directory, The root directory is the first directory in your filesystem hierarchy.
`cd /`
- `cd dir_1/dir_2/dir_3`: This command is used to move inside a directory from a directory
- `cd ~` or `cd`: this command is used to change directory to the home directory.
- `cd ..`:this command is used to move to the parent directory of current directory, or the directory one level up from the current directory. “..” represents parent directory. 
- `cd “dir name”` or `cd 'dir name'` or `cd dir\ name` : This command is used to navigate to a directory with white spaces.Instead of using double quotes we can use single quotes then also this command will work.

![ouput of all cd commands](../../Pictures/cdcommand.png)
>## chmod
- Change Mode - Change the access mode of a file
- 
Syntax :
`chmod [reference][operator][mode] file...`

| Reference                   | Class  |     Description|
|-----------------------------|--------|----------------|
| u                           | owner  |      file's owner|
| g                           | group  |      users who are members of the file's group|
| o                           | others |users who are neither the file's owner nor members of the file's group|            
| a                           | all    |All three of the above, same as ugo|

> "+" adding modes to classes<br>
> "-" removes modes from classes<br>
> "="  jo diya hoga wahi uss class ka mode ho jayega<br>+

|symbol |action|
|-----|--------|
|r|       Permission to read the file.|
|w|       Permission to write (or delete) the file.|
|x|       Permission to execute the file, or, in the case of a directory, search it.|
BEFORE: -rw-rw-r--  mik  mik  assgn1_client.c

COMMAND: chmod u=r assgn1_client.c

AFTER: -r--rw-r--  mik   mik   assgn1_client.c
>## chown
Syntax:  

chown [OPTION]… [OWNER][:[GROUP]] FILE…
chown [OPTION]… –reference=RFILE FILE…

`chown owner_name file_name`

![chown ka example](https://media.geeksforgeeks.org/wp-content/uploads/chown1.png)
`sudo` for changing owner to root
Refer [GFG chown](https://www.geeksforgeeks.org/chown-command-in-linux-with-examples/)
>## clear
Syntax:
`$clear`
Ctrl + L - Clears the terminal
Refer [GFG clear link](https://www.geeksforgeeks.org/clear-command-in-linux-with-examples/)
>## cp
* 'cp' stands for **copy**
* Syntax:

- `cp [OPTION] Source Destination`<br>
- Eg `cp Src_file Dest_file`
    - Src file se dest file me copy hoga, agar koi file nhi he, to create karke copy kardega
    - agar do directories k naam diye gaye hein, to src dir ke sare files dest dir me chalijayengi
- `cp [OPTION] Source Directory`<br>
- `cp [OPTION] Source-1 Source-2 Source-3 Source-n Directory`<br>

- `First and second syntax is used to copy Source file to Destination file or Directory.`
- `Third syntax is used to copy multiple Sources(files) to Directory.`

![cp command](../../Pictures/cp command.png)
Refer [GFG cp link](https://www.geeksforgeeks.org/cp-command-linux-examples/)
>## cut
It can be used to cut parts of a line by byte position, character and field.
Syntax:`cut OPTION... [FILE]...`

![cut command](../../Pictures/cut-bcmd.png)
-   We cam give list with ranges too (1-4, 6-9 etc)
* -b
* -c
* -f
* -d
* -complement
* -output-delimiter
* -version
* refer [GFG cut link](https://www.geeksforgeeks.org/cut-command-linux-examples/)
* refer [youtube link](https://youtu.be/eHGCxEVlHd0?list=PLqM7alHXFySFc4KtwEZTANgmyJm3NqS_L)

>## date
_**date**_ command is used to display the system date and time
`cal [ [month] year]` [arguments] are optional.
Eg - ` cal 03 1998`
![cal command](../../Pictures/calmoncmd.png)
Syntax:
* `date [OPTION]... [+FORMAT]`
* `date [-u|--utc|--universal] [MMDDhhmm[[CC]YY][.ss]]`
* `date +%m` - displays month number
* `+%h` - month name
* `"+%m +%h"` - month no and name
* ![date command](../../Pictures/datecmd.png)
* refer [GFG cut link](https://www.geeksforgeeks.org/date-command-linux-examples/)
* refer [youtube link](https://youtu.be/g6cPFj9ptdc)
>## deluser 

* ![userdel command](../../Pictures/userdelcmd.png)
* refer [GFG deluser  link](https://www.geeksforgeeks.org/date-command-linux-examples/)


>## delgroup
* ![userdel command](https://media.geeksforgeeks.org/wp-content/uploads/groupdel-1.png)
* refer [GFG delgroup link](https://www.geeksforgeeks.org/groupdel-command-in-linux-with-examples/)


>## echo
* ![echo command](https://media.geeksforgeeks.org/wp-content/uploads/echo1.png)
* -e 
    * `\b` removes all blank spaces
  Syntax`echo [option] [string]`

* refer [youtube link](https://youtu.be/g6cPFj9ptdc)
* refer [GFG echo  link](https://www.geeksforgeeks.org/echo-command-in-linux-with-examples/)

>## find
- find files and directories and perform subsequent operations on them.
  `$ find [where to start searching from] [expression determines what to find] [-options] [what to find]`
* ![find command](../../Pictures/ss find cmd.png)
  $ find ./GFG -name sample.txt 

* ![find command](https://media.geeksforgeeks.org/wp-content/uploads/1-60.png)
* `$ find ./GFG -name *.txt `
  It will give all files which have ‘.txt’ at the end. 
* refer [youtube link](https://youtu.be/oPdFGUrq-XQ)
* refer [GFG find  link](https://www.geeksforgeeks.org/find-command-in-linux-with-examples/)
>## grep
- grep filter __searches__ a file for a **particular pattern** of *characters*, and __displays__ all lines that contain that **pattern**.<br>
  `$grep -c "unix" geekfile.txt`<br>
  `Output:`<br>
  `2`
* refer [youtube link](https://www.youtube.com/watch?v=EQLFr8uC44k)
* refer [GFG grep  link](https://www.geeksforgeeks.org/grep-command-in-unixlinux/)

>## head
> print the top N number of data of the given input.

![find command](https://media.geeksforgeeks.org/wp-content/uploads/head.png)

* Syntax - `head [OPTION]... [FILE]...`

  `$ head -n 5 state.txt`<br>
  **o/p-<br>**
  Andhra Pradesh<br>
  Arunachal Pradesh<br>
  Assam<br>
  Bihar<br>
  Chhattisgarh<br>
* refer [youtube link](https://www.youtube.com/watch?v=ZZACz-filWU)
* refer [GFG head  link](https://www.geeksforgeeks.org/date-command-linux-examples/)
>## history
  **history** command is used to view the previously executed command.
  `$ history`<br>
  ![history command](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-from-2018-12-14-07-12-12.png)

* refer [youtube link](https://www.youtube.com/watch?v=o6hy4Q-YJLE)
* refer [GFG history  link](https://www.geeksforgeeks.org/history-command-in-linux-with-examples/)
>## ls

* The **ls** is the __list__ command in Linux. It will show --**the full list or content of your directory.**__ Just type ls and press the enter key. The whole content will be shown.
![ls command](https://static.javatpoint.com/linux/images/linux-directories-ls-command1.png)

![ls manual command](../../Pictures/lscmd.png)
* refer [youtube link](https://www.youtube.com/watch?v=C1btVko0CVE)
* refer [GFG ls  link](https://www.javatpoint.com/linux-ls)
>## man
**User Manual** of any command<br>
Syntax :`$man [OPTION]... [COMMAND NAME]...`
__**Example:-**__<br>
`$ man printf`<br>

![man command](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-from-2018-12-11-20-58-48.png)
* refer [youtube link](https://youtu.be/USMVhdydb4Y?list=PLqM7alHXFySFc4KtwEZTANgmyJm3NqS_L)
* refer [GFG man  link](https://www.geeksforgeeks.org/man-command-in-linux-with-examples/)
>## mkdir
Syntax :`mkdir [options...] [directories ...]`

__**Example:-**__<br>
`mkdir -p first/second/third`<br>
![mkdir command](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-from-2018-12-11-17-59-58.png)
* refer [youtube link](https://www.youtube.com/watch?v=Ep5KNBfo33s)
* refer [GFG mkdir  link](https://www.geeksforgeeks.org/mkdir-command-in-linux-with-examples/)
>## mv
Syntax :`mv [Option] source destination`

__**Example:-**__<br>
`mv cpintro.md vvi/jmi`<br>
![mv command](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-from-2018-12-11-17-59-58.png)

* refer [youtube link](https://www.youtube.com/watch?v=gBScrrFHMT4)
* refer [GFG mv  link](https://www.geeksforgeeks.org/mv-command-linux-examples/)
>## passwd
* **shutdown** command in Linux is used to __change the user account passwords.__<br>

Syntax :` passwd [options] [username] `

__**Example:-**__<br>
`passwd `<br>
![passwd command](https://media.geeksforgeeks.org/wp-content/uploads/passwd1-1.png)

* refer [youtube link](https://www.youtube.com/watch?v=5cZNa3qW9hY)
* refer [GFG passwd  link](https://www.geeksforgeeks.org/passwd-command-in-linux-with-examples/)
>## shutdown
* **passwd** command in Linux is used to __shutdown the system in a safe way.__<br>

Syntax :`shutdown [OPTIONS] [TIME] [MESSAGE]`

__**Example:-**__<br>
`sudo shutdown 05:00 `<br>
This will shotdown the machine at 5 in the morning. <br>

* refer [youtube link]()
* refer [GFG shutdown  link](https://www.geeksforgeeks.org/shutdown-command-in-linux-with-examples/)
>## ssh

* **scp (secure copy) ** protocol in Linux is used to __securely connect to a remote server/system.__<br>

Syntax :`ssh user_name@host(IP/Domain_name)`
ssh command consists of 3 different parts:

* ssh command instructs the system to establish an encrypted secure connection with the host machine.
* user_name represents the account that is being accessed on the host.
* host refers to the machine which can be a computer or a router that is being accessed. It can be an IP address (e.g. 192.168.1.24) or domain name(e.g. www.domainname.com).
__**Example:-**__<br>
`ssh-keygen `<br>
![ssh key rsa command](https://media.geeksforgeeks.org/wp-content/uploads/ssh_keygen.jpg)
* refer [youtube link](https://www.youtube.com/watch?v=v45p_kJV9i4)
* refer [GFG ssh  link](https://www.geeksforgeeks.org/ssh-command-in-linux-with-examples/)
>## scp
* **Secure Shell** command in Linux is used to __copy file(s) between servers in a secure way.__<br>
Syntax :`mv [Option] source destination`

__**Example:-**__<br>
`scp [-346BCpqrTv] [-c cipher] [-F ssh_config] [-i identity_file] [-l limit] [-o ssh_option] [-P port] [-S program] [[user@]host1:]file1 … [[user@]host2:]file2`<br>
![scp command](../../Pictures/scp cmd options.png)
* refer [youtube link](https://www.youtube.com/watch?v=fmMg6cyww14)
* refer [GFG scp  link](https://www.geeksforgeeks.org/scp-command-in-linux-with-examples/)
>## rsync
**rsync or remote synchronization** is a software utility for Unix-Like systems __**that efficiently sync files and directories between two hosts or machines.**__ One of them being the source or the local-host from which the files will be synced, the other one being the remote-host, on which synchronization will take place. There are basically two ways in which rsync can copy/sync data:
* Copying/syncing to/from another host over any remote shell like ssh, rsh.
* Copying/Syncing through rsync daemon using TCP.
  ![scp command](../../Pictures/rsynccmdop.png)
* refer [youtube link](https://www.youtube.com/watch?v=2PnAohLS-Q4)
* refer [GFG rsync  link](https://www.geeksforgeeks.org/rsync-command-in-linux-with-examples/)
>## ps
Linux provides us a utility called **ps** for viewing information related with the processes on a system which stands as abbreviation for __“Process Status”.__ **ps command** is used to __**list the currently running processes and their PIDs along with some other information depends on different options.**__
Syntax - `ps [options]`

![PS command](../../Pictures/pscmdop.png)
* refer [youtube link](https://www.youtube.com/watch?v=HSsYDoAHnso)
* refer [GFG ps  link](https://www.geeksforgeeks.org/ps-command-in-linux-with-examples/)
>## rm
- **rm** stands for __**remove**__ here.
- **By default, it does not remove directories.**
- Syntax:`rm [OPTION]... FILE...`

![rm command](../../Pictures/rm cmd.png)
* refer [youtube link](https://youtu.be/gcE5QvggzL4)
* refer [GFG rm  link](https://www.geeksforgeeks.org/rm-command-linux-examples/)
>## dir
- *dir* command in Linux is used to __**list the contents of a directory.**__
- __lists the files and folders in columns, sorted vertically and special characters are represented by backslash escape sequences.__ But unlike *ls*, when the output is on terminal, it does not produce __colored output__ as **ls** does.

- Syntax:` dir [OPTION] [FILE] `

![dir command](../../Pictures/dir cmd.png)
* refer [youtube link](https://www.youtube.com/watch?v=JCMRlMptRus)
* refer [GFG dir  link](https://www.geeksforgeeks.org/dir-command-in-linux-with-examples/)
>## tail
- It is the complementary of __**head**__ command
- *print the last N number of data of the given input.* __By default it prints the last 10 lines of the specified files.__

- Syntax:`tail [OPTION]... [FILE]...`

![tail command](../../Pictures/tailcmd.png)
* refer [youtube link](https://www.youtube.com/watch?v=1pD28tFgAb8)
* refer [GFG tail  link](https://www.geeksforgeeks.org/tail-command-linux-examples/)
>## touch
- The __**touch command**__ is a standard command used in UNIX/Linux operating system which is used to __create, change and modify timestamps of a file.__
- **cat** - Create file with content
- **touch** - Create file w/o content.(empty)

![touch command](../../Pictures/touchcmd.png)
* refer [youtube link](https://www.youtube.com/watch?v=tpUyBbD4LQE)
* refer [GFG touch  link](https://www.geeksforgeeks.org/touch-command-in-linux-with-examples/)

>## uname
- __**Information about the system**__
![uname command](../../Pictures/unamecmd.png)
* refer [youtube link](https://youtu.be/WnjofnvIIvg)
* refer [GFG uname  link](https://www.geeksforgeeks.org/uname-command-in-linux-with-examples/)

>## which
- **locate the executable file associated with the given command by searching it in the path environment variable.**
- 
![which command](../../Pictures/whichcmd.png)
* refer [youtube link](https://www.youtube.com/watch?v=MtnB8fajiJk)
* refer [GFG which  link](hhttps://www.geeksforgeeks.org/which-command-in-linux-with-examples/)

