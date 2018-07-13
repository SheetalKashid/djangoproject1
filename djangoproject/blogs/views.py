from django.shortcuts import render
from django.http import HttpResponse
from .models import blogs
from django.template import loader
# Create your views here.
def index(request):
	#return HttpResponse("Hello From Blogs!!!")

	Blogs=blogs.objects.all()
	template=loader.get_template("blogs/index.html")
	context={
		'title':'Latest Blogs',
		'blogs':Blogs
		}
	return HttpResponse(template.render(context))
#	return render(request,'blogs/index.html',context)
