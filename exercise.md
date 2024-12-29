# 1
# 2
- `git clone https://github.com/missing-semester/missing-semester.git`      
- ` git log --all --graph --decorate`  explore the version history by visualizing it as a graph.
- `git log -1 README.md` Show the last person to modify README.md 
-  ```
   `git blame _config.yml | grep collections` 
   `git show --pretty=format:"%s" a88b4eac | head -1`
   ```
    - Show the commit message associated with the last modification to the collections: line of _config.yml
    - Alternatively, we can use `git log --pretty=format:"%s" a88b4eac -1` 
# 3
Remove sensitive information from the repository.
-  `git filter-repo --path ./my_password --invert-paths`
- `git filter-repo`: A tool for rewriting Git history by filtering the repository's contents, replacing git filter-branch for better performance and flexibility.
- `--path ./my_password`: Specifies the path (file or directory) to be included in the filter. In this case, it's the my_password file or directory at the root of the repository.
- `--invert-paths`: Inverts the path filter, meaning it will exclude the specified path (./my_password) instead of including it.

# 4
- `git log --all --oneline`
- `git stash pop`
- `git stash list`
- `git stash show stash@{0}` 
    - `stash@{0}`: Refers to the most recent stash entry.
- `git stash pop `
# 5
```
 [alias]
     graph = log --all --graph --decorate --oneline
```     
- Alternatively in zsh, we can use the git config command to add the alias directly from the terminal.
 `git config --global alias.graph "log --all --graph --decorate --oneline"`
# 6
git config --global core.excludesfile ~/.gitignore .DS_Store