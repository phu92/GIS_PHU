from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        #입력창 fields
        self.fields['username'].disabled = True