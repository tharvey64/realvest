from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	url(r'^all$', views.show_all, name="Property List"),
	url(r'^single/([0-9]{12})$', views.single, name="Property List"),
	url(r'^seed$', views.edit_prop, name="Property Editing"),
	url(r'^seed$', views.seed_prop, name="Property Seeding"),
]
