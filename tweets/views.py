from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin


class TweetCreateView(LoginRequiredMixin,FormUserNeededMixin, CreateView):
    #model = Tweet
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    #success_url = '/tweet/'

class TweetUpdateView(LoginRequiredMixin,UserOwnerMixin, UpdateView):
    model = Tweet
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    success_url = '/tweet/'
    login_url = '/admin/'


class TweetDeleteView(LoginRequiredMixin,UserOwnerMixin, DeleteView):
    model = Tweet
    template_name = 'tweets/delete_confirm.html'
    success_url =  reverse_lazy("tweet:list")
    login_url = '/admin/'



class TweetListView(ListView):

    template_name = 'tweets/list_view.html'
    context_object_name = 'tweets'

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get("q",None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs






class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    template_name = 'tweets/detail_view.html'
    context_object_name = 'tweet'





# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     context = {
#         'object_list' : queryset
#     }
#     return render(request,'tweets/list_view.html',context)

# def tweet_detail_view(request, id=1):
#     obj = Tweet.objects.get(id=id)
#     context = {
#         'object': obj
#     }
#     return render(request,'tweets/detail_view.html',context)
