# Environment
Add 
```
/mvenv/
```
To .gitignore

Begin by typing
```
python.exe -m pip install --upgrade pip
``` 

This project uses venvs. 
Clone the project from GITHUB.
To create the venv in the project folder (Windows), type

```
py -m venv myenv
```
To activate the project (Windows), open a terminal window in VSCode and type

```
\myenv\Scripts\activate.ps1
```

To record the requirements from the original repo, type 
```
pip freeze > requirements.txt
```
To install the requirements, type 
```
pip install -r requirements.txt
```