// Auto-Timer Script
let timers = {};
let timerData = {};

let observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        const timerId = 't' + entry.target.id.substring(1);
        const box = document.getElementById('timer-box-' + timerId);
        if (entry.isIntersecting) {
            entry.target.classList.add('active-card');
            startTimer(timerId, box);
        } else {
            entry.target.classList.remove('active-card');
            stopTimer(timerId, box);
        }
    });
}, { root: null, rootMargin: '0px', threshold: 0.6 });

document.querySelectorAll('.question-card').forEach(card => {
    observer.observe(card);
    const qId = card.id.substring(1);
    timerData['t' + qId] = 0;
});

function startTimer(timerId, box) {
    if (timers[timerId]) return;
    if (box) box.classList.add('running');
    const display = document.getElementById(timerId);
    timers[timerId] = setInterval(() => {
        timerData[timerId]++;
        const m = Math.floor(timerData[timerId] / 60).toString().padStart(2, '0');
        const s = (timerData[timerId] % 60).toString().padStart(2, '0');
        if (display) display.innerText = `${m}:${s}`;
    }, 1000);
}

function stopTimer(timerId, box) {
    if (timers[timerId]) { clearInterval(timers[timerId]); delete timers[timerId]; }
    if (box) box.classList.remove('running');
}

function toggleSolution(id, btn) {
    var content = document.getElementById(id);
    var isCurrentlyOpen = content.style.display === "block";
    document.querySelectorAll('.solution-content').forEach(el => el.style.display = "none");
    document.querySelectorAll('.solution-btn').forEach(el => {
        el.classList.remove('active');
        el.innerHTML = '<i class="fas fa-eye"></i> Show Solution';
    });
    if (!isCurrentlyOpen) {
        content.style.display = "block";
        btn.classList.add('active');
        btn.innerHTML = '<i class="fas fa-eye-slash"></i> Hide Solution';
    }
}

function initImportantMarking() {
    // Create a unique storage key based on the URL path
    const pageKey = window.location.pathname;
    const storageKey = `sjmaths_important_${pageKey}`;

    // Load saved data
    let importantQuestions = JSON.parse(localStorage.getItem(storageKey)) || [];

    document.querySelectorAll('.question-card').forEach(card => {
        const qId = card.id;
        const header = card.querySelector('.q-header');

        if (!header) return;

        // Create the Star Button
        const btn = document.createElement('button');
        btn.className = 'mark-important-btn';
        btn.innerHTML = '<i class="fas fa-star"></i>';
        btn.title = 'Mark as Important';
        btn.setAttribute('aria-label', 'Mark as Important');

        // Apply saved state
        if (importantQuestions.includes(qId)) {
            btn.classList.add('active');
            card.classList.add('important');
        }

        // Click Handler
        btn.addEventListener('click', () => {
            const isActive = btn.classList.toggle('active');
            card.classList.toggle('important', isActive);

            if (isActive) {
                if (!importantQuestions.includes(qId)) importantQuestions.push(qId);
            } else {
                importantQuestions = importantQuestions.filter(id => id !== qId);
            }
            localStorage.setItem(storageKey, JSON.stringify(importantQuestions));
        });

        // Inject into Header (Group with Timer for alignment)
        const timer = header.querySelector('.timer-box');
        if (timer) {
            const wrapper = document.createElement('div');
            wrapper.style.display = 'flex';
            wrapper.style.alignItems = 'center';
            wrapper.style.gap = '10px';

            // Insert wrapper before timer, then move timer and btn inside
            timer.parentNode.insertBefore(wrapper, timer);
            wrapper.appendChild(timer);
            wrapper.appendChild(btn);
        } else {
            header.appendChild(btn);
        }
    });
}

// --- Sync State across Tabs ---
window.addEventListener('storage', (e) => {
    if (e.key && e.key.startsWith('sjmaths_important_')) {
        // If the storage key matches the current page, refresh icons
        const pageKey = window.location.pathname;
        const storageKey = `sjmaths_important_${pageKey}`;
        
        if (e.key === storageKey) {
            const newList = JSON.parse(e.newValue) || [];
            document.querySelectorAll('.question-card').forEach(card => {
                const btn = card.querySelector('.mark-important-btn');
                if (btn) {
                    const isActive = newList.includes(card.id);
                    btn.classList.toggle('active', isActive);
                    card.classList.toggle('important', isActive);
                }
            });
        }
    }
});

// --- Last Visited Tracker ---
const initLastVisited = () => {
    // Only track if we are on an actual exercise page (has questions)
    if (document.querySelector('.question-card')) {
        const pageTitle = document.title.replace(' | SJMaths', '').trim();

        const lastVisited = {
            title: pageTitle,
            url: window.location.href,
            timestamp: Date.now()
        };

        localStorage.setItem('sjmaths_last_visited', JSON.stringify(lastVisited));
    }
};

// --- Focus Mode ---
const initFocusMode = () => {
    // Check if we are on an exercise page
    if (!document.querySelector('.question-card')) return;

    const btn = document.createElement('button');
    btn.className = 'focus-mode-btn';
    btn.innerHTML = '<i class="fas fa-bullseye"></i> <span>Focus Mode</span>';
    btn.title = 'Toggle Focus Mode';
    
    btn.addEventListener('click', () => {
        const isFocus = document.body.classList.toggle('focus-mode');
        btn.classList.toggle('active', isFocus);
        
        if (isFocus) {
            btn.innerHTML = '<i class="fas fa-times"></i> <span>Exit Focus</span>';
        } else {
            btn.innerHTML = '<i class="fas fa-bullseye"></i> <span>Focus Mode</span>';
        }
    });

    document.body.appendChild(btn);
};

// --- Static Formula Data (Moved out of function for performance) ---
const formulaData = {
    'chapter-1-number-systems': {
        sections: [
            {
                title: 'Laws of Exponents',
                items: [
                    '$a^m \\cdot a^n = a^{m+n}$',
                    '$(a^m)^n = a^{mn}$',
                    '$\\frac{a^m}{a^n} = a^{m-n}$',
                    '$a^m b^m = (ab)^m$',
                    '$a^0 = 1, \\quad a^{-n} = \\frac{1}{a^n}$'
                ]
            },
            {
                title: 'Identities for Real Numbers',
                items: [
                    '$\\sqrt{ab} = \\sqrt{a}\\sqrt{b}$',
                    '$\\sqrt{\\frac{a}{b}} = \\frac{\\sqrt{a}}{\\sqrt{b}}$',
                    '$(\\sqrt{a}+\\sqrt{b})(\\sqrt{a}-\\sqrt{b}) = a-b$',
                    '$(a+\\sqrt{b})(a-\\sqrt{b}) = a^2-b$',
                    '$(\\sqrt{a}+\\sqrt{b})^2 = a+2\\sqrt{ab}+b$'
                ]
            }
        ]
    },
    'chapter-2-polynomials': {
        sections: [
            {
                title: 'Algebraic Identities',
                items: [
                    '$(x+y)^2 = x^2 + 2xy + y^2$',
                    '$(x-y)^2 = x^2 - 2xy + y^2$',
                    '$x^2 - y^2 = (x+y)(x-y)$',
                    '$(x+a)(x+b) = x^2 + (a+b)x + ab$',
                    '$(x+y+z)^2 = x^2+y^2+z^2+2xy+2yz+2zx$'
                ]
            },
            {
                title: 'Cubic Identities',
                items: [
                    '$(x+y)^3 = x^3 + y^3 + 3xy(x+y)$',
                    '$(x-y)^3 = x^3 - y^3 - 3xy(x-y)$',
                    '$x^3+y^3+z^3-3xyz = (x+y+z)(x^2+y^2+z^2-xy-yz-zx)$'
                ]
            },
            {
                title: 'Theorems',
                items: [
                    '<strong>Remainder Theorem:</strong> If $p(x)$ is divided by $(x-a)$, remainder is $p(a)$.',
                    '<strong>Factor Theorem:</strong> $(x-a)$ is a factor of $p(x)$ if $p(a) = 0$.'
                ]
            }
        ]
    },
    'chapter-3-coordinate-geometry': {
        sections: [
            {
                title: 'Cartesian System',
                items: [
                    '<strong>Origin:</strong> $(0, 0)$',
                    '<strong>x-axis:</strong> Horizontal line ($y=0$)',
                    '<strong>y-axis:</strong> Vertical line ($x=0$)',
                    '<strong>Quadrants:</strong> Four parts of the plane'
                ]
            },
            {
                title: 'Sign Convention',
                items: [
                    '<strong>Quad I:</strong> $(+, +)$',
                    '<strong>Quad II:</strong> $(-, +)$',
                    '<strong>Quad III:</strong> $(-, -)$',
                    '<strong>Quad IV:</strong> $(+, -)$'
                ]
            },
            {
                title: 'Coordinates',
                items: [
                    '$(x, y)$: Ordered pair',
                    '$x$: Abscissa (distance from y-axis)',
                    '$y$: Ordinate (distance from x-axis)'
                ]
            }
        ]
    },
    'chapter-4-linear-equations-in-two-variables': {
        sections: [
            {
                title: 'Standard Form',
                items: [
                    '$ax + by + c = 0$',
                    'where $a, b, c$ are real numbers',
                    '$a$ and $b$ are not both zero'
                ]
            },
            {
                title: 'Properties',
                items: [
                    'A linear equation in two variables has infinitely many solutions.',
                    'The graph of every linear equation in two variables is a straight line.',
                    '$x = 0$ is the equation of the y-axis.',
                    '$y = 0$ is the equation of the x-axis.'
                ]
            },
            {
                title: 'Lines Parallel to Axes',
                items: [
                    '$x = a$: Graph is parallel to y-axis',
                    '$y = a$: Graph is parallel to x-axis'
                ]
            }
        ]
    },
    'chapter-5-introduction-to-euclids-geometry': {
        sections: [
            {
                title: 'Euclid\'s Axioms',
                items: [
                    'Things equal to the same thing are equal to one another.',
                    'If equals are added to equals, the wholes are equal.',
                    'If equals are subtracted from equals, the remainders are equal.',
                    'Things which coincide with one another are equal to one another.',
                    'The whole is greater than the part.'
                ]
            },
            {
                title: 'Euclid\'s Postulates',
                items: [
                    'A straight line may be drawn from any one point to any other point.',
                    'A terminated line can be produced indefinitely.',
                    'A circle can be drawn with any centre and any radius.',
                    'All right angles are equal to one another.',
                    '<strong>Parallel Postulate:</strong> If a straight line falling on two straight lines makes the interior angles on the same side of it taken together less than two right angles, then the two straight lines, if produced indefinitely, meet on that side.'
                ]
            }
        ]
    },
    'chapter-6-lines-and-angles': {
        sections: [
            {
                title: 'Angle Properties',
                items: [
                    '<strong>Linear Pair:</strong> Sum is $180^\\circ$',
                    '<strong>Vertically Opposite:</strong> Equal',
                    '<strong>Complementary:</strong> Sum is $90^\\circ$',
                    '<strong>Supplementary:</strong> Sum is $180^\\circ$'
                ]
            },
            {
                title: 'Parallel Lines',
                items: [
                    'Corresponding angles are equal',
                    'Alternate interior angles are equal',
                    'Consecutive interior angles sum to $180^\\circ$'
                ]
            }
        ]
    },
    'chapter-7-triangles': {
        sections: [
            {
                title: 'Congruence Criteria',
                items: [
                    '<strong>SAS:</strong> Side-Angle-Side',
                    '<strong>ASA:</strong> Angle-Side-Angle',
                    '<strong>AAS:</strong> Angle-Angle-Side',
                    '<strong>SSS:</strong> Side-Side-Side',
                    '<strong>RHS:</strong> Right angle-Hypotenuse-Side'
                ]
            },
            {
                title: 'Triangle Properties',
                items: [
                    'Angles opposite to equal sides are equal',
                    'Sides opposite to equal angles are equal',
                    'Sum of angles = $180^\\circ$',
                    'Ext. Angle = Sum of interior opposite angles'
                ]
            },
            {
                title: 'Inequalities',
                items: [
                    'Angle opposite to longer side is larger',
                    'Side opposite to larger angle is longer',
                    'Sum of two sides > Third side'
                ]
            }
        ]
    },
    'chapter-8-quadrilaterals': {
        sections: [
            {
                title: 'Properties of Parallelogram',
                items: [
                    'Opposite sides are equal',
                    'Opposite angles are equal',
                    'Diagonals bisect each other'
                ]
            },
            {
                title: 'Mid-point Theorem',
                items: [
                    'The line segment joining the mid-points of two sides of a triangle is parallel to the third side and is half of it.'
                ]
            }
        ]
    },
    'chapter-9-circles': {
        sections: [
            {
                title: 'Chords & Centre',
                items: [
                    'Equal chords subtend equal angles at centre',
                    'Perpendicular from centre to chord bisects it',
                    'Equal chords are equidistant from centre'
                ]
            },
            {
                title: 'Angles Subtended by Arc',
                items: [
                    'Angle at centre is double the angle at remaining part',
                    'Angles in same segment are equal',
                    'Angle in semicircle is $90^\\circ$',
                    '<strong>Cyclic Quadrilateral:</strong> Sum of opposite angles is $180^\\circ$'
                ]
            }
        ]
    },
    'chapter-10-herons-formula': {
        sections: [
            {
                title: 'Heron\'s Formula',
                items: [
                    '<strong>Area of Triangle:</strong> $\\sqrt{s(s-a)(s-b)(s-c)}$',
                    'where $a, b, c$ are sides',
                    '<strong>Semi-perimeter ($s$):</strong> $s = \\frac{a+b+c}{2}$'
                ]
            }
        ]
    },
    'chapter-11-surface-areas-and-volumes': {
        sections: [
            {
                title: 'Surface Areas',
                items: [
                    '<strong>Cuboid (TSA):</strong> $2(lb+bh+hl)$',
                    '<strong>Cube (TSA):</strong> $6a^2$',
                    '<strong>Cylinder (CSA):</strong> $2\\pi rh$',
                    '<strong>Cone (CSA):</strong> $\\pi rl$',
                    '<strong>Sphere (SA):</strong> $4\\pi r^2$',
                    '<strong>Hemisphere (CSA):</strong> $2\\pi r^2$'
                ]
            },
            {
                title: 'Volumes',
                items: [
                    '<strong>Cuboid:</strong> $lbh$',
                    '<strong>Cube:</strong> $a^3$',
                    '<strong>Cylinder:</strong> $\\pi r^2 h$',
                    '<strong>Cone:</strong> $\\frac{1}{3}\\pi r^2 h$',
                    '<strong>Sphere:</strong> $\\frac{4}{3}\\pi r^3$',
                    '<strong>Hemisphere:</strong> $\\frac{2}{3}\\pi r^3$'
                ]
            }
        ]
    },
    'chapter-12-statistics': {
        sections: [
            {
                title: 'Measures of Central Tendency',
                items: [
                    '<strong>Mean ($\\bar{x}$):</strong> $\\frac{\\sum x_i}{n}$',
                    '<strong>Median:</strong> Middle value (sorted data)',
                    '<strong>Mode:</strong> Most frequent value'
                ]
            },
            {
                title: 'Graphical Representation',
                items: [
                    '<strong>Bar Graph:</strong> Uniform width bars with equal spacing',
                    '<strong>Histogram:</strong> Continuous class intervals',
                    '<strong>Class Mark:</strong> $\\frac{\\text{Upper Limit} + \\text{Lower Limit}}{2}$'
                ]
            }
        ]
    },
    'chapter-5-continuity-and-differentiability': {
        sections: [
            {
                title: 'Continuity',
                items: [
                    'Continuous at $c$ if $\\lim_{x \\to c} f(x) = f(c)$',
                    'LHL = RHL = Value of function'
                ]
            },
            {
                title: 'Differentiation Rules',
                items: [
                    'Product Rule: $\\frac{d}{dx}(uv) = u\\frac{dv}{dx} + v\\frac{du}{dx}$',
                    'Quotient Rule: $\\frac{d}{dx}(\\frac{u}{v}) = \\frac{v\\frac{du}{dx} - u\\frac{dv}{dx}}{v^2}$',
                    'Chain Rule: $\\frac{dy}{dx} = \\frac{dy}{dt} \\times \\frac{dt}{dx}$'
                ]
            },
            {
                title: 'Standard Derivatives',
                items: [
                    '$\\frac{d}{dx}(\\sin x) = \\cos x$',
                    '$\\frac{d}{dx}(\\cos x) = -\\sin x$',
                    '$\\frac{d}{dx}(\\tan x) = \\sec^2 x$',
                    '$\\frac{d}{dx}(e^x) = e^x$',
                    '$\\frac{d}{dx}(\\log x) = \\frac{1}{x}$'
                ]
            },
            {
                title: 'Mean Value Theorems',
                items: [
                    '<strong>Rolle\'s Theorem:</strong> $f\'(c) = 0$ for some $c \\in (a, b)$',
                    '<strong>MVT:</strong> $f\'(c) = \\frac{f(b)-f(a)}{b-a}$'
                ]
            }
        ]
    },
    'chapter-6-applications-of-derivatives': {
        sections: [
            {
                title: 'Rate of Change',
                items: [
                    '$\\frac{dy}{dt} = \\frac{dy}{dx} \\cdot \\frac{dx}{dt}$',
                    'Marginal Cost: $MC = \\frac{dC}{dx}$',
                    'Marginal Revenue: $MR = \\frac{dR}{dx}$'
                ]
            },
            {
                title: 'Increasing & Decreasing',
                items: [
                    'Strictly Increasing: $f\'(x) > 0$',
                    'Strictly Decreasing: $f\'(x) < 0$',
                    'Increasing: $f\'(x) \\ge 0$',
                    'Decreasing: $f\'(x) \\le 0$'
                ]
            },
            {
                title: 'Tangents & Normals',
                items: [
                    'Slope of Tangent ($m$): $f\'(x_0)$',
                    'Slope of Normal: $-\\frac{1}{m}$',
                    'Eq. of Tangent: $y-y_0 = m(x-x_0)$',
                    'Eq. of Normal: $y-y_0 = -\\frac{1}{m}(x-x_0)$'
                ]
            },
            {
                title: 'Maxima & Minima',
                items: [
                    'Critical Point: $f\'(x) = 0$',
                    '<strong>Second Derivative Test:</strong>',
                    'Local Maxima if $f\'\'(c) < 0$',
                    'Local Minima if $f\'\'(c) > 0$',
                    'Test Fails if $f\'\'(c) = 0$'
                ]
            }
        ]
    },
    'chapter-7-integrals': {
        sections: [
            {
                title: 'Standard Integrals',
                items: [
                    '$\\int x^n dx = \\frac{x^{n+1}}{n+1} + C$',
                    '$\\int \\frac{1}{x} dx = \\log|x| + C$',
                    '$\\int e^x dx = e^x + C$',
                    '$\\int a^x dx = \\frac{a^x}{\\log a} + C$',
                    '$\\int \\sin x dx = -\\cos x + C$',
                    '$\\int \\cos x dx = \\sin x + C$',
                    '$\\int \\sec^2 x dx = \\tan x + C$',
                    '$\\int \\csc^2 x dx = -\\cot x + C$',
                    '$\\int \\frac{dx}{\\sqrt{1-x^2}} = \\sin^{-1} x + C$',
                    '$\\int \\frac{dx}{1+x^2} = \\tan^{-1} x + C$'
                ]
            },
            {
                title: 'Integration by Substitution',
                items: [
                    '$\\int \\tan x dx = \\log|\\sec x| + C$',
                    '$\\int \\cot x dx = \\log|\\sin x| + C$',
                    '$\\int \\sec x dx = \\log|\\sec x + \\tan x| + C$',
                    '$\\int \\csc x dx = \\log|\\csc x - \\cot x| + C$'
                ]
            },
            {
                title: 'Special Integrals',
                items: [
                    '$\\int \\frac{dx}{x^2-a^2} = \\frac{1}{2a} \\log|\\frac{x-a}{x+a}| + C$',
                    '$\\int \\frac{dx}{a^2-x^2} = \\frac{1}{2a} \\log|\\frac{a+x}{a-x}| + C$',
                    '$\\int \\frac{dx}{x^2+a^2} = \\frac{1}{a} \\tan^{-1}\\frac{x}{a} + C$',
                    '$\\int \\frac{dx}{\\sqrt{a^2-x^2}} = \\sin^{-1}\\frac{x}{a} + C$',
                    '$\\int \\frac{dx}{\\sqrt{x^2\\pm a^2}} = \\log|x+\\sqrt{x^2\\pm a^2}| + C$'
                ]
            },
            {
                title: 'Integration by Parts',
                items: [
                    '$\\int u v dx = u \\int v dx - \\int (u\' \\int v dx) dx$',
                    '<strong>ILATE Rule:</strong> Inverse, Logarithmic, Algebraic, Trigonometric, Exponential'
                ]
            },
            {
                title: 'Properties of Definite Integrals',
                items: [
                    '$\\int_a^b f(x) dx = \\int_a^b f(t) dt$',
                    '$\\int_a^b f(x) dx = -\\int_b^a f(x) dx$',
                    '$\\int_a^b f(x) dx = \\int_a^c f(x) dx + \\int_c^b f(x) dx$',
                    '$\\int_a^b f(x) dx = \\int_a^b f(a+b-x) dx$',
                    '$\\int_0^a f(x) dx = \\int_0^a f(a-x) dx$',
                    '$\\int_{-a}^a f(x) dx = 2\\int_0^a f(x) dx$ (Even), $0$ (Odd)'
                ]
            }
        ]
    },
    'chapter-8-application-of-integrals': {
        sections: [
            {
                title: 'Area under Simple Curves',
                items: [
                    'Area bounded by curve $y=f(x)$, x-axis and lines $x=a, x=b$: $\\int_a^b y dx = \\int_a^b f(x) dx$',
                    'Area bounded by curve $x=g(y)$, y-axis and lines $y=c, y=d$: $\\int_c^d x dy = \\int_c^d g(y) dy$'
                ]
            },
            {
                title: 'Area between Two Curves',
                items: [
                    'Area between $y=f(x)$ and $y=g(x)$: $\\int_a^b [f(x) - g(x)] dx$',
                    'Where $f(x) \\ge g(x)$ in $[a, b]$'
                ]
            }
        ]
    },
    'chapter-9-differential-equations': {
        sections: [
            {
                title: 'Basic Concepts',
                items: [
                    '<strong>Order:</strong> Highest order derivative present',
                    '<strong>Degree:</strong> Power of highest order derivative (when polynomial in derivatives)'
                ]
            },
            {
                title: 'Methods of Solving',
                items: [
                    '<strong>Variable Separable:</strong> $\\int f(y) dy = \\int g(x) dx$',
                    '<strong>Homogeneous:</strong> Put $y=vx$, then $\\frac{dy}{dx} = v + x\\frac{dv}{dx}$',
                    '<strong>Linear DE:</strong> $\\frac{dy}{dx} + Py = Q$',
                    'Integrating Factor (I.F.) = $e^{\\int P dx}$',
                    'Solution: $y(\\text{I.F.}) = \\int (Q \\times \\text{I.F.}) dx + C$'
                ]
            }
        ]
    },
    'chapter-10-vector-algebra': {
        sections: [
            {
                title: 'Basic Concepts',
                items: [
                    '<strong>Magnitude:</strong> $|\\vec{a}| = \\sqrt{x^2+y^2+z^2}$',
                    '<strong>Unit Vector:</strong> $\\hat{a} = \\frac{\\vec{a}}{|\\vec{a}|}$',
                    '<strong>Direction Cosines:</strong> $l^2+m^2+n^2=1$'
                ]
            },
            {
                title: 'Scalar (Dot) Product',
                items: [
                    '$\\vec{a} \\cdot \\vec{b} = |\\vec{a}||\\vec{b}|\\cos\\theta$',
                    '$\\vec{a} \\cdot \\vec{b} = a_1b_1 + a_2b_2 + a_3b_3$',
                    '<strong>Projection of $\\vec{a}$ on $\\vec{b}$:</strong> $\\frac{\\vec{a} \\cdot \\vec{b}}{|\\vec{b}|}$',
                    'If $\\vec{a} \\perp \\vec{b}$, then $\\vec{a} \\cdot \\vec{b} = 0$'
                ]
            },
            {
                title: 'Vector (Cross) Product',
                items: [
                    '$\\vec{a} \\times \\vec{b} = |\\vec{a}||\\vec{b}|\\sin\\theta \\hat{n}$',
                    '$\\vec{a} \\times \\vec{b} = \\begin{vmatrix} \\hat{i} & \\hat{j} & \\hat{k} \\\\ a_1 & a_2 & a_3 \\\\ b_1 & b_2 & b_3 \\end{vmatrix}$',
                    '<strong>Area of Triangle:</strong> $\\frac{1}{2}|\\vec{a} \\times \\vec{b}|$',
                    '<strong>Area of Parallelogram:</strong> $|\\vec{a} \\times \\vec{b}|$'
                ]
            }
        ]
    },
    'chapter-11-three-dimensional-geometry': {
        sections: [
            {
                title: 'Direction Cosines & Ratios',
                items: [
                    '$l = \\cos\\alpha, m = \\cos\\beta, n = \\cos\\gamma$',
                    '$l^2 + m^2 + n^2 = 1$',
                    'Relation with DRs ($a,b,c$): $l = \\pm\\frac{a}{\\sqrt{a^2+b^2+c^2}}$'
                ]
            },
            {
                title: 'Equation of a Line',
                items: [
                    '<strong>Vector Form:</strong> $\\vec{r} = \\vec{a} + \\lambda\\vec{b}$',
                    '<strong>Cartesian Form:</strong> $\\frac{x-x_1}{a} = \\frac{y-y_1}{b} = \\frac{z-z_1}{c}$',
                    '<strong>Two Points:</strong> $\\frac{x-x_1}{x_2-x_1} = \\frac{y-y_1}{y_2-y_1} = \\frac{z-z_1}{z_2-z_1}$'
                ]
            },
            {
                title: 'Angle & Distance',
                items: [
                    '$\\cos\\theta = \\left|\\frac{\\vec{b_1} \\cdot \\vec{b_2}}{|\\vec{b_1}||\\vec{b_2}|}\\right|$',
                    '<strong>Shortest Distance (Skew):</strong> $\\left|\\frac{(\\vec{b_1} \\times \\vec{b_2}) \\cdot (\\vec{a_2} - \\vec{a_1})}{|\\vec{b_1} \\times \\vec{b_2}|}\\right|$',
                    '<strong>Distance (Parallel):</strong> $\\left|\\frac{\\vec{b} \\times (\\vec{a_2} - \\vec{a_1})}{|\\vec{b}|}\\right|$'
                ]
            }
        ]
    },
    'chapter-12-linear-programming': {
        sections: [
            {
                title: 'Linear Programming Problem (LPP)',
                items: [
                    '<strong>Objective Function:</strong> $Z = ax + by$ (to be optimized)',
                    '<strong>Constraints:</strong> Linear inequalities like $ax + by \\le c$',
                    '<strong>Feasible Region:</strong> Common region determined by all constraints',
                    '<strong>Corner Point Method:</strong> Optimal value occurs at a corner point of the feasible region.'
                ]
            }
        ]
    },
    'chapter-13-probability': {
        sections: [
            {
                title: 'Conditional Probability',
                items: [
                    '$P(A|B) = \\frac{P(A \\cap B)}{P(B)}, \\quad P(B) \\neq 0$',
                    '$P(A \\cap B) = P(A) P(B|A)$',
                    'If A and B are independent: $P(A \\cap B) = P(A)P(B)$'
                ]
            },
            {
                title: 'Multiplication Theorem & Independence',
                items: [
                    '$P(A \\cap B) = P(A) P(B|A) = P(B) P(A|B)$',
                    '<strong>Independent Events:</strong> $P(A \\cap B) = P(A) P(B)$',
                    'If A and B are independent, then:',
                    '(i) A and B\' are independent',
                    '(ii) A\' and B are independent',
                    '(iii) A\' and B\' are independent'
                ]
            },
            {
                title: 'Bayes\' Theorem & Total Probability',
                items: [
                    '<strong>Theorem of Total Probability:</strong> $P(A) = \\sum_{j=1}^{n} P(E_j) P(A|E_j)$',
                    '<strong>Bayes\' Theorem:</strong> $P(E_i|A) = \\frac{P(E_i) P(A|E_i)}{\\sum_{j=1}^{n} P(E_j) P(A|E_j)}$'
                ]
            },
            {
                title: 'Random Variables & Distributions',
                items: [
                    '<strong>Mean ($E(X)$):</strong> $\\mu = \\sum x_i p_i$',
                    '<strong>Variance:</strong> $\\sigma^2 = \\sum x_i^2 p_i - (\\sum x_i p_i)^2$',
                    '<strong>Binomial Dist:</strong> $P(X=r) = {^nC_r} p^r q^{n-r}$'
                ]
            }
        ]
    }
 };

// --- Formula Sheet Modal ---
const initFormulaSheet = () => {
    if (!document.querySelector('.question-card')) return;

    // 1. Create Button
    const btn = document.createElement('button');
    btn.className = 'formula-btn';
    btn.innerHTML = '<i class="fas fa-calculator"></i> <span>Formulas</span>';
    btn.title = 'Open Formula Sheet';
    document.body.appendChild(btn);

    // Determine current chapter content
    const path = window.location.pathname;
    let activeData = formulaData['chapter-1-number-systems']; // Default

    for (const key in formulaData) {
        if (path.includes(key)) {
            activeData = formulaData[key];
            break;
        }
    }

    // Generate HTML for sections
    const sectionsHTML = activeData.sections.map(section => `
        <div class="fm-section">
            <h3>${section.title}</h3>
            <div class="formula-grid">
                ${section.items.map(item => `<div class="formula-item">${item}</div>`).join('')}
            </div>
        </div>
    `).join('');

    // 2. Create Modal HTML
    const modalOverlay = document.createElement('div');
    modalOverlay.className = 'formula-modal-overlay';
    modalOverlay.innerHTML = `
        <div class="formula-modal">
            <div class="fm-header">
                <h2><i class="fas fa-square-root-variable"></i> Quick Formulas</h2>
                <button class="fm-close"><i class="fas fa-times"></i></button>
            </div>
            <div class="fm-body">
                ${sectionsHTML}
                <p style="text-align: center; color: #666; margin-top: 2rem; font-size: 0.9rem;">
                    <em>Note: This is a quick reference sheet. For full notes, visit the Chapter Notes section.</em>
                </p>
            </div>
        </div>
    `;
    document.body.appendChild(modalOverlay);

    // 3. Logic
    const closeBtn = modalOverlay.querySelector('.fm-close');
    
    function openModal() {
        modalOverlay.classList.add('active');
        document.body.style.overflow = 'hidden';
        // Ensure MathJax renders the modal content
        if (window.MathJax) MathJax.typesetPromise([modalOverlay]).catch(() => {});
    }

    function closeModal() {
        modalOverlay.classList.remove('active');
        document.body.style.overflow = '';
    }

    btn.addEventListener('click', openModal);
    closeBtn.addEventListener('click', closeModal);
    modalOverlay.addEventListener('click', (e) => { if (e.target === modalOverlay) closeModal(); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeModal(); });
};

// --- Main Initialization ---
document.addEventListener('DOMContentLoaded', () => {
    initImportantMarking();
    initLastVisited();
    initFocusMode();
    initFormulaSheet();
});