(function() {
            var btns = document.querySelectorAll('#levelNav .level-btn');
            var cards = document.querySelectorAll('#tab-practice .practice-card');
            var totalQuestions = 49;

            // Build progress dots
            var progressTrack = document.getElementById('progressTrack');
            if (progressTrack) {
                progressTrack.innerHTML = '';
                for (var i = 1; i <= totalQuestions; i++) {
                    var dot = document.createElement('span');
                    dot.className = 'progress-dot';
                    dot.id = 'dot-' + i;
                    dot.dataset.qId = i;
                    progressTrack.appendChild(dot);
                }
            }

            function showLevel(level) {
               cards.forEach(function(card) {
                    var cl = card.getAttribute('data-level');
                    if (cl === level) {
                        card.classList.add('level-active');
                    } else {
                        card.classList.remove('level-active');
                    }
                });
            }

            btns.forEach(function(btn) {
                btn.addEventListener('click', function() {
                    btns.forEach(function(b) { b.classList.remove('active'); });
                    this.classList.add('active');
                    var lvl = this.getAttribute('data-level');
                    showLevel(lvl);
                });
            });

            // Default: show level 1
            showLevel('1');

            // Track solution views
            var details = document.querySelectorAll('#tab-practice .solution-details');
            details.forEach(function(det, idx) {
                det.addEventListener('toggle', function() {
                    if (this.open) {
                        var dot = document.getElementById('dot-' + (idx + 1));
                        if (dot) dot.classList.add('completed');
                        var attempted = document.querySelectorAll('.progress-dot.completed').length;
                        var attemptedCount = document.getElementById('attemptedCount');
                        var correctCount = document.getElementById('correctCount');
                        var scoreDisplay = document.getElementById('scoreDisplay');
                        if (attemptedCount) attemptedCount.textContent = attempted + '/' + totalQuestions;
                        if (correctCount) correctCount.textContent = attempted + '/' + totalQuestions;
                        if (scoreDisplay) scoreDisplay.textContent = Math.round((attempted / totalQuestions) * 100) + '%';
                    }
                });
            });
        })();
