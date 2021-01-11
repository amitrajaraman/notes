---
layout:	page
title:	Advanced Bash
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script>

## sed

### Introduction

```sed``` is a *stream editor*. A stream editor is different from a usual editor like, say, SublimeText. In a stream editor, you can only edit things within a narrow examination window, which can be only a line or so. It is used as

	sed options script input-files

You mention what is be done in the script. Until the end of the file is reached, what it does is:

* ```sed``` reads a line of text from the input file to (a very limited) buffer, known as the *pattern space*.
* Based on the script and output, the line is processed.
* There is also a separate special buffer, known as the *hold space*, that can be used by some ```sed``` commands to hold and accumulate text between different iterations.

The script can either be inlined, in which case it is enclosed in ```""```, like ```sed "inline_script" input-files```.    
or it can be given as a file, in which case it is used as ```sed -f script_filename input-files```.    
Most ```sed```-related stuff can be found [here](https://www.grymoire.com/Unix/Sed.html#toc-uh-62b).

Some of the important ```sed``` options are:
* ```-n```: Don't print lines by default. By default, the content of the pattern space is automatically put in the output space. For example, if we only want to print (```p```) lines that have the word "Deceased" in it, we can do

		sed -n '/Deceased/p' covid_data.csv

* ```-f scriptfile```: We've already seen this, it's used to take the script from a file.
* ```-s```: Treat each file separately. For example, if we want to print the first 10 lines of each of the files, then we should use this option (if we don't, it'll only print the first 10 lines of the first file).
* ```-r```: This enables the use of extended regular expressions.

### Scripts

A script is written as

	[address] [!] command
	...
	[address] [!] command

A missing address means all lines and a ```!``` means that we look at all lines *except* the lines specified by address. The ```address``` can be

* a single line address:
	
	* If we only want to show line 3, we can do

			sed -n '3 p' inpFile.csv

		If we don't include ```-n```, it'll print line 3 twice.

	* If we only want to show the last line, we can do 

			sed -n '$ p' inpFile.csv

	* Suppose we want to substitute all ```_``` on line 10 with ``` ``` (and print the line). We can do

			sed -n -e '10 s/_/ /' -e '10 p' inpFile.csv

	The ```-e``` option is used to chain/join the two commands.



* a set of lines:

	* Say we want to show all directories in the current directory. We can then do (note the use of regular expressions)

			ls -al | sed -n '/^d/ p'

* a range of lines:
	
	* If we want to show all the lines between 1 and 10, we can do

			sed -n '1,10 p' inpFile

	* If we want to show all the lines between an ```if``` statement and the closest ```else```, we can do

			sed -n '/^if/,/^else/ p' inpFile.cpp

* a nested address:
	
	* If we want to show all the ```print``` statements between lines 10 and 25, we can do

			sed -n '20,30(/print/ p)' inpFile.py

* a complement of a particular address (```!```):

	* If we want to show all the non-```print``` statements between lines 10 and 25, we can do

			sed -n '20,30(/print/! p)' inpFile.py


### sed commands

Here we examine some basic ```sed``` commands.

* Line command:

	* this prints the numbers of the matching statements

			sed -n '20,30(/print/! =)' inpFile.py

* Modify commands:

	* ```insert```: It can be used to insert text before some address. If we want to insert ```2019 Batch``` (with some spaces beforehand) at the beginning of a file, we can do

			sed '1 i\
				2019 Batch' outpFile.csv

	* ```append```: It appends text after some address, it can only be used with single-line and set of lines address types.

	* ```change```: We can use it to replace an entire matched line with some other text.

	* ```delete```: It is used to delete an entire matched line.

	* ```s```(substitute): The syntax is

			[addr1] [,addr2] s/searchstr/replacestr/[flags]

		It replaces the text selected by the search string with replacement string. The search string can be a regex. Some flags that can be used are ```g``` which is used to replace all occurrences (otherwise it only replaces the first occurrence)

		We can also use a substitution back reference ```&```  to use the matched string as

			sed -r 's/19[0-9A-Z]{7}/&@iitb.ac.in/' inpFile.csv

		This converts ```190050015``` to ```190050015@iitb.ac.in``` for example.

		If there are multiple such search patterns we want to back reference, we can do

			sed -r 's/st1(r2[A-Z]{2})st3(r3[0-9]{2})/\1\2/' inpFile.csv

		This would convert ```st1r2KZst3r343``` to ```r2KZr343```

	* ```y```(transform): The syntax is

			[addr1][,addr2]y/listOfChars1/listOfChars2/

		It replaces characters in the first list with the corresponding characters in the second list.

* IO commands:

	* ```n``` (default ```sed``` workflow): It reads a line from the input stream to the pattern space, removing any trailing newline. It executes the given commands if the address specifications are met, and unless ```-n``` is used, it prints the pattern space to the output stream.

	* ```N```: After reading a line to the pattern space, it adds a newline and appends the next line of input to the pattern space. It then executes the commands and prints to the output stream. This is useful for processing multiple lines at the same time.

	* ```p```: We've already seen this, it is used to print the entire pattern space to the output. Unless ```-n``` is used, it will print the same line twice.

	* ```P```: This prints (only) the first line of the pattern space (the content up to and including a newline)

	* ```r filename```: This reads the filename and writes it directly to the output stream, it does *not* copy this to the pattern space.

	* ```w filename```: This reads the pattern space and writes it to the pattern space.

	* ```b```(branch unconditionally): This is like a ```goto``` statement. For example,

			sed -n -r '
				/19D[0-9]{6}/ b save
			w others.csv
			b
			:save
			w dd-students.csv
			' inpFile.csv

		writes the names of the dual-degree students to dd-students.csv and the remaining names to others.csv.

	* ```q```: This quits ```sed``` and does not process the rest of the file.

			sed -e '50q' datafile

		quits after printing the first 50 lines

	* ```h```: This is used to copy whatever is there in the pattern space to the hold space (overwriting the current content).

	* ```H```: This is used to append whatever is there in the pattern space to the hold space.

	* ```g```: This is used to copy whatever is there in the hold space to the pattern space (overwriting the current content).

	* ```G```: This is used to append whatever is there in the hold space to the pattern space.

		For example, if you want to transfer all the names of the dual-degree students to the end, you can do

			sed -r -e '/19D[0-9]{6}/ H' -e '/19D[0-9]{6}/ d' -e '$ G' inpFile.csv

Writing ```sed``` scripts in a scriptfile usually hugely improves readability. The ```above``` sed command is equivalent to

	#!/bin/sh
	sed -r '
	 /19D[0-9]{6} {
	 	H
	 	d
	 }
	  $ {
	  	G
	  }' inpFile.csv

The braces must appear on a different line from the ```sed``` commands.

## awk

### Introduction

```awk``` is a scripting language that is used for manipulating data and generating reports.    
Similar to ```sed```, it scans a file line by line, splits each input line into fields, compares input line/fields to a pattern, and performs the given action(s) on matched lines.

The basic ```awk``` syntax is

	awk [options] 'script' file(s)
	awk [options] -f scriptfile file(s)

If a pattern is missing, the action is applied to all lines. If the action is missing, the matched line is printed. You must have either a pattern or an action.

A *field* is a unit of data in a line. Each field is separated from the other fields by a field separator (by default whitespace). A *record* is a collection of the fields in a line, and a data file is made up of records.

We can address each field buffer by ```$1```, ```$2```, ..., ```$n```, where n is the number of fields in the given record. We can also refer to the entire record buffer by ```$0```.

```awk``` has several pre-defined variables:

* ```FS``` is the field separator (whitespace by default)
* ```RS``` is the record separator (```\n``` by default)
* ```NF``` is the number of fields in the current record
* ```NR``` is the number of the current record
* ```OFS``` is the output field separator (space by default)
* ```ORS``` is the output record separator (```\n``` by default)
* ```FILENAME``` is the current filename.

For example,

	ls -al | awk '{print NR, $9}'

will number and print the files in the current directory

### Script Structure

```awk``` scripts are divded into three major parts.

	BEGIN {pre-processing statements}

	pattern (action)
	pattern (action)

	END {post-processing statements}

The part following ```BEGIN``` is done at the beginning of before ```awk``` starts reading any records from the input file. It is helpful for initializing variables, creating report headings, etc.    
The body contains the logic to be applied to the input file, one record at a time.    
The part following ```END``` is done after all the records in the file have been processed. It is useful for reporting aggregates such as, say, the mean of the data.

Each part of the body can be written well-formatted as

	pattern {
			 statement
			 statement
			 ...
			 statement
			}

We've already seen two patterns, namely ```BEGIN``` and ```END```. Some other patterns are

* Regular expressions: enclosed by ```/```s like in ```sed```. This matches any record that contains the given regex. For example, to print all records with the text ```special``` anywhere,
	
		awk '/special/ {print}'

* Explicit pattern-matching expressions: ```~``` for matching and ```!~``` for not matching. For example, to print the records whose first field matches ```19D[A-Z0-9]+```,

		awk -F, '($1~/19D[A-Z0-9]+/){print NR, $0}' inpFile.csv

	Note that ```/special/ {print}``` is the same as ```($0~/special/)```.

* We can have expressions that have arithmetic operators in them. For example,

		awk '$3 * $4 > 500 {print $0}' file

	prints the records that have the product of the third and fourth fields greater than 500.

* Range patterns: These are used as 
		
		pattern1, pattern2 {action}

	For example,

		awk /190050009/,/190050015/{print} inpFile.csv

```awk``` expressions are made up of variables, constants, and operators.

What if we want to pass shell variables to an ```awk``` script? The scope of a user-defined variable does not extend to an ```awk``` script, we must instead use the ```-v``` switch like

	printf $a
	printf "\n"
	awk -v v="$a" ' 
	BEGIN  {
		print "Printing v"; print v'}'
	inpFile.csv

Here, ```$a``` is a variable outside the ```awk``` script, that we pass to the ```awk``` by creating a new variable with name ```v```.

We can also make *associative arrays*, which are something like maps in C++, where the indices are defined by use. For example, in [this data](covidData.csv), we can run the following script to find the number of cases per state:

	awk -F '
	# ($9~/[A-Z][A-Z]/)
	{
		state[$9]=state[$9]+$10
	}
	END {
		for (i in state) {
			print state[i], i;
		}
	}' covidCases.csv

For output in ```awk```, we can use ```print```, ```printf``` (like in C), and ```sprintf``` (like in C).