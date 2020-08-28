from django.urls import path, include
from . import views
# from newsletter_subscription.backend import ModelBackend
# from newsletter_subscription.urls import newsletter_subscriptions_urlpatterns


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('career/', views.career, name='career'),
    path('staffing/', views.staffing, name='staffing'),
    path('productdevelopment/', views.productdevelopment, name='productdevelopment'),
    path('projectmanagement/', views.projectmanagement, name='projectmanagement'),
    path('itconsulting/', views.itconsulting, name='itconsulting'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.successView, name='success'),
    # url(r'^newsletter/', include(newsletter_subscriptions_urlpatterns(backend=ModelBackend(Subscription),
    #     )),

]