from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class PasswordHasher:
    def __init__(self, password):
        self.password = password.encode('utf-8')

    def generate_hash(self):
        return pwd_context.hash(self.password)

    def verify_password(self, hashed_password):
        return pwd_context.verify(self.password, hashed_password)

if __name__ == "__main__":
    hasher = PasswordHasher("mysecretpassword")
    hashed_password = hasher.generate_hash()
    print(hashed_password)
