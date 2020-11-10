from django.shortcuts import render, redirect
from .forms import BiodataForm, LayoutForm
from .models import Biodata, Layouting

# Create your views here.
def index(request):
    # Store all the data
    form = LayoutForm()
    data = Biodata.objects.all()

    # Initiate the variable to pass into the query set parameter
    # Also to prevent error at the initiate rendering
    search = ''
    groupby = 'All'
    sorting = 'Ascending'

    # Make sure that the request is POST
    if request.method == 'POST':
        form = LayoutForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            groupby = form.cleaned_data['groupby']
            sorting = form.cleaned_data['sorting']

    # Condition to satisfy the user wish
    if groupby != 'All':
        data = data.filter(classroom = groupby).filter(nickname__icontains = '%s' % search)
        if sorting == 'Ascending':
            data = data.order_by('nickname')
        else:
            data = data.order_by('-nickname')
    else:
        data = data.filter(nickname__icontains = '%s' % search)
        if sorting == 'Ascending':
            data = data.order_by('nickname')
        else:
            data = data.order_by('-nickname')
            
    content = {
        'data' : data,
        'form' : form,
    }
    return render(request, 'restAPI/list.html', content)

def inputUser(request):
    form = BiodataForm()
    if request.method == 'POST':
        form = BiodataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    content = {
        'data' : form
    }
    return render(request, 'restAPI/input.html', content)