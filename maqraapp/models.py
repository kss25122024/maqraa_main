from datetime import date, timezone
import datetime
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User, Group
from django.utils import timezone
from embed_video.fields import EmbedVideoField










# نموذج أساسي يحتوي على الوقت والتفعيل
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="وقت الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="وقت التعديل")
   
    activate = models.BooleanField(default=True, verbose_name="تفعيل")

    class Meta:
        abstract = True

# نموذج المعلمين
class Language(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="اللغة")

    def __str__(self):
        return self.name

# نموذج المعلمين
class Teachers(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    CAREER_PATH_CHOICES = [
        ('1', 'تأسيس'),
        ('2', 'إجازة1'),
        ('3', 'إجازة2'),
        ('4', 'حفظ'),
    ]

    # العلاقات مع User
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="teacher_profile")

    # البيانات الشخصية
    first_name = models.CharField(max_length=256, verbose_name="الاسم الأول")
    second_name = models.CharField(max_length=256, verbose_name="الاسم الثاني")
    last_name = models.CharField(max_length=256, verbose_name="اللقب")
    email = models.EmailField(verbose_name="الإيميل", unique=False, null=True, blank=True)  # Made optional
    mobile = PhoneNumberField(verbose_name="رقم الجوال", null=True)
    mobile_whatsapp = PhoneNumberField(verbose_name="رقم الواتس", blank=True, null=True)

    # معلومات إضافية
    gender = models.CharField(max_length=10, verbose_name="الجنس", choices=GENDER_CHOICES)
    birthday = models.DateField(verbose_name="تاريخ الميلاد")
    nationality = models.CharField(max_length=256, verbose_name="الجنسية")
    country = models.CharField(max_length=256, verbose_name="الدولة")
    certificates = models.CharField(verbose_name="شهادات وإجازات الحفظ", max_length=256, blank=True, null=True)
    language = models.ManyToManyField(Language, verbose_name="اللغات التي تعرفها", blank=True)

    # البيانات الخاصة بالنظام
    password = models.CharField(max_length=256, verbose_name="كلمة المرور")  # كلمة المرور ستُشفر لاحقًا
    career_path = models.CharField(max_length=256, verbose_name="المسار الذي ترغب في التدريس", choices=CAREER_PATH_CHOICES)
    cv_teacher = models.FileField(verbose_name="السيرة الذاتية", upload_to="teachers/cvs/", blank=True, null=True)
    username = models.CharField(max_length=255, verbose_name="اسم المستخدم", unique=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)

    activate = models.BooleanField(default=True, verbose_name="تفعيل")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"  # إظهار الاسم الكامل

    def save(self, *args, **kwargs):
        # تشفير كلمة المرور قبل الحفظ إذا لم تكن مشفرة بالفعل
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)

        # حفظ الكائن
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        # التحقق من مطابقة كلمة المرور مع كلمة المرور المشفرة
        return check_password(raw_password, self.password)









class Department(models.Model):
    name = models.CharField(max_length=256, verbose_name="اسم القسم")

    def __str__(self):
        return self.name


class Msar(models.Model):
    name = models.CharField(max_length=255, verbose_name="المسار")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="القسم", default=1)
    
    def __str__(self):
        return f"{self.name} ({self.department.name})"


class TypeRead(models.Model):
    name = models.CharField(max_length=100, verbose_name="نوع القراءة")
    msar = models.ForeignKey(Msar, on_delete=models.CASCADE, verbose_name="المسار", default=1)

    def __str__(self):
        return self.name



class Halaqa(models.Model):
    name = models.CharField(max_length=256, verbose_name="اسم الحلقة")
    level = models.CharField(max_length=256, verbose_name="مستوى الحلقة")
    type_class = models.ForeignKey(TypeRead, on_delete=models.CASCADE, verbose_name="نوع القراءة")
    count = models.IntegerField(verbose_name="الطاقة الاستيعابية للحلقة")
    start_time = models.TimeField(verbose_name="وقت بداية الحلقة")
    end_time = models.TimeField(verbose_name="وقت نهاية الحلقة")
    teacher = models.ForeignKey('Teachers', on_delete=models.CASCADE, verbose_name="الأستاذ", null=True, blank=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, verbose_name="القسم", default=1)  # تحديد القيمة الافتراضية هنا
    msar = models.ForeignKey(Msar, on_delete=models.CASCADE, verbose_name="المسار", default=1)
    activate = models.BooleanField(default=True, verbose_name="تفعيل")

    def __str__(self):
        return self.name





class Students(models.Model):  # ليس BaseModel بل models.Model
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile")
    first_name = models.CharField(max_length=30, verbose_name="الأسم الأول للطالب")
    second_name = models.CharField(max_length=50, verbose_name="الأسم الثاني للطالب")
    last_name = models.CharField(max_length=50, verbose_name="لقب الطالب")
    birthday = models.DateField(verbose_name="تاريخ الميلاد")
    nationality = models.CharField(max_length=256, verbose_name="الجنسية")
    # Removed country field as requested
    gender = models.CharField(max_length=256, verbose_name="الجنس")
    email = models.EmailField(verbose_name="الإيميل",  null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="اللغة التي تعرفها")
    mobile = PhoneNumberField(verbose_name="رقم الجوال", null=True, blank=True)
    whatsapp = PhoneNumberField(verbose_name="رقم الواتس اب", null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    username = models.CharField(max_length=50, verbose_name="اسم المستخدم", unique=True)
    password = models.CharField(max_length=128, verbose_name="كلمة المرور") # Note: Storing passwords here is not recommended. Use Django's built-in User model for authentication.
    halaqa = models.ForeignKey('Halaqa', on_delete=models.CASCADE, verbose_name="الحلقة", null=True, blank=True)
    activate = models.BooleanField(default=True, verbose_name="تفعيل")

    def __str__(self):
        return self.username






    
    
    
    

    def save(self, *args, **kwargs):
        # Hash the password before saving if it's not already hashed
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)

        # Save the object
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        # Check if the provided password matches the hashed password
        return check_password(raw_password, self.password)


class StudentLink(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='links', verbose_name="الطالب")
    title = models.CharField(max_length=255, verbose_name="عنوان الرابط")
    url = models.URLField(verbose_name="الرابط")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    class Meta:
        verbose_name = "رابط الطالب"
        verbose_name_plural = "روابط الطلاب"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} for {self.student.username}"
# نموذج المشرفين
class Supervisor(BaseModel):
    name = models.CharField(max_length=256, verbose_name="الاسم الثلاثي")
    email = models.EmailField(verbose_name="الإيميل")
    password = models.CharField(max_length=256, verbose_name="كلمة المرور")
    username = models.CharField(max_length=255, verbose_name="اسم المستخدم", unique=True, default='default-username')
    activate = models.BooleanField(default=True, verbose_name="تفعيل")

# نموذج المعلم المشرف على الحلقة
class Teatcher_class_supervisor(models.Model):
    name = models.CharField(max_length=255, verbose_name="الاسم")
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE, verbose_name="المدرس")
    teacher_class = models.ForeignKey(Halaqa, on_delete=models.CASCADE, verbose_name="الحلقة")
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE, verbose_name="المشرف")
    
    
    


class StudentTask(models.Model):
    name = models.CharField(max_length=255, verbose_name="الاسم")
    student = models.ForeignKey('Students', on_delete=models.CASCADE, verbose_name="الطالب")
    halaqa_name = models.CharField(max_length=255, verbose_name="اسم الحلقة", default=1)
    msar = models.CharField(max_length=255, verbose_name="المسار", default=1)
    department = models.CharField(max_length=255, verbose_name="القسم", default=1)
    week_start = models.DateField(verbose_name="تاريخ بداية الأسبوع", blank=True, null=True)
    week_end = models.DateField(verbose_name="تاريخ نهاية الأسبوع", blank=True, null=True)
    week_number = models.IntegerField(verbose_name="رقم الأسبوع", blank=True, null=True)
    count_bage = models.FloatField(verbose_name="عدد الصفحات")
    ayah_count = models.IntegerField(verbose_name="عدد الآيات", blank=True, null=True)

    Task_CHOICES = [
        ('1', 'حفظ'),
        ('2', 'مراجعة'),
        ('3', 'تلقين'),
    ]

    CATEGORY_CHOICES = [
        ('1', 'فئة المبتدئين'),
        ('2', 'فئة ثلاثة أجزاء'),
        ('3', 'فئة خمسة أجزاء'),
        ('4', 'فئة عشرة أجزاء'),
        ('5', 'فئة خمسة عشر جزء'),
        ('6', 'فئة عشرون جزء'),
        ('7', 'فئة خمسة وعشرون جزء'),
    ]

    task_student = models.CharField(
        max_length=10,
        choices=Task_CHOICES,
        default='1',
        verbose_name="مهمة الطالب"
    )

    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        verbose_name="الفئة",
        blank=True,
        null=True
    )

    surah = models.CharField(
        max_length=255,
        verbose_name="السورة",
        blank=True,
        null=True
    )

    ayah = models.CharField(
        max_length=255,
        verbose_name="الاية",
        blank=True,
        null=True
    )

    ayah_number = models.IntegerField(
        verbose_name="رقم الاية",
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.task_student

    def save(self, *args, **kwargs):
        if self.week_number is None:
            # حساب رقم الأسبوع الجديد بناءً على الطالب
            previous_tasks = StudentTask.objects.filter(student=self.student).order_by('-week_number')
            if previous_tasks.exists():
                self.week_number = previous_tasks.first().week_number + 1
            else:
                self.week_number = 1

        super().save(*args, **kwargs)

        # منطق للحصول على السور والآيات بشكل ديناميكي بناءً على الفئة المختارة
        surah_mapping = {
            '1': ["الفاتحة", "الناس", "الفلق", "الإخلاص", "المسد", "النصر", "الكافرون", "الكوثر", "الماعون", "قريش", "الفيل", "الهمزة", "العصر", "التكاثر", "القارعة", "العاديات", "الزلزلة", "البينة", "القدر", "العلق", "التين", "الشرح", "الضحى", "الليل", "الشمس", "البلد", "الفجر", "الغاشية", "الأعلى", "الطارق", "البروج", "الإنشقاق", "المطففين", "الانفطار", "التكوير", "عبس", "النازعات", "النبأ"],
            '2': ["المرسلات", "الإنسان", "القيامة", "المدثر", "المزمل", "الجن", "نوح", "المعارج", "الحاقة", "القلم", "الملك", "التحريم", "الطلاق", "التغابن", "المنافقون", "الجمعة", "الصف", "الممتحنة", "الحشر", "المجادلة"],
            '3': ["الحديد", "الواقعة", "الرحمن", "القمر", "النجم", "الطور", "الذاريات", "ق", "الحجرات", "الفتح", "محمد", "الأحقاف"],
            '4': ["الجاثية", "الدخان", "الزخرف", "الشورى", "فصلت", "غافر", "الزمر", "ص", "الصافات", "يس", "فاطر", "سبأ", "الأحزاب", "السجدة", "لقمان", "الروم"],
            '5': ["العنكبوت", "القصص", "النمل", "الشعراء", "الفرقان", "النور", "المؤمنون", "الحج", "الأنبياء", "طه", "مريم"],
            '6': ["الكهف", "الإسراء", "النحل", "الحجر", "إبراهيم", "الرعد", "يوسف", "هود", "يونس"],
            '7': ["التوبة", "الأنفال", "الأعراف", "الأنعام", "المائدة", "النساء", "آل عمران", "البقرة"]
        }

        ayah_mapping = {
            "الفاتحة": 7,
            "النساء": 176,
            "المائدة": 120,
            "الأنعام": 165,
            "الأعراف": 206,
            "الأنفال": 75,
            "التوبة": 129,
            "يونس": 109,
            "هود": 123,
            "يوسف": 111,
            "الرعد": 43,
            "إبراهيم": 52,
            "الحجر": 99,
            "النحل": 128,
            "الإسراء": 111,
            "الكهف": 110,
            "مريم": 98,
            "طه": 135,
            "الأنبياء": 112,
            "الحج": 78,
            "المؤمنون": 118,
            "النور": 64,
            "الفرقان": 77,
            "الشعراء": 227,
            "النمل": 93,
            "القصص": 88,
            "العنكبوت": 69,
            "الروم": 60,
            "لقمان": 34,
            "السجدة": 30,
            "الأحزاب": 73,
            "سبأ": 54,
            "فاطر": 45,
            "يس": 83,
            "الصافات": 182,
            "ص": 88,
            "الزمر": 75,
            "غافر": 85,
            "فصلت": 54,
            "الشورى": 53,
            "الزخرف": 89,
            "الدخان": 59,
            "الجاثية": 37,
            "الأحقاف": 35,
            "محمد": 38,
            "الفتح": 29,
            "الحجرات": 18,
            "ق": 45,
            "الذاريات": 60,
            "الطور": 49,
            "النجم": 62,
            "القمر": 55,
            "الرحمن": 78,
            "الواقعة": 96,
            "الحديد": 29,
            "المجادلة": 22,
            "الحشر": 24,
            "الممتحنة": 13,
            "الصف": 14,
            "الجمعة": 11,
            "المنافقون": 11,
            "التغابن": 18,
            "الطلاق": 12,
            "التحريم": 12,
            "الملك": 30,
            "القلم": 52,
            "الحاقة": 52,
            "المعارج": 44,
            "نوح": 28,
            "الجن": 28,
            "المزمل": 20,
            "المدثر": 56,
            "القيامة": 40,
            "الإنسان": 31,
            "المرسلات": 50,
            "النبأ": 40,
            "النازعات": 46,
            "عبس": 42,
            "التكوير": 29,
            "الانفطار": 19,
            "المطففين": 36,
            "الانشقاق": 25,
            "البروج": 22,
            "الطارق": 17,
            "الأعلى": 19,
            "الغاشية": 26,
            "الفجر": 30,
            "البلد": 20,
            "الشمس": 15,
            "الليل": 21,
            "الضحى": 11,
            "الشرح": 8,
            "التين": 8,
            "العلق": 19,
            "القدر": 5,
            "البينة": 8,
            "الزلزلة": 8,
            "العاديات": 11,
            "القارعة": 11,
            "التكاثر": 8,
            "العصر": 3,
            "الهمزة": 9,
            "الفيل": 5,
            "قريش": 4,
            "الماعون": 7,
            "الكوثر": 3,
            "الكافرون": 6,
            "النصر": 3,
            "المسد": 5,
            "الإخلاص": 4,
            "الفلق": 5,
            "الناس": 6,
            "البقرة": 286,
            "آل عمران": 200,
        }

        # الحصول على السور بناءً على الفئة
        if self.category and self.category in surah_mapping:
            self.surah = ', '.join(surah_mapping[self.category])

        # الحصول على الآيات بناءً على السورة
        if self.surah in ayah_mapping:
            self.ayah_number = ayah_mapping[self.surah]

        super().save(*args, **kwargs)











# نموذج دور المستخدمين
class UserRole(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('supervisor', 'Supervisor'),
        ('admin', 'Admin'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"









class DailyMemorizationTask(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)

    حفظ_الفئة = [
        (1, 'فئة المبتدئين'),
        (2, 'فئة ثلاثة أجزاء'),
        (3, 'فئة خمسة أجزاء'),
        (4, 'فئة عشرة أجزاء'),
        (5, 'فئة خمسة عشر جزء'),
        (6, 'فئة عشرون جزء'),
        (7, 'فئة خمسة وعشرون جزء'),
    ]

    MemorizationTask = models.IntegerField(choices=حفظ_الفئة, default=1)
    previous_surah = models.CharField(max_length=100,  blank=True)
    previous_ayat = models.PositiveIntegerField(default=1, )
    current_surah = models.CharField(max_length=100, blank=True)
    current_ayat = models.PositiveIntegerField(default=1, )
    pages = models.PositiveIntegerField()
    partial_page = models.FloatField(choices=[(0, '0'), (0.25, '0.25'), (0.5, '0.5'), (0.75, '0.75')])
    grade = models.PositiveIntegerField()
    date = models.DateField(default=timezone.now)
    memorized_ayat_count = models.PositiveIntegerField(default=0)

    # تعريف surah_mapping و ayah_mapping كما في الكود السابق

    surah_mapping = {
        1: ["الفاتحة", "الناس", "الفلق", "الإخلاص", "المسد", "النصر", "الكافرون", "الكوثر", "الماعون", "قريش", "الفيل", "الهمزة", "العصر", "التكاثر", "القارعة", "العاديات", "الزلزلة", "البينة", "القدر", "العلق", "التين", "الشرح", "الضحى", "الليل", "الشمس", "البلد", "الفجر", "الغاشية", "الأعلى", "الطارق", "البروج", "الإنشقاق", "المطففين", "الانفطار", "التكوير", "عبس", "النازعات", "النبأ"],
        2: ["المرسلات", "الإنسان", "القيامة", "المدثر", "المزمل", "الجن", "نوح", "المعارج", "الحاقة", "القلم", "الملك", "التحريم", "الطلاق", "التغابن", "المنافقون", "الجمعة", "الصف", "الممتحنة", "الحشر", "المجادلة"],
        3: ["الحديد", "الواقعة", "الرحمن", "القمر", "النجم", "الطور", "الذاريات", "ق", "الحجرات", "الفتح", "محمد", "الأحقاف"],
        4: ["الجاثية", "الدخان", "الزخرف", "الشورى", "فصلت", "غافر", "الزمر", "ص", "الصافات", "يس", "فاطر", "سبأ", "الأحزاب", "السجدة", "لقمان", "الروم"],
        5: ["العنكبوت", "القصص", "النمل", "الشعراء", "الفرقان", "النور", "المؤمنون", "الحج", "الأنبياء", "طه", "مريم"],
        6: ["الكهف", "الإسراء", "النحل", "الحجر", "إبراهيم", "الرعد", "يوسف", "هود", "يونس"],
        7: ["التوبة", "الأنفال", "الأعراف", "الأنعام", "المائدة", "النساء", "آل عمران", "البقرة"]
    }

    ayah_mapping = {
        "الفاتحة": 7,
        "البقرة": 286,
        "آل عمران": 200,
        "النساء": 176,
        "المائدة": 120,
        "الأنعام": 165,
        "الأعراف": 206,
        "الأنفال": 75,
        "التوبة": 129,
        "يونس": 109,
        "هود": 123,
        "يوسف": 111,
        "الرعد": 43,
        "إبراهيم": 52,
        "الحجر": 99,
        "النحل": 128,
        "الإسراء": 111,
        "الكهف": 110,
        "مريم": 98,
        "طه": 135,
        "الأنبياء": 112,
        "الحج": 78,
        "المؤمنون": 118,
        "النور": 64,
        "الفرقان": 77,
        "الشعراء": 227,
        "النمل": 93,
        "القصص": 88,
        "العنكبوت": 69,
        "الروم": 60,
        "لقمان": 34,
        "السجدة": 30,
        "الأحزاب": 73,
        "سبأ": 54,
        "فاطر": 45,
        "يس": 83,
        "الصافات": 182,
        "ص": 88,
        "الزمر": 75,
        "غافر": 85,
        "فصلت": 54,
        "الشورى": 53,
        "الزخرف": 89,
        "الدخان": 59,
        "الجاثية": 37,
        "الأحقاف": 35,
        "محمد": 38,
        "الفتح": 29,
        "الحجرات": 18,
        "ق": 45,
        "الذاريات": 60,
        "الطور": 49,
        "النجم": 62,
        "القمر": 55,
        "الرحمن": 78,
        "الواقعة": 96,
        "الحديد": 29,
        "المجادلة": 22,
        "الحشر": 24,
        "الممتحنة": 13,
        "الصف": 14,
        "الجمعة": 11,
        "المنافقون": 11,
        "التغابن": 18,
        "الطلاق": 12,
        "التحريم": 12,
        "الملك": 30,
        "القلم": 52,
        "الحاقة": 52,
        "المعارج": 44,
        "نوح": 28,
        "الجن": 28,
        "المزمل": 20,
        "المدثر": 56,
        "القيامة": 40,
        "الإنسان": 31,
        "المرسلات": 50,
        "النبأ": 40,
        "النازعات": 46,
        "عبس": 42,
        "التكوير": 29,
        "الانفطار": 19,
        "المطففين": 36,
        "الانشقاق": 25,
        "البروج": 22,
        "الطارق": 17,
        "الأعلى": 19,
        "الغاشية": 26,
        "الفجر": 30,
        "البلد": 20,
        "الشمس": 15,
        "الليل": 21,
        "الضحى": 11,
        "الشرح": 8,
        "التين": 8,
        "العلق": 19,
        "القدر": 5,
        "البينة": 8,
        "الزلزلة": 8,
        "العاديات": 11,
        "القارعة": 11,
        "التكاثر": 8,
        "العصر": 3,
        "الهمزة": 9,
        "الفيل": 5,
        "قريش": 4,
        "الماعون": 7,
        "الكوثر": 3,
        "الكافرون": 6,
        "النصر": 3,
        "المسد": 5,
        "الإخلاص": 4,
        "الفلق": 5,
        "الناس": 6,
    }

    def save(self, *args, **kwargs):
        # Ensure the choices for previous_surah and current_surah match the selected category
        surah_choices = self.surah_mapping.get(self.MemorizationTask, [])
        self._meta.get_field('previous_surah').choices = [(surah, surah) for surah in surah_choices]
        self._meta.get_field('current_surah').choices = [(surah, surah) for surah in surah_choices]
        
        if self.previous_surah:
            self._meta.get_field('previous_ayat').choices = [(i, i) for i in range(1, self.ayah_mapping.get(self.previous_surah, 1) + 1)]
        if self.current_surah:
            self._meta.get_field('current_ayat').choices = [(i, i) for i in range(1, self.ayah_mapping.get(self.current_surah, 1) + 1)]

        super(DailyMemorizationTask, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.get_MemorizationTask_display()} - {self.previous_surah} {self.previous_ayat} to {self.current_surah} {self.current_ayat}'





class DailyReviewTask(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)

    مراجعة_الفئة = [
        (1, 'فئة المبتدئين'),
        (2, 'فئة ثلاثة أجزاء'),
        (3, 'فئة خمسة أجزاء'),
        (4, 'فئة عشرة أجزاء'),
        (5, 'فئة خمسة عشر جزء'),
        (6, 'فئة عشرون جزء'),
        (7, 'فئة خمسة وعشرون جزء'),
    ]

    ReviewTask = models.IntegerField(choices=مراجعة_الفئة, default=1)
    previous_surah = models.CharField(max_length=100, blank=True)
    previous_ayat = models.PositiveIntegerField(default=1)
    current_surah = models.CharField(max_length=100, blank=True)
    current_ayat = models.PositiveIntegerField(default=1)
    pages = models.PositiveIntegerField()
    partial_page = models.FloatField(choices=[(0, '0'), (0.25, '0.25'), (0.5, '0.5'), (0.75, '0.75')])
    grade = models.PositiveIntegerField()
    date = models.DateField(default=timezone.now)
    reviewed_ayat_count = models.PositiveIntegerField(default=0)

    surah_mapping = {
        1: ["الفاتحة", "الناس", "الفلق", "الإخلاص", "المسد", "النصر", "الكافرون", "الكوثر", "الماعون", "قريش", "الفيل", "الهمزة", "العصر", "التكاثر", "القارعة", "العاديات", "الزلزلة", "البينة", "القدر", "العلق", "التين", "الشرح", "الضحى", "الليل", "الشمس", "البلد", "الفجر", "الغاشية", "الأعلى", "الطارق", "البروج", "الإنشقاق", "المطففين", "الانفطار", "التكوير", "عبس", "النازعات", "النبأ"],
        2: ["المرسلات", "الإنسان", "القيامة", "المدثر", "المزمل", "الجن", "نوح", "المعارج", "الحاقة", "القلم", "الملك", "التحريم", "الطلاق", "التغابن", "المنافقون", "الجمعة", "الصف", "الممتحنة", "الحشر", "المجادلة"],
        3: ["الحديد", "الواقعة", "الرحمن", "القمر", "النجم", "الطور", "الذاريات", "ق", "الحجرات", "الفتح", "محمد", "الأحقاف"],
        4: ["الجاثية", "الدخان", "الزخرف", "الشورى", "فصلت", "غافر", "الزمر", "ص", "الصافات", "يس", "فاطر", "سبأ", "الأحزاب", "السجدة", "لقمان", "الروم"],
        5: ["العنكبوت", "القصص", "النمل", "الشعراء", "الفرقان", "النور", "المؤمنون", "الحج", "الأنبياء", "طه", "مريم"],
        6: ["الكهف", "الإسراء", "النحل", "الحجر", "إبراهيم", "الرعد", "يوسف", "هود", "يونس"],
        7: ["التوبة", "الأنفال", "الأعراف", "الأنعام", "المائدة", "النساء", "آل عمران", "البقرة"]
    }

    ayah_mapping = {
        "الفاتحة": 7,
        "البقرة": 286,
        "آل عمران": 200,
        "النساء": 176,
        "المائدة": 120,
        "الأنعام": 165,
        "الأعراف": 206,
        "الأنفال": 75,
        "التوبة": 129,
        "يونس": 109,
        "هود": 123,
        "يوسف": 111,
        "الرعد": 43,
        "إبراهيم": 52,
        "الحجر": 99,
        "النحل": 128,
        "الإسراء": 111,
        "الكهف": 110,
        "مريم": 98,
        "طه": 135,
        "الأنبياء": 112,
        "الحج": 78,
        "المؤمنون": 118,
        "النور": 64,
        "الفرقان": 77,
        "الشعراء": 227,
        "النمل": 93,
        "القصص": 88,
        "العنكبوت": 69,
        "الروم": 60,
        "لقمان": 34,
        "السجدة": 30,
        "الأحزاب": 73,
        "سبأ": 54,
        "فاطر": 45,
        "يس": 83,
        "الصافات": 182,
        "ص": 88,
        "الزمر": 75,
        "غافر": 85,
        "فصلت": 54,
        "الشورى": 53,
        "الزخرف": 89,
        "الدخان": 59,
        "الجاثية": 37,
        "الأحقاف": 35,
        "محمد": 38,
        "الفتح": 29,
        "الحجرات": 18,
        "ق": 45,
        "الذاريات": 60,
        "الطور": 49,
        "النجم": 62,
        "القمر": 55,
        "الرحمن": 78,
        "الواقعة": 96,
        "الحديد": 29,
        "المجادلة": 22,
        "الحشر": 24,
        "الممتحنة": 13,
        "الصف": 14,
        "الجمعة": 11,
        "المنافقون": 11,
        "التغابن": 18,
        "الطلاق": 12,
        "التحريم": 12,
        "الملك": 30,
        "القلم": 52,
        "الحاقة": 52,
        "المعارج": 44,
        "نوح": 28,
        "الجن": 28,
        "المزمل": 20,
        "المدثر": 56,
        "القيامة": 40,
        "الإنسان": 31,
        "المرسلات": 50,
        "النبأ": 40,
        "النازعات": 46,
        "عبس": 42,
        "التكوير": 29,
        "الانفطار": 19,
        "المطففين": 36,
        "الانشقاق": 25,
        "البروج": 22,
        "الطارق": 17,
        "الأعلى": 19,
        "الغاشية": 26,
        "الفجر": 30,
        "البلد": 20,
        "الشمس": 15,
        "الليل": 21,
        "الضحى": 11,
        "الشرح": 8,
        "التين": 8,
        "العلق": 19,
        "القدر": 5,
        "البينة": 8,
        "الزلزلة": 8,
        "العاديات": 11,
        "القارعة": 11,
        "التكاثر": 8,
        "العصر": 3,
        "الهمزة": 9,
        "الفيل": 5,
        "قريش": 4,
        "الماعون": 7,
        "الكوثر": 3,
        "الكافرون": 6,
        "النصر": 3,
        "المسد": 5,
        "الإخلاص": 4,
        "الفلق": 5,
        "الناس": 6,
    }

    def save(self, *args, **kwargs):
        # Ensure the choices for previous_surah and current_surah match the selected category
        surah_choices = self.surah_mapping.get(self.ReviewTask, [])
        self._meta.get_field('previous_surah').choices = [(surah, surah) for surah in surah_choices]
        self._meta.get_field('current_surah').choices = [(surah, surah) for surah in surah_choices]
        
        if self.previous_surah:
            self._meta.get_field('previous_ayat').choices = [(i, i) for i in range(1, self.ayah_mapping.get(self.previous_surah, 1) + 1)]
        if self.current_surah:
            self._meta.get_field('current_ayat').choices = [(i, i) for i in range(1, self.ayah_mapping.get(self.current_surah, 1) + 1)]

        super(DailyReviewTask, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.get_ReviewTask_display()} - {self.previous_surah} {self.previous_ayat} to {self.current_surah} {self.current_ayat}'





class DailyTalqeenTask(models.Model):  # تغيير اسم النموذج
    student = models.ForeignKey(Students, on_delete=models.CASCADE)

    تلقين_الفئة = [
        (1, 'فئة المبتدئين'),
        (2, 'فئة ثلاثة أجزاء'),
        (3, 'فئة خمسة أجزاء'),
        (4, 'فئة عشرة أجزاء'),
        (5, 'فئة خمسة عشر جزء'),
        (6, 'فئة عشرون جزء'),
        (7, 'فئة خمسة وعشرون جزء'),
    ]

    TalqeenTask = models.IntegerField(choices=تلقين_الفئة, default=1)  # تغيير اسم الحقل
    previous_surah = models.CharField(max_length=100, blank=True)
    previous_ayat = models.PositiveIntegerField(default=1)
    current_surah = models.CharField(max_length=100, blank=True)
    current_ayat = models.PositiveIntegerField(default=1)
    pages = models.PositiveIntegerField()
    partial_page = models.FloatField(choices=[(0, '0'), (0.25, '0.25'), (0.5, '0.5'), (0.75, '0.75')])
    grade = models.PositiveIntegerField()
    date = models.DateField(default=timezone.now)
    Talqeen_ayat_count = models.PositiveIntegerField(default=0)  # تغيير اسم الحقل

    surah_mapping = {
        1: ["الفاتحة", "الناس", "الفلق", "الإخلاص", "المسد", "النصر", "الكافرون", "الكوثر", "الماعون", "قريش", "الفيل", "الهمزة", "العصر", "التكاثر", "القارعة", "العاديات", "الزلزلة", "البينة", "القدر", "العلق", "التين", "الشرح", "الضحى", "الليل", "الشمس", "البلد", "الفجر", "الغاشية", "الأعلى", "الطارق", "البروج", "الإنشقاق", "المطففين", "الانفطار", "التكوير", "عبس", "النازعات", "النبأ"],
        2: ["المرسلات", "الإنسان", "القيامة", "المدثر", "المزمل", "الجن", "نوح", "المعارج", "الحاقة", "القلم", "الملك", "التحريم", "الطلاق", "التغابن", "المنافقون", "الجمعة", "الصف", "الممتحنة", "الحشر", "المجادلة"],
        3: ["الحديد", "الواقعة", "الرحمن", "القمر", "النجم", "الطور", "الذاريات", "ق", "الحجرات", "الفتح", "محمد", "الأحقاف"],
        4: ["الجاثية", "الدخان", "الزخرف", "الشورى", "فصلت", "غافر", "الزمر", "ص", "الصافات", "يس", "فاطر", "سبأ", "الأحزاب", "السجدة", "لقمان", "الروم"],
        5: ["العنكبوت", "القصص", "النمل", "الشعراء", "الفرقان", "النور", "المؤمنون", "الحج", "الأنبياء", "طه", "مريم"],
        6: ["الكهف", "الإسراء", "النحل", "الحجر", "إبراهيم", "الرعد", "يوسف", "هود", "يونس"],
        7: ["التوبة", "الأنفال", "الأعراف", "الأنعام", "المائدة", "النساء", "آل عمران", "البقرة"]
    }

    ayah_mapping = {
        "الفاتحة": 7,
        "البقرة": 286,
        "آل عمران": 200,
        "النساء": 176,
        "المائدة": 120,
        "الأنعام": 165,
        "الأعراف": 206,
        "الأنفال": 75,
        "التوبة": 129,
        "يونس": 109,
        "هود": 123,
        "يوسف": 111,
        "الرعد": 43,
        "إبراهيم": 52,
        "الحجر": 99,
        "النحل": 128,
        "الإسراء": 111,
        "الكهف": 110,
        "مريم": 98,
        "طه": 135,
        "الأنبياء": 112,
        "الحج": 78,
        "المؤمنون": 118,
        "النور": 64,
        "الفرقان": 77,
        "الشعراء": 227,
        "النمل": 93,
        "القصص": 88,
        "العنكبوت": 69,
        "الروم": 60,
        "لقمان": 34,
        "السجدة": 30,
        "الأحزاب": 73,
        "سبأ": 54,
        "فاطر": 45,
        "يس": 83,
        "الصافات": 182,
        "ص": 88,
        "الزمر": 75,
        "غافر": 85,
        "فصلت": 54,
        "الشورى": 53,
        "الزخرف": 89,
        "الدخان": 59,
        "الجاثية": 37,
        "الأحقاف": 35,
        "محمد": 38,
        "الفتح": 29,
        "الحجرات": 18,
        "ق": 45,
        "الذاريات": 60,
        "الطور": 49,
        "النجم": 62,
        "القمر": 55,
        "الرحمن": 78,
        "الواقعة": 96,
        "الحديد": 29,
        "المجادلة": 22,
        "الحشر": 24,
        "الممتحنة": 13,
        "الصف": 14,
        "الجمعة": 11,
        "المنافقون": 11,
        "التغابن": 18,
        "الطلاق": 12,
        "التحريم": 12,
        "الملك": 30,
        "القلم": 52,
        "الحاقة": 52,
        "المعارج": 44,
        "نوح": 28,
        "الجن": 28,
        "المزمل": 20,
        "المدثر": 56,
        "القيامة": 40,
        "الإنسان": 31,
        "المرسلات": 50,
        "النبأ": 40,
        "النازعات": 46,
        "عبس": 42,
        "التكوير": 29,
        "الانفطار": 19,
        "المطففين": 36,
        "الانشقاق": 25,
        "البروج": 22,
        "الطارق": 17,
        "الأعلى": 19,
        "الغاشية": 26,
        "الفجر": 30,
        "البلد": 20,
        "الشمس": 15,
        "الليل": 21,
        "الضحى": 11,
        "الشرح": 8,
        "التين": 8,
        "العلق": 19,
        "القدر": 5,
        "البينة": 8,
        "الزلزلة": 8,
        "العاديات": 11,
        "القارعة": 11,
        "التكاثر": 8,
        "العصر": 3,
        "الهمزة": 9,
        "الفيل": 5,
        "قريش": 4,
        "الماعون": 7,
        "الكوثر": 3,
        "الكافرون": 6,
        "النصر": 3,
        "المسد": 5,
        "الإخلاص": 4,
        "الفلق": 5,
        "الناس": 6,
    }

    def save(self, *args, **kwargs):
        # Ensure the choices for previous_surah and current_surah match the selected category
        surah_choices = self.surah_mapping.get(self.TalqeenTask, [])
        self._meta.get_field('previous_surah').choices = [(surah, surah) for surah in surah_choices]
        self._meta.get_field('current_surah').choices = [(surah, surah) for surah in surah_choices]
        
        if self.previous_surah:
            self._meta.get_field('previous_ayat').choices = [(i, i) for i in range(1, self.ayah_mapping.get(self.previous_surah, 1) + 1)]
        if self.current_surah:
            self._meta.get_field('current_ayat').choices = [(i, i) for i in range(1, self.ayah_mapping.get(self.current_surah, 1) + 1)]

        super(DailyTalqeenTask, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.get_TalqeenTask_display()} - {self.previous_surah} {self.previous_ayat} to {self.current_surah} {self.current_ayat}'








class WeeklyPlan(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    
    # الحفظ
    memorization_task = models.IntegerField(choices=[(i, f'فئة {i}') for i in range(1, 8)])
    memorization_previous_surah = models.CharField(max_length=100)
    memorization_previous_ayat = models.IntegerField()
    memorization_current_surah = models.CharField(max_length=100)
    memorization_current_ayat = models.IntegerField()
    
    # المراجعة
    review_task = models.IntegerField(choices=[(i, f'فئة {i}') for i in range(1, 8)])
    review_previous_surah = models.CharField(max_length=100)
    review_previous_ayat = models.IntegerField()
    review_current_surah = models.CharField(max_length=100)
    review_current_ayat = models.IntegerField()
    
    # التلقين
    talqeen_task = models.IntegerField(choices=[(i, f'فئة {i}') for i in range(1, 8)])
    talqeen_previous_surah = models.CharField(max_length=100)
    talqeen_previous_ayat = models.IntegerField()
    talqeen_current_surah = models.CharField(max_length=100)
    talqeen_current_ayat = models.IntegerField()

    def __str__(self):
        return f"خطة أسبوعية للطالب {self.student.username}"






class WeeklyLecture(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    youtube_link = EmbedVideoField()  # استخدام EmbedVideoField لحقل الفيديو
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title










class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=256, verbose_name="الأسم الأول للأدمن", default="Unknown")
    second_name = models.CharField(max_length=256, verbose_name="الأسم الثاني للأدمن", default="Unknown")
    last_name = models.CharField(max_length=256, verbose_name="لقب الأدمن", default="Unknown")
    username = models.CharField(max_length=250, verbose_name="اسم المستخدم", default="default_username")

    def __str__(self):
        return self.username

    
    
    
    
    
    
    
    
    



class FAQ(BaseModel):
    ANSWER_TYPE_CHOICES = [
        ('text', 'Text'),
        ('video', 'Video'),
        ('image', 'Image'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='faq_questions', verbose_name="المستخدم")
    question = models.TextField(verbose_name="السؤال")
    answer_type = models.CharField(max_length=10, choices=ANSWER_TYPE_CHOICES, verbose_name="نوع الإجابة")
    text_answer = models.TextField(verbose_name="الإجابة النصية", blank=True, null=True)
    video_answer = EmbedVideoField(verbose_name="الإجابة الفيديو", blank=True, null=True)
    image_answer = models.ImageField(upload_to='faq_images/', verbose_name="الإجابة الصورة", blank=True, null=True)
    answered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='faq_answers', verbose_name="أجاب عليه")

    class Meta:
        verbose_name = "سؤال شائع"
        verbose_name_plural = "الأسئلة الشائعة"
        ordering = ['-created_at']

    def __str__(self):
        return self.question[:50] + '...' if len(self.question) > 50 else self.question


class Message(BaseModel):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages', verbose_name="المرسل")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages', verbose_name="المستلم")
    subject = models.CharField(max_length=255, verbose_name="الموضوع", blank=True, null=True)
    content = models.TextField(verbose_name="المحتوى")

    class Meta:
        verbose_name = "رسالة"
        verbose_name_plural = "الرسائل"
        ordering = ['-created_at']

    def __str__(self):
        return f"From {self.sender.username} to {self.recipient.username}: {self.subject or 'No Subject'}"
