/**
 * Shared Chapter List Logic
 * Renders chapter cards (Link or Accordion style) into a container.
 * 
 * @param {Array} chapters - Array of chapter objects
 * @param {String} containerId - ID of the container element
 * @param {Object} config - Configuration options { type: 'link'|'accordion', metaText, getMeta, generateLinks }
 */
export function initChapterList(chapters, containerId, config = {}) {
    const container = document.getElementById(containerId);
    if (!container) return;

    container.innerHTML = '';

    chapters.forEach((chapter) => {
        // Determine chapter number based on original array index
        const originalIndex = chapters.indexOf(chapter);
        const chapNum = originalIndex + 1;
        const badgeNum = chapNum.toString().padStart(2, '0');

        let card;

        if (config.type === 'link') {
            // Link Style Card (e.g., Class 10 Worksheets)
            card = document.createElement('a');
            card.href = chapter.url;
            card.className = 'chapter-card';
            card.innerHTML = `
                <div class="chap-badge">${badgeNum}</div>
                <div class="chap-info">
                    <div class="chap-title">${chapter.name}</div>
                    <div class="chap-meta">${config.metaText || '<i class="far fa-file-alt"></i> Practice Worksheets'}</div>
                </div>
                <div class="action-icon">
                    <i class="fas fa-chevron-right"></i>
                </div>
            `;
        } else {
            // Accordion Style Card (e.g., Class 9 Exemplar/Worksheets)
            card = document.createElement('div');
            card.className = 'chapter-card';
            
            const metaContent = config.getMeta ? config.getMeta(chapter) : 'Resources';
            const linksHtml = config.generateLinks ? config.generateLinks(chapter, chapNum) : '';

            card.innerHTML = `
                <div class="card-header">
                    <div class="chap-badge">${badgeNum}</div>
                    <div class="chap-info">
                        <div class="chap-title">${chapter.name}</div>
                        <div class="chap-meta">${metaContent}</div>
                    </div>
                    <div class="toggle-icon">
                        <i class="fas fa-chevron-down"></i>
                    </div>
                </div>
                <div class="exercise-panel">
                    <div class="exercise-list">
                        ${linksHtml}
                    </div>
                </div>
            `;

            // Accordion Toggle Logic
            const header = card.querySelector('.card-header');
            header.addEventListener('click', (e) => {
                e.stopPropagation();
                toggleAccordion(card);
            });
        }
        
        container.appendChild(card);
    });
}

function toggleAccordion(activeCard) {
    const panel = activeCard.querySelector('.exercise-panel');
    const isActive = activeCard.classList.contains('active');
    
    // Close all other open cards
    document.querySelectorAll('.chapter-card.active').forEach(c => {
        if (c !== activeCard) {
            c.classList.remove('active');
            c.querySelector('.exercise-panel').style.maxHeight = null;
        }
    });

    // Toggle current card
    activeCard.classList.toggle('active');
    if (!isActive) {
        panel.style.maxHeight = panel.scrollHeight + "px";
    } else {
        panel.style.maxHeight = null;
    }
}