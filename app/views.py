from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import User, Venue,Lesson, Appointment, Payment

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'
    
class ClassesPageView(TemplateView):
    template_name = 'app/classes.html'

class Class1PageView(TemplateView):
    template_name = 'app/class1.html'

class Class2PageView(TemplateView):
    template_name = 'app/class2.html'

class Class3PageView(TemplateView):
    template_name = 'app/class3.html'

class ContactPageView(TemplateView):
    template_name = 'app/contact.html'
    
class AppointmentPageView(TemplateView):
    template_name = 'app/appointment.html'
    
class DatabasePageView(TemplateView):
    template_name = 'app/database.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['venues'] = Venue.objects.all()
        context['lessons'] = Lesson.objects.all()
        context['appointments'] = Appointment.objects.all()
        context['payments'] = Payment.objects.all()
         # Dashboard summary data
        context['user_count'] = User.objects.count()
        context['venue_count'] = Venue.objects.count()
        context['lesson_count'] = Lesson.objects.count()
        context['appointment_count'] = Appointment.objects.count()
        context['payment_count'] = Payment.objects.count()
        
        return context
    
class UserCreateView1(CreateView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'role']
    template_name = 'app/add_user.html'
    
    def get_success_url(self):
        return reverse_lazy('database') + '?sections=users'

class VenueCreateView(CreateView):
    model = Venue
    fields = ['name', 'address', 'city']
    template_name = 'app/venue_create.html'
    
    def get_success_url(self):
        return reverse_lazy('database') + '?sections=venue'

class LessonCreateView(CreateView):
    model = Lesson
    fields = ['title','description','duration_minutes','price','location']
    template_name = 'app/lesson_create.html'
    
    def get_success_url(self):
        return reverse_lazy('database') + '?sections=lesson'
    
class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ['lesson', 'instructor', 'student','date_time','status']
    template_name = 'app/appointment_create.html'
    
    def get_success_url(self):
        return reverse_lazy('database') + '?sections=appointment'

class PaymentCreateView(CreateView):
    model = Payment
    fields = ['appointment', 'amount', 'payment_date','status']
    template_name = 'app/payment_create.html'
    
    def get_success_url(self):
        return reverse_lazy('database') + '?sections=payment'
    
class UserUpdateView1(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'role']
    template_name = 'app/update_user.html'
    
    def get_success_url(self):
        return reverse_lazy('database') + '?sections=user'

class VenueUpdateView(UpdateView):
    model = Venue
    fields = ['name', 'address', 'city']
    template_name = 'app/update_venue.html'
    
    def get_success_url(self):
        return reverse_lazy('database') + '?sections=venue'
    
class LessonUpdateView(UpdateView):
    model = Lesson
    fields = ['title','description','duration_minutes','price','location']
    template_name = 'app/update_lesson.html'
    
    def get_success_url(self):
        return reverse_lazy('database') + '?sections=lesson'

class AppointmentUpdateView(UpdateView):
    model = Appointment
    fields = ['lesson', 'instructor', 'student','date_time','status']
    template_name = 'app/update_appointment.html'
    
    def get_success_url(self):
        return reverse_lazy('database') + '?sections=appointment'

class PaymentUpdateView(UpdateView):
    model = Payment
    fields = ['appointment', 'amount', 'payment_date','status']
    template_name = 'app/update_payment.html'
    
    def get_success_url(self):
        return reverse_lazy('database') + '?sections=payment'
    
class UserDeleteView1(DeleteView):
    model = User
    template_name = 'app/delete_user.html'
    success_url = reverse_lazy('database')

class VenueDeleteView(DeleteView):
    model = Venue
    template_name = 'app/delete_venue.html'
    success_url = reverse_lazy('database')

class LessonDeleteView(DeleteView):
    model = Lesson
    template_name = 'app/delete_lesson.html'
    success_url = reverse_lazy('database')

class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'app/delete_appointment.html'
    success_url = reverse_lazy('database')

class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'app/delete_payment.html'
    success_url = reverse_lazy('database')
    

