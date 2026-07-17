const fs = require('fs');
const path = require('path');

const indexPath = path.join(__dirname, '..', 'class-11-applied-mathematics', 'index.html');
let content = fs.readFileSync(indexPath, 'utf8');

// The new replacement script
const newScript = `    <!-- Tracker Interactive Logic -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const checkboxes = document.querySelectorAll('.syllabus-checkbox');
            const storedProgress = JSON.parse(localStorage.getItem('class-11-applied-mathematics-progress')) || {};
            
            // 1. Initialize checkboxes from local storage
            checkboxes.forEach(checkbox => {
                const id = checkbox.id;
                if (storedProgress[id]) {
                    checkbox.checked = true;
                }

                // Save status changes
                checkbox.addEventListener('change', () => {
                    storedProgress[checkbox.id] = checkbox.checked;
                    localStorage.setItem('class-11-applied-mathematics-progress', JSON.stringify(storedProgress));
                    updateProgress();
                });

                // Parent list item click logic
                const parent = checkbox.closest('.syllabus-item');
                if (parent) {
                    parent.addEventListener('click', (e) => {
                        if (e.target !== checkbox && e.target.tagName !== 'A') {
                            checkbox.checked = !checkbox.checked;
                            checkbox.dispatchEvent(new Event('change'));
                        }
                    });
                }
            });

            // 2. Main progress update function
            function updateProgress() {
                const units = [1, 2, 3, 4, 5, 6, 7];
                let globalTotal = 0;
                let globalChecked = 0;
                
                units.forEach(unitNum => {
                    const section = document.getElementById(\`unit-\${unitNum}\`);
                    if (!section) return;
                    
                    const unitCheckboxes = section.querySelectorAll('.syllabus-checkbox');
                    const total = unitCheckboxes.length;
                    const checked = Array.from(unitCheckboxes).filter(cb => cb.checked).length;
                    
                    globalTotal += total;
                    globalChecked += checked;
                    
                    const percentage = total > 0 ? Math.round((checked / total) * 100) : 0;
                    
                    // Update Unit Progress Bar in the Summary Header
                    const barFill = document.getElementById(\`unit-\${unitNum}-progress-fill\`);
                    const barText = document.getElementById(\`unit-\${unitNum}-progress-text\`);
                    
                    if (barFill) barFill.style.width = \`\${percentage}%\`;
                    if (barText) barText.textContent = \`(\${percentage}%)\`;
                    
                    // Update Unit Count Badge in the Accordion Header
                    const countBadge = document.getElementById(\`subj-\${unitNum}-count\`);
                    if (countBadge) countBadge.textContent = \`\${checked}/\${total}\`;
                });
                
                // Update Global Progress Bar
                const globalPercentage = globalTotal > 0 ? Math.round((globalChecked / globalTotal) * 100) : 0;
                const globalFill = document.getElementById('global-progress-fill');
                const globalText = document.getElementById('global-progress-text');
                
                if (globalFill) globalFill.style.width = \`\${globalPercentage}%\`;
                if (globalText) globalText.textContent = \`\${globalPercentage}%\`;
            }

            // 3. Accordion Toggle Logic
            window.toggleSubject = function(subjId) {
                const content = document.getElementById(subjId);
                const icon = document.getElementById(\`\${subjId}-icon\`);
                
                if (content && icon) {
                    content.classList.toggle('active');
                    if (content.classList.contains('active')) {
                        icon.classList.remove('fa-chevron-down');
                        icon.classList.add('fa-chevron-up');
                    } else {
                        icon.classList.remove('fa-chevron-up');
                        icon.classList.add('fa-chevron-down');
                    }
                }
            };
            
            // 4. Open specific subject from Examination Plan links
            window.openSubject = function(unitId, subjId, event) {
                if (event) event.preventDefault();
                
                const content = document.getElementById(subjId);
                const icon = document.getElementById(\`\${subjId}-icon\`);
                
                if (content && icon && !content.classList.contains('active')) {
                    content.classList.add('active');
                    icon.classList.remove('fa-chevron-down');
                    icon.classList.add('fa-chevron-up');
                }
                
                const target = document.getElementById(unitId);
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            };

            // Run initial progress calculation
            updateProgress();
        });
    </script>`;

// Find the start of the Tracker Interactive Logic and replace until the end of the script tag
const startRegex = /<!-- Tracker Interactive Logic -->[\s\S]*?(?=<\/script>)<\/script>/;
if (startRegex.test(content)) {
    content = content.replace(startRegex, newScript);
    fs.writeFileSync(indexPath, content, 'utf8');
    console.log("Successfully replaced script in index.html");
} else {
    // If we can't find the comment, look for the script starting with document.addEventListener('DOMContentLoaded', () => {
    // and containing 'gs-polity-geo'
    const fallbackRegex = /<script>\s*document\.addEventListener\('DOMContentLoaded'[\s\S]*?gs-polity-geo[\s\S]*?(?=<\/script>)<\/script>/;
    if (fallbackRegex.test(content)) {
        content = content.replace(fallbackRegex, newScript);
        fs.writeFileSync(indexPath, content, 'utf8');
        console.log("Successfully replaced script in index.html using fallback regex");
    } else {
        console.error("Could not find the script block to replace!");
    }
}
