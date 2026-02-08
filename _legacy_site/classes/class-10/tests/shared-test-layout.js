(function () {
    const config = window.testConfig || {
        title: 'Test',
        subtitle: '',
        time: 'N/A',
        marks: 'N/A',
        backLink: '../../index.html',
        backText: 'Class 10 Home',
        instructions: []
    };

    const headerHTML = `
    <header class="header">
        <div class="container">
            <div class="header-nav-bar">
                <a href="${config.backLink}" class="back-link">
                    <i class="fas fa-arrow-left"></i> ${config.backText}
                </a>
            </div>
            <div class="exam-header-details">
                <h1>${config.title}</h1>
                <h2>${config.subtitle}</h2>
                <div class="exam-meta">
                    <p><strong>Time:</strong> ${config.time}</p>
                    <p><strong>Max. Marks:</strong> ${config.marks}</p>
                </div>
            </div>
        </div>
    </header>`;

    const footerHTML = `
    <footer class="footer">
        <div class="container">
            <p>&copy; 2026 SJMaths. All rights reserved.</p>
            <p><a href="${config.backLink}">Back to Dashboard</a></p>
        </div>
    </footer>`;

    // Inject Header immediately at the start of body
    document.body.insertAdjacentHTML('afterbegin', headerHTML);

    const initLayout = () => {
        // Inject Footer after main content
        const main = document.querySelector('main');
        if (main) {
            main.insertAdjacentHTML('afterend', footerHTML);
        } else {
            document.body.insertAdjacentHTML('beforeend', footerHTML);
        }

        // Inject Instructions if present
        if (config.instructions && config.instructions.length > 0) {
            const firstSection = document.querySelector('.question-section');
            if (firstSection && !firstSection.querySelector('.general-instructions')) {
                const listItems = config.instructions.map(item => `<li>${item}</li>`).join('');
                const instructionsHTML = `
                    <div class="general-instructions">
                        <h4>General Instructions:</h4>
                        <ul>
                            ${listItems}
                        </ul>
                    </div>
                `;
                firstSection.insertAdjacentHTML('afterbegin', instructionsHTML);
            }
        }
    };

    // Wait for DOM to be ready before injecting footer and instructions
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initLayout);
    } else {
        initLayout();
    }
})();