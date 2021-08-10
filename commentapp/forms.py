from django.forms import ModelForm

from commentapp.models import Comment


class CommentCreationForm(ModelForm):
    class Meta:#메타 데이터
        model = Comment
        fields = ['content']