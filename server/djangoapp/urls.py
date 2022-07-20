from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
app_name = 'djangoapp'
urlpatterns = [
   
    path(route='about',view=views.about,name='about'),
    path(route='contact',view=views.contact,name='contact'),
    path('logout/',view=views.logout_request,name='logout'),
    path('login/',view=views.login_request,name='login'),
    path('registration/', view=views.registration_request, name='registration'),
    path(route='', view=views.get_dealerships, name='index'),
    path('review/<int:id>/',view=views.add_review,name='add_review'),
    path('dealer/<int:id>/', views.get_dealer_details, name='dealer_details'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)