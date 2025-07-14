from django.contrib import admin
from .models import (
    Department, TypeRead, Halaqa, Students, Teachers, DailyTalqeenTask,
    Supervisor, Teatcher_class_supervisor, StudentTask, UserRole, Msar, DailyMemorizationTask,DailyReviewTask, Students,
    StudentLink # Add StudentLink here
    
)
from .views import import_students_view # Import the view

from django import forms

from .utils import assign_halaqa  # تأكد من وجود ملف utils.py ووظيفة assign_halaqa


from .forms import DailyReviewTaskForm


from .models import WeeklyLecture
from .forms import WeeklyLectureForm





# القسم
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# نوع القراءة
@admin.register(TypeRead)
class TypeReadAdmin(admin.ModelAdmin):
    list_display = ('name', 'msar')
    list_filter = ('msar',)
    search_fields = ('name', 'msar__name')

# المسار
@admin.register(Msar)
class MsarAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')
    search_fields = ('name', 'department__name')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset

    def get_list_display(self, request):
        return self.list_display

    def get_search_fields(self, request):
        return self.search_fields

# الحلقة

@admin.register(Halaqa)
class HalaqaAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'type_class', 'count', 'start_time', 'end_time', 'teacher', 'department', 'activate', 'current_student_count')
    search_fields = ('name', 'level', 'type_class__name')
    list_filter = ('level', 'type_class', 'activate')

    def current_student_count(self, obj):
        return Students.objects.filter(halaqa=obj).count()

    current_student_count.short_description = 'عدد الطلاب الحالي'


# الطالب
# admin.py


class StudentsAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'second_name', 'last_name', 'mobile', 'whatsapp', 'halaqa']
    search_fields = ['username', 'first_name', 'second_name', 'last_name', 'mobile', 'whatsapp']
    list_filter = ['halaqa']

    def get_urls(self):
        urls = super().get_urls()
        from django.urls import path
        custom_urls = [
            path('import_students/', self.admin_site.admin_view(import_students_view), name='import_students'),
        ]
        return custom_urls + urls

    def save_model(self, request, obj, form, change):
        if not change:  # إذا كان هذا تسجيل جديد
            assign_halaqa(obj)
        super().save_model(request, obj, form, change)

admin.site.register(Students, StudentsAdmin)
#admin.site.register(Halaqa)


# المعلم
@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'last_name', 'email', 'mobile', 'gender', 'nationality', 'activate')
    search_fields = ('first_name', 'second_name', 'last_name', 'email', 'mobile')
    list_filter = ('gender', 'nationality', 'activate')

# المشرف
@admin.register(Supervisor)
class SupervisorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'activate')
    search_fields = ('name', 'email')
    list_filter = ('activate',)

# مشرف الصف
@admin.register(Teatcher_class_supervisor)
class Teacher_class_supervisorAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'teacher_class', 'supervisor')
    search_fields = ('name', 'teacher__username', 'teacher_class__name', 'supervisor__name')
    list_filter = ('teacher_class',)

# أدوار المستخدم
@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    search_fields = ('user__username', 'role')
    list_filter = ('role',)

# تسجيل النماذج الأخرى
@admin.register(StudentTask)
class StudentTaskAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'student', 'halaqa_name', 'msar', 'department', 'week_start',
        'week_end', 'week_number', 'count_bage', 'ayah_count', 'task_student',
        'category', 'surah', 'ayah', 'ayah_number'
    ]
    list_filter = ['task_student', 'category']
    search_fields = ['name', 'student__name']

    class Media:
        js = (
            'admin/js/student_task.js',  # إضافة ملف الجافاسكريبت
        )














SURAH_CHOICES_DICT = {
    '1': ["الفاتحة", "الناس", "الفلق", "الإخلاص", "المسد", "النصر", "الكافرون", "الكوثر", "الماعون", "قريش", "الفيل", "الهمزة", "العصر", "التكاثر", "القارعة", "العاديات", "الزلزلة", "البينة", "القدر", "العلق", "التين", "الشرح", "الضحى", "الليل", "الشمس", "البلد", "الفجر", "الغاشية", "الأعلى", "الطارق", "البروج", "الإنشقاق", "المطففين", "الانفطار", "التكوير", "عبس", "النازعات", "النبأ"],
    '2': ["المرسلات", "الإنسان", "القيامة", "المدثر", "المزمل", "الجن", "نوح", "المعارج", "الحاقة", "القلم", "الملك", "التحريم", "الطلاق", "التغابن", "المنافقون", "الجمعة", "الصف", "الممتحنة", "الحشر", "المجادلة"],
    '3': ["الحديد", "الواقعة", "الرحمن", "القمر", "النجم", "الطور", "الذاريات", "ق", "الحجرات", "الفتح", "محمد", "الأحقاف"],
    '4': ["الجاثية", "الدخان", "الزخرف", "الشورى", "فصلت", "غافر", "الزمر", "ص", "الصافات", "يس", "فاطر", "سبأ", "الأحزاب", "السجدة", "لقمان", "الروم"],
    '5': ["العنكبوت", "القصص", "النمل", "الشعراء", "الفرقان", "النور", "المؤمنون", "الحج", "الأنبياء", "طه", "مريم"],
    '6': ["الكهف", "الإسراء", "النحل", "الحجر", "إبراهيم", "الرعد", "يوسف", "هود", "يونس"],
    '7': ["التوبة", "الأنفال", "الأعراف", "الأنعام", "المائدة", "النساء", "آل عمران", "البقرة"]
}

AYAH_COUNT_DICT = {
    "الفاتحة": 7, "النساء": 176, "المائدة": 120, "الأنعام": 165, "الأعراف": 206, "الأنفال": 75,
    "التوبة": 129, "يونس": 109, "هود": 123, "يوسف": 111, "الرعد": 43, "إبراهيم": 52, "الحجر": 99,
    "النحل": 128, "الإسراء": 111, "الكهف": 110, "مريم": 98, "طه": 135, "الأنبياء": 112, "الحج": 78,
    "المؤمنون": 118, "النور": 64, "الفرقان": 77, "الشعراء": 227, "النمل": 93, "القصص": 88,
    "العنكبوت": 69, "الروم": 60, "لقمان": 34, "السجدة": 30, "الأحزاب": 73, "سبأ": 54, "فاطر": 45,
    "يس": 83, "الصافات": 182, "ص": 88, "الزمر": 75, "غافر": 85, "فصلت": 54, "الشورى": 53, "الزخرف": 89,
    "الدخان": 59, "الجاثية": 37, "الأحقاف": 35, "محمد": 38, "الفتح": 29, "الحجرات": 18, "ق": 45,
    "الذاريات": 60, "الطور": 49, "النجم": 62, "القمر": 55, "الرحمن": 78, "الواقعة": 96, "الحديد": 29,
    "المجادلة": 22, "الحشر": 24, "الممتحنة": 13, "الصف": 14, "الجمعة": 11, "المنافقون": 11,
    "التغابن": 18, "الطلاق": 12, "التحريم": 12, "الملك": 30, "القلم": 52, "الحاقة": 52,
    "المعارج": 44, "نوح": 28, "الجن": 28, "المزمل": 20, "المدثر": 56, "القيامة": 40, "الإنسان": 31,
    "المرسلات": 50, "النبأ": 40, "النازعات": 46, "عبس": 42, "التكوير": 29, "الانفطار": 19,
    "المطففين": 36, "الانشقاق": 25, "البروج": 22, "الطارق": 17, "الأعلى": 19, "الغاشية": 26,
    "الفجر": 30, "البلد": 20, "الشمس": 15, "الليل": 21, "الضحى": 11, "الشرح": 8, "التين": 8,
    "العلق": 19, "القدر": 5, "البينة": 8, "الزلزلة": 8, "العاديات": 11, "القارعة": 11,
    "التكاثر": 8, "العصر": 3, "الهمزة": 9, "الفيل": 5, "قريش": 4, "الماعون": 7, "الكوثر": 3,
    "الكافرون": 6, "النصر": 3, "المسد": 5, "الإخلاص": 4, "الفلق": 5, "الناس": 6, "البقرة": 286,
    "آل عمران": 200
}

class DailyMemorizationTaskForm(forms.ModelForm):
    MemorizationTask = forms.ChoiceField(
        choices=[
            ('1', 'المبتدئين'),
            ('2', 'ثلاثة أجزاء'),
            ('3', 'خمسة أجزاء'),
            ('4', 'عشرة أجزاء'),
            ('5', 'خمسة عشر جزء'),
            ('6', 'عشرون جزء'),
            ('7', 'خمسة وعشرون جزء')
        ],
        widget=forms.Select(attrs={'onchange': 'this.form.submit()'})
    )
    previous_surah = forms.ChoiceField(choices=[])
    previous_ayat = forms.IntegerField(min_value=1, initial=1)
    current_surah = forms.ChoiceField(choices=[])
    current_ayat = forms.IntegerField(min_value=1, initial=1)

    class Meta:
        model = DailyMemorizationTask
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        memorization_task = self.data.get('MemorizationTask', '1')
        self.update_choices(memorization_task)
        self.update_ayat_fields('previous_surah')
        self.update_ayat_fields('current_surah')

    def update_choices(self, task):
        surah_choices = [(surah, surah) for surah in SURAH_CHOICES_DICT[task]]
        self.fields['previous_surah'].choices = surah_choices
        self.fields['current_surah'].choices = surah_choices

    def update_ayat_fields(self, surah_field):
        surah = self.data.get(surah_field)
        if surah and surah in AYAH_COUNT_DICT:
            ayat_count = AYAH_COUNT_DICT[surah]
            self.fields['previous_ayat'].max_value = ayat_count
            self.fields['current_ayat'].max_value = ayat_count
        else:
            self.fields['previous_ayat'].max_value = 1
            self.fields['current_ayat'].max_value = 1

    def clean(self):
        cleaned_data = super().clean()
        task = cleaned_data.get("MemorizationTask")
        self.update_choices(task)
        self.update_ayat_fields('previous_surah')
        self.update_ayat_fields('current_surah')
        return cleaned_data

class DailyMemorizationTaskAdmin(admin.ModelAdmin):
    form = DailyMemorizationTaskForm
    list_display = ('student', 'get_MemorizationTask_display', 'previous_surah', 'previous_ayat', 'current_surah', 'current_ayat', 'date')
    list_filter = ('MemorizationTask', 'date')
    search_fields = ('student__name', 'previous_surah', 'current_surah')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        return form

admin.site.register(DailyMemorizationTask, DailyMemorizationTaskAdmin)



# forms.py




class DailyReviewTaskAdmin(admin.ModelAdmin):
    form = DailyReviewTaskForm
    list_display = ('student', 'ReviewTask', 'date', 'grade')
    search_fields = ('student__first_name', 'student__last_name', 'ReviewTask')

admin.site.register(DailyReviewTask, DailyReviewTaskAdmin)





@admin.register(DailyTalqeenTask)
class DailyTalqeenTaskAdmin(admin.ModelAdmin):
    list_display = (
        'student', 'TalqeenTask', 'previous_surah', 'previous_ayat',
        'current_surah', 'current_ayat', 'pages', 'partial_page', 'grade', 
        'date', 'Talqeen_ayat_count'
    )
    list_filter = ('TalqeenTask', 'date', 'grade')
    search_fields = ('student__first_name', 'student__last_name', 'previous_surah', 'current_surah')
    date_hierarchy = 'date'
    ordering = ('-date',)

admin.site.site_header = "إدارة مهام التلقين اليومية"
admin.site.site_title = "لوحة إدارة التلقين"
admin.site.index_title = "مرحبا بكم في لوحة إدارة التلقين اليومية"














@admin.register(WeeklyLecture)
class WeeklyLectureAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'youtube_link', 'created_at']  # إضافة حقل created_at إلى قائمة العرض
    search_fields = ['title', 'description']
    form = WeeklyLectureForm  # استخدام النموذج المخصص


from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'recipient', 'content', 'created_at')

admin.site.register(Message, MessageAdmin)



@admin.register(StudentLink)
class StudentLinkAdmin(admin.ModelAdmin):
    list_display = ('student', 'title', 'url', 'created_at')
    list_filter = ('student',)
    search_fields = ('student__username', 'title', 'url')


from django.contrib import admin
from .models import Admin

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'second_name', 'last_name', 'username')
    search_fields = ('user__username', 'first_name', 'last_name')
