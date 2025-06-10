from django.urls import path
from .views import home_view, AboutPageView, Error404View

urlpatterns = [
    path("", home_view, name="home"),  # Page d'accueil
    path("about/", AboutPageView.as_view(), name="about"),
    path("error/", Error404View.as_view(), name="error"),
]

# from django.urls import path
# from .views import home_view, AboutPageView, list_view

# urlpatterns = [
#     # path("", HomePageView.as_view(), name="home"),
#     path("", home_view, name="home"),
#     path("list/", list_view, name="list"),
#     path("about/", AboutPageView.as_view(), name="about"),
   
# ]
