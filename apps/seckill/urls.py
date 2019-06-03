from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^busy$', views.busy, name='busy'),
    url(r'^category/$', views.category, name='category'),

    url(r'^set_check/$', views.set_check, name='set_check'),
    # url(r'^secaddcart/$', views.addcart, name='secaddcart'),#计数器
    url(r'^getstock/$', views.getstock, name='getstock'),  # 取库存
    url(r'^secaddcart/$', views.secaddcart, name='secaddcart'),  # 队列
    url(r'^productdetail/$', views.productdetail, name='productdetail'),
    url(r'^getserverdatetime/$', views.getserverdatetime, name='getserverdatetime'),
    url(r'^paychoice/$', views.paychoice, name='paychoice'),
    url(r'^paying', views.paying, name="paying"),
    #  url(r'^alipayed_notify/$', views.alipay_async_notify, name="alipayed_notify"),
    #  url(r'^alipayed_success/$', views.alipay_success , name="alipayed_success"),
    #  #url(r'^alipayorder_query/$', 'alipay_order_query'),

    url(r'^wxpaying$', views.paying_for_weixin_pay, name="wxpaying"),

]
