---
layout: page
title: Git
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script>

## Version Control

Modern software is built

* Incrementally
* Collaboratively
* In multiple strands that are finally merged together

Version control records changes to the files over a set of time so that you can go back and look at specific versions later.

* The version currently being worked on is called the *checkout*
* The difference $$\Delta$$ between one version and another is called the *patch set*.

You can have a localized version control system and a collaborative version control system.

A localized version control system sucks beause it does not have collaboration, does not have multiple strands of development, and if something goes wrong with the system it's being worked on, then things will probably go wrong.

In a centralized version control system, you do have collaboration and possibly multiple strands of development, but it's vulnerable and if the system goes down, then it'll be down for everyone.

We thus reach the idea of a **distributed version control system**. Though there is a central repository (in the cloud perhaps), there is also a local version in every remote repository. This rectifies the issues since if an individual's system crashes, he can get a backup from the central repository. And if the server dies, any of the clients' data can be copied back into the central repository.

## Git

Git was designed to

* have simple design,
* be fast,
* support highly non-linear parallel development, and
* be fully distributed.

Due to this, Git can support large projects. 

Git is slightly different from even a distributed version control system. 

* In other vc systems, each version just has the patch set compared to the previous version. In Git on the other hand, every _commit_ (version) is a reference to a full record of all files. 
* Most operations are _local_, not central. You only need to go non-local to sync it up with the cloud. 
* Finally, Git has _integrity_. Everything in Git is (SHA-1) hashed. Each file or directory is referred to by the hash value. The usage of a hash value is important because if the data gets corrupted even slightly, the hash value will be hugely different (so we will be able to detect the corruption).

The basic workflow in Git goes as follows.

* Assume a version in your working directory.
* Make whatever changes to the files you want to.
* Stage some/all the modified files and commit it to the local repository.
* Repeat.
* At some point of time, when you'd like to sync it up with a remote repository, you _push_ it to the cloud so that someone else can _pull_ it.

## Basic Commands in Git

### Installation and Making a Repository

	sudo apt-get install git
	git config --global user.name "username"
	git config --global user.email "email address"
	git config --global core.editor "editorname (like sublimetext)"
	git config --global merge.tool meld #tool used to merge
	git config --list
	
When you want to make a new repository in say a directory called ```CS251-2020```, you first create a directory, go into it as follows, and initialize an empty git repo as follows:

	mkdir CS251-2020; cd CS251-2020
	git init

If you try ```ls -a``` now, you'll see that there's actually a lot of (hidden) files despite the directory appearing empty. The actual local repository where stuff is stored is in the ```.git``` directory.

## Basic Usage

```git status``` can be used to see the current information: the current branch (we will define this later), commit information, and if there are any uncommitted or unstaged ("untracked") files.

If we want to stage a file (or changes to a file), say ```file.txt```, we can do ```git add file.txt```. If we now do ```git status``` again, we see that there is a new/modified file called ```file.txt```.

To commit all staged files, we can do ```git commit -m "Message"```. The Message" is a message that is done while committing which we can see later (to easily recognize changes that have been done). If you'd prefer to write a longer message, just doing ```git commit``` opens your editor to type a message.

```git log ``` displays a log of all the commits along with their timestamps, corresponding messages, and hash values. The ```HEAD -> master``` text next to one of commits shows which commit the one in use is.

## Git Objects (and their structures)

Git consists of several objects, each of which is named by its hash value. There are three types of objects in Git:

* Blobs: They contain some metadata (such as the size of the blob) and the actual contents of the file. Note that the contents may not be in ASCII, they may be binary-coded.
* Trees: They correspond to a collection of files or directories, which may or may not constitute an actual directory. It is essentially a record that contains a table with first the size of the tree, and then pointers to the elements of the collection (which can be blobs (files) or trees (directories)).
* Commits: It is a pointer to a tree that corresponds to the commit along with some metadata (author, previous commit etc).

Finally, there is a ```HEAD``` pointer which points to the current commit.

There are three "areas" in Git, the working area, the staging area and the commit.

We use ```ls -l``` to view the content of the working area. We can also easily look at the content of a file in the working area using ```cat```.

We can use ```git ls-files -s``` to view the content of the staging area. However, if we now want to see the content of a file in the staging area, we cannot just use ```cat```. we must use the hash value that we see when using ```git ls-files -s``` as ```git cat-file -p "hashvalue"``` (```-p``` for ```--pretty```). An easier way to find the hash value of ```file.txt``` is to do ```git hash-object file.txt```.

Finally, if we want to view the content of the commit area, we use ```git ls-tree HEAD```. We can view the content of a particular file using ```git show HEAD:file.txt```.

When we do ```git status```, ```nothing to commit, working tree clean``` means that the all three areas have the same contents. We can use ```git ls-files -s``` to look at the contents of the staging area.

The relation between the three areas can be understood more clearly as:

* Creating a file ```file.txt``` adds a file to the working area. ```git add file.txt```.
* ```git add file.txt``` adds the file to the staging area. Note that ```file.txt``` is still there in the working area!
* ```git commit -m "message"``` adds all files in the staging area to the commit. Note that the files newly added to the commit are still there in both the staging area and the working area!
* If we now edit ```file.txt```, then while the content of the file is the same in the staging area and the commit, it is different in the working area.
* Now, say we add ```file.txt``` to the staging area and then edit ```file.txt``` in the working area a bit more (so that the content of the file is different in the working area, the staging area, and the commit). 
* If we now do ```git commit -m "message"```, then the working area's version of ```file.txt``` will be different from the version in the staging area and commit (which are both the version of ```file.txt``` which was there in the staging area). If, however, we do ```git commit file.txt -m "message"```, then all three versions will become the same as the version which was in the working area.

## Some More Commands

We now introduce an important command called ```git diff```, which can be used to see how files have changed between commits. ```git diff``` gives the difference(s) between a commited file and a _modified_ file (in the working directory), while ```git diff --cached``` gives the difference(s) between a commited file and a _staged_ file. ```git log -p file.txt``` can be used to see the difference across multiple commits.

If we want to see the difference between ```a.txt``` and ```b.txt``` in the working directory, we can do ```git diff --no-index a.txt b.txt```.