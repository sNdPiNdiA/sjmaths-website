function toggleNavTabDropdown(button, event) {
    event.stopPropagation();
    var parent = button.closest('.nav-tab-item');
    var isOpen = parent.classList.contains('active-open');

    document.querySelectorAll('.nav-tab-item').forEach(function(item) {
        item.classList.remove('active-open');
    });

    if (!isOpen) {
        parent.classList.add('active-open');
    }
}

function openMobileDockDrawer(tabId, titleText) {
    var drawer = document.getElementById('dockDrawerOverlay');
    var contentBox = document.getElementById('dockDrawerContent');
    var titleBox = document.getElementById('dockDrawerTitle');
    var sourceCard = document.getElementById(tabId);

    if (drawer && contentBox && sourceCard) {
        titleBox.innerHTML = titleText;
        contentBox.innerHTML = sourceCard.innerHTML;
        drawer.classList.add('active');
    }
}

function closeMobileDockDrawer() {
    var drawer = document.getElementById('dockDrawerOverlay');
    if (drawer) {
        drawer.classList.remove('active');
    }
}

function switchTab(tabType, url, event) {
    if (event) {
        event.preventDefault();
        event.stopPropagation();
    }

    // 1. Update active tab pill state on desktop
    document.querySelectorAll('.nav-tab-pill').forEach(function(pill) {
        pill.classList.remove('active');
    });

    // Find the pill matching the tabType or from event target
    var targetPillClass = tabType + '-tab';
    if (tabType === 'pyqs') targetPillClass = 'pyq-tab';
    if (tabType === 'sheets') targetPillClass = 'sheet-tab';

    if (event && event.currentTarget) {
        var pill = event.currentTarget.closest('.nav-tab-item');
        if (pill) {
            var innerPill = pill.querySelector('.nav-tab-pill');
            if (innerPill) innerPill.classList.add('active');
        }
    } else {
        var pill = document.querySelector('.' + targetPillClass);
        if (pill) pill.classList.add('active');
    }

    // 2. Update active dock button state on mobile
    document.querySelectorAll('.mobile-dock-btn').forEach(function(btn) {
        btn.classList.remove('active');
        if (btn.getAttribute('onclick') && btn.getAttribute('onclick').indexOf(tabType) !== -1) {
            btn.classList.add('active');
        }
    });

    // Close mobile drawer
    closeMobileDockDrawer();

    // 3. Show/hide content panels
    var notesPanel = document.getElementById('notes-tab-content');
    var iframePanel = document.getElementById('iframe-tab-content');
    var iframe = document.getElementById('tab-iframe');

    if (tabType === 'notes') {
        if (iframePanel) iframePanel.style.display = 'none';
        if (notesPanel) notesPanel.style.display = 'block';
        if (iframe) iframe.src = '';
    } else {
        if (notesPanel) notesPanel.style.display = 'none';
        if (iframePanel) iframePanel.style.display = 'block';
        if (iframe && url) {
            iframe.src = url;
        }
    }
}

document.addEventListener('click', function(e) {
    if (!e.target.closest('.nav-tab-item')) {
        document.querySelectorAll('.nav-tab-item').forEach(function(item) {
            item.classList.remove('active-open');
        });
    }
});
