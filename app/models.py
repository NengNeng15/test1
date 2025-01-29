from django.db import models

class User(models.Model):
    Role_Of_User = [
        ('Instructor', 'instructor'),
        ('Student', 'student'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=10, choices=Role_Of_User)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"

class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration_minutes = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    location = models.ForeignKey(Venue, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Appointment(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='instructor_appointments')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_appointments')
    date_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ])

    def __str__(self):
        return f"Appointment for {self.lesson.title} with {self.instructor} and {self.student} on {self.date_time}"

class Payment(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    payment_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
        ('Failed', 'Failed'),
    ])

    def __str__(self):
        return f"Payment for {self.appointment} - {self.status}"