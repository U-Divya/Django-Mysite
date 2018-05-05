


from django.shortcuts import render,redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .models import Blog
from .forms import BlogForm

# Create your views here.
def index(request):

	var=Blog.objects.all().order_by('title')

	paginator=Paginator(var,3)
	page=request.GET.get('page')
	try:
		p=paginator.page(page)
	except PageNotAnInteger:
		p=paginator.page(1)
	except EmptyPage:
		p=paginator.page(paginator.num_pages)

	return render(request,'index.html',{'var':p})

def postform(request):
	form=BlogForm(request.POST)				#from from class is BlogFrom and request.POST is from corresponding html file
	if form.is_valid():
		post=form.save(commit=False)
		post.published="2018-01-01"
		post.save()
		return redirect('/blogging/')
	return render(request,'postform.html',{'form':form})
