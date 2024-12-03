from django.shortcuts import redirect, render
from . models import Profile, Movie
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect('profile_list')
    return render(request, 'index.html')

@login_required(login_url='login')
def profile_list(request):
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles, 
    }
    return render(request, 'profileList.html', context)

@login_required(login_url='login')
def profile_create(request):
    if request.method == 'POST':
        profile_name = request.POST['name']
        age_limit = request.POST['age_limit']
        profile = Profile.objects.create(user=request.user, name=profile_name, age_limit=age_limit)
        profile.save()
        return redirect('profile_list')
    return render(request, 'profileCreate.html')

@login_required(login_url='login')
def movie_list(request, profile_id):
    profile = Profile.objects.get(uuid=profile_id)
    movies = Movie.objects.filter(age_limit=profile.age_limit)
    context = {
        'movies': movies,
    }
    return render(request, 'movieList.html',context)

@login_required(login_url='login')
def movie_detail(request, movie_id):
    try:
        movie = Movie.objects.get(uuid=movie_id)
        context = {
            'movie': movie,
        }
        return render(request, 'movieDetail.html', context)
    except Movie.DoesNotExist:
        return redirect('profile_list')

@login_required(login_url='login')    
def movieplay(request, movie_id):
    try:
        movie = Movie.objects.get(uuid=movie_id)  
        movie = movie.video.values()
        context = {
                'movie':list(movie)
            }

        return render(request, 'playmovie.html', context)
    except Movie.DoesNotExist:
        return redirect('profile_list')