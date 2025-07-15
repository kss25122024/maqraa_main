function updateSurahOptions(selectElement) {
    const taskValue = selectElement.value;
    const surahMapping = {
        '1': ["الفاتحة", "الناس", "الفلق", "الإخلاص", "المسد", "النصر", "الكافرون", "الكوثر", "الماعون", "قريش", "الفيل", "الهمزة", "العصر", "التكاثر", "القارعة", "العاديات", "الزلزلة", "البينة", "القدر", "العلق", "التين", "الشرح", "الضحى", "الليل", "الشمس", "البلد", "الفجر", "الغاشية", "الأعلى", "الطارق", "البروج", "الإنشقاق", "المطففين", "الانفطار", "التكوير", "عبس", "النازعات", "النبأ"],
        '2': ["المرسلات", "الإنسان", "القيامة", "المدثر", "المزمل", "الجن", "نوح", "المعارج", "الحاقة", "القلم", "الملك", "التحريم", "الطلاق", "التغابن", "المنافقون", "الجمعة", "الصف", "الممتحنة", "الحشر", "المجادلة"],
        '3': ["الحديد", "الواقعة", "الرحمن", "القمر", "النجم", "الطور", "الذاريات", "ق", "الحجرات", "الفتح", "محمد", "الأحقاف"],
        '4': ["الجاثية", "الدخان", "الزخرف", "الشورى", "فصلت", "غافر", "الزمر", "ص", "الصافات", "يس", "فاطر", "سبأ", "الأحزاب", "السجدة", "لقمان", "الروم"],
        '5': ["العنكبوت", "القصص", "النمل", "الشعراء", "الفرقان", "النور", "المؤمنون", "الحج", "الأنبياء", "طه", "مريم"],
        '6': ["الكهف", "الإسراء", "النحل", "الحجر", "إبراهيم", "الرعد", "يوسف", "هود", "يونس"],
        '7': ["التوبة", "الأنفال", "الأعراف", "الأنعام", "المائدة", "النساء", "آل عمران", "البقرة"]
    };

    const ayahMapping = {
        "الفاتحة": 7, "البقرة": 286, "آل عمران": 200, "النساء": 176, "المائدة": 120, "الأنعام": 165, "الأعراف": 206, "الأنفال": 75, "التوبة": 129, "يونس": 109, "هود": 123, "يوسف": 111, "الرعد": 43, "إبراهيم": 52, "الحجر": 99, "النحل": 128, "الإسراء": 111, "الكهف": 110, "مريم": 98, "طه": 135, "الأنبياء": 112, "الحج": 78, "المؤمنون": 118, "النور": 64, "الفرقان": 77, "الشعراء": 227, "النمل": 93, "القصص": 88, "العنكبوت": 69, "الروم": 60, "لقمان": 34, "السجدة": 30, "الأحزاب": 73, "سبأ": 54, "فاطر": 45, "يس": 83, "الصافات": 182, "ص": 88, "الزمر": 75, "غافر": 85, "فصلت": 54, "الشورى": 53, "الزخرف": 89, "الدخان": 59, "الجاثية": 37, "الأحقاف": 35, "محمد": 38, "الفتح": 29, "الحجرات": 18, "ق": 45, "الذاريات": 60, "الطور": 49, "النجم": 62, "القمر": 55, "الرحمن": 78, "الواقعة": 96, "الحديد": 29, "المجادلة": 22, "الحشر": 24, "الممتحنة": 13, "الصف": 14, "الجمعة": 11, "المنافقون": 11, "التغابن": 18, "الطلاق": 12, "التحريم": 12, "الملك": 30, "القلم": 52, "الحاقة": 52, "المعارج": 44, "نوح": 28, "الجن": 28, "المزمل": 20, "المدثر": 56, "القيامة": 40, "الإنسان": 31, "المرسلات": 50, "النبأ": 40, "النازعات": 46, "عبس": 42, "التكوير": 29, "الانفطار": 19, "المطففين": 36, "الانشقاق": 25, "البروج": 22, "الطارق": 17, "الأعلى": 19, "الغاشية": 26, "الفجر": 30, "البلد": 20, "الشمس": 15, "الليل": 21, "الضحى": 11, "الشرح": 8, "التين": 8, "العلق": 19, "القدر": 5, "البينة": 8, "الزلزلة": 8, "العاديات": 11, "القارعة": 11, "التكاثر": 8, "العصر": 3, "الهمزة": 9, "الفيل": 5, "قريش": 4, "الماعون": 7, "الكوثر": 3, "الكافرون": 6, "النصر": 3, "المسد": 5, "الإخلاص": 4, "الفلق": 5, "الناس": 6
    };

    const previousSurahSelect = document.getElementById('id_previous_surah');
    const currentSurahSelect = document.getElementById('id_current_surah');
    const previousAyatSelect = document.getElementById('id_previous_ayat');
    const currentAyatSelect = document.getElementById('id_current_ayat');

    // Clear current options
    previousSurahSelect.innerHTML = '';
    currentSurahSelect.innerHTML = '';
    previousAyatSelect.innerHTML = '';
    currentAyatSelect.innerHTML = '';

    // Populate new options for surahs
    const surahs = surahMapping[taskValue] || [];
    surahs.forEach((surah) => {
        const option = new Option(surah, surah);
        previousSurahSelect.add(option);
        currentSurahSelect.add(new Option(surah, surah));
    });

    // Populate new options for ayats based on selected surah
    function updateAyatOptions(surahSelect, ayatSelect) {
        const surah = surahSelect.value;
        const ayatCount = ayahMapping[surah] || 1;
        ayatSelect.innerHTML = '';
        for (let i = 1; i <= ayatCount; i++) {
            ayatSelect.add(new Option(i, i));
        }
    }

    previousSurahSelect.addEventListener('change', function() {
        updateAyatOptions(previousSurahSelect, previousAyatSelect);
    });

    currentSurahSelect.addEventListener('change', function() {
        updateAyatOptions(currentSurahSelect, currentAyatSelect);
    });
}

function saveData() {
    const form = document.querySelector('form');
    form.submit();
}
