# Learn command line

Please follow and complete the free online [Bash Scripting Tutorial](https://ryanstutorials.net/bash-scripting-tutorial/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. You should be able to go through these in a couple of hours.

**Note:** Bash is not installed on a PC. Rather, PC users must install Cygwin. Once Cygwin has been installed, the command line interface witll _emulate_ bash. You can find all information regarding Cygwin [here](https://www.cygwin.com/).

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > pwd -- Show current working directory path <br />
> > mkdir [directory] -- Creates a directory <br />
> > rmdir [directory] -- Removes a directory (directory must be empty) <br />
> > touch [filename] -- Creates a file if it does not exist <br />
> > rm [filename] -- Deletes a file <br />
> > ls [directory] -- Lists files in given directory (default: current directory) <br />
> > cp [filename] [filename] -- Copies a file given by the first argument into the file given by the second argument <br />
> > ls -a -- Shows hidden files <br />
> > mv [filename] [filename] -- Moves a file <br />
> > man [command name] -- Shows information about a command <br />

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > `ls` -- Lists files in a directory <br />
> > `ls -a` -- Includes hidden files <br />
> > `ls -l` -- Shows details about all files listed <br />
> > `ls -lh` -- Shows details about all files with human readable sizes <br />
> > `ls -lah` -- Includes hidden files, Shows details about all files with human readable sizes <br />
> > `ls -t` -- Lists files sorted by modification time, newest first <br />
> > `ls -Glp` -- Shows details about all files, ignores group names, and appends '/' to directories <br />

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > `ls -d` -- Displays only directories <br />
> > `ls -m` -- Displays names as a comma-separates list <br />
> > `ls -n` -- Displays long format list with GID and UID numbers <br />
> > `ls -x` -- Lists files row-by-row rather than by column <br />
> > `ls -1` -- Displays each entry on a line <br />

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs [command]  -- Reads STDIN as a list of arguments, separated by blanks
ls *.md | xargs -i cp {} markdown/{} -- collects all files with '.md' extension and copies them to 'markdown' directory

 

