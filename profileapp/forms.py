from django.forms import ModelForm

from profileapp.models import Profile

class ProfileCreationForm(ModelForm):
    class Meta:#내부 클래스
        model = Profile
        fields = ['image', 'nickname', 'message']