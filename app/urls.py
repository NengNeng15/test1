from django.urls import path
from .views import (HomePageView, AboutPageView,
                    DatabasePageView,UserCreateView1,VenueCreateView,LessonCreateView,AppointmentCreateView,
                    PaymentCreateView,UserUpdateView1,UserDeleteView1,VenueUpdateView,LessonUpdateView,AppointmentUpdateView,
                    PaymentUpdateView,VenueDeleteView,LessonDeleteView,AppointmentDeleteView,PaymentDeleteView,ClassesPageView,
                    ContactPageView,Class1PageView,Class2PageView,AppointmentPageView,Class3PageView)
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('database/', DatabasePageView.as_view(), name='database'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('classes/', ClassesPageView.as_view(), name='classes'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('appointment/', AppointmentPageView.as_view(), name='appointment'),
    path('class1/', Class1PageView.as_view(), name='class1'),
    path('class2/', Class2PageView.as_view(), name='class2'),
    path('class3/', Class3PageView.as_view(), name='class3'),
    
    path('adduser/create/', UserCreateView1.as_view(), name='adduser'),
    path('venue/create/', VenueCreateView.as_view(), name='addvenue'),
    path('lesson/create/', LessonCreateView.as_view(), name='addlesson'),
    path('appointment/create/', AppointmentCreateView.as_view(), name='addappointment'),
    path('payment/create/', PaymentCreateView.as_view(), name='addpayment'),
    
    path('users/<int:pk>/update/', UserUpdateView1.as_view(), name='user_update'),
    path('venue/<int:pk>/update/', VenueUpdateView.as_view(), name='venue_update'),
    path('lesson/<int:pk>/update/', LessonUpdateView.as_view(), name='lesson_update'),
    path('appointment/<int:pk>/update/', AppointmentUpdateView.as_view(), name='appointment_update'),
    path('payment/<int:pk>/update/', PaymentUpdateView.as_view(), name='payment_update'),
    
    path('users/<int:pk>/delete/', UserDeleteView1.as_view(), name='delete_user'),
    path('venue/<int:pk>/delete/', VenueDeleteView.as_view(), name='delete_venue'),
    path('lesson/<int:pk>/delete/', LessonDeleteView.as_view(), name='delete_lesson'),
    path('appointment/<int:pk>/delete/', AppointmentDeleteView.as_view(), name='delete_appointment'),
    path('payment/<int:pk>/delete/', PaymentDeleteView.as_view(), name='delete_payment'),
]