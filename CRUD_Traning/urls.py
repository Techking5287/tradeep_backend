from django.contrib import admin  
from django.urls import path  
from users import views
from graphene_django.views import GraphQLView

urlpatterns = [  
    path('register', views.register),  
    path('login', views.login),  
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('admin/', admin.site.urls),  
    # path('emp', views.emp),  
    # path('show',views.show),  
    # path('edit/<int:id>', views.edit),  
    # path('update/<int:id>', views.update),  
    # path('delete/<int:id>', views.destroy),
    # url(r'^api-auth/', include('rest_framework.urls'))
]  