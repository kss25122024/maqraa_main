# utils.py
from django.core.exceptions import ValidationError
from .models import Halaqa, Students

def assign_halaqa(student):
    available_halaqas = Halaqa.objects.filter(activate=True)
    for halaqa in available_halaqas:
        if Students.objects.filter(halaqa=halaqa).count() < halaqa.count:
            student.halaqa = halaqa
            return

    raise ValidationError('لا توجد حلقة متاحة بسعة كافية لتسجيل الطالب.')
