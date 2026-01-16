import { signOut } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

export function handleUserProfile(user, auth) {
    const targets = ['authBtn', 'mobileAuthBtn'];

    targets.forEach(id => {
        const authBtn = document.getElementById(id);
        if (!authBtn) return;

        // Infer base path from the existing login button's href to ensure correct relative links
        const loginHref = authBtn.getAttribute('href') || 'login.html';
        const basePath = loginHref.replace(/login\.html$/, '');

        if (user) {
            // 1. Get User Details
            const displayName = user.displayName || user.email.split('@')[0];
            // Generate a random avatar if none exists
            const photoURL = user.photoURL || `https://ui-avatars.com/api/?name=${encodeURIComponent(displayName)}&background=random&color=fff&bold=true`;

            // 2. Create Profile HTML Structure
            const parent = authBtn.parentElement;
            const isList = parent.tagName === 'UL' || parent.tagName === 'OL';
            const wrapperTag = isList ? 'li' : 'div';
            
            const profileContainer = document.createElement(wrapperTag);
            profileContainer.className = 'user-profile-item';
            profileContainer.style.position = 'relative';
            if (isList) profileContainer.style.marginLeft = '10px';
            else profileContainer.style.display = 'inline-block';

            // Mobile adjustments
            const isMobile = id === 'mobileAuthBtn';
            const dropdownRight = isMobile ? '-10px' : '0';

            profileContainer.innerHTML = `
                <div class="profile-trigger" style="cursor: pointer; display: flex; align-items: center; gap: 10px; padding: 5px;">
                    <img src="${photoURL}" alt="Profile" style="width: 38px; height: 38px; border-radius: 50%; object-fit: cover; border: 2px solid var(--primary); box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                    ${!isMobile ? `<span class="user-name" style="font-weight: 600; font-size: 0.9rem; color: var(--text-dark); display: none;">${displayName}</span>` : ''}
                    ${!isMobile ? `<i class="fas fa-chevron-down" style="font-size: 0.8rem; color: var(--text-light);"></i>` : ''}
                </div>
                
                <div class="profile-dropdown" style="
                    display: none;
                    position: absolute;
                    top: 140%;
                    right: ${dropdownRight};
                    background: white;
                    min-width: 240px;
                    padding: 15px;
                    border-radius: 16px;
                    box-shadow: 0 10px 40px rgba(0,0,0,0.15);
                    border: 1px solid rgba(0,0,0,0.05);
                    z-index: 10000;
                    animation: fadeIn 0.2s ease;
                ">
                    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 15px; padding-bottom: 15px; border-bottom: 1px solid #eee;">
                        <img src="${photoURL}" style="width: 45px; height: 45px; border-radius: 50%;">
                        <div style="overflow: hidden;">
                            <div style="font-weight: 700; color: var(--text-dark); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${displayName}</div>
                            <div style="font-size: 0.75rem; color: var(--text-light); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${user.email}</div>
                        </div>
                    </div>

                    <ul style="list-style: none; padding: 0; margin: 0;">
                        <li style="margin-bottom: 5px;">
                            <a href="${basePath}pages/profile.html" style="display: flex; align-items: center; gap: 12px; padding: 10px; color: var(--text-dark); border-radius: 10px; transition: background 0.2s; font-size: 0.9rem;">
                                <i class="fas fa-user-circle" style="color: var(--primary); width: 20px;"></i> My Profile
                            </a>
                        </li>
                        <li style="margin-bottom: 5px;">
                            <a href="${basePath}pages/settings.html" style="display: flex; align-items: center; gap: 12px; padding: 10px; color: var(--text-dark); border-radius: 10px; transition: background 0.2s; font-size: 0.9rem;">
                                <i class="fas fa-cog" style="color: var(--primary); width: 20px;"></i> Settings
                            </a>
                        </li>
                        <li style="margin-top: 10px; border-top: 1px solid #eee; padding-top: 10px;">
                            <a href="#" class="logoutAction" style="display: flex; align-items: center; gap: 12px; padding: 10px; color: var(--secondary); border-radius: 10px; transition: background 0.2s; background: rgba(231, 76, 60, 0.05); font-weight: 600; font-size: 0.9rem;">
                                <i class="fas fa-sign-out-alt" style="width: 20px;"></i> Logout
                            </a>
                        </li>
                    </ul>
                </div>
            `;

            // 3. Replace the existing Login button
            if (isList) {
                const parentLi = authBtn.closest('li');
                if (parentLi) parentLi.replaceWith(profileContainer);
                else authBtn.replaceWith(profileContainer);
            } else {
                authBtn.replaceWith(profileContainer);
            }

            // 4. Add Event Listeners
            const trigger = profileContainer.querySelector('.profile-trigger');
            const dropdown = profileContainer.querySelector('.profile-dropdown');
            const logoutBtn = profileContainer.querySelector('.logoutAction');

            // Toggle Dropdown
            trigger.addEventListener('click', (e) => {
                e.stopPropagation();
                // Close other dropdowns
                document.querySelectorAll('.profile-dropdown').forEach(d => {
                    if (d !== dropdown) d.style.display = 'none';
                });
                
                const isVisible = dropdown.style.display === 'block';
                dropdown.style.display = isVisible ? 'none' : 'block';
            });

            // Close on click outside
            document.addEventListener('click', () => {
                dropdown.style.display = 'none';
            });

            dropdown.addEventListener('click', (e) => e.stopPropagation());

            // Logout Logic
            logoutBtn.addEventListener('click', async (e) => {
                e.preventDefault();
                if (confirm("Are you sure you want to logout?")) {
                    await signOut(auth);
                    window.location.reload();
                }
            });
        }
    });
}