import re
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.forms import MultiWidget, TextInput, Select
from phonenumbers import parse, is_valid_number, NumberParseException
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import Group # Import Group model
from .models import Students, Teachers, TypeRead, Department, Halaqa, StudentTask, Msar, DailyMemorizationTask, DailyReviewTask, DailyTalqeenTask, WeeklyPlan, WeeklyLecture, UserRole, Supervisor, Language, StudentLink # Import StudentLink

class ListAwarePhoneNumberField(PhoneNumberField):
    def to_python(self, value):
        if isinstance(value, list):
            # Join the list elements into a single string
            value = ''.join(value)
        # Call the parent class's to_python with the potentially modified value
        return super().to_python(value)



class LoginForm(AuthenticationForm):
    username = forms.CharField(label="الايميل", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="كلمة المرور")

TYPE_REGISTER_OPTIONS = [
    ("1", " بمكافأة "),
    ("2", " محتسب"),
    # Add any additional options needed
]
KEY_CONTRY=[
    ('+967', 'اليمن'),
    ('+966', 'المملكة العربية السعودية'),
    ('+1', 'الولايات المتحدة'),
    ('+1-CA', 'كندا'),
    ('+33', 'فرنسا'),
    ('+971', 'الإمارات العربية المتحدة'),
    ('+20', 'مصر'),
    ('+44', 'المملكة المتحدة'),
    ('+49', 'ألمانيا'),
    ('+965', 'الكويت'),
    ('+974', 'قطر'),
    ('+973', 'البحرين'),
    ('+968', 'عمان'),
    ('+962', 'الأردن'),
    ('+963', 'سوريا'),
    ('+961', 'لبنان'),
    ('+218', 'ليبيا'),
    ('+249', 'السودان'),
    ('+213', 'الجزائر'),
    ('+212', 'المغرب'),
    ('+216', 'تونس'),
    ('+964', 'العراق'),
    ('+970', 'فلسطين'),
    ('+222', 'موريتانيا'),
    ('+252', 'الصومال'),
    ('+55', 'البرازيل'),
    ('+54', 'الأرجنتين'),
    ('+91', 'الهند'),
    ('+86', 'الصين'),
    ('+7', 'روسيا'),
    ('+39', 'إيطاليا'),
    ('+34', 'إسبانيا'),
    ('+61', 'أستراليا'),
    ('+234', 'نيجيريا'),
    ('+81', 'اليابان'),
    ('+82', 'كوريا الجنوبية'),
    ('+27', 'جنوب أفريقيا'),
    ('+52', 'المكسيك'),
    ('+62', 'إندونيسيا'),
    ('+92', 'باكستان'),
    ('+46', 'السويد'),
    ('+47', 'النرويج'),
    ('+358', 'فنلندا'),
    ('+45', 'الدنمارك'),
    ('+48', 'بولندا'),
    ('+420', 'التشيك'),
    ('+351', 'البرتغال'),
    ('+30', 'اليونان'),
    ('+36', 'هنغاريا'),
    ('+90', 'تركيا'),
    ('+40', 'رومانيا'),
    ('+359', 'بلغاريا'),
    ('+381', 'صربيا'),
    ('+385', 'كرواتيا'),
    ('+421', 'سلوفاكيا'),
    ('+386', 'سلوفينيا'),
    ('+43', 'النمسا'),
    ('+32', 'بلجيكا'),
    ('+41', 'سويسرا'),
    ('+31', 'هولندا'),
    ('+372', 'إستونيا'),
    ('+371', 'لاتفيا'),
    ('+370', 'ليتوانيا'),
    ('+373', 'مولدوفا'),
    ('+375', 'روسيا البيضاء'),
    ('+380', 'أوكرانيا'),
    ('+84', 'فيتنام'),
    ('+60', 'ماليزيا'),
    ('+63', 'الفلبين'),
    ('+65', 'سنغافورة'),
    ('+66', 'تايلاند'),
    ('+855', 'كمبوديا'),
    ('+856', 'لاوس'),
    ('+976', 'منغوليا'),
    ('+850', 'كوريا الشمالية'),
]

COUNTRIES = [
    ('ye', 'اليمن'),
    ('sa', 'السعودية'),
    ('eg', 'مصر'),
    ('ae', 'الإمارات'),
    ('kw', 'الكويت'),
    ('qa', 'قطر'),
    ('bh', 'البحرين'),
    ('om', 'عمان'),
    
    ('jo', 'الأردن'),
    ('sy', 'سوريا'),
    ('lb', 'لبنان'),
    ('ly', 'ليبيا'),
    ('sd', 'السودان'),
    ('dz', 'الجزائر'),
    ('ma', 'المغرب'),
    ('tn', 'تونس'),
    ('iq', 'العراق'),
    ('ps', 'فلسطين'),
    ('kw', 'الكويت'),
    ('mr', 'موريتانيا'),
    ('bh', 'البحرين'),
    ('so', 'الصومال'),
    ('ae', 'الإمارات العربية المتحدة'),
    ('dz', 'الجزائر'),
    ('br', 'البرازيل'),
    ('ar', 'الأرجنتين'),
    ('fr', 'فرنسا'),
    ('it', 'إيطاليا'),
    ('se', 'السويد'),
    ('no', 'النرويج'),
    ('fi', 'فنلندا'),
    ('dk', 'الدنمارك'),
    ('pl', 'بولندا'),
    ('cz', 'التشيك'),
    ('pt', 'البرتغال'),
    ('gr', 'اليونان'),
    ('hu', 'هنغاريا'),
    ('tr', 'تركيا'),
    ('ro', 'رومانيا'),
    ('bg', 'بلغاريا'),
    ('rs', 'صربيا'),
    ('hr', 'كرواتيا'),
    ('sk', 'سلوفاكيا'),
    ('si', 'سلوفينيا'),
    ('at', 'النمسا'),
    ('be', 'بلجيكا'),
    ('ch', 'سويسرا'),
    ('nl', 'هولندا'),
    ('ee', 'إستونيا'),
    ('lv', 'لاتفيا'),
    ('lt', 'ليتوانيا'),
    ('md', 'مولدوفا'),
    ('by', 'روسيا البيضاء'),
    ('ua', 'أوكرانيا'),
    ('bg', 'بلغاريا'),
    ('ae', 'الإمارات'),
    ('cn', 'الصين'),
    ('vn', 'فيتنام'),
    ('my', 'ماليزيا'),
    ('ph', 'الفلبين'),
    ('sg', 'سنغافورة'),
    ('th', 'تايلاند'),
    ('id', 'إندونيسيا'),
    ('kh', 'كمبوديا'),
    ('la', 'لاوس'),
    ('mn', 'منغوليا'),
    ('kp', 'كوريا الشمالية'),
]

GENDER_CHOICES = [
    ('male', 'ذكر'),
    ('female', 'انثى'),
]




NATIVE_LANGUAGE_NAMES = {
    'العربية': 'العربية',
    'English': 'English',
    'Français': 'Français',
    'Español': 'Español',
    'Deutsch': 'Deutsch',
    '中文': '中文',
    'Русский': 'Русский',
    'Português': 'Português',
    'Italiano': 'Italiano',
    '한국어': '한국어',
    '日本語': '日本語',
    'Türkçe': 'Türkçe',
    'اردو': 'اردو',
    'বাংলা': 'বাংলা',
    'हिन्दी': 'हिन्दी',
    # Add more languages as needed
}


class TeacherForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'تأكيد كلمة المرور'}),
        label="تأكيد كلمة المرور"
    )

    nationality = forms.ChoiceField(
        choices=COUNTRIES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="الجنسية"
    )
    

    mobile = ListAwarePhoneNumberField(
        widget=PhoneNumberPrefixWidget(widgets=[Select(choices=KEY_CONTRY), TextInput()]),
        label="رقم الجوال",
        initial='+967' # Set initial value with Yemen country code
    )
    mobile_whatsapp = ListAwarePhoneNumberField(
        widget=PhoneNumberPrefixWidget(widgets=[Select(choices=KEY_CONTRY), TextInput()]),
        label="رقم الواتس",
        initial='+967' # Set initial value with Yemen country code
    )

    # Define language field as ModelChoiceField for single select dropdown
    language = forms.ModelChoiceField(
        queryset=Language.objects.all(), # Initial queryset, will be ordered in __init__
        widget=forms.Select(attrs={'class': 'form-select'}), # Use Select widget
        label="اللغة التي تعرفها", # Changed label to singular
        required=False, # Make it optional
        empty_label="-- اختر لغة --" # Add an empty choice
    )

    class Meta:
        model = Teachers
        fields = [
            'first_name',
            'second_name',
            'last_name',
            'email', # Made optional as per user feedback
            'mobile',
            'mobile_whatsapp',
            'gender',
            'birthday',
            'nationality',
            'country',
            'certificates',
            'language', # Added back for dropdown
            'password',
            'confirm_password',
            'career_path',
            'cv_teacher',
            'username',
            'activate',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'الاسم الأول'}),
            'second_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'الاسم الثاني'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اللقب'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'البريد الإلكتروني', 'required': False}), # Made optional
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'كلمة المرور'}),
            'birthday': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'career_path': forms.Select(attrs={'class': 'form-select'}),
            'cv_teacher': forms.FileInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم المستخدم'}),
            'activate': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Get all languages ordered by name
        all_languages = list(Language.objects.all().order_by('name'))

        # Build the choices list using native names
        language_choices = [('', self.fields['language'].empty_label)]
        for lang in all_languages:
            language_choices.append((lang.id, NATIVE_LANGUAGE_NAMES.get(lang.name, lang.name)))

        # Set the choices for the language field
        self.fields['language'].choices = language_choices


    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("كلمة المرور يجب أن تكون على الأقل 8 أحرف")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        # Add back password matching validation
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("كلمات المرور غير متطابقة!")

        # Keep the password length validation
        if password and len(password) < 8:
             self.add_error('password', "كلمة المرور يجب أن تكون على الأقل 8 أحرف")

        

        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Teachers.objects.filter(username=username).exists():
            raise forms.ValidationError("اسم المستخدم محجوز!")
        return username

    # Removed the separate clean_mobile and clean_mobile_whatsapp methods

    def save(self, commit=True):
        # Create the Teacher instance but don't save yet
        teacher = super().save(commit=False)

        # Handle the language ManyToManyField if commit is True
        if commit:
            # Ensure the instance is saved to the database before setting ManyToMany fields
            # This save will happen in the view after assigning the user
            # teacher.save() # Removed this line

            selected_language = self.cleaned_data.get('language')
            if selected_language:
                # Set the selected language
                teacher.language.set([selected_language])
            else:
                # If no language is selected, default to Arabic
                try:
                    arabic_language = Language.objects.get(name='العربية')
                    teacher.language.set([arabic_language])
                except Language.DoesNotExist:
                    # Handle case where Arabic language is not in the database
                    teacher.language.set([]) # Set to empty if Arabic not found

            self.save_m2m() # Save ManyToMany data

        return teacher




class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']
        labels = {
            'name': 'اسم القسم',
        }

class TypeReadForm(forms.ModelForm):
    class Meta:
        model = TypeRead
        fields = ['name', 'msar']
        labels = {
            'name': 'نوع القراءة',
            'msar': 'المسار',
        }




class MsarForm(forms.ModelForm):
    class Meta:
        model = Msar
        fields = ['name', 'department']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
        }



class HalaqaForm(forms.ModelForm):
    class Meta:
        model = Halaqa
        fields = ['name', 'level', 'type_class', 'count', 'start_time', 'end_time', 'teacher', 'department', 'msar', 'activate']
        labels = {
            'name': 'اسم الحلقة',
            'level': 'مستوى الحلقة',
            'type_class': 'نوع القراءة',
            'count': 'الطاقة الاستيعابية للحلقة',
            'start_time': 'وقت بداية الحلقة',
            'end_time': 'وقت نهاية الحلقة',
            'teacher': 'الأستاذ',
            'department': 'القسم',
            'msar': 'المسار',
            'activate': 'تفعيل',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.TextInput(attrs={'class': 'form-control'}),
            'type_class': forms.Select(attrs={'class': 'form-control'}),
            'count': forms.NumberInput(attrs={'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control'}),
            'teacher': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'msar': forms.Select(attrs={'class': 'form-control'}),
            'activate': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        msar = cleaned_data.get('msar')

        if name and msar:
            # Check if a Halaqa with the same name and msar already exists
            # Exclude the current instance if updating
            qs = Halaqa.objects.filter(name=name, msar=msar)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)

            if qs.exists():
                raise forms.ValidationError("اسم الحلقة موجود بالفعل في هذا المسار.")

        return cleaned_data




from django import forms
from django.contrib.auth.models import User
from .models import Students
from django import forms
from .models import Students
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.forms import MultiWidget, TextInput, Select
from .models import Language # Import Language model

class StudentForm(forms.ModelForm):
    # Define mobile and whatsapp as PhoneNumberFields
    mobile = ListAwarePhoneNumberField(
        label="رقم الجوال",
        required=False, # Make it optional if needed
        initial='+967' # Set initial value with Yemen country code
        # Widget is defined in Meta class
    )
    whatsapp = PhoneNumberField(
        label="رقم الواتس",
        required=False, # Make it optional if needed
        initial='+967' # Set initial value with Yemen country code
        # Widget is defined in Meta class
    )

    # Define language field as ModelChoiceField for single select dropdown
    language = forms.ModelChoiceField(
        queryset=Language.objects.all().order_by('name'), # Order languages alphabetically
        widget=forms.Select(attrs={'class': 'form-select'}), # Use Select widget
        label="اللغة التي تعرفها",
        required=False, # Make it optional
        empty_label="-- اختر لغة --" # Add an empty choice
    )

    # Add confirm_password field back for validation
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'تأكيد كلمة المرور'}),
        label="تأكيد كلمة المرور"
    )


    class Meta:
        model = Students
        fields = [
            'first_name', 'second_name', 'last_name', 'birthday',
            'nationality', 'gender', 'email', 'language',
            'mobile', 'whatsapp', 'username', 'password',
            'group', 'activate', 'halaqa' # Added group, activate, and halaqa fields
        ]
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'second_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            # Assign PhoneNumberPrefixWidget to mobile and whatsapp
            'mobile': PhoneNumberPrefixWidget(widgets=[Select(choices=KEY_CONTRY), TextInput()]),
            'whatsapp': PhoneNumberPrefixWidget(widgets=[Select(choices=KEY_CONTRY), TextInput()]),
        }
    
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="الجنس"
    )

    nationality = forms.ChoiceField(
        choices=COUNTRIES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="الجنسية"
    )

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("كلمة المرور يجب أن تكون على الأقل 8 أحرف")
        return password

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Get all languages ordered by name
        all_languages = list(Language.objects.all().order_by('name'))

        # Build the choices list using native names
        language_choices = [('', self.fields['language'].empty_label)]
        for lang in all_languages:
            language_choices.append((lang.id, NATIVE_LANGUAGE_NAMES.get(lang.name, lang.name)))

        # Set the choices for the language field
        self.fields['language'].choices = language_choices

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        # Add back password matching validation
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("كلمات المرور غير متطابقة!")

        # Keep the password length validation (already in clean_password, but good to have here too)
        if password and len(password) < 8:
             self.add_error('password', "كلمة المرور يجب أن تكون على الأقل 8 أحرف")

        # The mobile and whatsapp fields are now cleaned in clean_mobile and clean_whatsapp


        return cleaned_data

    def save(self, commit=True):
        # Create the Student instance but don't save yet
        student = super().save(commit=False)

        # Handle the language ForeignKey
        selected_language = self.cleaned_data.get('language')
        if selected_language:
            student.language = selected_language
        else:
             # If no language is selected, default to Arabic (adjust if 'العربية' is not a valid Language object)
             try:
                 arabic_language = Language.objects.get(name='العربية')
                 student.language = arabic_language
             except Language.DoesNotExist:
                 # Handle case where Arabic language is not in the database
                 student.language = None # Or set to a default if applicable
             
        # The mobile and whatsapp fields are now handled by clean_mobile and clean_whatsapp
        # Assign the cleaned PhoneNumber objects to the student instance
        student.mobile = self.cleaned_data.get('mobile')
        student.whatsapp = self.cleaned_data.get('whatsapp')

        # Save the student instance if commit is True
        if commit:
            student.save()

        return student


class StudentTaskForm(forms.ModelForm):
    class Meta:
        model = StudentTask
        fields = [
            'name',
            'student',
            'halaqa_name',
            'msar',
            'department',
            'week_start',
            'week_end',
            'week_number',
            'count_bage',
            'task_student',
            'category',
            'surah',
            'ayah',
            'ayah_number'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'student': forms.Select(attrs={'class': 'form-control'}),
            'halaqa_name': forms.TextInput(attrs={'class': 'form-control'}),
            'msar': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'week_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'week_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'week_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'count_bage': forms.NumberInput(attrs={'class': 'form-control'}),
            'task_student': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control', 'onchange': 'updateSurahs()'}),
            'surah': forms.TextInput(attrs={'class': 'form-control', 'onchange': 'updateAyahs()'}),
            'ayah': forms.TextInput(attrs={'class': 'form-control'}),
            'ayah_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    class Media:
        js = ('js/6.js',)




class DailyMemorizationTaskForm(forms.ModelForm):
    class Meta:
        model = DailyMemorizationTask
        fields = [
            'student', 'MemorizationTask', 'previous_surah', 'previous_ayat',
            'current_surah', 'current_ayat', 'pages', 'partial_page', 'grade',
            'date', 'memorized_ayat_count'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'student': 'اسم الطالب',
            'MemorizationTask': 'فئة الحفظ',
            'previous_surah': 'السورة السابقة',
            'previous_ayat': 'الاية السابقة',
            'current_surah': 'السورة الحالية',
            'current_ayat': 'الاية الحالية',
            'pages': 'عدد الصفحات',
            'partial_page': 'أجزاء الصفحة',
            'grade': 'الدرجة',
            'date': 'التاريخ',
            'memorized_ayat_count': 'عدد الايات المحفوظة',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # تحديث الخيارات للحقل MemorizationTask
        self.fields['MemorizationTask'].widget.attrs.update({'onchange': 'updateSurahOptions(this)'})

        # الحصول على الفئة المختارة
        if 'MemorizationTask' in self.data:
            memorization_task = int(self.data.get('MemorizationTask'))
        elif self.instance.pk:
            memorization_task = self.instance.MemorizationTask
        else:
            memorization_task = None

        # تحديث خيارات السور بناءً على الفئة المختارة
        if memorization_task:
            surahs = DailyMemorizationTask.surah_mapping.get(memorization_task, [])
            surah_choices = [(surah, surah) for surah in surahs]
            self.fields['previous_surah'].choices = surah_choices
            self.fields['current_surah'].choices = surah_choices
        else:
            self.fields['previous_surah'].choices = []
            self.fields['current_surah'].choices = []

        # تحديث خيارات الآيات بناءً على السورة المختارة
        if 'previous_surah' in self.data:
            previous_surah = self.data.get('previous_surah')
            ayat_count = DailyMemorizationTask.ayah_mapping.get(previous_surah, 1)
            self.fields['previous_ayat'].choices = [(i, i) for i in range(1, ayat_count + 1)]
        elif self.instance.pk and self.instance.previous_surah:
            previous_surah = self.instance.previous_surah
            ayat_count = DailyMemorizationTask.ayah_mapping.get(previous_surah, 1)
            self.fields['previous_ayat'].choices = [(i, i) for i in range(1, ayat_count + 1)]
        else:
            self.fields['previous_ayat'].choices = []

        if 'current_surah' in self.data:
            current_surah = self.data.get('current_surah')
            ayat_count = DailyMemorizationTask.ayah_mapping.get(current_surah, 1)
            self.fields['current_ayat'].choices = [(i, i) for i in range(1, ayat_count + 1)]
        elif self.instance.pk and self.instance.current_surah:
            current_surah = self.instance.current_surah
            ayat_count = DailyMemorizationTask.ayah_mapping.get(current_surah, 1)
            self.fields['current_ayat'].choices = [(i, i) for i in range(1, ayat_count + 1)]
        else:
            self.fields['current_ayat'].choices = []

    class Media:
        js = ('static/js/7.js',)




# forms.py


from django import forms
from .models import DailyReviewTask

class DailyReviewTaskForm(forms.ModelForm):
    class Meta:
        model = DailyReviewTask
        fields = [
            'student', 'ReviewTask', 'previous_surah', 'previous_ayat',
            'current_surah', 'current_ayat', 'pages', 'partial_page', 'grade',
            'date', 'reviewed_ayat_count'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'student': 'اسم الطالب',
            'ReviewTask': 'فئة المراجعة',
            'previous_surah': 'السورة السابقة',
            'previous_ayat': 'الاية السابقة',
            'current_surah': 'السورة الحالية',
            'current_ayat': 'الاية الحالية',
            'pages': 'عدد الصفحات',
            'partial_page': 'أجزاء الصفحة',
            'grade': 'الدرجة',
            'date': 'التاريخ',
            'reviewed_ayat_count': 'عدد الايات المراجعة',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # تحديث الخيارات للحقل ReviewTask
        self.fields['ReviewTask'].widget.attrs.update({'onchange': 'updateSurahOptions(this)'})

        # الحصول على الفئة المختارة
        if 'ReviewTask' in self.data:
            review_task = int(self.data.get('ReviewTask'))
        elif self.instance.pk:
            review_task = self.instance.ReviewTask
        else:
            review_task = None

        # تحديث خيارات السور بناءً على الفئة المختارة
        if review_task:
            surahs = DailyReviewTask.surah_mapping.get(review_task, [])
            surah_choices = [(surah, surah) for surah in surahs]
            self.fields['previous_surah'].choices = surah_choices
            self.fields['current_surah'].choices = surah_choices
        else:
            self.fields['previous_surah'].choices = []
            self.fields['current_surah'].choices = []

        # تحديث خيارات الآيات بناءً على السورة المختارة
        if 'previous_surah' in self.data:
            previous_surah = self.data.get('previous_surah')
            ayat_count = DailyReviewTask.ayah_mapping.get(previous_surah, 1)
            self.fields['previous_ayat'].choices = [(i, i) for i in range(1, ayat_count + 1)]
        elif self.instance.pk and self.instance.previous_surah:
            previous_surah = self.instance.previous_surah
            ayat_count = DailyReviewTask.ayah_mapping.get(previous_surah, 1)
            self.fields['previous_ayat'].choices = [(i, i) for i in range(1, ayat_count + 1)]
        else:
            self.fields['previous_ayat'].choices = []

        if 'current_surah' in self.data:
            current_surah = self.data.get('current_surah')
            ayat_count = DailyReviewTask.ayah_mapping.get(current_surah, 1)
            self.fields['current_ayat'].choices = [(i, i) for i in range(1, ayat_count + 1)]
        elif self.instance.pk and self.instance.current_surah:
            current_surah = self.instance.current_surah
            ayat_count = DailyReviewTask.ayah_mapping.get(current_surah, 1)
            self.fields['current_ayat'].choices = [(i, i) for i in range(1, ayat_count + 1)]
        else:
            self.fields['current_ayat'].choices = []

    class Media:
        js = ('static/js/7.js',)




class DailyTalqeenTaskForm(forms.ModelForm):
    class Meta:
        model = DailyTalqeenTask
        fields = [
            'student', 'TalqeenTask', 'previous_surah', 'previous_ayat',
            'current_surah', 'current_ayat', 'pages', 'partial_page', 'grade',
            'date', 'Talqeen_ayat_count'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # تحديث الخيارات للحقل TalqeenTask
        self.fields['TalqeenTask'].widget.attrs.update({'onchange': 'updateSurahOptions(this)'})
        
        # الحصول على الفئة المختارة
        talqeen_task = None
        if 'TalqeenTask' in self.data:
            talqeen_task = int(self.data.get('TalqeenTask'))
        elif self.instance.pk:
            talqeen_task = self.instance.TalqeenTask

        # تحديث خيارات السور بناءً على الفئة المختارة
        if talqeen_task is not None:
            surahs = DailyTalqeenTask.surah_mapping.get(talqeen_task, [])
            surah_choices = [(surah, surah) for surah in surahs]
            self.fields['previous_surah'].choices = surah_choices
            self.fields['current_surah'].choices = surah_choices
        else:
            self.fields['previous_surah'].choices = []
            self.fields['current_surah'].choices = []

        # تحديث خيارات الآيات بناءً على السورة المختارة
        previous_surah = self.data.get('previous_surah') or self.instance.previous_surah
        if previous_surah:
            ayat_count = DailyTalqeenTask.ayah_mapping.get(previous_surah, 1)
            self.fields['previous_ayat'].choices = [(i, i) for i in range(1, ayat_count + 1)]
        else:
            self.fields['previous_ayat'].choices = []

        current_surah = self.data.get('current_surah') or self.instance.current_surah
        if current_surah:
            ayat_count = DailyTalqeenTask.ayah_mapping.get(current_surah, 1)
            self.fields['current_ayat'].choices = [(i, i) for i in range(1, ayat_count + 1)]
        else:
            self.fields['current_ayat'].choices = []

    class Media:
        js = ('static/js/7.js',)




class WeeklyPlanForm(forms.ModelForm):
    class Meta:
        model = WeeklyPlan
        # Remove 'student' from the fields list as it's handled by the view
        fields = [
            'memorization_task', 'memorization_previous_surah', 'memorization_previous_ayat',
            'memorization_current_surah', 'memorization_current_ayat',
            'review_task', 'review_previous_surah', 'review_previous_ayat',
            'review_current_surah', 'review_current_ayat',
            'talqeen_task', 'talqeen_previous_surah', 'talqeen_previous_ayat',
            'talqeen_current_surah', 'talqeen_current_ayat'
        ]
        labels = {
            'memorization_task': 'فئة الحفظ',
            'review_task': 'فئة المراجعة',
            'talqeen_task': 'فئة التلقين',
            'memorization_previous_surah': 'السورة السابقة (حفظ)',
            'memorization_previous_ayat': 'الآية السابقة (حفظ)',
            'memorization_current_surah': 'السورة الحالية (حفظ)',
            'memorization_current_ayat': 'الآية الحالية (حفظ)',
            'review_previous_surah': 'السورة السابقة (مراجعة)',
            'review_previous_ayat': 'الآية السابقة (مراجعة)',
            'review_current_surah': 'السورة الحالية (مراجعة)',
            'review_current_ayat': 'الآية الحالية (مراجعة)',
            'talqeen_previous_surah': 'السورة السابقة (تلقين)',
            'talqeen_previous_ayat': 'الآية السابقة (تلقين)',
            'talqeen_current_surah': 'السورة الحالية (تلقين)',
            'talqeen_current_ayat': 'الآية الحالية (تلقين)',
        }

    # Removed the __init__ method as 'student' is no longer in Meta.fields
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self.instance and self.instance.pk:
    #         self.fields.pop('student', None)
    #     else:
    #          self.fields['student'].required = True
    #          self.fields['student'].queryset = Students.objects.all()


class WeeklyLectureForm(forms.ModelForm):
    class Meta:
        model = WeeklyLecture
        fields = ['title', 'description', 'youtube_link']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'youtube_link': forms.TextInput(attrs={'class': 'form-control'}),  # استخدام TextInput لـ EmbedVideoField
        }


from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']



from django import forms
from .models import Admin

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['user', 'first_name', 'second_name', 'last_name', 'username']

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField(label="Select Excel File")

class StudentLinkForm(forms.ModelForm):
    class Meta:
        model = StudentLink
        fields = ['student', 'title', 'url']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'student': 'الطالب',
            'title': 'عنوان الرابط',
            'url': 'الرابط',
        }
