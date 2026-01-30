export async function initSharedHeader(customHandler = null, componentPathPrefix = '') {
    // Logic is now initialized directly, assuming header and footer are pre-inlined
    await initializeLogic(customHandler, componentPathPrefix);

    // Update footer year, assuming footer is already in the DOM
    const yearSpan = document.getElementById('footer-year');
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }
}

async function initializeLogic(searchHandler, componentPathPrefix) {
    // 1. Highlight Active Link
    const currentPath = window.location.pathname;
    // Normalize path (e.g. /index.html -> /)
    const normalize = p => p.replace('/index.html', '/').replace(/\/$/, '') || '/';
    const currentNorm = normalize(currentPath);

    document.querySelectorAll('nav a').forEach(link => {
        const linkPath = new URL(link.href, window.location.origin).pathname;
        const linkNorm = normalize(linkPath);
        
        if (currentNorm === linkNorm || (linkNorm !== '/' && currentNorm.startsWith(linkNorm))) {
            link.classList.add('active');
        }
    });

    // 2. Firebase Auth
    try {
        // Dynamic Import: Loads Firebase only AFTER header HTML is visible
        const { onAuthStateChanged, signOut } = await import("https://www.gstatic.com/firebasejs/12.8.0/firebase-auth.js");
        const { auth } = await import("./assets/js/firebase-config.js");

        onAuthStateChanged(auth, (user) => {
            const loginBtn = document.getElementById('authBtn'); 
            // Also check if we already replaced it (to prevent duplicates or logic errors)
            const existingDropdown = document.getElementById('headerProfileBtn');
            
            if (!loginBtn && !existingDropdown) return;

            if (user) {
                const name = user.displayName || "Student";
                const photo = user.photoURL || `https://ui-avatars.com/api/?name=${encodeURIComponent(name)}&background=random&color=fff`;
                
                // 1. Build Dropdown HTML
                const dropdownHTML = `
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <a href="${componentPathPrefix}notifications.html" id="headerNotificationBtn" title="Notifications" style="background: none; border: none; cursor: pointer; position: relative; color: var(--text-dark);">
                            <i class="fas fa-bell" style="font-size: 1.2rem;"></i>
                            <span id="notification-badge" style="display: none; position: absolute; top: -5px; right: -5px; background: var(--secondary); color: white; border-radius: 50%; width: 18px; height: 18px; font-size: 0.7rem; font-weight: bold; line-height: 18px; text-align: center; border: 1px solid white;"></span>
                        </a>
                        <div class="profile-dropdown-wrapper" style="position: relative; display: inline-block;">
                            <button id="headerProfileBtn" style="background: none; border: none; cursor: pointer; padding: 0; display: flex; align-items: center;">
                                <img src="${photo}" alt="Profile" style="width: 38px; height: 38px; border-radius: 50%; object-fit: cover; border: 2px solid var(--primary); box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                            </button>
                            <div id="headerProfileDropdown" style="display: none; position: absolute; right: 0; top: 120%; background: white; min-width: 220px; border-radius: 12px; box-shadow: 0 10px 40px rgba(0,0,0,0.15); padding: 10px; z-index: 10000; border: 1px solid rgba(0,0,0,0.05);">
                                <div style="padding: 10px 15px; border-bottom: 1px solid #eee; margin-bottom: 5px;">
                                    <div style="font-weight: 700; color: var(--text-dark);">${name}</div>
                                    <div style="font-size: 0.8rem; color: var(--text-light); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${user.email}</div>
                                </div>
                                <a href="${componentPathPrefix}dashboard.html" style="display: flex; align-items: center; gap: 10px; padding: 10px 15px; color: var(--text-dark); text-decoration: none; border-radius: 8px; transition: background 0.2s;">
                                    <i class="fas fa-th-large" style="color: var(--primary); width: 20px;"></i> Dashboard
                                </a>
                                <a href="${componentPathPrefix}my-submissions.html" style="display: flex; align-items: center; gap: 10px; padding: 10px 15px; color: var(--text-dark); text-decoration: none; border-radius: 8px; transition: background 0.2s;">
                                    <i class="fas fa-clipboard-check" style="color: var(--primary); width: 20px;"></i> My Submissions
                                </a>
                                <a href="${componentPathPrefix}profile.html" style="display: flex; align-items: center; gap: 10px; padding: 10px 15px; color: var(--text-dark); text-decoration: none; border-radius: 8px; transition: background 0.2s;">
                                    <i class="fas fa-user" style="color: var(--primary); width: 20px;"></i> My Profile
                                </a>
                                <a href="${componentPathPrefix}settings.html" style="display: flex; align-items: center; gap: 10px; padding: 10px 15px; color: var(--text-dark); text-decoration: none; border-radius: 8px; transition: background 0.2s;">
                                    <i class="fas fa-cog" style="color: var(--primary); width: 20px;"></i> Settings
                                </a>
                                <div style="border-top: 1px solid #eee; margin: 5px 0;"></div>
                                <button id="headerLogoutBtn" style="width: 100%; text-align: left; background: none; border: none; padding: 10px 15px; color: var(--secondary); cursor: pointer; border-radius: 8px; display: flex; align-items: center; gap: 10px; font-size: 0.95rem; font-family: inherit;">
                                    <i class="fas fa-sign-out-alt" style="width: 20px;"></i> Logout
                                </button>
                            </div>
                        </div>
                    </div>
                `;

                // 2. Inject Dropdown
                if (loginBtn) {
                    const tempDiv = document.createElement('div');
                    tempDiv.innerHTML = dropdownHTML;
                    loginBtn.replaceWith(tempDiv.firstElementChild);
                }

                // 3. Attach Events
                const btn = document.getElementById('headerProfileBtn');
                const dropdown = document.getElementById('headerProfileDropdown');
                const logoutBtn = document.getElementById('headerLogoutBtn');

                if (btn && dropdown) {
                    btn.addEventListener('click', (e) => {
                        e.stopPropagation();
                        dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
                    });
                    document.addEventListener('click', (e) => {
                        if (dropdown.style.display === 'block' && !dropdown.contains(e.target) && !btn.contains(e.target)) {
                            dropdown.style.display = 'none';
                        }
                    });
                    // Hover effect helper
                    dropdown.querySelectorAll('a, button').forEach(el => {
                        el.addEventListener('mouseenter', () => el.style.backgroundColor = '#f8f9fa');
                        el.addEventListener('mouseleave', () => el.style.backgroundColor = 'transparent');
                    });
                }

                if (logoutBtn) {
                    logoutBtn.addEventListener('click', async () => {
                        try {
                            await signOut(auth);
                            window.location.href = `${componentPathPrefix}login.html`;
                        } catch (error) {
                            console.error("Logout failed", error);
                        }
                    });
                }

                // 4. Notification Badge Listener
                document.addEventListener('notificationsUpdated', (e) => {
                    const badge = document.getElementById('notification-badge');
                    if (badge) {
                        const count = e.detail.count;
                        badge.textContent = count;
                        badge.style.display = count > 0 ? 'block' : 'none';
                    }
                });


            } else if (existingDropdown) {
                // User logged out but dropdown exists -> Revert to Login Button
                const a = document.createElement('a');
                a.href = `${componentPathPrefix}login.html`;
                a.className = 'auth-btn-pill';
                a.id = 'authBtn';
                a.textContent = 'Login';
                existingDropdown.parentElement.replaceWith(a);
            }
        });
    } catch (e) { /* Firebase not configured */ }

    // 3. Mobile Menu
    const mobileToggle = document.querySelector('.mobile-toggle');
    const navMenu = document.querySelector('.desktop-nav') || document.querySelector('nav');
    
    if (mobileToggle && navMenu) {
        mobileToggle.addEventListener('click', (e) => {
            e.stopPropagation(); // Prevent conflict with global navigation scripts
            const isOpen = navMenu.classList.toggle('active');
            const toggleIcon = mobileToggle.querySelector('i');
            if (toggleIcon) {
                toggleIcon.classList.toggle('fa-bars', !isOpen);
                toggleIcon.classList.toggle('fa-times', isOpen);
            }
            mobileToggle.setAttribute('aria-expanded', isOpen);
        });
        
        // Close on click outside
        document.addEventListener('click', (e) => {
            if (navMenu.classList.contains('active') && !navMenu.contains(e.target) && !mobileToggle.contains(e.target)) {
                navMenu.classList.remove('active');
                const toggleIcon = mobileToggle.querySelector('i');
                if (toggleIcon) {
                    toggleIcon.classList.add('fa-bars');
                    toggleIcon.classList.remove('fa-times');
                }
            }
        });
    }

    // 4. Search Logic
    const searchInput = document.querySelector('.header-search input');
    const searchBtn = document.querySelector('.header-search button');

    if (searchInput && searchBtn && searchHandler) {
        if (searchHandler.placeholder) searchInput.placeholder = searchHandler.placeholder;

        const performSearch = () => {
            const query = searchInput.value.toLowerCase().trim();
            if (query === "") return;
            searchHandler.onSearch(query);
        };

        searchBtn.addEventListener('click', performSearch);
        searchInput.addEventListener('keypress', (e) => { if (e.key === 'Enter') performSearch(); });
    }
}