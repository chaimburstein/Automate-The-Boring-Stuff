# Practice Questions Chapter 2 - Flow Control

## 1. What are the two values of Boolean data type? How do you write them?
  * True, False
  * Always use capital letters at beggining of True and False

## 2. What are the three Boolean Operators
  1. and - will only == True if both Boolean expressions or values are True
  2. or - will == True if one Boolean expression or value is true
  3. not - will flip the Bloolean value: not True evaluates to False

## 3. Write out truth tables of each Boolean operator.

### and
|Expression|Evaluates to...|
|---|---|
|True and True|True|
|True and False|False|
|False and True|False|
|False and False|False|

### or
|Expression|Evaluates to...|
|---|---|
|True or True|True|
|True or False|True|
|False or True|True|
|False or False |False|

### not
|Expression|Evaluates to...|
|not True | False |
|not not True | True|
|not not not True | False|
|not False| True |

## 4 What do the follwing expressions evaluate to?
|Expression| Evaluates to...|
|---|---|
|(5>4) and (3==5)| False|
| not (5>4) | False |
|(5>4) or (3==5) | True|
|not((5>4) or (3==5)) | False |
|(True and True) and (True == False) | False|
|(not False) or (not True) | True|
