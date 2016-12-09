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





