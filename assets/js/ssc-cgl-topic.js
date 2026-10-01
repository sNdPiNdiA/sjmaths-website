document.addEventListener('DOMContentLoaded', () => {
            // Scroll active nav item into view
            setTimeout(() => {
                const activeItem = document.querySelector('.sub-nav-item.active');
                const navContainer = document.querySelector('.subject-nav');
                if (activeItem && navContainer) {
                    const containerWidth = navContainer.offsetWidth;
                    const itemOffset = activeItem.offsetLeft;
                    const itemWidth = activeItem.offsetWidth;
                    navContainer.scrollLeft = itemOffset - (containerWidth / 2) + (itemWidth / 2);
                }
            }, 100);

            // Handle checklist local storage
            const checkboxes = document.querySelectorAll('.checklist-checkbox');
            const storageKey = 'ssc-cgl-prep-checklist';
            const progress = JSON.parse(localStorage.getItem(storageKey)) || {};

            checkboxes.forEach(chk => {
                if (progress[chk.id]) {
                    chk.checked = true;
                }
                chk.addEventListener('change', () => {
                    progress[chk.id] = chk.checked;
                    localStorage.setItem(storageKey, JSON.stringify(progress));
                });

                // Allow clicking parent checklist-item to toggle checkbox
                const parent = chk.closest('.checklist-item');
                if (parent) {
                    parent.addEventListener('click', (e) => {
                        if (e.target !== chk) {
                            chk.checked = !chk.checked;
                            chk.dispatchEvent(new Event('change'));
                        }
                    });
                }
            });
        });
