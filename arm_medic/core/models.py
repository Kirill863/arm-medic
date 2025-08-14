from accounts.models import User as AccountUser

class User(AccountUser):
    class Meta:
        proxy = True