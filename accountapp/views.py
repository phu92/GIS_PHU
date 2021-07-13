from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# # Create your views here.
# def hello_world(request):
#     return render(request, 'accountapp/hello_world.html')
from django.urls import reverse

from accountapp.models import NewModel


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
