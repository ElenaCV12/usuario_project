from rest_framework.routers import DefaultRouter
from usuario.api.views import UsuarioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
urlpatterns = router.urls
