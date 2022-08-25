from django.shortcuts import render

# Create your views here.
def homepage_view(request):
    return render(request,'Demoapp/output.html')

def me_view(request):
    me1 = "pretty"
    me2 = "sundari!!"
    me3 = "beautyfull"

    my_dict={'m1':me1, 'm2':me2, 'm3':me3}
    return render(request,'Demoapp/me.html',my_dict)

def mine_view(request):
        mine1 = "yashubabyyy"
        mine2 = "loveee"
        mine3 = "beautyfull"

        my_dict={'m1':mine1, 'm2':mine2, 'm3':mine3}
        return render(request,'Demoapp/mine.html',my_dict)

def food_view(request):
            food1 = "yummyyy"
            food2 = "tastyyy"
            food3 = "avdla aplyala !!!"

            my_dict={'m1':food1, 'm2':food2, 'm3':food3}
            return render(request,'Demoapp/food.html',my_dict)
