from django.urls import URLPattern, path
from admin_app import views

urlpatterns = [
    path('', views.authn),
    path('home/', views.ad_home),
    path('home/update/<int:id>', views.ad_home_update),
    path('home/delete/<int:id>', views.ad_home_delete),
    path('resume/', views.ad_resume),
    path('education/', views.ad_education),
    path('education/update/<int:id>', views.ad_education_update),
    path('education/delete/<int:id>', views.ad_education_delete),
    path('intern/', views.ad_intern),
    path('intern/update/<int:id>', views.ad_intern_update),
    path('intern/delete/<int:id>', views.ad_intern_delete),
    path('skill/', views.ad_skill),
    path('skill/update/<int:id>', views.ad_skill_update),
    path('skill/delete/<int:id>', views.ad_skill_delete),
    path('query/', views.ad_query),
    path('query/delete/<int:id>', views.ad_query_delete),
    path('work/', views.ad_work),
]