from django.shortcuts import render
from django.shortcuts import redirect
from .forms import UploadImageForm
from django.core.files.storage import FileSystemStorage
# Create your views here.
def first_view(request):
    return render(request, 'opencv_webapp/first_view.html', {})
#first view hamsoo -> html definition

def uimage(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            f = {'form': form, 'uploaded_file_url': uploaded_file_url}
            return render(request, 'opencv_webapp/uimage.html', f)
    else:
        form = UploadImageForm()
        return render(request, 'opencv_webapp/uimage.html', {'form': form})
