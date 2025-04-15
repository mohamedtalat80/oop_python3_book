# Custom Exceptions in Python

This project explains how to define and use custom exceptions in Python for precise error handling.

## Why Use Custom Exceptions?
To specify errors clearly in your code, making it easier for developers to handle them differently.

## When to Use Custom Exceptions?
When building a library or API and need to provide specific exceptions for other programmers to handle.

## How to Use Custom Exceptions?
Create a class that inherits from `Exception` (or a similar exception), add data if needed, and raise it when the error occurs.

## Key Notes
- Inherit from `Exception` for standard custom exceptions, not `BaseException`, unless stopping the program is intended.
- Custom exceptions should clarify the error and suggest fixes for the client programmer.
- They are most useful in libraries/APIs to provide distinct error handling.

## Code Examples
Check the examples in the file: [custom_exceptions.py](src/custom_exceptions.py)
# Case Study
## analysis phase
user(name,password)
Authorizor(UserObject)
Authunticator(UserObject)
## Design phase
### Userclass
#### Attr
- username
- password
- islogged_in 
#### Methods 
- check password () --> check if the pssword of the user is valid or not 
- encrypt password() --> for encripting the passwword to prevent secuirty issues 
### AuthExceptionclass
#### Attr
- username
- password
- user object  
#### Methods 
+ class UsernameAlreadyExists -> to raise an exception if the username the user enter is exist
+ class PasswordTooShort -> to raise an exception if the user enter short password 
+ class InvalidUsername
+ class InvalidPassword
+ class NotLoggedInError
+ class NotPermittedError
### Authenticator
#### Attr
- user object  
#### Methods 
+ add user (username,password) -> to add user to User class 
+ login(username, password )-> allow user to log in into the system
+ logout(username) -> allow user to logout
+ is_loged_in (username) -> check if the user is loggedin or not
### Autherizor
#### Attr
- authenticator object 
- permissions {} -> dict
#### Methods 
+ add_permaission(prem_name) -> create a new permission, unless it already exists
+ premit_user() -> add a username to a permission, unless either the permission or the username doesn't yet exist 
+ check_permission(perm_name, username) -. check if the user is lخgged in the authenticator and also have the permission 
revoke_permission(username,permission_name) -> revokes the user permission 
### class PermissionError(Exception) -> raise any error that related of permission if the permaission is already exist or it not existed 
----------------------------------------------------------------------------------------------------------------------------------
## editor.py
### editior class 
#### Attr
- username
- menu_map(login,test,change,quit)-> dict 
#### Methods 
+ login() -> make the user enter a username and password and authenticate the user inputs  then log him in 
+ is_permitted() -> check the permissions of the user 
+ test() -> allow the user if he has  the permission to test the program
+ change() -> allow the user if he has  the permission to change the program
+ quit () -> make the user exits the program 
+ menu () let the user chose from a menu a the command that he want to excute 