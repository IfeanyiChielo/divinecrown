# from django.urls import path
# from .views import HomePageView, AboutPageView, CreatepostPageView

# urlpatterns = [
#     path('', HomePageView.as_view (), name = 'home'),
#     path('about/', AboutPageView.as_view (), name = 'about'),
#     path('createpost/', CreatepostPageView.as_view (), name = 'createpost'),
# ]

from django.urls import path
from .views import index, Basep_view, register, user_login, user_logout, special,dashboard_with_pivot, pivot_data, soapprod_list, soapprod_form, soapprod_delete
# from .views import show, edit, destroy, emp, update
from . import views
from .views import creamprod_list, appindex, creamprod_form, shop,creamprod_delete,staffrec_list, staffrec_form, staffrec_delete, soapsales_list, soapsales_form, soapsales_delete, creamsales_list, creamsales_form, creamsales_delete
#from .views import HomePageView, Nameview_view

urlpatterns = [
    path('', index, name = 'index'),
    # path('namev/', Namev_view, name = 'namev'),
    path('shop/', shop, name = 'shop'),
    path('appindex/', appindex, name = 'appindex'),
    path('basep/', Basep_view, name = 'basep'),
    path('registration/', register, name = 'registration'),
    path('login/', user_login, name = 'login'), 
    path('logout/', user_logout, name = 'logout'), 
    path('special/', special, name = 'special'),
    path('data/', pivot_data, name='pivot_data'),
    path('dashboard_with_pivot/', dashboard_with_pivot, name='dashboard_with_pivot'), 

    path('soapprod_inset/', soapprod_form,name='soapprod_insert'),
    path('<int:id>/',soapprod_form, name='soapprod_update'), 
    path('<id>/delete/',soapprod_delete,name='soapprod_delete'),
    path('lists/',soapprod_list,name='soapprod_list'),
    path('creamprod_inset/', creamprod_form,name='creamprod_insert'),
    path('cream/<int:id>/', creamprod_form, name='creamprod_update'), 
    path('delete/<int:id>/', creamprod_delete, name='creamprod_delete'),
    path('listc/', creamprod_list,name='cream/creamprod_list'),
    # path('create_view/', create_view, name = 'create_view'),
    # path('list_view/', list_view, name = 'list_view'),
    # path('<id>/delete/', delete_view, name='delete_view'),
    # path('<id>/', detail_view, name = 'detail_view'), 
    # path('<id>/update/', update_view, name = 'update_view'),
    # path('<id>/delete/', delete_view, name='delete_view'),
    path('staffrec_insert/', staffrec_form,name='staff/staffrec_insert'),
    path('staff/<int:staff_id>/',staffrec_form, name='staff/staffrec_update'), 
    path('staff/<staff_id>/delete/',staffrec_delete,name='staff/staffrec_delete'),
    path('listst/', staffrec_list,name='staff/staffrec_list'),
    path('soapsales_insert/', soapsales_form,name='soapsales/soapsales_insert'),
    path('soapsales/<int:id>/',soapsales_form, name='soapsales/soapsales_update'), 
    path('soapsales/<id>/delete/',soapsales_delete,name='soapsales/soapsales_delete'),
    path('listss/', soapsales_list,name='soapsales/soapsales_list'),
    path('creamsales_insert/', creamsales_form,name='cream/creamsales_insert'),
    path('soapsales/<int:id>/',soapsales_form, name='cream/creamsales_update'), 
    path('soapsales/<id>/delete/',soapsales_delete,name='cream/creamsales_delete'),
    path('listcs/', creamsales_list,name='cream/creamsales_list'),

    #URL FOR EMPLOYEES   
    # path('indexemp/', emp, name = 'indexemp'),  
    # path('show/',show, name = 'show'),  
    # path('edit/<int:id>', edit, name = 'edit' ),  
    # path('update/<int:id>',update, name = 'update'),  
    # path('delete/<int:id>', destroy, name = 'destroy'),  
    ]