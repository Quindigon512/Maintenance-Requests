from django.urls import path
from . import views

app_name = "mainRequest"

# URLConf
urlpatterns = [
    path('staff/', views.staff, name = "staff"),
    path('tenant/', views.tenant, name = "tenant"),
    path('addRequest/', views.addRequest, name='addRequest'),
    path('sortNum/', views.sortNum, name = 'sortNum'),
    path('sortPending/', views.sortPending, name = 'sortPending'),
    path('sortCompleted/', views.sortCompleted, name = 'sortCompleted'),
    path('filterByArea/', views.filterByArea, name = 'filterByArea'),
    path('filterByDate/', views.filterByDate, name = 'filterByDate'),
    path('update_status/<int:request_id>/', views.update_status, name = 'update_status'),
]
