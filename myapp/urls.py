from django.urls import path
from .views import home,about,team,testimonial,service,contact,error_404,feature,cars,blog

urlpatterns = [
    path('', home,name='home-as'),
    path('about/', about,name='about-as'),
    path('team/', team,name='team-as'),
    path('testimonial/', testimonial,name='testimonial-as'),
    path('service/', service,name='service-as'),
    path('contact/', contact,name='contact-as'),
    path('feature/', feature,name='feature-as'),
    path('cars/', cars,name='cars-as'),
    path('blog/', blog,name='blog-as'),
    path('error_404/', error_404,name='error_404-as'),
]
