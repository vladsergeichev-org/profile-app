import hashlib
import os
from dataclasses import dataclass
from typing import Tuple
from config import PWD_SECRET as SALT


@dataclass
class PasswordHelper:
    password_hash: bytes = None
    salt: bytes = None

    def verify(self, password: str) -> bool:
        if self.password_hash is None or self.salt is None:
            return False
        return self.password_hash == self.hash(password)

    def hash(self, password: str) -> bytes:
        if self.salt is None:
            self.salt = os.urandom(16)
        return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), self.salt, 100000)

    def create(self, password: str) -> Tuple[bytes, bytes]:
        return self.hash(password), self.salt


def test_password_helper():
    passw = "1234"
    password_helper = PasswordHelper()
    password_hash = password_helper.hash(passw)
    password_hash_2 = password_helper.hash(passw)
    assert password_hash_2 == password_hash


def test_password_helper_verify():
    passw = "1234"
    password_helper = PasswordHelper()
    password_hash = password_helper.hash(passw)
    password_helper_2 = PasswordHelper(password_hash)
    assert password_helper_2.verify(passw)
