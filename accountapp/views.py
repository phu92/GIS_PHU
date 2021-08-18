from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# # Create your views here.
# def hello_world(request):
#     return render(request, 'accountapp/hello_world.html')
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.forms import AccountCreationForm
from accountapp.models import NewModel
from accountapp.templates.accountapp.decorators import account_ownership_required
from articleapp.models import Article


@login_required
def hello_world(request):
        if request.method == "POST":

            temp = request.POST.get('input_text')

            new_model = NewModel()
            new_model.text = temp  # temp의 값을 객체 변수명에 저장
            new_model.save()  # DB에저장
            # 절대 주소 대신 라우터 재연결 하게
            return HttpResponseRedirect(reverse('accountapp:hello_world'))
        else:
            data_list = NewModel.objects.all()
            return render(request, 'accountapp/hello_world.html',
                          context={'data_list': data_list})

#class based view
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
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
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'