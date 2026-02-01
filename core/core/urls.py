"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from home.views import *
from vege.views import *

#For Media Files
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # type: ignore

urlpatterns = [
    path('', home, name='home'),
    path('receipes/', receipes, name='receipes'),
    path('delete_receipe/<receipe_id>/', delete_receipe, name='delete_receipe'),
    path('update_receipe/<receipe_id>/', update_receipe, name='update_receipe'),
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('logout/', logout_page, name='logout_page'),

    path('students/',get_students, name='get_students'),

    #Here "name" is used for dinamic URL in application
    # how to use in html : {% url 'see_marks' id %} : set url dynamic if change url it auto reflec here
    path('see-marks/<student_id>',see_marks, name='see_marks'),

    #sample pages
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),
    path('send-email/', send_email, name='send_email'),
]

# Serving Media Files in Development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()