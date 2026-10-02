document.addEventListener('DOMContentLoaded', function() {
            document.querySelectorAll('[data-mini-test]').forEach(function(test) {
                var submit = test.querySelector('.mini-test-submit');
                var reset = test.querySelector('.mini-test-reset');
                var results = test.querySelector('.mini-test-results');

                function resetTest() {
                    test.querySelectorAll('input[type="radio"]').forEach(function(input) { input.checked = false; });
                    test.querySelectorAll('.mini-test-question').forEach(function(card) {
                        card.classList.remove('mini-correct', 'mini-wrong');
                        var solution = card.querySelector('.mini-test-solution');
                        if (solution) solution.open = false;
                    });
                    if (results) results.style.display = 'none';
                }

                if (submit) {
                    submit.addEventListener('click', function() {
                        var questions = Array.prototype.slice.call(test.querySelectorAll('.mini-test-question'));
                        var correct = 0;
                        questions.forEach(function(card) {
                            var answer = card.getAttribute('data-mini-answer');
                            var selected = card.querySelector('input[type="radio"]:checked');
                            var solution = card.querySelector('.mini-test-solution');
                            card.classList.remove('mini-correct', 'mini-wrong');
                            if (selected && selected.value === answer) {
                                correct += 1;
                                card.classList.add('mini-correct');
                            } else {
                                card.classList.add('mini-wrong');
                            }
                            if (solution) solution.open = true;
                        });
                        var total = questions.length || 10;
                        var accuracy = Math.round((correct / total) * 100);
                        test.querySelectorAll('.mini-test-score, .mini-test-score-hi').forEach(function(el) { el.textContent = correct + '/' + total; });
                        test.querySelectorAll('.mini-test-accuracy, .mini-test-accuracy-hi').forEach(function(el) { el.textContent = accuracy + '%'; });
                        if (results) results.style.display = 'block';
                    });
                }
                if (reset) reset.addEventListener('click', resetTest);
                resetTest();
            });
        });
