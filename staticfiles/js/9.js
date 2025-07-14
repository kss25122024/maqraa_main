

    const categorySurahs = {
        "المبتدئين": ["الفاتحة", "الناس", "الفلق", "الإخلاص", "المسد", "النصر", "الكافرون", "الكوثر", "الماعون", "قريش", "الفيل", "الهمزة", "العصر", "التكاثر", "القارعة", "العاديات", "الزلزلة", "البينة", "القدر", "العلق", "التين", "الشرح", "الضحى", "الليل", "الشمس", "البلد", "الفجر", "الغاشية", "الأعلى", "الطارق", "البروج", "الإنشقاق", "المطففين", "الانفطار", "التكوير", "عبس", "النازعات", "النبأ"],
        "ثلاثة أجزاء": ["المرسلات", "الإنسان", "القيامة", "المدثر", "المزمل", "الجن", "نوح", "المعارج", "الحاقة", "القلم", "الملك", "التحريم", "الطلاق", "التغابن", "المنافقون", "الجمعة", "الصف", "الممتحنة", "الحشر", "المجادلة"],
        "خمسة أجزاء": ["الحديد", "الواقعة", "الرحمن", "القمر", "النجم", "الطور", "الذاريات", "ق", "الحجرات", "الفتح", "محمد", "الأحقاف"],
        "عشرة أجزاء": ["الجاثية", "الدخان", "الزخرف", "الشورى", "فصلت", "غافر", "الزمر", "ص", "الصافات", "يس", "فاطر", "سبأ", "الأحزاب", "السجدة", "لقمان", "الروم"],
        "خمسة عشر جزء": ["العنكبوت", "القصص", "النمل", "الشعراء", "الفرقان", "النور", "المؤمنون", "الحج", "الأنبياء", "طه", "مريم"],
        "عشرون جزء": ["الكهف", "الإسراء", "النحل", "الحجر", "إبراهيم", "الرعد", "يوسف", "هود", "يونس"],
        "خمسة وعشرون جزء": ["التوبة", "الأنفال", "الأعراف", "الأنعام", "المائدة", "النساء", "آل عمران", "البقرة"]
    };
    
    const surahAyatCounts = {
        // أضف باقي السور وعدد آياتها هنا
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
        "الناس": 6
        
        // ...
    };
    
    function updateSurahOptions(categorySelect, rowIndex) {
        const category = categorySelect.value;
        const surahSelect = document.getElementById(`surah-options-${rowIndex}`);
        surahSelect.innerHTML = "";
    
        categorySurahs[category].forEach(surah => {
            const option = document.createElement("option");
            option.value = surah;
            option.text = surah;
            surahSelect.appendChild(option);
        });
    
        // تحديث خيارات الآيات لأول سورة في الفئة
        updateAyatOptions(surahSelect, rowIndex);
    }
    
    function updateAyatOptions(surahSelect, rowIndex) {
        const surah = surahSelect.value;
        const ayatCount = surahAyatCounts[surah];
        const ayatSelect = document.getElementById(`ayat-options-${rowIndex}`);
        ayatSelect.innerHTML = "";
    
        for (let i = 1; i <= ayatCount; i++) {
            const option = document.createElement("option");
            option.value = i;
            option.text = i;
            ayatSelect.appendChild(option);
        }
    }
    
    function saveMemorizationTask() {
        const memorizationTask = {
            category: document.getElementById("category-select").value,
            previous_surah: document.getElementById("previous-surah").value,
            previous_ayat: document.getElementById("previous-ayat").value,
            current_surah: document.getElementById("current-surah").value,
            current_ayat: document.getElementById("current-ayat").value,
            pages: document.getElementById("pages").value,
            partial_page: document.getElementById("partial-page").value,
            grade: document.getElementById("grade").value,
            memorized_ayat_count: document.getElementById("memorized-ayat-count").value
        };
    
        fetch("/save-memorization-task/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: JSON.stringify(memorizationTask)
        }).then(response => {
            if (response.ok) {
                alert("تم حفظ المهمة بنجاح!");
            } else {
                alert("حدث خطأ أثناء حفظ المهمة.");
            }
        }).catch(error => {
            console.error("Error:", error);
            alert("حدث خطأ أثناء حفظ المهمة.");
        });
    }
    
    // وظيفة للحصول على CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + "=")) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    // تهيئة الخيارات عند تحميل الصفحة
    document.addEventListener("DOMContentLoaded", function() {
        const categorySelects = document.querySelectorAll('select[onchange^="updateSurahOptions"]');
        categorySelects.forEach((select, index) => {
            updateSurahOptions(select, index);
        });
    
        // تعيين القيم الأولية للخيارات السابقة والحالية
        const previousSurahSelect = document.getElementById("previous-surah");
        const currentSurahSelect = document.getElementById("current-surah");
    
        previousSurahSelect.addEventListener("change", function() {
            memorizationTask.previous_surah = previousSurahSelect.value;
            checkSurahCategory();
        });
    
        currentSurahSelect.addEventListener("change", function() {
            memorizationTask.current_surah = currentSurahSelect.value;
            checkSurahCategory();
        });
    
        // تعيين القيمة الأولية لفئة الحفظ
        const categorySelect = document.getElementById("category-select");
        categorySelect.addEventListener("change", function() {
            memorizationTask.category = categorySelect.value;
            const surahSelects = document.querySelectorAll('select[onchange^="updateSurahOptions"]');
            surahSelects.forEach((select, index) => {
                updateSurahOptions(categorySelect, index);
            });
        });
    
        // حفظ المهمة عند الضغط على الزر
        const saveButton = document.getElementById("save-button");
        saveButton.addEventListener("click", function() {
            saveMemorizationTask();
        });
    });
    