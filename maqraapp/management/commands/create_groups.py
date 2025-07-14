# your_app/management/commands/create_groups.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Create groups and assign users to them'

    def handle(self, *args, **kwargs):
        # Create groups if they don't already exist
        students_group, created = Group.objects.get_or_create(name='students')
        teachers_group, created = Group.objects.get_or_create(name='teachers')

        # Add users to the appropriate groups
        try:
            student_user = User.objects.get(email='student@example.com')  # Replace with actual email
            student_user.groups.add(students_group)
            self.stdout.write(self.style.SUCCESS('Successfully added student to the students group'))

            teacher_user = User.objects.get(email='teacher@example.com')  # Replace with actual email
            teacher_user.groups.add(teachers_group)
            self.stdout.write(self.style.SUCCESS('Successfully added teacher to the teachers group'))

        except User.DoesNotExist as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
