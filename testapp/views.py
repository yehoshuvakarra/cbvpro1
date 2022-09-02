from django.views.generic import View,TemplateView
from django.http import HttpResponse

# Create your views here.

class HelloWorldView(View):
    def get(self,request):
        return HttpResponse('<h1>This is from class based view</h>')
#to return template
class HelloWorldTemplateView(TemplateView):
    template_name = 'testapp/results.html'

#to return tepmlates with context
class HelloWorldTemplateContext(TemplateView):
    template_name = 'testapp/info.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        #why super class
        #we are calling super classs parent class get_context_data
        context['name']='jashuva'
        context['subject']='python'
        context['marks']=100
        return context
