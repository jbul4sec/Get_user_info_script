# Script for retrieving details of all users from computer

## Usage
Go to your working directory. Copy main.py to your working directory. Then run command:
```commandline
python main.py
```
In case if 'python main.py' doesn't work use:
```commandline
python3 main.py
```
## Output to console
Output will be like:
```commandline
--->     [v] Details for user USERNAME were written to file user_USERNAME.txt. Open it with notepad++
```
## Expected results
- every user info will be written to a file: current_working_dir/user_USERNAME.txt where USERNAME is name of user.
- to escape problems with encoding on Windows use Notepad++.
- tested for Windows, other OS not tested yet.
