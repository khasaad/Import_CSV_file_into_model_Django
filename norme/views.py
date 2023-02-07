from django.http import JsonResponse
from django.views import View

from .models import Norme

# Create your views here.
class MyData(View):
    def get(self, request):
        data_list = list(Norme.objects.values())
        return JsonResponse(data_list, safe=False) 

class MyDataDetail(View):
    def get(self, request, pk):
        data_list = {"norme": list(Norme.objects.filter(pk=pk).values())}
        return JsonResponse(data_list, safe=False)  