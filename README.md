# *envfileparser*
___
This package is as simple as possible to get variables from .env files or files with a similar structure.

![](https://img.shields.io/pypi/v/envfileparser?style=for-the-badge)
![](https://img.shields.io/badge/covarage-97%25-green?style=for-the-badge&logo=appveyor)
![](https://img.shields.io/badge/license-GPLv3-blue?style=for-the-badge&logo=appveyor)
![](https://img.shields.io/pypi/pyversions/envfileparser?style=for-the-badge)
### Description
> The package 
> has no dependencies and works with files 
> located in the same directory as the file from 
> which the functions of this package were called. 
> 
> Function ```get_env()``` takes the name of the target variable 
> as a string and an optional second parameter - 
> the path to the file. After that, the function returns the 
> value of the variable also as a string.
> 
> Function ```get_envs()``` accepts a sequence of variable 
> names as a string, and also an optional 
> parameter-the path to the file. 
> This function returns a list of strings 
> that are the values of the desired variables.
> 
> By default, ```.env``` is specified 
> as the path. Empty lines and lines without 
> the ```'='``` character are skipped. 
> In addition, commenting with a prefix of the ```'#'```
> character is supported.In the event that 
> the specified variable is 
> missing or the desired file cannot be found, 
> the corresponding exceptions are thrown.
## Getting started
___
#### Install [envfileparser](https://pypi.org/project/envfileparser/) from [PyPi](https://pypi.org/) with pip: `pip install envfileparser`
### Usage example:
```python
from envfileparser import get_env, get_envs

CONST_ONE = get_env('CONST1')
CONST_TWO = get_env('CONST2', file_path='configs/.env')

variables = get_envs('VAR1', 'VAR2', 'VAR3')
v1, v2, v3 = variables[0], variables[1], variables[2]
```
#### Correct .env file example:
```env
# Service token.
API_TOKEN = f3u12yf36f12f418449go3294g238

PORT = 3417
IP = 127.0.0.1 # loopback

USER = 'ADMIN'
PASSWORD="12345678"
```
___
*If your value contains the " # "character, 
then be sure to put it in quotation marks-otherwise 
the parser will take all subsequent characters (including the" # " character) as a comment:*
The .env file:
```conf
VAR1 = envfile#parser
VAR2 = "envfile#parser"
```
Python code:
```python
from envfileparser import get_env, get_envs

print(*get_envs('VAR1', 'VAR2'), sep='\n')
```
Output:
```
envfile
envfile#parser
```
___
**New version ``0.0.7``:** 
- Fixed problems with comments.
- Removing spaces in the right and left side of the values.
