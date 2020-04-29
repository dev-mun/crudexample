from rest_framework import routers
from person import api_views as person_views

router = routers.DefaultRouter()
router.register(r'persons', person_views.PeopleViewset)
