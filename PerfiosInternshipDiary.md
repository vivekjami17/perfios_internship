# Internship Diary

>## 27th Feb, 2023
- [x] Learned Markdown Documentation
  - https://daringfireball.net/projects/markdown/
  - https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
- [x] Made My Resume using the syntax of Markdown Doc.

>## 28th Feb, 2023
On Leave
- [x] Had to go to College for Project Work Review Phase - 1

>## 1st March
- [x] Documented most of the topics which I learnt in Markdown (documentation me jo padha he) in MarkdownDoc.md file.

>## 2nd March
Started Learning UNIX Commands
- adduser
- addgroup
- cat(15 types)
- cd

>## 3rd March(UNIX Commands Continuation)
> Commands 
- chmod
- clear
- cp
- cut
- date
- deluser
- delgroup
- echo
- find
- grep 
- head
- history
- man
- mkdir
- mv
- passwd
- shutdown
- ssh
- scp
- rsync
- ps

>## 6th March(UNIX Commands Continuation and End)
- ps
- rm 
- dir
- tail
- touch 
- uname 
- which

> Git Commands
- add
- checkout
- clone
- commit
- config
- gitignore
- log
- init
- merge
- gitk
- status
- pull

>## 7th March (Git Commands continuation)
- remote
- stash
Mosh Hamedani
1. Introduction
2. What is Git
3. Using git
4. Installing git
5. COnfiguring git
6. Getting help
7. Taking snapshots
8. Initializing a repository
9. Git Workflow
10. Staging files

>## 8th March (Git Continuation)
11. Committing changes
12. Committing Best practices
13. Skipping the staging area
14. Removing files
15. Renaming or Moving files

>## 9th March (Git Completion)
17. Ignoring files
18. Short Status
19. Viewing the Staged and Unstaged changes
20. VIsual Diff Tools
21. Viewing the history
22. Viewing a commit
23. Unstaging files
24. Discarding local changes
25. Restoring a File to an Earlier version

- Started Python Learning

>## 10th March
- Lists
- Dictionaries
- Tuples
-  Set
- Frozen Sets
- String
- Linked List
- deque - stack
- deque - queue
- Binary tree



Modules in Python
- OS [ref link](https://www.geeksforgeeks.org/os-module-python-examples/)
- argparse [ref link](https://www.geeksforgeeks.org/os-module-python-examples/)
- pandas [ref link](https://pandas.pydata.org/docs/)

>## 13th March
- Functions
- Decorators
- Classes and Objects
- Modules
- packages
- libraries
- framework
- Lamda expression

>## 14th March
- Venv
- Error Handling
  
- ## Creating a SSH tunnel
  - SSH tunneling, or SSH port forwarding, is a method of transporting arbitrary data over an encrypted SSH connection. SSH tunnels allow connections made to a local port (that is, to a port on your own desktop) to be forwarded to a remote machine via a secure channel. 

 - Local Port Forwarding 
 - Remote port forwarding
 - Dynamic Port forwarding 

>## task assigned
- Establish connection between 5 machines
- View files and directories after connection
- Transfer files from one machine to another machine 
-------
* All the tasks to be done without password also

>## tasks accomplished
- Using `ssh` to establish connection between different linux machines.
```bash
 sudo apt update
 sudo apt install openssh-server 
```
- Established connection with 'vaibhavraj' user using the below ssh command

```bash
vivek@vivek-Latitude-5531:~$ ssh vaibhavraj@192.168.10.94
The authenticity of host '192.168.10.94 (192.168.10.94)' can't be established.
ECDSA key fingerprint is SHA256:ZqJv9EkLkKPQMlDTCIk6py66cJUV0N3bTc3YJEambn0.
Are you sure you want to continue connecting (yes/no/[fingerprint])? y
Please type 'yes', 'no' or the fingerprint: yes 
Warning: Permanently added '192.168.10.94' (ECDSA) to the list of known hosts.
vaibhavraj@192.168.10.94's password: 
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 5.14.0-1058-oem x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

 * Introducing Expanded Security Maintenance for Applications.
   Receive updates to over 25,000 software packages with your
   Ubuntu Pro subscription. Free for personal use.

     https://ubuntu.com/pro

Expanded Security Maintenance for Applications is not enabled.

9 updates can be applied immediately.
6 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

vaibhavraj@vaibhavraj-Latitude-5531:~$ ls
abc.txt  Documents  Music     Public  Templates
Desktop  Downloads  Pictures  snap    Videos
vaibhavraj@vaibhavraj-Latitude-5531:~$ whoami
vaibhavraj
```
2.  Transfered files from `vaibhavraj` user *( another machine to my machine)*
```bash
vaibhavraj@vaibhavraj-Latitude-5531:~$ ls
abc.txt  Documents  Music     Public  Templates
Desktop  Downloads  Pictures  snap    Videos
vaibhavraj@vaibhavraj-Latitude-5531:~$ cat abc.txt
gfh hfi
vaibhavraj@vaibhavraj-Latitude-5531:~$ scp abc.txt vivek@192.168.10.104:/home/vivek/perfios_internship
vivek@192.168.10.104's password: 
abc.txt                                       100%    8     0.6KB/s   00:00    
vaibhavraj@vaibhavraj-Latitude-5531:~$ 
```

3. Transfering files to a **destination path** (my machine to another machine)
```bash
vivek@vivek-Latitude-5531:~/perfios_internship$ scp file@vivek.txt vaibhavraj@192.168.10.94:/home/vaibhavraj/Downloads
vaibhavraj@192.168.10.94's password: 
file@vivek.txt                                100%    0     0.0KB/s   00:00   
```
# Remote Log In (W/O Password)
4. Establishing **SSH** connection between 5 machines.
  - Create a guest account in all machines with same passwords.
  ```bash
  vivek@vivek-Latitude-5531:~$ sudo adduser guest
  ```
  ```bash
  guest@vivek-Latitude-5531:~$ ssh guest@192.168.10.94
The authenticity of host '192.168.10.94 (192.168.10.94)' can't be established.
ECDSA key fingerprint is SHA256:ZqJv9EkLkKPQMlDTCIk6py66cJUV0N3bTc3YJEambn0.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.10.94' (ECDSA) to the list of known hosts.
guest@192.168.10.94's password: 
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 5.14.0-1058-oem x86_64)

  ```
  - Logging into the Guest account has three steps/ commmands to be executed :-

  ```bash
  guest@vivek-Latitude-5531:/home/vivek$ ssh-keygen -b 4096
  The key's randomart image is:
+---[RSA 4096]----+
|                 |
|       . o       |
|        + o      |
|       +   .     |
|      . S .      |
|    .o.+.O o     |
|    oo=+=o*      |
|  . .XB*E+       |
|   +OX%Ooo       |
+----[SHA256]-----+
  ```
  ```bash
  guest@vivek-Latitude-5531:~$ ssh-copy-id guest@192.168.10.94
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/guest/.ssh/id_rsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new key
  ```
  Logging in :-
  ```bash
  guest@vivek-Latitude-5531:~$ ssh guest@192.168.10.94

  ```
  Viewing and Transferring files in another account( guest )
  ```bash
  guest@vaibhavraj-Latitude-5531:~$ ls
guest@vaibhavraj-Latitude-5531:~$ touch abc.txtx
guest@vaibhavraj-Latitude-5531:~$ ls
abc.txtx
guest@vaibhavraj-Latitude-5531:~$ ls
abc.txtx
guest@vaibhavraj-Latitude-5531:~$ ls
abc.txtx
guest@vaibhavraj-Latitude-5531:~$ echo "Vivek's file" > file.txt
guest@vaibhavraj-Latitude-5531:~$ ls
abc.txtx  file.txt
guest@vaibhavraj-Latitude-5531:~$ 
```
## Task Done!!!

>## March 15

v- Problem Statements discussed with Snigdha and teammates

1.  - Ansible for Deployment 
    - Output of Ansible script provided by Athena
    -  Understand the output looking like
    - Code - extract karke pdf report
    - Pdf report
    - Data avail for ops team (any changes being made ) through Ops team.
----------------
2. - Metrics-
      - Uptime (Devops team worked on)
      - Downtime
      - Capactiy
      - App - req, n/w, throughput , income and outgoing req etc

- Making sense - Grapgh (bar, line,gauge etc)
- Elastic search 
- Python - plotly
- Prometheus Graphana 
- D3JS -  JS Library
Inputs in diff file format
Framework`
Automated, monthly wise, date range (All in graphs)
-----------------
### Explored:-
1. **D3JS**
2. **ANsible**
--------
Both have Python has a base

>## March 16
Project Name : **Secura**
--------------------
CIS Compliance report based on Ansible Dry Run Output.Parse the output of the Ansible Dry Run/Check of CIS Ansible scripts run for one or many hosts and generate a report based on current server setup and whether any changes are to be made or not. 

Project Name : **Nebula**
------------------------------
Coverage of different variations of _**Devops Metrics**_(uptime, capacity etc) using D3.JS visualisations. 

