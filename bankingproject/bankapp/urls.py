from django.urls import path, includefrom . import viewsfrom bankapp import viewsurlpatterns = [    path("",views.index,name="index"),    path('login/', views.login, name='login'),    path('register/', views.register, name='register'),    path('newpage/', views.newpage, name='newpage'),    path('login/newpage/', views.newpage, name='newpage'),    path('about/', views.about, name='about'),    path('about/about/', views.about, name='about'),    path('about/about/about/', views.about, name='about'),    # path('application_form/', views.application_form, name='application_form'),    path('form/', views.form, name='form'),    path('login/newpage/form/', views.form, name='form'),    path('submit/', views.submit, name='submit'),]