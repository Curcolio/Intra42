from django.shortcuts import render, get_object_or_404

def index_view(request):
    return render(request, 'activities/index.html', {'sess' : request.session})
