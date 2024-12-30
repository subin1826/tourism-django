from django.contrib import admin
from django.urls import path,include
from.import views as v


urlpatterns = [

    path('home/',v.home,name='home'),
    path('',v.index,name='index'),
    path('register/',v.register,name='register'),
    path('login/',v.Userlogin,name='login'),
    path('details/',v.Package_data,name='Package_data'),
    path('vreg/',v.vendor_reg,name='vendor_reg'),
    path('vlog/',v.vendor_login,name='vendor_login'),
    path('dash/',v.dash,name='dash'),
    path('payment/',v.payment,name='payment'),
    path('datas/<int:pk>/delete',v.delt,name="delt"),
    path('datas/<int:pk>/edited',v.edited,name="edited"),
    path('details1/',v.Package_data1,name='Package_data1'),
    path('userdash/',v.user_dash,name='userdash'),
    path('out/',v.uslogout,name='uslogout'),
   
 

   
    
    

    

]

    
