document.addEventListener('DOMContentLoaded', function() {
    const memorizationTaskField = document.getElementById('id_MemorizationTask');
    const previousSurahField = document.getElementById('id_previous_surah');
    const currentSurahField = document.getElementById('id_current_surah');

    const surahMapping = {
        1: ["الفاتحة", "الناس", "الفلق", "الإخلاص", "المسد", "النصر", "الكافرون", "الكوثر", "الماعون", "قريش", "الفيل", "الهمزة", "العصر", "التكاثر", "القارعة", "العاديات", "الزلزلة", "البينة", "القدر", "العلق", "التين", "الشرح", "الضحى", "الليل", "الشمس", "البلد", "الفجر", "الغاشية", "الأعلى", "الطارق", "البروج", "الإنشقاق", "المطففين", "الانفطار", "التكوير", "عبس", "النازعات", "النبأ"],
        2: ["المرسلات", "الإنسان", "القيامة", "المدثر", "المزمل", "الجن", "نوح", "المعارج", "الحاقة", "القلم", "الملك", "التحريم", "الطلاق", "التغابن", "المنافقون", "الجمعة", "الصف", "الممتحنة", "الحشر", "المجادلة"],
        3: ["الحديد", "الواقعة", "الرحمن", "القمر", "النجم", "الطور", "الذاريات", "ق", "الحجرات", "الفتح", "محمد", "الأحقاف"],
        4: ["الجاثية", "الدخان", "الزخرف", "الشورى", "فصلت", "غافر", "الزمر", "ص", "الصافات", "يس", "فاطر", "سبأ", "الأحزاب", "السجدة", "لقمان", "الروم"],
        5: ["العنكبوت", "القصص", "النمل", "الشعراء", "الفرقان", "النور", "المؤمنون", "الحج", "الأنبياء", "طه", "مريم"],
        6: ["الكهف", "الإسراء", "النحل", "الحجر", "إبراهيم", "الرعد", "يوسف", "هود", "يونس"],
        7: ["التوبة", "الأنفال", "الأعراف", "الأنعام", "المائدة", "النساء", "آل عمران", "البقرة"]
    };

    function updateSurahOptions(task) {
        const options = surahMapping[task] || [];
        previousSurahField.innerHTML = '';
        currentSurahField.innerHTML = '';

        options.forEach(function(surah) {
            const option1 = document.createElement('option');
            option1.value = surah;
            option1.textContent = surah;
            previousSurahField.appendChild(option1);

            const option2 = document.createElement('option');
            option2.value = surah;
            option2.textContent = surah;
            currentSurahField.appendChild(option2);
        });
    }

    memorizationTaskField.addEventListener('change', function() {
        updateSurahOptions(this.value);
    });

    // تحديث الخيارات عند تحميل الصفحة إذا كان هناك قيمة مختارة بالفعل
    if (memorizationTaskField.value) {
        updateSurahOptions(memorizationTaskField.value);
    }
});
