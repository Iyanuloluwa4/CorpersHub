from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Connect


class ConnectView (ListView):
    login_url = reverse_lazy('login')
    template_name = 'connect.html'
    model = Connect
    context_object_name = 'avaialable_jobs'

    def get_context_data(self, **kwargs):
        context = super(ConnectView, self).get_context_data(**kwargs)
        context['available_jobs'] = Connect.objects.all().order_by('client')
        return context

    # Queryset for class
    #def get_queryset(self):
     #   return AbstractModel.objects(
          #username=self.request.user
      #  )
