from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe


class Course(models.Model):
    # teacher = models.ForeignKey(User, verbose_name="Teacher", on_delete=models.CASCADE)
    user = models.ManyToManyField(User, verbose_name="Student")
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True, unique=True)
    subtitle = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='uploads/course', null=True)
    status = models.BooleanField(default=True)
    featured = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    available_at = models.DateTimeField(auto_now_add=True, editable=True, )
    created_at = models.DateTimeField(auto_now_add=True, editable=False, )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.title) + ": $" + str(self.price)

    def get_absolute_url(self):
        return reverse("course_details", kwargs={"slug": self.slug})  # new

    def course_image(self):
        if self.image:
            return mark_safe('<img src="{}" height="60" />'.format(self.image.url))

    course_image.short_description = 'Image view'
    course_image.allow_tags = True


# Pivot Table
# class CourseStudent(models.Model):
#     status = models.BooleanField(default=True)
#     student = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)


class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True, unique=True)
    status = models.BooleanField(default=True)
    description = models.TextField(null=True)
    available_at = models.DateTimeField(auto_now_add=True, editable=True, )
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, )

    class Meta:
        ordering = ['-order', '-created_at']

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("section_detail", kwargs={"slug": self.slug})  # new


CONTENT_CHOICES = (
    ('note', 'Note'),
    ('live_class', 'Live Class'),
    ('recorded_class', 'Recorded Class'),
    ('exam', 'Exam'),
    ('assignment', 'Assignment'),
)


class Content(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    status = models.BooleanField(default=True)
    type = models.CharField(max_length=30, choices=CONTENT_CHOICES, null=True)
    available_at = models.DateTimeField(auto_now_add=True, editable=True, )
    end_date = models.DateTimeField(auto_now=True, editable=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, )

    class Meta:
        ordering = ['-created_at']
        abstract = True


class Note(Content):
    note = models.TextField(null=True)


CLASS_SOURCE = (
    ('google_meet', 'Google Meet'),
    ('zoom', 'Zoom'),
    ('facebook_live', 'Facebook Live'),
)


class LiveClass(Content):
    link = models.CharField(max_length=200)
    source = models.CharField(max_length=200, choices=CLASS_SOURCE)
    duration = models.IntegerField()


class RecordedClass(Content):
    link = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    duration = models.IntegerField()


class Exam(Content):
    total_marks = models.IntegerField()
    total_questions = models.IntegerField()
    duration = models.IntegerField()
    result_date = models.DateTimeField(auto_now_add=True, editable=True, )


class Assignment(Content):
    instruction = models.TextField(null=True)
    duration = models.IntegerField()
    total_marks = models.IntegerField(null=True)


class Mcq(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.TextField()
    question_image = models.ImageField(upload_to='uploads/mcq', null=True)
    a = models.CharField(max_length=200)
    b = models.CharField(max_length=200)
    c = models.CharField(max_length=200)
    d = models.CharField(max_length=200)
    e = models.CharField(max_length=200)
    mark = models.IntegerField(default=1)
    answer = models.CharField(max_length=200)
    answer_image = models.ImageField(upload_to='uploads/mcq', null=True)
    student = models.ManyToManyField(User)


# Pivot Table
# class McqUser(models.Model):
#     exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
#     mcq = models.ForeignKey(Mcq, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)


class Result(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    duration = models.IntegerField(null=True)
    start_time = models.DateTimeField(auto_now_add=True, editable=True, null=True)
    end_time = models.DateTimeField(auto_now_add=True, editable=True, null=True)
    total_marks = models.IntegerField(null=True)
    obtained_marks = models.DecimalField(max_digits=10, decimal_places=2)


class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True, editable=True, null=True)
    total_marks = models.IntegerField(null=True)
    obtained_marks = models.DecimalField(max_digits=10, decimal_places=2)
    file = models.FileField(verbose_name="Assignment File", upload_to='uploads/assignment/', blank=True)
