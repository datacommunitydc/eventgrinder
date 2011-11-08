from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages

from account.utility import get_current_user, profile_required, get_current_profile, admin_required

from eventsite import site_required
from forms import AddLinkForm
from models import Link

@site_required        
def add(request):
	if request.method == 'POST':
		form=AddLinkForm(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.INFO, "Thank you for submitting a link!")
			return redirect('/')


	else:
		form=AddLinkForm()
	return(render_to_response('links/add.html', locals(), context_instance=RequestContext(request)))
	

@admin_required
def review(request):
	if request.method=='POST':
		link=Link.get_by_id(int(request.POST['id']))
		link.status=request.POST['action']
		link.put()

	approved_links=Link.all().filter('status =', 'approved')
	submitted_links=Link.all().filter('status =', 'submitted')
	return(render_to_response('links/review.html', locals(), context_instance=RequestContext(request)))