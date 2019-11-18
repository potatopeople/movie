import random
from .token_verify import TokenVerify

class Tokens:
    strs = r'1234567890-=qwertyuiop[];lkjhgfdsazxcvbnm,./!@#$%^&*()_+<>?:{}'
    tokens = list
    username = str

    def __init__(self, username):
        self.username = username

    @property
    def create_token(self):
        self.tokens = random.sample(self.strs, 30)
        for i, user in enumerate(self.username):
            if i + 2 <= 20:
                self.tokens.insert(i + i + i, user)
            else:
                self.tokens.append(user)
        tokens = ''.join(self.tokens)
        self.save_token(tokens)
        return tokens

    def save_token(self,token):
        userObj = {'username': self.username,'token': token}
        TokenVerify(userObj)
