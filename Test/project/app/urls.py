from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update/<int:id>', views.update ,name='update'),
    path('update_tax', views.updateTax ,name='updatetax'),
    path('tax_less_than', views.lessThan, name = 'lessthan10k'),
    path('tax_great_than', views.greatThan, name = 'greatthan10k'),
    path('change_user_tax', views.changeUserTax, name = 'changeusertax')
]