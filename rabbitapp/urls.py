from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'rabbitapp'

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('contact/', views.ContactView.as_view(), name='contact'), # メール問い合わせのモジュール
    path('shop/', views.ShopView.as_view(), name='shop'), # 店用のモジュール
    path('add_to_cart/', views.AddToCartView.as_view(), name='add_to_cart'), # アイテム購入のモジュール
    path('item-detail/<int:pk>', views.DetailView.as_view(),name='detail'), # 店のアイテムのモジュール 
    path('cart/', views.CartView.as_view(),name='cart'), # カートのモジュール
    path('record/', views.RecordView.as_view(),name='record'), # 購入履歴のモジュール
    path('go_to_record/', views.GoToRecordView.as_view(),name='go_to_record'),
]

urlpatterns += static (
    settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)