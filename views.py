from django.http import HttpResponse
from django.template import loader
from .models import BikeModel

def bikemodel_list(request):
    bikemodels = BikeModel.objects.all().values()
    template = loader.get_template('bikemodel_list.html')
    context = {
        'bikemodels': bikemodels,
    }
    return HttpResponse(template.render(context, request))
  
def bikemodel_detail(request, id):
    bikemodel = BikeModel.objects.get(id=id)
    template = loader.get_template('bikemodel_detail.html')
    context = {
        'bikemodel': bikemodel,
    }
    return HttpResponse(template.render(context, request))
