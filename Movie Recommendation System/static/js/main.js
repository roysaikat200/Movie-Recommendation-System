document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('movieSearch');
    const optionsContainer = document.querySelector('.options-container');
    const movieForm = document.getElementById('movieForm');
    const hiddenInput = document.getElementById('movie');
    const loadingSection = document.getElementById('loading');
    const options = Array.from(document.querySelectorAll('.option'));
    const flashMessages = document.querySelector('.flash-messages');
    let currentFocus = -1;

    // Function to filter movies based on search input
    function filterMovies(searchTerm) {
        return options.filter(option => 
            option.textContent.toLowerCase().includes(searchTerm.toLowerCase())
        );
    }

    // Function to display filtered options
    function showFilteredOptions(filteredOptions) {
        optionsContainer.innerHTML = '';
        filteredOptions.forEach(option => {
            optionsContainer.appendChild(option.cloneNode(true));
        });
        optionsContainer.classList.add('active');
    }

    // Handle search input
    searchInput.addEventListener('input', (e) => {
        const searchTerm = e.target.value;
        const filteredOptions = filterMovies(searchTerm);
        showFilteredOptions(filteredOptions);
        currentFocus = -1;
        
        // Clear any existing flash messages when user starts typing
        if (flashMessages) {
            flashMessages.innerHTML = '';
        }
    });

    // Handle keyboard navigation
    searchInput.addEventListener('keydown', (e) => {
        const activeOptions = optionsContainer.querySelectorAll('.option');
        if (e.key === 'ArrowDown') {
            currentFocus++;
            if (currentFocus >= activeOptions.length) currentFocus = 0;
            highlightOption(activeOptions);
            e.preventDefault();
        } else if (e.key === 'ArrowUp') {
            currentFocus--;
            if (currentFocus < 0) currentFocus = activeOptions.length - 1;
            highlightOption(activeOptions);
            e.preventDefault();
        } else if (e.key === 'Enter') {
            if (currentFocus > -1) {
                e.preventDefault();
                activeOptions[currentFocus].click();
            } else if (hiddenInput.value) {
                // If a movie is selected and Enter is pressed, submit the form
                e.preventDefault();
                const submitButton = movieForm.querySelector('button[type="submit"]');
                submitButton.click();
            }
        }
    });

    // Highlight selected option
    function highlightOption(options) {
        options.forEach(opt => opt.classList.remove('selected'));
        if (currentFocus > -1) {
            options[currentFocus].classList.add('selected');
            options[currentFocus].scrollIntoView({ block: 'nearest' });
        }
    }

    // Handle option selection
    optionsContainer.addEventListener('click', (e) => {
        if (e.target.classList.contains('option')) {
            const selectedText = e.target.textContent.trim();
            searchInput.value = selectedText;
            hiddenInput.value = selectedText;
            optionsContainer.classList.remove('active');
            
            // Clear any existing flash messages when option is selected
            if (flashMessages) {
                flashMessages.innerHTML = '';
            }
        }
    });

    // Close options container when clicking outside
    document.addEventListener('click', (e) => {
        if (!searchInput.contains(e.target) && !optionsContainer.contains(e.target)) {
            optionsContainer.classList.remove('active');
        }
    });

    // Show options container when focusing on search input
    searchInput.addEventListener('focus', () => {
        const filteredOptions = filterMovies(searchInput.value);
        showFilteredOptions(filteredOptions);
    });

    // Handle form submission
    movieForm.addEventListener('submit', (e) => {
        if (!hiddenInput.value) {
            e.preventDefault();
            return;
        }
        loadingSection.style.display = 'block';
        const recommendationsSection = document.querySelector('.recommendations-section');
        if (recommendationsSection) {
            recommendationsSection.classList.add('fade-out');
        }
    });
});