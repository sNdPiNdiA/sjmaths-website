const quotes = [
    { text: "Education is the most powerful weapon which you can use to change the world.", author: "Nelson Mandela" },
    { text: "The beautiful thing about learning is that no one can take it away from you.", author: "B.B. King" },
    { text: "Mathematics is not about numbers, equations, computations, or algorithms: it is about understanding.", author: "William Paul Thurston" },
    { text: "Live as if you were to die tomorrow. Learn as if you were to live forever.", author: "Mahatma Gandhi" },
    { text: "The expert in anything was once a beginner.", author: "Helen Hayes" },
    { text: "Success is the sum of small efforts, repeated day in and day out.", author: "Robert Collier" },
    { text: "There is no substitute for hard work.", author: "Thomas Edison" },
    { text: "Strive for progress, not perfection.", author: "Unknown" },
    { text: "The only way to learn mathematics is to do mathematics.", author: "Paul Halmos" },
    { text: "Believe you can and you're halfway there.", author: "Theodore Roosevelt" },
    { text: "Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.", author: "Albert Einstein" },
    { text: "Failure is the opportunity to begin again more intelligently.", author: "Henry Ford" },
    { text: "Education is not the filling of a pail, but the lighting of a fire.", author: "W.B. Yeats" },
    { text: "Pure mathematics is, in its way, the poetry of logical ideas.", author: "Albert Einstein" }
];

export function initDailyQuote() {
    const container = document.getElementById('daily-quote-container');
    if (!container) return;

    // 1. Calculate Day of Year (0-365)
    const now = new Date();
    const start = new Date(now.getFullYear(), 0, 0);
    const diff = now - start;
    const oneDay = 1000 * 60 * 60 * 24;
    const dayOfYear = Math.floor(diff / oneDay);

    // 2. Select Quote (Modulo ensures it loops back to start after list ends)
    const quoteIndex = dayOfYear % quotes.length;
    const quote = quotes[quoteIndex];

    // 3. Render
    container.innerHTML = `
        <div class="quote-icon"><i class="fas fa-quote-left"></i></div>
        <div class="quote-content">
            <blockquote>"${quote.text}"</blockquote>
            <cite>- ${quote.author}</cite>
        </div>
        <div class="quote-decoration"></div>
    `;

    // Optional: Add fade-in effect
    container.style.opacity = 0;
    requestAnimationFrame(() => {
        container.style.transition = 'opacity 0.8s ease';
        container.style.opacity = 1;
    });
}