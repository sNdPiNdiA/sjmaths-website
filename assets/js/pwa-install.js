// assets/js/pwa-install.js
document.addEventListener('DOMContentLoaded', () => {
    const installButton = document.getElementById('install-pwa-btn');
    let deferredPrompt;

    window.addEventListener('beforeinstallprompt', (e) => {
        // Prevent the mini-infobar from appearing on mobile
        e.preventDefault();
        // Stash the event so it can be triggered later.
        deferredPrompt = e;
        // Update UI to notify the user they can install the PWA
        if (installButton) {
            installButton.style.display = 'block';
        }
    });

    if (installButton) {
        installButton.addEventListener('click', async () => {
            // Hide the app provided install promotion
            installButton.style.display = 'none';
            // Show the install prompt
            if (deferredPrompt) {
                deferredPrompt.prompt();
                // Wait for the user to respond to the prompt
                const { outcome } = await deferredPrompt.userChoice;
                // Optionally, send analytics event with outcome of user choice
                console.log(`User response to the install prompt: ${outcome}`);
                // We've used the prompt, and can't use it again, throw it away
                deferredPrompt = null;
            }
        });
    }

    window.addEventListener('appinstalled', () => {
        // Hide the install button
        if (installButton) {
            installButton.style.display = 'none';
        }
        // Clear the deferredPrompt so it can be garbage collected
        deferredPrompt = null;
        // Optionally, send analytics event to indicate successful installation
        console.log('PWA was installed');
    });
});
