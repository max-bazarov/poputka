import bcrypt


def hash_password(password: str) -> bytes:
    '''
    The bcrypt hashing algorithm incorporates the salt value into
    the resulting hashed password. When you use bcrypt.hashpw() to hash
    a password, it combines the password bytes with the salt and performs
    multiple rounds of hashing to generate the final hash.
    The salt is stored together with the hashed password.
    '''
    encoded_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(encoded_password, salt)


def check_password(password: str, password_from_db: str) -> bool:
    '''
    When you want to verify a password using bcrypt.checkpw(),
    it extracts the salt from the stored hashed password and uses
    it to hash the provided password.
    Then, it compares the generated hash with the stored hash.
    If the two hashes match, it means that the passwords are the same.
    '''
    password = password.encode('utf-8')
    return bcrypt.checkpw(password, password_from_db)
