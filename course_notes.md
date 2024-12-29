### `git cat-file -p HEAD^{tree}`
- The command shows the contents of the tree object
### `git cat-file -p <hash>`
- Display the content of a Git object identified by `<hash>`.
The -p option shows the content in a human-readable format
### Output of git status
[master (root-commit) f552935] Add hello.txt
 1 file changed, 1 insertion(+)
 create mode 100644 hello.txt
- `f552935` is the truncated sha-1 hash
## Concept
- `History` is just a linear sequence of snapshops
- `merge` changes from different parallel branches
- `master` is default referent and represents the most up-to-date version of your project.
- `Head` is a special reference and refers to where you are currently looking right now.
- `Staging area`: Prepares and organizes changes for the next commit.
- `Upstream branch`: The upstream branch is the default branch that your local branch will pull changes from or push changes to when you run commands like git pull or git push without specifying a remote branch.
- All the git commands don't talk to the internet. It all works locally. So you need commands to retrieve changes that you made somewhere else.

    ```mermaid
    graph LR
        A --> B
        B --> C
        B --> D
        C --> E
        D --> E
        E[+feature +bugfix]
        C[+feature]
        D[+bugfix]
    ```
- the `git fetch` doesn't change any of our local references like our history.
- `git pull` is the same as `git fetch; git merge`
- `fast-forward` The changes that are being pulled are simply ahead of your current commit, so Git can move your branch pointer forward without any conflicts or need for a new merge commit.
- Like many command line tools, Git provides a configuration file (or dotfile) called `~/.gitconfig.`

## Commands
Here are the explanations for the Git commands you've listed:

- **`git init`**  
   Initializes a new Git repository in the current directory. Creates a `.git` directory to start tracking changes.

- **`git help <subcommand>`**  
   Displays help for a specific Git subcommand, such as `git help status`.

- **`git status`**  
   Shows the current status of your working directory, including staged, unstaged, and untracked files.

- **`git add hello.txt`**  
   Stages the file `hello.txt` for commit, meaning that it will be included in the next commit.

- **`git commit`**  
   Commits the staged changes to the local repository. This typically opens an editor for entering a commit message.

- **`git log`**  
   Displays the commit history for the current branch, showing commit IDs, author information, and commit messages.

- **`git log --all --graph --decorate`**  
   Shows the commit history for all branches (`--all`), in a graphical format (`--graph`), and with branch and tag names (`--decorate`).

- **`git --no-pager log --all --graph --decorate --oneline`**  
   Displays the commit history without paging through the output (`--no-pager`), shows a graphical representation (`--graph`), includes branch names and tags (`--decorate`), and condenses each commit to a single line (`--oneline`).

- **`git diff hello.txt`**  
   Displays the differences between the current version of `hello.txt` and the last committed version.

- **`git branch -vv`**  
    Lists all local branches with their corresponding remote-tracking branch and the last commit on each branch.

- **`git checkout -b dog`**  
    Creates a new branch named `dog` and switches to it.

- **`git merge cat`**  
    Merges the branch `cat` into the current branch.

- **`git merge --abort`**  
    Aborts a merge in progress, restoring the working directory to the state it was in before the merge started.

- **`git merge --continue`**  
    Continues a merge process that is in a conflicted state, typically after resolving conflicts.

- **`git remote`**  
    Lists all remotes associated with the repository.

- **`git remote add <name> <url>`**  
    Adds a new remote named `<name>` with the URL `<url>` to the repository.

- **`git push <remote> <local branch>:<remote branch>`**  
    Pushes a local branch to a remote repository. This syntax pushes the local branch to a specified remote branch.

- **`git push`**  
    Pushes changes from the local branch to its corresponding remote branch.

- **`git clone <url> <folder>`**  
    Clones a remote repository from the specified URL into the given folder on the local machine.

- **`git branch --set-upstream-to=origin/master`**  
    Sets the upstream branch for the current local branch to `origin/master`, which means that future pushes and pulls will reference this remote branch.

- **`git branch -vv`**  
    Lists all branches along with their tracking information and the latest commit message.

- **`git fetch`**  
    Fetches the latest changes from the remote repository but does not merge them into your working directory.

- **`git pull`**  
    Fetches changes from the remote repository and automatically merges them into the current branch.

- **`git clone --shallow`**  
    Clones the repository with a shallow history (limited to a specific number of recent commits).

- **`git blame <file>`**  
    Shows who last modified each line of the specified file.

- **`git show`**  
    Displays detailed information about a commit, such as the commit message, changes made, and diffs.

- **`git stash`**  
    Stashes the current changes (both staged and unstaged) temporarily, allowing you to work on something else before coming back to them.
- 
    ```
    git checkout hello.txt
    Updated 1 path from the index
    ```
    - This command would revert hello.txt back to its last committed state
    - Updated 1 path from the index" means that Git has updated the hello.txt file by restoring it from the staging area (index)

---
-   ```
    diff --git a/animal.py b/animal.py
    index 3978a29..7ff9948 100644
    --- a/animal.py
    +++ b/animal.py
    @@ -12,5 +12,6 @@ def main():
        else:
            default()
    
    +
    if __name__ == '__main__':
        main()
    ```
    `diff --git a/animal.py b/animal.py`

    - Indicates that this is a comparison (diff) between two versions of the file animal.py.
    - `a/animal.py`: Represents the file in the old version.
    - `b/animal.py`: Represents the file in the new version.

    `index 3978a29..7ff9948 100644`:

    - `3978a29` is the hash of the file in the old version.
    - `7ff9948` is the hash of the file in the new version.
    - `100644`: Represents the file permissions (a regular file with read/write permissions).

    Change Context
    - `--- a/animal.py`:Indicates the old version of the file (animal.py).
    - `+++ b/animal.py`:Indicates the new version of the file (animal.py).

    `@@ -12,5 +12,6 @@ def main()::`
    - This is the hunk header, specifying which lines are affected:
    - `-12,5`: In the old file, the changes start at line 12 and cover 5 lines.
    - `+12,6`: In the new file, the changes also start at line 12 but now cover 6 lines.
    - This tells us that one line was added.
    - The `def main():` line is not changed but is included in the diff to give you a sense of where in the code the modifications happened. 


