document.addEventListener('DOMContentLoaded', () => {
    const guessInput = document.getElementById('guess-input');
    guessInput.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
            makeGuess();
        }
    });
});
function makeGuess() {
    const guessInput = document.getElementById('guess-input');
    const feedback = document.getElementById('feedback');
    const userGuess = guessInput.value;

    fetch('/guess', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `guess=${userGuess}`,
    })
    .then(response => response.json())
    .then(data => {
        feedback.textContent = data.feedback;
        feedback.classList.remove('fade-in'); 
        void feedback.offsetWidth; 
        feedback.classList.add('fade-in'); 
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
