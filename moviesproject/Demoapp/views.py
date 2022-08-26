from django.shortcuts import render
from Demoapp.models import Movie
from Demoapp.forms import MovieForm

# Create your views here.
def index_view(request):
    return render(request,'Demoapp/index.html')

def addmovie_view(request):
    formobj = MovieForm()
    if request.method == 'POST':
        formobj = MovieForm(request.POST)
        if formobj.is_valid():
            formobj.save()
        return render(request,'Demoapp/index.html')
    return render(request,'Demoapp/addmovie.html',{'fobj':formobj})

def movielist_view(request):
    movielistobj = Movie.objects.all()
    return render(request,'Demoapp/movielist.html',{'mlist':movielistobj})
