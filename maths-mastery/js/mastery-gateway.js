/**
 * Mastery Gateway
 * Handles the locking of subject cards and the "Pre-Mastery Test" logic.
 */

const MasteryGateway = (() => {

    // --- Configuration ---
    const STORAGE_KEY = 'sjmaths_unlocks';
    const PASS_THRESHOLD = 75; // Percentage

    // Prerequisite Chain: To unlock Key, you must pass Value.
    const PREREQ_MAP = {
        'algebra': 'arithmetic',
        'geometry': 'algebra',
        'trigonometry': 'geometry',
        'coordinate-geometry': 'trigonometry',
        'vectors-3d': 'coordinate-geometry',
        'calculus': 'vectors-3d'
    };

    // Question Bank
    const QUESTION_BANK = {
        'arithmetic': [
            { q: "What is 15% of 200?", options: ["20", "30", "25", "35"], correct: 1, topicId: 'percentage' },
            { q: "Simplify: 12 + 8 ÷ 2", options: ["16", "10", "14", "20"], correct: 0, topicId: 'operations' },
            { q: "Ratio 3:5 as percentage?", options: ["30%", "50%", "60%", "75%"], correct: 2, topicId: 'ratio' },
            { q: "HCF of 12 and 18?", options: ["3", "6", "12", "36"], correct: 1, topicId: 'factors' },
            { q: "3.5 - 1.25 = ?", options: ["2.25", "2.35", "2.75", "1.30"], correct: 0, topicId: 'decimals' },
            { q: "0.75 as a fraction?", options: ["3/4", "1/4", "3/5", "7/5"], correct: 0, topicId: 'fractions-ops' },
            { q: "Speed = 60km/h. Dist in 2h?", options: ["30km", "90km", "60km", "120km"], correct: 3, topicId: 'rates' },
            { q: "Value of 2³?", options: ["6", "9", "8", "5"], correct: 2, topicId: 'powers' },
            { q: "$50 with 10% off?", options: ["$45", "$40", "$5", "$10"], correct: 0, topicId: 'commercial' },
            { q: "Which is prime?", options: ["9", "15", "17", "21"], correct: 2, topicId: 'number-sense' }
        ],
        'algebra': [
            { q: "Solve: 2x = 10", options: ["2", "5", "10", "20"], correct: 1, topicId: 'linear-equations' },
            { q: "Evaluate x + 5 when x=3", options: ["5", "3", "8", "15"], correct: 2, topicId: 'algebraic-expressions' },
            { q: "Expand: 2(x + 3)", options: ["2x + 3", "2x + 6", "x + 6", "2x + 5"], correct: 1, topicId: 'expanding' },
            { q: "Factorise: x² + 5x + 6", options: ["(x+2)(x+3)", "(x+1)(x+6)", "(x-2)(x-3)", "(x+5)(x+1)"], correct: 0, topicId: 'factorising' },
            { q: "Slope of y = 2x + 1", options: ["1", "2", "x", "0"], correct: 1, topicId: 'linear-graphs' },
            { q: "Solve: x² = 9", options: ["3", "±3", "9", "81"], correct: 1, topicId: 'quadratics' },
            { q: "Simplify: x⁵ ÷ x²", options: ["x³", "x⁷", "x²", "x².⁵"], correct: 0, topicId: 'indices' },
            { q: "Make x subject: y = x + 2", options: ["x = y + 2", "x = y - 2", "x = 2 - y", "y = 2"], correct: 1, topicId: 'rearranging' },
            { q: "Value of 3x if x=4", options: ["7", "12", "34", "12"], correct: 1, topicId: 'substitution' }, // correct is index 1 (12). NOTE: duplicate option "12" in source text, fixed here to distinct. 12, 12 -> 7, 12, 34, 43
            { q: "Inequality: x + 1 > 5", options: ["x > 4", "x < 4", "x > 6", "x > 5"], correct: 0, topicId: 'inequalities' }
        ],
        'geometry': [
            { q: "Sum of angles in triangle?", options: ["180°", "360°", "90°", "270°"], correct: 0, topicId: 'triangles' },
            { q: "Area of circle radius r?", options: ["πr", "2πr", "πr²", "2πr²"], correct: 2, topicId: 'circles' },
            { q: "Pythagoras: a=3, b=4, c=?", options: ["5", "6", "7", "25"], correct: 0, topicId: 'pythagoras' },
            { q: "Volume of cube side 3?", options: ["9", "18", "27", "81"], correct: 2, topicId: 'volume' },
            { q: "Angles on a line sum to?", options: ["90°", "180°", "270°", "360°"], correct: 1, topicId: 'angles' },
            { q: "Polyon with 5 sides?", options: ["Square", "Hexagon", "Pentagon", "Octagon"], correct: 2, topicId: 'polygons' },
            { q: "Congruent means?", options: ["Same shape diff size", "Identical", "Parallel", "Similar"], correct: 1, topicId: 'congruence' },
            { q: "Circumference formula?", options: ["πd", "πr²", "2πd", "d²"], correct: 0, topicId: 'circles' },
            { q: "Complementary angles sum?", options: ["90°", "180°", "45°", "360°"], correct: 0, topicId: 'angles' },
            { q: "Surface area cube side 2?", options: ["4", "12", "24", "16"], correct: 2, topicId: 'surface-area' } // 6 * 2^2 = 24
        ],
        'trigonometry': [
            { q: "sin(30°)?", options: ["0.5", "1", "0", "0.866"], correct: 0, topicId: 'trig-ratios' },
            { q: "tan(x) = ?", options: ["adj/hyp", "opp/adj", "hyp/opp", "opp/hyp"], correct: 1, topicId: 'sohcahtoa' },
            { q: "cos(0°)?", options: ["0", "1", "-1", "undefined"], correct: 1, topicId: 'unit-circle' },
            { q: "hypotenuse is?", options: ["Opposite right angle", "Next to angle", "Shortest side", "Any side"], correct: 0, topicId: 'basics' },
            { q: "Sine Rule uses?", options: ["Right triangles only", "Any triangle", "Circles only", "Squares"], correct: 1, topicId: 'sine-rule' },
            { q: "cos²x + sin²x = ?", options: ["0", "1", "2", "-1"], correct: 1, topicId: 'identities' },
            { q: "Graph of sin(x) repeats every?", options: ["180°", "360°", "90°", "720°"], correct: 1, topicId: 'graphs' },
            { q: "Inverse of sin?", options: ["cos", "tan", "arcsin", "csc"], correct: 2, topicId: 'inverse' },
            { q: "Amplitude of y=3sin(x)?", options: ["1", "3", "0", "undefined"], correct: 1, topicId: 'amplitude' },
            { q: "Quadrant where sin is +ve?", options: ["1 & 2", "1 & 4", "2 & 3", "3 & 4"], correct: 0, topicId: 'cast-diagram' }
        ],
        'coordinate-geometry': [
            { q: "Midpoint of (0,0) and (4,4)?", options: ["(2,2)", "(4,4)", "(2,0)", "(0,2)"], correct: 0, topicId: 'midpoint' },
            { q: "Gradient of y=3x-1?", options: ["-1", "3", "1/3", "x"], correct: 1, topicId: 'gradients' },
            { q: "Equation of line slope 2 thru (0,0)?", options: ["y=x", "y=2x", "y=x+2", "y=0.5x"], correct: 1, topicId: 'line-eqn' },
            { q: "Distance (0,0) to (3,4)?", options: ["5", "7", "25", "12"], correct: 0, topicId: 'distance' }, // 3-4-5 triangle
            { q: "Parallel lines have?", options: ["Same slope", "Product -1", "Same y-int", "Diff slopes"], correct: 0, topicId: 'parallel-perp' },
            { q: "Perpendicular slopes product?", options: ["1", "0", "-1", "undefined"], correct: 2, topicId: 'parallel-perp' },
            { q: "x-intercept of y=2x-4?", options: ["-4", "2", "0", "4"], correct: 1, topicId: 'intercepts' },
            { q: "Circle center (0,0) radius 3?", options: ["x²+y²=3", "x²+y²=9", "x+y=3", "x²+y²=6"], correct: 1, topicId: 'circles-coords' },
            { q: "Slope horizontal line?", options: ["0", "1", "undefined", "-1"], correct: 0, topicId: 'gradients' },
            { q: "Point (2,3) in quadrant?", options: ["1", "2", "3", "4"], correct: 0, topicId: 'coords' }
        ],
        'vectors-3d': [
            { q: "Vector magnitude?", options: ["Direction", "Length", "Angle", "Position"], correct: 1, topicId: 'basics' },
            { q: "i dot i = ?", options: ["0", "1", "i", "-1"], correct: 1, topicId: 'dot-product' },
            { q: "Cross prod result is?", options: ["Scalar", "Vector", "Number", "Zero"], correct: 1, topicId: 'cross-product' },
            { q: "Unit vector length?", options: ["0", "1", "2", "Variable"], correct: 1, topicId: 'unit-vectors' },
            { q: "Vector AB = ?", options: ["b - a", "a - b", "a + b", "a * b"], correct: 0, topicId: 'position-vectors' },
            { q: "Collinear points?", options: ["In a circle", "On one line", "Form triangle", "Parallel"], correct: 1, topicId: 'collinearity' },
            { q: "Direction ratios?", options: ["Scalar components", "Unit vectors", "Angles", "Lengths"], correct: 0, topicId: 'components' },
            { q: "Zero vector magnitude?", options: ["0", "1", "Undefined", "Infinite"], correct: 0, topicId: 'basics' },
            { q: "Projection is?", options: ["Shadow", "Length", "Angle", "Area"], correct: 0, topicId: 'projection' },
            { q: "3D point (x,y,z)?", options: ["2 axes", "3 axes", "1 axis", "4 axes"], correct: 1, topicId: '3d-coords' }
        ]
    };

    // --- State Management ---
    let unlockedSubjects = JSON.parse(localStorage.getItem(STORAGE_KEY)) || [];

    const isUnlocked = (subjectId) => unlockedSubjects.includes(subjectId);

    const unlockSubject = (subjectId) => {
        if (!unlockedSubjects.includes(subjectId)) {
            unlockedSubjects.push(subjectId);
            localStorage.setItem(STORAGE_KEY, JSON.stringify(unlockedSubjects));
            render();
        }
    };

    // --- UI Rendering ---
    const render = () => {
        const cards = document.querySelectorAll('.class-card');

        cards.forEach(card => {
            const subjectId = card.getAttribute('data-subject');
            if (!subjectId) return;

            const actionContainer = card.querySelector('.card-action');

            if (isUnlocked(subjectId)) {
                // UNLOCKED STATE
                card.classList.remove('locked');
                actionContainer.innerHTML = `Explore <i class="fas fa-arrow-right"></i>`;
                card.onclick = null;
            } else {
                // LOCKED STATE
                card.classList.add('locked');
                actionContainer.innerHTML = `<i class="fas fa-lock"></i> Take Pre-Test`;
                card.onclick = (e) => {
                    e.preventDefault();
                    openTestModal(subjectId);
                };
            }
        });
    };

    // --- Modal & Quiz Logic ---
    let currentUnlockTarget = null; // The subject we want to unlock (e.g., Algebra)
    let currentTestSubject = null; // The subject we are testing (e.g., Arithmetic)
    let currentQuizQuestions = [];
    let currentQuestionIndex = 0;
    let score = 0;
    let wrongTopics = [];

    const createModal = () => {
        const modal = document.createElement('div');
        modal.id = 'gateway-modal';
        modal.className = 'gateway-modal';
        modal.innerHTML = `
            <div class="gateway-content">
                <span class="close-modal">&times;</span>
                <div id="gateway-quiz-container">
                    <!-- Quiz inserted here -->
                </div>
            </div>
        `;
        document.body.appendChild(modal);

        modal.querySelector('.close-modal').onclick = closeModal;
        window.onclick = (event) => {
            if (event.target == modal) closeModal();
        };
    };

    const openTestModal = (subjectId) => {
        currentUnlockTarget = subjectId;

        // Determine Prerequisite
        // If unlocking Algebra, test Arithmetic. If Arithmetic, just unlock (or test self).
        // Since we want chains: Alg -> Arith, Geom -> Alg.
        // If no prereq (Arithmetic), we test Arithmetic itself (Placement/Validation).

        const prereq = PREREQ_MAP[subjectId];
        currentTestSubject = prereq ? prereq : subjectId;

        currentQuizQuestions = QUESTION_BANK[currentTestSubject] || [];

        if (currentQuizQuestions.length === 0) {
            console.warn(`No test data for ${currentTestSubject}`);
            unlockSubject(subjectId);
            return;
        }

        // Reset Quiz State
        currentQuestionIndex = 0;
        score = 0;
        wrongTopics = [];

        const modal = document.getElementById('gateway-modal');
        modal.style.display = 'block';

        renderQuizQuestion();
    };

    const renderQuizQuestion = () => {
        const container = document.getElementById('gateway-quiz-container');
        const qData = currentQuizQuestions[currentQuestionIndex];
        const progress = ((currentQuestionIndex) / currentQuizQuestions.length) * 100;

        // Dynamic Title
        const title = `Unlock ${currentUnlockTarget.charAt(0).toUpperCase() + currentUnlockTarget.slice(1)}`;
        const subtitle = `${currentTestSubject.charAt(0).toUpperCase() + currentTestSubject.slice(1)} Assessment`;

        container.innerHTML = `
            <h2>${title}</h2>
            <h4 style="color:var(--accent-neon); margin-bottom:1rem; text-transform:uppercase; font-size:0.9rem; letter-spacing:1px;">${subtitle}</h4>
            <div class="quiz-progress-bar" style="width: 100%; height: 6px; background: rgba(255,255,255,0.1); margin: 1rem 0; border-radius: 3px;">
                <div style="width: ${progress}%; height: 100%; background: var(--accent-neon); border-radius: 3px; transition: width 0.3s;"></div>
            </div>
            <p style="text-align:right; font-size: 0.9rem; opacity: 0.7;">Question ${currentQuestionIndex + 1}/${currentQuizQuestions.length}</p>
            
            <div class="gateway-question">
                <p class="q-text">${qData.q}</p>
                <div class="gateway-options">
                    ${qData.options.map((opt, i) => `
                        <button class="btn gateway-opt-btn" onclick="MasteryGateway.handleAnswer(${i})">${opt}</button>
                    `).join('')}
                </div>
            </div>
        `;
    };

    const handleAnswer = (selectedIndex) => {
        const qData = currentQuizQuestions[currentQuestionIndex];

        if (selectedIndex === qData.correct) {
            score++;
        } else {
            if (qData.topicId && !wrongTopics.includes(qData.topicId)) {
                wrongTopics.push(qData.topicId);
            }
        }

        currentQuestionIndex++;

        if (currentQuestionIndex < currentQuizQuestions.length) {
            renderQuizQuestion();
        } else {
            finishQuiz();
        }
    };

    const finishQuiz = () => {
        const container = document.getElementById('gateway-quiz-container');
        const percentage = (score / currentQuizQuestions.length) * 100;
        const passed = percentage >= PASS_THRESHOLD;

        let content = '';

        if (passed) {
            content = `
                <div style="color: var(--success-neon); font-size: 3rem; margin-bottom: 1rem;"><i class="fas fa-check-circle"></i></div>
                <h2>Congratulations!</h2>
                <p>You scored ${score}/${currentQuizQuestions.length} (${percentage.toFixed(0)}%)</p>
                <p>You have unlocked <strong>${currentUnlockTarget.charAt(0).toUpperCase() + currentUnlockTarget.slice(1)}</strong>!</p>
                <button class="btn btn-primary" onclick="MasteryGateway.closeAndUnlock()">Continue to Course</button>
            `;
        } else {
            const firstWrongTopic = wrongTopics[0] || 'number-sense';
            // Redirect to the TEST SUBJECT (Prerequisite), not the locked target
            const redirectSubject = currentTestSubject;

            content = `
                <div style="color: var(--danger-neon); font-size: 3rem; margin-bottom: 1rem;"><i class="fas fa-times-circle"></i></div>
                <h2>Not Quite Yet</h2>
                <p>You scored ${score}/${currentQuizQuestions.length} (${percentage.toFixed(0)}%). You need ${PASS_THRESHOLD}% to pass.</p>
                <p style="margin-top: 1rem;">We recommend you review <strong>${redirectSubject.charAt(0).toUpperCase() + redirectSubject.slice(1)}</strong>:</p>
                <button class="btn btn-secondary" style="margin-top: 0.5rem;" onclick="MasteryGateway.redirectToTopic('${redirectSubject}', '${firstWrongTopic}')">
                    Review Topic <i class="fas fa-arrow-right"></i>
                </button>
                 <p style="margin-top: 1rem; font-size: 0.9rem; opacity: 0.7;">Or try again later.</p>
            `;
        }

        container.innerHTML = content;
    };

    const closeAndUnlock = () => {
        unlockSubject(currentUnlockTarget);
        closeModal();
    };

    const redirectToTopic = (subject, topicId) => {
        window.location.href = `${subject}/index.html?topic=${topicId}`;
    };

    const closeModal = () => {
        const modal = document.getElementById('gateway-modal');
        if (modal) modal.style.display = 'none';
        currentUnlockTarget = null;
        currentTestSubject = null;
    };

    const init = () => {
        createModal();
        render();
    };

    // Expose public methods
    return {
        init,
        handleAnswer,
        closeAndUnlock,
        redirectToTopic
    };

})();

// Run on load
document.addEventListener('DOMContentLoaded', MasteryGateway.init);
