function openTab(evt, tabId) {
            document.querySelectorAll('.tab-panel').forEach(function(panel) {
                panel.classList.remove('active');
            });
            document.querySelectorAll('.main-tabs-nav .tab-btn').forEach(function(button) {
                button.classList.remove('active');
            });

            var panel = document.getElementById(tabId);
            if (panel) panel.classList.add('active');

            var button = evt && evt.currentTarget
                ? evt.currentTarget
                : document.querySelector('.main-tabs-nav .tab-btn[onclick*="' + tabId + '"]');
            if (button) button.classList.add('active');
        }

        function normalizeInitialTab() {
            var requested = window.location.hash.replace('#', '');
            var allowed = ['tab-theory', 'tab-practice', 'tab-pyqs', 'tab-mini-test'];
            var defaultTab = allowed.indexOf(requested) !== -1 ? requested : 'tab-theory';
            openTab(null, defaultTab);
        }

        document.addEventListener('DOMContentLoaded', normalizeInitialTab);
        window.addEventListener('pageshow', normalizeInitialTab);
