---
layout: page
title: Bash and the Command Line Interface
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script>

Unix has several commands for various purposes. They can be slightly modified using "options".

An example of a command is ls which lists all the files in a particular directory (not mentioning any directory lists all the files in the current directory). This can be modified as
	
	ls -ltr Documents

which lists all the contents of the Documents directory in the long format (```l```), sorted by time (```t```), and in reverse order (```r```).
Each of l, t, and r is an option. We can also write these separately or in a verbose function (like ```ls -l -t --reverse Documents```).

If we want to find information about a particular command, we use the ```man``` command (Example: ```man ls```).

You can interact by two means:

* Command Line Interface: Interaction directly from the command line in a terminal.
* Bash Script: If you want to combine commands, using CLI may be unwieldy, so we write the commands in a file: a Bash script.

In a directory, we use ```.``` to represent the directory itself and ```..``` to represent the parent directory.

We can set up shortcuts as ```alias <shortcut>='<desired command>'```.

## Common File Management Commands

* ```mkdir```: Makes a directory with the given name.  
Usage: ```mkdir dirname``` creates a directory with name ```dirname```.

* ```cat```: Concatenate files and display result.  
Usage: ```cat file1 file2``` appends file2 to file1. If we only use one file, it will just display the file. If we want to write the concatenation into a new file, we can use ```cat file1 file2 > file``` to "redirect" the output (that would go to the console) to ```file```.

* ```cp```: Copies from source file/folder(s) to destination file/folder(s).  
Usage: ```cp src file``` copies the content of ```src``` to ```file```. If we use something like ```cp src1 src2 folder```, ```src1``` and ```src2``` are copied into ```folder```. To copy a directory (and recursively all the directories inside it), we need to use something like ```cp -rR srcdir folder```. <!--```-r``` represents that ```srcdir``` is a directory, not a file and ```-R``` means "recursive". If we just use ```-r```, it copies the folder ignoring the contents of any nested folders.-->

* ```mv```: Similar to ```cp``` except that the original file/folder is removed.(```mv``` means "move")  
Usage: ```mv src file```.

* ```tree```: Prints the folder structure in a very pretty organized tree-like structure.  
Usage: ```tree dirname```.

* ```ls```: Discussed earlier. See the [permissions](#permissions) section.

* ```chmod```: If as an owner, I want to change the permissions, I can use this command.  
Usage: Say I want to set the permissions of a directory ```dirname``` to ```rwxrw-r-x```. The method to do this is to split this into three triads (```rwx```, ```rw-```, and ```r-x```), convert each one to a binary representation depending on whether or not it is set (```111```, ```110```, and ```101```), and convert each number to decimal form (```7```, ```6```, and ```5```). Then the resulting command I must use is ```chmod 765 dirname```. (Experiment with this!)

## <a name="permissions"></a>Permissions

Let us consider the long format of ```ls``` in particular.
Consider the long format displayed as
	
	drwxr-xrw- 4 amit amit 4096 Aug 16 10:27 'CS251'

The data displayed is the permissions, number of links, owner, group, size, date, and name in that order.

* Permission: The first triad is what the owner can do. The second triad is what the group members can do. The third triad is what the third triad can do.  
If we are considering a file, then ```r``` means readable, ```w``` means writable, and ```x``` means executable. The first character represents what the thing under consideration is (```f``` for file, ```d``` for directory, ```l``` for link, etc.)  
On the other hand, if we are considering a directory, ```r``` means that you can list the files in the directory, ```w``` means that you can add/delete the files in the directory, and Execution of a directory just means that you can step into a directory. Note that the ```w``` bit is meaningless if the ```x``` bit is not set.  
So in the example given, ```CS251``` is a directory. The owner, ```amit``` can list and add/delete the files in it. Members of the group ```amit``` can list the files in the directory and step into it, but cannot add/delete files. Note that they may be able to edit individual files in the directory depending on the individual permissions, but they cannot add/delete them. Other users  can only list the files in the directory (Despite the ```w``` bit being set, they cannot add/delete files since the ```x``` bit isn't set).

* Group: Each person on the system belongs to one or more groups.
* Owner: The person on the system who creates a particular file/folder is deemed its owner. The owner can change the group that a particular file/folder belongs to. So if I want to collaborate with someone else in the group ```team```, I can change the group from ```amit``` to ```team``` and give other people the permission to do whatever.s

## File System Representation and more Commands

A directory is just a table of pairs: the name of the file/directory and a pointer. The pointer points to something called an ```inode```, which just has all the information displayed when we use ```ls -l```: permissions, owner/group, link, timestamp, size, and finally a pointer to where the file content is actually stored.

The ```size``` of a directory is the size of the _table_, as a result of which it is either ```4096``` or a multiple of it. When allocating memory for the table, it is done so in chunks of ```4096```.

* ```ln```: Sometimes, we create shortcuts to a file (on our Desktop for example). To do this, we use the ```ln``` command. This can be implemented in two ways:
	* Purely a shortcut. So opening the shortlink opens the original file but copying the shortcut elsewhere just results in another shortcut to the same file. This is known as a _symbolic link_ or _soft link_. This is essentially a pointer to the name of the file in the table, not its ```inode```. A symbolic link to ```a.txt``` can be created using ```ln -s slink a.txt```.  
	* Alternatively, we may desire that copying the shortcut elsewhere copies the contents of the original file itself. This is commonly known as an _alias_ or a _hard link_. This is essentially a pointer to the ```inode``` of the original file. A hard link to ```a.txt``` can be created using ```ln hlink a.txt```.  

	An important distinction arises when we delete the original file (which removes its name and pointer from the table) but not the shortcut. The soft link will break, since the entry will have a dangling pointer. However, the hard link will continue to work. This is because the ```inode``` and the file content is still there and undeleted.  
	Look at links in particular after doing ```ls -l```.

* ```cmp```: This is used to compare two files byte by byte.  
Usage: ```cmp file1 file2```

* ```diff```: This is used to compare two files line by line.  
Usage: ```diff file1.txt file2.txt```. Compares the two files and indicates changes to be made to ```file1.txt``` to make it identical to ```file2.txt```. In the output, ```a``` is "add", ```c``` is "change", and ```d``` is "delete". A ```<``` indicates a line in the first file and a ```>``` indicates a line in the second file.

* ```find```: Search the system for file(s) with particular properties and take possible actions.  
Usage: ```find <starting point> <expression>```. For example, if we want to search for a file named ```notes1.md``` within the directory ```/Documents```, we write ```find /Documents -name notes1.md```. Some possible things to include in the expression are
	* ```-name```: Name of the file. If we want a particular type of file, say ```.txt``` , we can search for ```*.txt```.
	* ```-type```: Type of the file (```d``` for directory, ```f``` for file).
	* ```-perm```: Permissions of the file (in a format similar to that used in ```chmod``` such as ```765```)
	* ```-size```: Find files of a particular size. We use ```c``` to mean bytes. So if we want a file with size greater than 100 bytes, we write ```-size +100c```. If we want say between 50 and 100 bytes, we can write ```-size +50c -size -100c```.
	* ```-exec```: Action to be taken on all the file(s) returned.  

	So if we want to list in long format all ```.txt``` files in the current directory that are at least 100 bytes, we write

		find . -name '*.txt' -size +100c -exec ls -al {} \;

* ```egrep```: This is equivalent to ```grep -E```. ```egrep``` stands for "Extended Global Regular Expression Print".  
Usage: ```egrep <regex> <filename>```. Prints every line in ```filename``` containing the regular expression ```regex```.
	* ```egrep wurd grep.txt``` prints all lines in ```grep.txt``` that contains the string ```wurd```.
	* ```egrep 'a b' grep.txt``` prints all lines that contains the string ```a b```. We use the quotations because there is a space in the string.
	* ```egrep 'hi|hey' grep.txt``` prints all lines that contain either the string ```hi``` or ```hey```.
	* ```egrep '(Th)?is' grep.txt``` prints all lines that contain ```is``` or ```This```.
	* ```egrep '[a-z]{2,5}' grep.txt``` prints all lines that contain strings made of characters from ```a``` to ```z``` of length between ```2``` and ```5``` (inclusive). If we want only length ```5```, we can use ```{5}``` instead of ```{2,5}```.
	* ```egrep -v <expression> grep.txt``` prints all lines that _don't_ contain strings satisfying ```<expression>```.
	* ```ls -al | egrep '^d.*'``` finds directories. ```^d``` means that it begins with ```d``` (We can similarly use ```$``` to mean that it ends there). The output of ```ls -al``` is "piped" to the ```egrep``` by the ```|```. Piping is often used to give the output of one command as input to another.

* ```cut```: Cuts each line into several "fields" using a given delimiter. For example, if we want to cut up each line of a ```.csv``` file into several fields (separated by ```,```) and output the third field in each line, we can use

		cut -d "," -f 3 csvfile.csv

If we want everything _but_ the third field, we can add the ```--complement``` option.