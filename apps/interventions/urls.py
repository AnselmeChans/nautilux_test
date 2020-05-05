from rest_framework.routers import DefaultRouter

from .views import  UserViewSet, InterventionViewSet

#from .views import  CommandViewSet, UserViewSet, InterventionViewSet

router = DefaultRouter()
#router.register('commands', CommandViewSet, base_name='commands')
router.register('interventions', InterventionViewSet, base_name='interventions')

router.register('users', UserViewSet)
