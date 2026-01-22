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
    'chapter-1-real-numbers': {
        sections: [
            {
                title: 'Fundamental Theorem of Arithmetic',
                items: [
                    'Every composite number can be expressed as a product of primes uniquely.',
                    'HCF$(a, b) \\times$ LCM$(a, b) = a \\times b$'
                ]
            },
            {
                title: 'Irrational Numbers',
                items: [
                    'If a prime $p$ divides $a^2$, then $p$ divides $a$.',
                    '$\\sqrt{2}, \\sqrt{3}, 5-\\sqrt{3}$ are irrational numbers.'
                ]
            }
        ]
    },
    'chapter-2-polynomials-c10': {
        sections: [
            {
                title: 'Quadratic Polynomials',
                items: [
                    'Standard Form: $p(x) = ax^2 + bx + c$',
                    'Sum of zeros ($\\alpha + \\beta$) = $-\\frac{b}{a}$',
                    'Product of zeros ($\\alpha\\beta$) = $\\frac{c}{a}$',
                    'Formation: $k[x^2 - (\\text{Sum})x + \\text{Product}]$'
                ]
            },
            {
                title: 'Cubic Polynomials',
                items: [
                    'Standard Form: $ax^3 + bx^2 + cx + d$',
                    '$\\alpha + \\beta + \\gamma = -\\frac{b}{a}$',
                    '$\\alpha\\beta + \\beta\\gamma + \\gamma\\alpha = \\frac{c}{a}$',
                    '$\\alpha\\beta\\gamma = -\\frac{d}{a}$'
                ]
            },
            {
                title: 'Division Algorithm',
                items: [
                    '$p(x) = g(x)q(x) + r(x)$',
                    'deg $r(x) <$ deg $g(x)$ or $r(x) = 0$'
                ]
            }
        ]
    },
    'chapter-3-pair-of-linear-equations-in-two-variables': {
        sections: [
            {
                title: 'Consistency',
                items: [
                    '$a_1x+b_1y+c_1=0, a_2x+b_2y+c_2=0$',
                    '$\\frac{a_1}{a_2} \\neq \\frac{b_1}{b_2}$: Intersecting (Unique Solution)',
                    '$\\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2}$: Coincident (Infinite Solutions)',
                    '$\\frac{a_1}{a_2} = \\frac{b_1}{b_2} \\neq \\frac{c_1}{c_2}$: Parallel (No Solution)'
                ]
            },
            {
                title: 'Algebraic Methods',
                items: [
                    'Substitution Method',
                    'Elimination Method',
                    'Cross-Multiplication: $\\frac{x}{b_1c_2-b_2c_1} = \\frac{y}{c_1a_2-c_2a_1} = \\frac{1}{a_1b_2-a_2b_1}$'
                ]
            }
        ]
    },
    'chapter-4-quadratic-equations': {
        sections: [
            {
                title: 'Quadratic Formula',
                items: [
                    'Roots of $ax^2+bx+c=0$:',
                    '$x = \\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}$'
                ]
            },
            {
                title: 'Nature of Roots',
                items: [
                    'Discriminant $D = b^2-4ac$',
                    '$D > 0$: Two distinct real roots',
                    '$D = 0$: Two equal real roots ($x = -b/2a$)',
                    '$D < 0$: No real roots'
                ]
            }
        ]
    },
    'chapter-5-arithmetic-progressions': {
        sections: [
            {
                title: 'General Term',
                items: [
                    '$a_n = a + (n-1)d$',
                    '$a$: First term, $d$: Common difference'
                ]
            },
            {
                title: 'Sum of n Terms',
                items: [
                    '$S_n = \\frac{n}{2}[2a + (n-1)d]$',
                    '$S_n = \\frac{n}{2}(a + a_n)$',
                    'Sum of first $n$ positive integers: $\\frac{n(n+1)}{2}$'
                ]
            },
            {
                title: 'Properties',
                items: [
                    'If $a, b, c$ are in AP, then $2b = a + c$'
                ]
            }
        ]
    },
    'chapter-6-triangles': {
        sections: [
            {
                title: 'Similarity',
                items: [
                    'Criteria: <strong>AAA, SSS, SAS</strong>',
                    'Ratio of Areas: $\\frac{\\text{ar}(ABC)}{\\text{ar}(PQR)} = (\\frac{AB}{PQ})^2 = (\\frac{BC}{QR})^2 = (\\frac{CA}{RP})^2$'
                ]
            },
            {
                title: 'Theorems',
                items: [
                    '<strong>BPT:</strong> If line || to one side, it divides other two sides in same ratio.',
                    '<strong>Pythagoras:</strong> In right $\\Delta$, $H^2 = P^2 + B^2$.'
                ]
            }
        ]
    },
    'chapter-7-coordinate-geometry': {
        sections: [
            {
                title: 'Formulas',
                items: [
                    '<strong>Distance:</strong> $\\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$',
                    '<strong>Section Formula:</strong> $(\\frac{m_1x_2+m_2x_1}{m_1+m_2}, \\frac{m_1y_2+m_2y_1}{m_1+m_2})$',
                    '<strong>Mid-point:</strong> $(\\frac{x_1+x_2}{2}, \\frac{y_1+y_2}{2})$',
                    '<strong>Centroid:</strong> $(\\frac{x_1+x_2+x_3}{3}, \\frac{y_1+y_2+y_3}{3})$',
                    '<strong>Area of $\\Delta$:</strong> $\\frac{1}{2}|x_1(y_2-y_3) + x_2(y_3-y_1) + x_3(y_1-y_2)|$'
                ]
            }
        ]
    },
    'chapter-8-introduction-to-trigonometry': {
        sections: [
            {
                title: 'Trigonometric Ratios',
                items: [
                    '$\\sin\\theta = P/H, \\cos\\theta = B/H, \\tan\\theta = P/B$',
                    '$\\csc\\theta = H/P, \\sec\\theta = H/B, \\cot\\theta = B/P$'
                ]
            },
            {
                title: 'Identities',
                items: [
                    '$\\sin^2\\theta + \\cos^2\\theta = 1$',
                    '$1 + \\tan^2\\theta = \\sec^2\\theta$',
                    '$1 + \\cot^2\\theta = \\csc^2\\theta$'
                ]
            },
            {
                title: 'Values',
                items: [
                    '$\\sin$: $0, 1/2, 1/\\sqrt{2}, \\sqrt{3}/2, 1$',
                    '$\\cos$: $1, \\sqrt{3}/2, 1/\\sqrt{2}, 1/2, 0$',
                    '$\\tan$: $0, 1/\\sqrt{3}, 1, \\sqrt{3}, \\text{ND}$'
                ]
            }
        ]
    },
    'chapter-9-applications-of-trigonometry': {
        sections: [
            {
                title: 'Heights and Distances',
                items: [
                    '<strong>Line of Sight:</strong> Line from eye to object.',
                    '<strong>Angle of Elevation:</strong> Object above horizontal level.',
                    '<strong>Angle of Depression:</strong> Object below horizontal level.'
                ]
            }
        ]
    },
    'chapter-10-circles': {
        sections: [
            {
                title: 'Tangents',
                items: [
                    'Tangent $\\perp$ Radius at point of contact.',
                    'Tangents from external point are equal in length.',
                    'They subtend equal angles at the centre.',
                    'They are equally inclined to the line joining the centre and that point.'
                ]
            }
        ]
    },
    'chapter-11-areas-related-to-circles': {
        sections: [
            {
                title: 'Formulas',
                items: [
                    'Circumference $= 2\\pi r$',
                    'Area $= \\pi r^2$',
                    'Arc Length $= \\frac{\\theta}{360} \\times 2\\pi r$',
                    'Sector Area $= \\frac{\\theta}{360} \\times \\pi r^2$',
                    'Segment Area = Sector Area - $\\Delta$ Area',
                    'Area of Ring $= \\pi(R^2 - r^2)$'
                ]
            }
        ]
    },
    'chapter-12-surface-areas-and-volumes': {
        sections: [
            {
                title: 'Basic Solids',
                items: [
                    '<strong>Cuboid:</strong> TSA $2(lb+bh+hl)$, Vol $lbh$',
                    '<strong>Cube:</strong> TSA $6a^2$, Vol $a^3$',
                    '<strong>Cylinder:</strong> CSA $2\\pi rh$, Vol $\\pi r^2h$',
                    '<strong>Cone:</strong> CSA $\\pi rl$, Vol $\\frac{1}{3}\\pi r^2h$',
                    '<strong>Sphere:</strong> SA $4\\pi r^2$, Vol $\\frac{4}{3}\\pi r^3$',
                    '<strong>Hemisphere:</strong> CSA $2\\pi r^2$, Vol $\\frac{2}{3}\\pi r^3$'
                ]
            },
            {
                title: 'Frustum of Cone',
                items: [
                    '$h$: height, $l$: slant height, $r_1, r_2$: radii',
                    'Vol: $\\frac{1}{3}\\pi h(r_1^2+r_2^2+r_1r_2)$',
                    'CSA: $\\pi l(r_1+r_2)$, where $l=\\sqrt{h^2+(r_1-r_2)^2}$',
                    'TSA: $\\pi l(r_1+r_2) + \\pi r_1^2 + \\pi r_2^2$'
                ]
            }
        ]
    },
    'chapter-13-statistics': {
        sections: [
            {
                title: 'Mean',
                items: [
                    'Direct: $\\bar{x} = \\frac{\\sum f_ix_i}{\\sum f_i}$',
                    'Assumed Mean: $\\bar{x} = a + \\frac{\\sum f_id_i}{\\sum f_i}$',
                    'Step Deviation: $\\bar{x} = a + (\\frac{\\sum f_iu_i}{\\sum f_i})h$'
                ]
            },
            {
                title: 'Mode & Median',
                items: [
                    'Mode $= l + (\\frac{f_1-f_0}{2f_1-f_0-f_2})h$',
                    'Median $= l + (\\frac{n/2-cf}{f})h$',
                    '<strong>3 Median = Mode + 2 Mean</strong>'
                ]
            }
        ]
    },
    'chapter-14-probability': {
        sections: [
            {
                title: 'Concepts',
                items: [
                    '$P(E) = \\frac{\\text{Favourable Outcomes}}{\\text{Total Outcomes}}$',
                    '$0 \\le P(E) \\le 1$',
                    '$P(E) + P(\\text{not } E) = 1$',
                    'Sure Event: $P(E)=1$, Impossible: $P(E)=0$'
                ]
            },
            {
                title: 'Outcomes',
                items: [
                    'Coin: H, T (2)',
                    'Two Coins: HH, HT, TH, TT (4)',
                    'Dice: 1, 2, 3, 4, 5, 6',
                    'Cards: 52 Total (26 Red, 26 Black), 4 Suits (13 each), 12 Face Cards'
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
    },
    'chapter-1-sets': {
        sections: [
            {
                title: 'Set Operations',
                items: [
                    'Union: $A \\cup B = \\{x: x \\in A \\text{ or } x \\in B\\}$',
                    'Intersection: $A \\cap B = \\{x: x \\in A \\text{ and } x \\in B\\}$',
                    'Difference: $A - B = \\{x: x \\in A, x \\notin B\\}$',
                    'Complement: $A\' = U - A$'
                ]
            },
            {
                title: 'Formulas',
                items: [
                    '$n(A \\cup B) = n(A) + n(B) - n(A \\cap B)$',
                    '$(A \\cup B)\' = A\' \\cap B\'$ (De Morgan)'
                ]
            }
        ]
    },
    'chapter-2-relations-and-functions': {
        sections: [
            {
                title: 'Cartesian Product',
                items: [
                    '$A \\times B = \\{(a, b): a \\in A, b \\in B\\}$',
                    '$n(A \\times B) = n(A) \\times n(B)$'
                ]
            }
        ]
    },
    'chapter-3-trigonometric-functions': {
        sections: [
            {
                title: 'Formulas',
                items: [
                    '$l = r\\theta$ ($\\theta$ in radians)',
                    '$\\sin(x \\pm y) = \\sin x \\cos y \\pm \\cos x \\sin y$',
                    '$\\cos(x \\pm y) = \\cos x \\cos y \\mp \\sin x \\sin y$',
                    '$\\tan(x \\pm y) = \\frac{\\tan x \\pm \\tan y}{1 \\mp \\tan x \\tan y}$',
                    '$\\sin 2x = 2\\sin x \\cos x$',
                    '$\\cos 2x = \\cos^2 x - \\sin^2 x$'
                ]
            }
        ]
    },
    'chapter-4-complex-numbers-and-quadratic-equations': {
        sections: [
            {
                title: 'Complex Numbers',
                items: [
                    '$z = a + ib$, $|z| = \\sqrt{a^2+b^2}$',
                    'Polar: $z = r(\\cos\\theta + i\\sin\\theta)$',
                    'Roots: $x = \\frac{-b \\pm i\\sqrt{4ac-b^2}}{2a}$'
                ]
            }
        ]
    },
    'chapter-5-linear-inequalities': {
        sections: [
            {
                title: 'Rules',
                items: [
                    'Multiplying/Dividing by negative number reverses inequality sign.'
                ]
            }
        ]
    },
    'chapter-6-permutations-and-combinations': {
        sections: [
            {
                title: 'Formulas',
                items: [
                    '$^nP_r = \\frac{n!}{(n-r)!}$',
                    '$^nC_r = \\frac{n!}{r!(n-r)!}$',
                    '$^nC_r + ^nC_{r-1} = ^{n+1}C_r$'
                ]
            }
        ]
    },
    'chapter-7-binomial-theorem': {
        sections: [
            {
                title: 'Expansion',
                items: [
                    '$(a+b)^n = \\sum_{k=0}^n {^nC_k} a^{n-k} b^k$',
                    '$T_{r+1} = {^nC_r} a^{n-r} b^r$'
                ]
            }
        ]
    },
    'chapter-8-sequences-and-series': {
        sections: [
            {
                title: 'AP & GP',
                items: [
                    'AP Sum: $S_n = \\frac{n}{2}[2a + (n-1)d]$',
                    'GP Sum: $S_n = \\frac{a(r^n-1)}{r-1}$',
                    '$\\sum n = \\frac{n(n+1)}{2}$',
                    '$\\sum n^2 = \\frac{n(n+1)(2n+1)}{6}$'
                ]
            }
        ]
    },
    'chapter-9-straight-lines': {
        sections: [
            {
                title: 'Equations',
                items: [
                    '$y-y_1 = m(x-x_1)$',
                    '$y = mx + c$',
                    'Distance: $d = \\frac{|Ax_1+By_1+C|}{\\sqrt{A^2+B^2}}$'
                ]
            }
        ]
    },
    'chapter-10-conic-sections': {
        sections: [
            {
                title: 'Standard Equations',
                items: [
                    'Circle: $(x-h)^2 + (y-k)^2 = r^2$',
                    'Parabola: $y^2 = 4ax$',
                    'Ellipse: $\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1$',
                    'Hyperbola: $\\frac{x^2}{a^2} - \\frac{y^2}{b^2} = 1$'
                ]
            }
        ]
    },
    'chapter-11-introduction-to-three-dimensional-geometry': {
        sections: [
            {
                title: 'Formulas',
                items: [
                    'Distance: $\\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2}$',
                    'Section: $(\\frac{m_1x_2+m_2x_1}{m_1+m_2}, \\dots)$'
                ]
            }
        ]
    },
    'chapter-12-limits-and-derivatives': {
        sections: [
            {
                title: 'Limits',
                items: [
                    '$\\lim_{x \\to 0} \\frac{\\sin x}{x} = 1$',
                    '$\\lim_{x \\to a} \\frac{x^n-a^n}{x-a} = na^{n-1}$'
                ]
            },
            {
                title: 'Derivatives',
                items: [
                    '$\\frac{d}{dx}(x^n) = nx^{n-1}$',
                    'Product Rule: $uv\' + vu\'$',
                    'Quotient Rule: $\\frac{vu\' - uv\'}{v^2}$'
                ]
            }
        ]
    },
    'chapter-13-statistics-c11': {
        sections: [
            {
                title: 'Dispersion',
                items: [
                    'Mean Deviation: $\\frac{\\sum |x_i - \\bar{x}|}{n}$',
                    'Variance ($\\sigma^2$): $\\frac{\\sum (x_i - \\bar{x})^2}{n}$',
                    'Standard Deviation: $\\sigma = \\sqrt{\\text{Variance}}$'
                ]
            }
        ]
    },
    'chapter-14-probability-c11': {
        sections: [
            {
                title: 'Axioms',
                items: [
                    '$P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$',
                    '$P(\\text{not } A) = 1 - P(A)$'
                ]
            }
        ]
    }
 };

// --- Formula Sheet Modal ---
const initFormulaSheet = () => {
    // Inject CSS for Formula Modal if not present
    if (!document.getElementById('formula-sheet-styles')) {
        const style = document.createElement('style');
        style.id = 'formula-sheet-styles';
        style.textContent = `
            .formula-modal-overlay {
                position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                background: rgba(0,0,0,0.6); z-index: 10001;
                display: none; justify-content: center; align-items: center;
                backdrop-filter: blur(5px);
            }
            .formula-modal-overlay.active { display: flex; animation: fadeIn 0.3s; }
            .formula-modal {
                background: var(--soft1, #fff); width: 90%; max-width: 600px;
                max-height: 85vh; border-radius: 16px; overflow: hidden;
                box-shadow: 0 20px 50px rgba(0,0,0,0.3); display: flex; flex-direction: column;
                border: 1px solid var(--glass-border, rgba(255,255,255,0.1));
            }
            .fm-header {
                padding: 15px 20px; border-bottom: 1px solid rgba(0,0,0,0.1);
                display: flex; justify-content: space-between; align-items: center;
                background: var(--glass-bg);
            }
            .fm-header h2 { margin: 0; font-size: 1.2rem; color: var(--primary); }
            .fm-close { background: none; border: none; font-size: 1.2rem; cursor: pointer; color: var(--text-main); }
            .fm-body { padding: 20px; overflow-y: auto; }
            .fm-section { margin-bottom: 20px; }
            .fm-section h3 { font-size: 1rem; color: var(--secondary); margin-bottom: 10px; border-left: 3px solid var(--secondary); padding-left: 10px; }
            .formula-grid { display: grid; gap: 10px; }
            .formula-item { background: rgba(0,0,0,0.03); padding: 10px; border-radius: 8px; font-size: 0.95rem; }
            .formula-btn {
                background: var(--soft1, #fff); color: var(--text-main, #333);
                border: none; width: 45px; height: 45px; border-radius: 50%;
                display: flex; align-items: center; justify-content: center;
                cursor: pointer; box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                transition: transform 0.2s; font-size: 1.1rem; margin-right: 10px;
            }
            .formula-btn:hover { transform: translateY(-2px); color: var(--primary); }
            body.dark-mode .formula-btn { background: #2a2a2a; color: #fff; }
            @media (max-width: 640px) {
                .formula-modal { width: 95%; max-height: 80vh; }
                .fm-header { padding: 12px 15px; }
                .fm-body { padding: 15px; }
                .formula-item { font-size: 0.9rem; }
            }
        `;
        document.head.appendChild(style);
    }

    // Determine current chapter content
    const path = window.location.pathname.toLowerCase();
    let activeData = null;

    for (const key in formulaData) {
        const lowerKey = key.toLowerCase();
        
        // Special handling for Class 10 Polynomials collision
        if (key === 'chapter-2-polynomials-c10') {
            if (path.includes('class-10') && path.includes('chapter-2-polynomials')) {
                activeData = formulaData[key];
                break;
            }
            continue;
        }
        // Avoid Class 9 Polynomials showing up for Class 10
        if (key === 'chapter-2-polynomials' && path.includes('class-10')) {
            continue;
        }

        // Special handling for Class 11 Statistics & Probability
        if (key === 'chapter-13-statistics-c11' || key === 'chapter-14-probability-c11') {
            const shortKey = key.replace('-c11', '');
            if (path.includes('class-11') && path.includes(shortKey)) {
                activeData = formulaData[key];
                break;
            }
            continue;
        }

        // Avoid Class 10/9 data showing up for Class 11
        if (path.includes('class-11') && (key === 'chapter-13-statistics' || key === 'chapter-14-probability')) {
            continue;
        }

        if (path.includes(lowerKey)) {
            activeData = formulaData[key];
            break;
        }
    }

    // Fallback for Class 10 if strict key match failed
    if (!activeData && path.includes('class-10')) {
        // Check double digits first to avoid partial matches (e.g., 'chapter-1-' matches 'chapter-10-')
        if (path.includes('chapter-10-')) activeData = formulaData['chapter-10-circles'];
        else if (path.includes('chapter-11-')) activeData = formulaData['chapter-11-areas-related-to-circles'];
        else if (path.includes('chapter-12-')) activeData = formulaData['chapter-12-surface-areas-and-volumes'];
        else if (path.includes('chapter-13-')) activeData = formulaData['chapter-13-statistics'];
        else if (path.includes('chapter-14-')) activeData = formulaData['chapter-14-probability'];
        else if (path.includes('chapter-1-')) activeData = formulaData['chapter-1-real-numbers'];
        else if (path.includes('chapter-2-')) activeData = formulaData['chapter-2-polynomials-c10'];
        else if (path.includes('chapter-3-')) activeData = formulaData['chapter-3-pair-of-linear-equations-in-two-variables'];
        else if (path.includes('chapter-4-')) activeData = formulaData['chapter-4-quadratic-equations'];
        else if (path.includes('chapter-5-')) activeData = formulaData['chapter-5-arithmetic-progressions'];
        else if (path.includes('chapter-6-')) activeData = formulaData['chapter-6-triangles'];
        else if (path.includes('chapter-7-')) activeData = formulaData['chapter-7-coordinate-geometry'];
        else if (path.includes('chapter-8-')) activeData = formulaData['chapter-8-introduction-to-trigonometry'];
        else if (path.includes('chapter-9-')) activeData = formulaData['chapter-9-applications-of-trigonometry'];
    }

    if (!activeData) return;

    // 1. Find or Create Button
    let btn = document.querySelector('.formula-btn');
    if (!btn) {
        btn = document.createElement('button');
        btn.className = 'formula-btn';
        btn.innerHTML = '<i class="fas fa-calculator"></i>';
        btn.title = 'Open Formula Sheet';
        btn.setAttribute('aria-label', 'Open Formula Sheet');

        const floatingControls = document.querySelector('.floating-controls');
        if (floatingControls) {
            const themeBtn = floatingControls.querySelector('.theme-toggle-btn');
            if (themeBtn) floatingControls.insertBefore(btn, themeBtn);
            else floatingControls.appendChild(btn);
        } else {
            document.body.appendChild(btn);
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