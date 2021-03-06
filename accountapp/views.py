from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# # Create your views here.

from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.forms import AccountCreationForm
from accountapp.models import NewModel
from accountapp.templates.accountapp.decorators import account_ownership_required
from articleapp.models import Article

#class based view
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('articleapp:list')
    #reverse 그대로 사용시 에러 발생, 함수와 클래스의 불러오는 방식이 다르기 때문
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 20

    def get_context_data(self, **kwargs):
        article_list = Article.objects.filter(writer=self.object)
        return super().get_context_data(object_list=article_list,
                                        **kwargs)


has_ownership = [login_required, account_ownership_required]

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView): #crete view 참조
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    #success_url = reverse_lazy('accountapp:detail') #아직 사용 불가
    template_name = 'accountapp/update.html'

    def get_success_url(self):#self = target_profile
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk})

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'#유저 정보에 접근하기 위해
    success_url = reverse_lazy('articleapp:list')
    template_name = 'accountapp/delete.html'