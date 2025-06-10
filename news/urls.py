from django.urls import path
from .views import news_view, news_detail, news_create, news_update, news_delete 
# HomePageView
urlpatterns = [
    # mode class
    # path("news/", NewsPageView.as_view(), name="news"),
    # mode fonction
    path("news/", news_view, name="news"),
    # path("home/", HomePageView.as_view(), name="home"),
   # link/function name views/url templates
    path("news/details/<int:id>/", news_detail, name="news_detail"),
    path("news/create/", news_create, name="news_create"),
    path("news/<int:id>/update/", news_update, name="news_update"),
    path("news/<int:id>/delete/", news_delete, name="news_delete"),

]