from django.core.management.base import BaseCommand
from maqraapp.models import Language

class Command(BaseCommand):
    help = 'Populates the database with a list of common languages.'

    def handle(self, *args, **options):
        languages = [
            'العربية',       # Arabic
            'English',      # English
            '普通话',       # Mandarin Chinese
            'हिन्दी',       # Hindi
            'Español',      # Spanish
            'Français',     # French
            'বাংলা',        # Bengali
            'Português',    # Portuguese
            'Русский',      # Russian
            '日本語',       # Japanese
            'Deutsch',      # German
            'Basa Jawa',    # Javanese
            '한국어',       # Korean
            'Türkçe',       # Turkish
            'Tiếng Việt',   # Vietnamese
            'Italiano',     # Italian
            'اردو',         # Urdu
            'فارسی',        # Persian
            'Bahasa Melayu',# Malay
            'Kiswahili',    # Swahili
            'Nederlands',   # Dutch
            'Ελληνικά',     # Greek
            'Svenska',      # Swedish
            'Norsk',        # Norwegian
            'Dansk',        # Danish
        ]

        self.stdout.write(self.style.SUCCESS('Adding languages to the database...'))

        for lang_name in languages:
            language, created = Language.objects.get_or_create(name=lang_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added language: {lang_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Language already exists: {lang_name}'))

        self.stdout.write(self.style.SUCCESS('Finished populating languages.'))