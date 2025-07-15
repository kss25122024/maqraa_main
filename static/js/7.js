function updateSurahOptions(selectElement) {
    const taskValue = selectElement.value;
    fetch(`/get_surahs?category=${taskValue}`)
        .then(response => response.json())
        .then(data => {
            const surahs = data.surahs || [];
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
            surahs.forEach((surah) => {
                previousSurahSelect.add(new Option(surah, surah));
                currentSurahSelect.add(new Option(surah, surah));
            });

            // Trigger change event to update ayat options
            previousSurahSelect.addEventListener('change', function() {
                updateAyatOptions(this, previousAyatSelect);
            });
            currentSurahSelect.addEventListener('change', function() {
                updateAyatOptions(this, currentAyatSelect);
            });

            updateAyatOptions(previousSurahSelect, previousAyatSelect);
            updateAyatOptions(currentSurahSelect, currentAyatSelect);
        });
}

function updateAyatOptions(surahSelect, ayatSelect) {
    const surah = surahSelect.value;
    fetch(`/get_ayahs?surah=${surah}`)
        .then(response => response.json())
        .then(data => {
            const ayahs = data.ayahs || [];
            ayatSelect.innerHTML = '';
            ayahs.forEach((ayah) => {
                ayatSelect.add(new Option(ayah, ayah));
            });
        });
}

function saveData() {
    const form = document.querySelector('form');
    form.submit();
}
