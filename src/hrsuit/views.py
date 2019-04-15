from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect


def index_view(request):
	return render(request,'index.html',{})