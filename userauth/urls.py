from django.urls import path


from .views import signin,signup,dash,signout
urlpatterns= [
  path('signup/',signup),
  path('signin/',signin,name='signin'),
  path('dash/',dash,name='dash'),
  path('signout/',signout,name='signout')
]