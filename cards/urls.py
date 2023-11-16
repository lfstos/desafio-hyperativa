from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import CartaoListCreateView, LoteListCreateView, ConsultarCartaoView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('cartoes/', CartaoListCreateView.as_view(), name='cartao-list-create'),
    path('lotes/', LoteListCreateView.as_view(), name='lote-list-create'),
    path('consultar_cartao/<str:numero_cartao>/',
         ConsultarCartaoView.as_view(), name='consultar-cartao'),
]
