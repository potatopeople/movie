class UserIntro:

    username = 'username'
    password = 'passwords'

    @property
    def usernames(self):
        return UserIntro.username

    @property
    def passwords(self):
        return UserIntro.password