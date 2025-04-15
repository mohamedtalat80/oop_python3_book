class UserValidationError(Exception):
    def __init__(self, username: str, email: str, issues: dict):
        self.username = username
        self.email = email
        self.issues = issues  # تصحيح الإملاء
        message = "User validation error: " + "; ".join(f"{k}={v}" for k, v in issues.items())
        super().__init__(message)

    def suggested_fixes(self):
        fixes = []
        if "username" in self.issues:  # تصحيح التحقق
            fixes.append(f"Username '{self.username}' should be no more than 10 characters, no spaces.")
        if "email" in self.issues:  # تصحيح التحقق
            fixes.append(f"Email '{self.email}' should be in correct format (e.g., user@domain.com).")
        return fixes

class UserManager:
    def validate_user(self, username, email):
        issues = {}  # تصحيح الإملاء
        if len(username) > 10 or " " in username:
            issues["username"] = "username should be no more than 10 characters, no spaces"
        if "@" not in email or "." not in email.split("@")[-1]:  # تحقق أدق للـ email
            issues["email"] = "email should be in correct format (e.g., user@domain.com)"
        if issues:  # نقل التحقق لبرا
            raise UserValidationError(username, email, issues)
        return True

try:
    user_manager = UserManager()
    user_manager.validate_user("mohamed", "mohamed@gmail")  # الـ email غلط هنا
except UserValidationError as e:
    print(e)
    print("Suggested fixes:")
    for fix in e.suggested_fixes():  # تصحيح الاستدعاء
        print(f"- {fix}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")