from django.shortcuts import redirect

def OnlySuperUser(view_func):
	def wrapper_function(request,*args,**kwargs):
		if request.user.is_superuser:
			return view_func(request,*args,**kwargs)

		else : 
			return redirect('/')
	return wrapper_function