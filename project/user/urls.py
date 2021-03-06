from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (
	logout, password_reset, 
	password_reset_done, 
	password_reset_confirm,
	password_reset_complete
	)


urlpatterns = [
	url(r'^$', views.landing_page, name="login"),
	url(r'^register$', views.register, name="register"),
	url(r'^login$', views.home, name="home"),
	url(r'^logout$', logout, {'template_name':'user/logout.html'}),
	url(r'^account$', views.account_private, name="private_account"),
	url(r'^account/edit$', views.account_edit, name="edit_account"),
	url(r'^account/change-password$', views.change_password, name="change_password"),
	url(r'^account/reset-password$', password_reset, name='password_reset'),
	url(r'^account/reset-password/done$', password_reset_done, name='password_reset_done'),
	url(r'^account/reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)﻿$', password_reset_confirm, name='password_reset_confirm'),
	url(r'^account/reset-password/complete﻿$', password_reset_complete, name='password_reset_complete'),
	


]