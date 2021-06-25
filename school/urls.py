from django.urls import path, include

from .views import StudentsViewSet, CoursesViewSet, RegistrationsViewSet, ListStudentRegistrations, ListCourseStudents
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename='Students')
router.register('courses', CoursesViewSet, basename='Courses')
router.register('registrations', RegistrationsViewSet, basename='Registrations')


urlpatterns = [
    path('', include(router.urls)),
    path('students/<int:pk>/registrations/', ListStudentRegistrations.as_view()),
    path('courses/<int:pk>/students/', ListCourseStudents.as_view())
]