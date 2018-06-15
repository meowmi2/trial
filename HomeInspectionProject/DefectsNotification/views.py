from django.shortcuts import render
from django.http import HttpResponse
#from DefectsNotification import forms
from DefectsNotification.forms import AddressForm
from django.views.generic import View, TemplateView
# Create your views here.


class IndexView(TemplateView):
    template_name = 'defects_notification/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['insert'] = 'hello world'
        return context


def AddressFormView(request):
    form = AddressForm()

    if request.method == 'POST':
        form = AddressForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
        else:
            print('form invalid')

    return render(request, 'DefectsNotification/summary.html', {'form':form} )
