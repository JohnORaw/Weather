# Environment
Add 
```
/mvenv/
```
To .gitignore to prevent the myenv folder from synching to GITHUB
 
To update before beginning, type 
```
python.exe -m pip install --upgrade pip
``` 

This project used venvs, if you want to use PIP, no choice anymore!. 
Clone the project from GITHUB.
To create the venv in the project folder (Windows), type

```
py -m venv myenv
```
To activate the project (Windows), open a terminal window in VSCode and type

```
\myenv\Scripts\activate.ps1
```

To install the requirements, type 
```
pip install -r requirements.txt
```

If the requirements change, to record the requirements from the repo, type 
```
pip freeze > requirements.txt
```