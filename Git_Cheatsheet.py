Initialize folder as git repo = git init (need to be in working dir...)

git status -- Tells you what files have been modified, what is staged and ready for commit, etc...

git add 'filename'  --> for entering single files into staging.

git add .  --> for entering all files/dirs/etc into the staging area (track...)

---->This puts them into the staging area...

git commit  --> takes a snapshot of proj in time (but only files you have added to staging)

---->This will open up a text editor, 1st line = Summary, next few lines more description...
---->If you dont enter any message then the commit will be aborted...

git commit -m "enter summary here..."

---->This will eliminate the need to go into a text editor to enter summary and description...

#issue w/ commit being aborted right away b/c of message being opened in sublime
#Correction w/ :

git config --global core.editor "'C:\Program Files\Sublmie Text 2\sublime_text.exe' -m -w"


Working with modified files (compare to previous versions, etc...)
-How to see exactly whats changed in a file since the last commit...

git diff (will show you what the diff is b/t the new and previous version...shows you lines for you to get your bearing
			and then w/ - and + show what has been removed and what has been added...)
		--> only works on unstaged files

		--> Need to use git diff --staged for those that you have added into the staging area...(will show same way...)



In global config file you can set up so text editor is used to do comparison from (git diff) as opposed to in the commandline
window where it can be hard to read if there are lots of changes...

##The power of branches...
"""allow to experimentnt, fix, play w/ code w/o altering the master.  At the end you can if so desire merge the changes from a 
branch back into the master """

Create a branch (from w/in the dir you want to make the branch of...)

git branch 'newname'

--after create, need to move into branch (it doesnt happen on its own and can cause confusion when start making changes
	without realizing that you are still in master and not new branch...)

switch between branches...

git checkout 'name of branch you want'

can use checkout for older commits, individual files, 

can eliminate issue w/ forgetting to move to new branch when created by:

git checkout -b bugFix

git branch

-->This will give you a list of all the branches avail and you can ensure what branch you are actually on...