from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Teacher, Student

@receiver(post_save, sender=get_user_model())
def assign_group_to_user(sender, instance, created, **kwargs):
    if created:
        if instance.user_role == 'Teacher':
            group = Group.objects.get(name='teacher')
            instance.groups.add(group)
        elif instance.user_role == 'Student':
            group = Group.objects.get(name='student')
            instance.groups.add(group)
        elif instance.user_role == 'Principal':
            group = Group.objects.get(name='Principal')
            instance.groups.add(group)

@receiver(post_save, sender=get_user_model())
def create_teacher_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_role == 'Teacher':
            Teacher.objects.create(user=instance)

@receiver(post_save, sender=get_user_model())
def save_teacher_profile(sender, instance, **kwargs):
    if instance.user_role == 'Teacher':
        instance.teacher.save()



@receiver(post_save, sender=get_user_model())
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_role == 'Student':
            Student.objects.create(user=instance)

@receiver(post_save, sender=get_user_model())
def save_student_profile(sender, instance, **kwargs):
    if instance.user_role == 'Student':
        instance.student.save()