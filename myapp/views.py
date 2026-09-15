from django.shortcuts import render, redirect
from .models import Complaint

def splash(request):
    return render(request, 'splash.html')

def home(request):
    return render(request, 'home.html')

# ... un complaint function keela irukkattum
def complaint(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile') or request.POST.get('phone')
        village = request.POST.get('village')
        category = request.POST.get('category')
        location = request.POST.get('location')
        photo = request.FILES.get('photo')
        petition_photo = request.FILES.get('petition_photo')

        Complaint.objects.create(
            name=name,
            mobile=mobile,
            phone=mobile,
            village=village,
            category=category,
            location=location,
            photo=photo,
            petition_photo=petition_photo
        )
        
        return redirect('/success/')
    
    return render(request, 'complaint.html')


def success(request):
    return render(request, 'success.html')

def status(request):
    complaint = None
    searched = False

    if request.method == 'POST':
        village = request.POST.get('village')
        mobile = request.POST.get('mobile')

        searched = True

        complaint = Complaint.objects.filter(
            village=village,
            mobile=mobile
        ).first()

    return render(request, 'status.html', {
        'complaint': complaint,
        'searched': searched
    })