# project2

echo "# project2" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/serihesap/project2.git
git push -u origin master
                
…or push an existing repository from the command line
git remote add origin https://github.com/serihesap/project2.git
git push -u origin master

git reset --hard HEAD
git push -f origin HEAD^:master

git rm .env --cached
git commit -m "Stopped tracking .env File"

Using your favorite text editor, open the file .git/info/exclude
Add rules to the exclude file as you would the .gitignore file
