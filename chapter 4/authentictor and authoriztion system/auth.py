import hashlib
class User :
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_logged_in = False
    
    def encrypt_password(self,password :str) -> str:
        hash_string=(password+self.username)
        return hashlib.sha256(hash_string.encode()).hexdigest()
    def check_password(self,password:str) -> bool:
        password_encrypted = self.encrypt_password(password)
        return self.password == password_encrypted
class AuthException(Exception):
    def __init__(self,username :str,user=None):
        super().__init__(username,user  )
        self.username = username
        self.user = user
class UsernameAlreadyExists(AuthException):
    pass
class PasswordTooShort(AuthException):
    pass
class InvalidUsername(AuthException):
    pass
class InvalidPassword(AuthException):
    pass
class NotLoggedInError(AuthException):
    pass
class NotPermittedError(AuthException):
    pass
class PermissionError(Exception):
    pass
class Authenticator:
    def __init__(self):
        self.users = {}
    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExists(f"Username '{username}' already exists.")
        if len(password) < 8:
            raise PasswordTooShort("Password must be at least 8 characters long.")
        self.users[username] = User(username, password)
    def login(self,username,password):
        try:
            user=self.users[username]
        except KeyError:
            raise InvalidUsername(username)
        if not user.check_password(password):
            raise InvalidPassword(username,user)
        user.is_logged_in=True
        return True
    def is_logged_in(self,username):
        try:
            user=self.users[username]
        except KeyError:
            raise InvalidUsername(username)
        return user.is_logged_in
    def logout(self,username):
        try:
            user=self.users[username]
        except KeyError:
            raise InvalidUsername(username)
        user.is_logged_in=False
        return True
class Authorizer:
    def __init__(self,authenticator:Authenticator):
        self.authenticator=authenticator
        self.permissions={}
    def add_permission(self,permission_name):
        try:
            prem_set=self.permissions[permission_name]
        except KeyError:
            self.permissions[permission_name]=set()
        else:
            raise PermissionError(f"Permission '{permission_name}' already exists.")
    def permit_user(self,username,permission_name):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(f"User '{username}' is not logged in.")
        try:
            prem_set=self.permissions[permission_name]
        except KeyError:
            raise PermissionError(f"Permission '{permission_name}' does not exist.")
        prem_set.add(username)
    def check_permission(self,username,permission_name):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(f"User '{username}' is not logged in.")
        try:
            prem_set=self.permissions[permission_name]
        except KeyError:
            raise PermissionError(f"Permission '{permission_name}' does not exist.")
        if username not in prem_set:
            raise NotPermittedError(f"User '{username}' does not have permission '{permission_name}'.")
        return True
    def revoke_permission(self,username,permission_name):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(f"User '{username}' is not logged in.")
        try:
            prem_set=self.permissions[permission_name]
        except KeyError:    
            raise PermissionError(f"Permission '{permission_name}' does not exist.")
        if username not in prem_set:    
            raise NotPermittedError(f"User '{username}' does not have permission '{permission_name}'.")
        prem_set.remove(username)
        return True
    def __repr__(self):
            return f"Authorizer(permissions={self.permissions})"

authenticator=Authenticator()
autherizer=Authorizer(authenticator)
