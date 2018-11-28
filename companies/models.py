from datetime import datetime

from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator


class Company(models.Model):
    company_name = models.CharField(max_length=380,null=True, blank=True, default=None )
    headquarters = models.CharField(max_length=180, null=True, blank=True, default=None)
    industry = models.CharField(max_length=180, null=True, blank=True, default=None)
    logo = models.ImageField(null=True, blank=True, default=None, upload_to='company_img')
    short_description = models.CharField(max_length=380, null=True, blank=True, default=None)
    long_description = models.TextField(null=True, blank=True, default=None)
    
    REMOTE_CHOICES = (
        ('Remote Friendly', 'Remote Friendly'),
        ('Remote First', 'Remote First'),
        ('Remote OK', 'Remote OK'),
        ('Partially Remote', 'Partially Remote'),
        ('Unknown', 'Unknown'),
    ) 
    remoteness = models.CharField(
        max_length=15,
        choices=REMOTE_CHOICES,
        default='Remote OK'
    )
    EMPLOYEE_CHOICES = (
        ('1-10 people', '1-10 people'),
        ('1-20 people', '1-20 people'),
        ('1-50 people', '1-50 people'),
        ('100+ people', '100+ people'),
        ('500+ people', '500+ people'),
    )
    number_of_employees = models.CharField(
        max_length=16,
        choices=EMPLOYEE_CHOICES,
        default='1-10 people'
    )

    year_founded = models.PositiveIntegerField(
            validators=[
                MinValueValidator(1900), 
                MaxValueValidator(datetime.now().year)],
            help_text="Use the following format: <YYYY>", null=True, blank=True, default=None)

    question_1 = models.BooleanField(help_text='Is the team fully remote?', default=False)
    question_2 = models.BooleanField(help_text='Does the team get together or have a retreat?', default=False)
    question_3 = models.BooleanField(help_text='Can you work in your timezone?', default=False)
    website = models.URLField(null=True, blank=True, default=None)
    twitter = models.URLField(null=True, blank=True, default=None)
    facebook = models.URLField(null=True, blank=True, default=None)
    github = models.URLField(null=True, blank=True, default=None)
    linkedin = models.URLField(null=True, blank=True, default=None)

    def __str__(self):
        return '%s - %s' % (
            self.company_name, self.short_description
        )