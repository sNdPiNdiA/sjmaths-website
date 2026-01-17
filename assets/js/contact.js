import { showToast } from './utils.js';

const contactForm = document.querySelector('form');

if (contactForm) {
    contactForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        
        const form = event.target;
        const submitBtn = form.querySelector('button[type="submit"]');
        const originalBtnText = submitBtn.innerHTML;

        // Disable button and show loading state
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';

        try {
            const formData = new FormData(form);
            const data = Object.fromEntries(formData.entries());

            const response = await fetch(form.action, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify(data)
            });

            if (response.ok) {
                showToast('Message sent successfully! We will get back to you soon.', 'success');
                form.reset();
            } else {
                const result = await response.json();
                if (result.errors) {
                    showToast(result.errors.map(error => error.message).join(', '), 'error');
                } else {
                    showToast('Oops! There was a problem submitting your form.', 'error');
                }
            }
        } catch (error) {
            console.error('Form submission error:', error);
            showToast('Network error. Please check your connection and try again.', 'error');
        } finally {
            // Restore button state
            submitBtn.disabled = false;
            submitBtn.innerHTML = originalBtnText;
        }
    });
}