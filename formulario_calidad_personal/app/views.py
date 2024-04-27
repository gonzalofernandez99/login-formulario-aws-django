from django.shortcuts import render
from .forms import LoginForm, DataForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Process login logic here
            # You can use Cognito AWS SDK to handle authentication
            # Example: authenticate_user(form.cleaned_data['username'], form.cleaned_data['password'])
            return render(request, 'form.html')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def form(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            # Process form data and save it to the SQL database
            # Example: save_data(form.cleaned_data['field1'], form.cleaned_data['field2'])
            return render(request, 'success.html')
    else:
        form = DataForm()
    return render(request, 'form.html', {'form': form})