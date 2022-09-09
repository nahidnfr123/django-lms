from django.contrib.auth.models import User
from django.db import models

from course.models import Course


class Payment(models.Model):
    course = models.ForeignKey(Course, verbose_name="Teacher", on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(User, verbose_name="Teacher", on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, editable=False,)
