>## 1. add
Syntax - `git add <directory>`
- __Add file contents to the index__
- Stage all changes in <directory> for the next commit.
  Replace <directory> with a <file> to change a specific file.

>## 2. checkout
Syntax - ` git checkout -b <branch>`<br>
`git checkout <branch>`
- Create and checkout a new branch named <branch>.
- Drop the -b flag to checkout an existing branch.

>## 3. clone
Syntax - ` git clone <repo>`<br>
-  Clone repository located at __<repo>__ on to a local machine.
- Original repository can be located on the local filesystem or on a remote machine via **HTTP or SSH**
>## 4. commit
* Syntax - ` git commit -m "<message>"`<br>
  - Commit the staged snapshot, but instead of launching a text editor, use <message> as the commit message.<br>
* Syntax - ` git commit --amend>"`<br>
  - Replace the last commit with the staged changes and last commit combined. 
  - Use with nothing staged to edit tje last commit's message.

>## 5. config
* Syntax - `git config --global user.name <name>`
  * Define **author name** to be used for all the commits by the current user.
* Syntax - `git config --global user.email <email>`
  * Define **author email** to be used for all the commits by the current user.
* Syntax - `git config --global alias. <alias-name> <git-command>`
  * Create shortcut for a Git Command. E.g. **alias.glog** "log --grapgh --oneline" will set __"git glog"__ equivalent to "git log--graph--oneline"
* Syntax - `git config --system core.editor <editor>`
  * Set text editor used by commands for all users on the machine <editor> arg should be the command that launches the desired editor (e.g., vi).
* Syntax - `git config --global --edit`
  * Open the global configuration file in a text editor for manual editing.
>## 6. gitignore
- Ignored files are tracked in a special file named `.gitignore` that is checked in at the root of your repository. 
- There is **no explicit git ignore command:** instead the __.gitignore__ file must be edited and committed by hand when you have new files that you wish to ignore. 
- __**.gitignore**__ files contain patterns that are matched against file names in your repository to determine whether or not they should be ignored.


>## 7. log
- `git log`
  - Display the entire commit history using the default format.
- `git log -<limit>`
  - Limit number of commits by <limit>.<br>
E.g. **”git log -5”** will limit to 5 commits.
  - `git log --oneline`
    - Condense each commit to a single line.
  - `git log -p`
    - Display the full difference of each commit
  - `git log --stat`
    - Include which files were altered and the relative number of
lines that were added or deleted from each of them.
  - ` git log --author= ”<pattern>”`
    - Search for commits by a particular author.
  - `git log --grep=”<pattern>”`
    - Search for commits with a commit message that matches <pattern>
  - `git log <since>..<until>`
    - Show commits that occur between <since> and <until>. Args can be a
commit ID, branch name, HEAD, or any other kind of revision reference
  - `git log -- <file>`
    - Only display commits that have the specified file.
  - `git log --graph --decorate`
    - **--graph** flag draws a text based graph of commits on left side of commit
msgs. **--decorate** adds names of branches or tags of commits shown.
>## 8. init
- `git init <directory>`
    - Create empty Git repo in specified directory. 
    - Run with no arguments to initialize the current directory as a git repository.
>## 9. merge
- `git merge <branch>`
  - Merge <branch> into the current branch.
>## 10. gitk
- `    gitk [<options>] [<revision range>] [--] [<path>…]    <revision range>`
  - __Gitk__ is a graphical repository browser. 
  - It was the first of its kind.
  - It can be thought of as a GUI wrapper for **git log**. 
  - It is useful for exploring and visualizing the history of a repository.
  - It’s written in __**tcl/tk**__ which makes it portable across operating systems.
>## 11. status
- `git status`
  - List which files are staged, unstaged and untracked.
>## 12. pull
- `git pull <remote>`
  - Fetch the specified remote's copy of current branch and immediately merge it into local copy.
- `git pull --rebase <remote>`
  - Fetch the remote's copy of current branch and rebases it into the local copy. 
  - Uses `git rebase` instead of merge to integrate the branch.
>## 13. remote
- `git remote`
  - Shows remote repos
- `git remote add <name> <uri>`
  - Create a new connection to a remote repo.
  - After adding a remote, you can use **<name>** as a shortcut for **<url>** in other commands.
  - Adds a new remote called *<name>*
- ` git remote rm <name>`
  - remotes *<name>*
>## 14. stash
- `git stash push -m "New Tax Rules"`
  - creates a new stash
- `git stash list`
  - List all the stashes
- `git stash show stash@{1}` 
  - Shows the given stash.
- `git stash show 1`
  - shortcut for `stash@{1}`
- `git stash apply 1`
  - Applies the given stash to the working dir
- `git stash drop 1`
  - Deletes the given stash
-  `git stash clear`
  - Deletes all the stashes


# Refer this for `Cheat Sheet` [git cheat sheet](../../Downloads/Git-Cheat-Sheet-Mosh-Hamedani.pdf)