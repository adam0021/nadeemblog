from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from blog.models import *
from .forms import PostForm,commentform


# Create your views here.
#def home(request):
    #return HttpResponse("<h1> hello</h1>")


def home(request):
    q=Post.objects.all().order_by("-timestamp")
    context={
    "q":q,
    }


    return render(request,'home.html',context)








def post_list(request):
    queryset=Post.objects.all().order_by("-timestamp")
    context={
    "queryset":queryset,
    "title":"list"


    }
    return render(request,"base.html",context)




def post_detail(request,id):
    instance=get_object_or_404(Post,id=id)
    context={
    "title":"Detail",
    "instance":instance
    }
    return render(request,"post_detail.html",context)



def post_create(request):
    form=PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request,"Not successfuly created")
    context={
    "form":form
    }
    return render(request,'post_form.html',context)


def post_update(request,id=None):
    instance=get_object_or_404(Post,id=id)

    form=PostForm(request.POST or None,request.FILES or None,instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    context={

    "form":form,
    "instance":instance
    }


    return render(request,'post_form.html',context)


def post_delete(request,id=None):
        instance=get_object_or_404(Post,id=id)
        instance.delete()
        return redirect("/post")



def comment(request):
	comm=comment.objects.all()
	return render(request,'post_detail.html',{'comm':comm})




def add_comment(request,id):
	post=get_object_or_404(Post,id=id)
	if request.method=='POST':
		form=commentform(request.POST)
		if form.is_valid():
			comment=form.save(commit=False)
			comment.post=post
			comment.save()

			return redirect('/post',id=post.id)
	else:
  		form=commentform()
  		return render(request,'add_comment.html',{'form':form})








