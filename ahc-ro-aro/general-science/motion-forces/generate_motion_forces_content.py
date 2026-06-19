# -*- coding: utf-8 -*-
import json
import os
import sys

# Ensure UTF-8 output encoding
sys.stdout.reconfigure(encoding='utf-8')

TOPIC = "motion-forces"
TOPIC_DISPLAY = "Motion & Forces"
TOPIC_DISPLAY_HI = "गति और बल"

BASE_DIR = rf"c:\Users\sande\Documents\GitHub\sjmaths-website\ahc-ro-aro\general-science\{TOPIC}"
HI_DIR = os.path.join(BASE_DIR, "hi")
os.makedirs(HI_DIR, exist_ok=True)

# ----------------- ENGLISH DATA DEFINITIONS -----------------
breadcrumbs_en = {
    "parent": "General Science",
    "parentUrl": "../",
    "current": "Motion & Forces"
}

hero_en = {
    "title": "Motion & Forces",
    "description": "Master the laws of motion, types of forces—gravitational, frictional, centripetal, centrifugal—Newton's three laws, momentum, inertia, impulse, and conservation principles."
}

labels_en = {
    "clickToExpand": "Click to expand details",
    "mockIntro": {
        "title": "Interactive Motion & Forces Mock Test",
        "description": "Assess your understanding of motion, forces, Newton's laws, friction, gravity, momentum, and related concepts. This timed mock test consists of 15 questions.",
        "startBtn": "Start Mock Test"
    },
    "mockPlay": {
        "prevBtn": "Previous Question",
        "nextBtn": "Next Question",
        "submitBtn": "Submit Test"
    }
}

timeline_en = {
    "title": "Historical Development of Classical Mechanics",
    "description": "Key milestones in the understanding of motion and forces.",
    "cards": [
        {
            "period": "Aristotelian Physics",
            "date": "c. 330 BCE",
            "details": "Aristotle proposed that heavier objects fall faster, and that a force is required to maintain motion (a view later disproven by Galileo and Newton)."
        },
        {
            "period": "Galileo's Experiments",
            "date": "c. 1590-1600",
            "details": "Galileo Galilei conducted experiments with inclined planes and free-falling objects, establishing the concept of inertia and uniform acceleration."
        },
        {
            "period": "Newton's Principia Mathematica",
            "date": "1687",
            "details": "Sir Isaac Newton published 'Philosophiæ Naturalis Principia Mathematica', laying down the three laws of motion and the law of universal gravitation."
        },
        {
            "period": "Einstein's Theory of Relativity",
            "date": "1905-1915",
            "details": "Albert Einstein's special and general theories of relativity redefined concepts of motion, gravity, and space-time at high velocities and strong gravitational fields."
        }
    ]
}

mnemonics_en = {
    "title": "Motion & Forces Mnemonics",
    "description": "Quick memory triggers to recall key concepts, laws, and formulas for competitive exams.",
    "items": [
        {
            "title": "Mnemonic 1: Newton's Three Laws (Number Trick)",
            "phrase": "\"1st Law — Inertia (Laziness), 2nd Law — F=ma (Formula), 3rd Law — Action-Reaction (Pair)\"",
            "decryption": "Remember them by the number sequence:<br>• **1st Law (Law of Inertia)**: Body at rest stays at rest; body in motion stays in motion — <strong>I</strong> for Inertia.<br>• **2nd Law**: F = ma — <strong>F</strong> for Force formula.<br>• **3rd Law**: Every action has an equal and opposite reaction — <strong>P</strong> for Pair of forces."
        },
        {
            "title": "Mnemonic 2: Types of Friction Order",
            "phrase": "\"S-K-R (Static > Kinetic > Rolling)\"",
            "decryption": "Friction types from highest to lowest:<br>• <strong>S</strong> — Static Friction (highest, required to start motion)<br>• <strong>K</strong> — Kinetic/Sliding Friction (moderate, opposes motion)<br>• <strong>R</strong> — Rolling Friction (lowest, wheels reduce it)"
        },
        {
            "title": "Mnemonic 3: Factors Affecting Friction",
            "phrase": "\"N-R-I (Nature, Roughness, Incline)\"",
            "decryption": "Key factors:<br>• <strong>N</strong> — Nature of surfaces in contact<br>• <strong>R</strong> — Roughness of the surfaces<br>• <strong>I</strong> — Independent of area of contact (trick: 'I' reminds you it's Independent of area)"
        }
    ]
}

flashcards_en = {
    "title": "Active Recall Flashcards",
    "description": "Hover or click to reveal the answers. Revisit these cards to build instant recall.",
    "items": [
        {
            "question": "What is Newton's first law of motion also known as?",
            "answer": "The **Law of Inertia** — a body at rest remains at rest, and a body in motion continues in uniform motion unless acted upon by an external unbalanced force.",
            "icon": "fa-bed"
        },
        {
            "question": "State Newton's Second Law of Motion mathematically.",
            "answer": "**F = ma** (Force = Mass × Acceleration). The rate of change of momentum of a body is directly proportional to the applied force and takes place in the direction of the force.",
            "icon": "fa-square-root-variable"
        },
        {
            "question": "What is the SI unit of momentum?",
            "answer": "**kg·m/s** (Kilogram meter per second). Momentum = mass × velocity.",
            "icon": "fa-arrow-right"
        },
        {
            "question": "What is the difference between mass and weight?",
            "answer": "**Mass** is the amount of matter (scalar, constant everywhere, measured in kg). **Weight** is the gravitational force on an object (vector, W = mg, varies with gravity).",
            "icon": "fa-scale-balanced"
        }
    ]
}

traps_en = {
    "title": "Common Exam Traps to Avoid",
    "items": [
        "<strong>Trap 1:</strong> Confusing mass with weight. Mass is constant regardless of location; weight changes with gravitational field strength (e.g., weight on the Moon is 1/6th that on Earth, but mass remains the same).",
        "<strong>Trap 2:</strong> Believing that a body in uniform circular motion has no acceleration. In uniform circular motion, the speed is constant, but the direction keeps changing — hence there is <strong>centripetal acceleration</strong> directed toward the center.",
        "<strong>Trap 3:</strong> Thinking that zero net force means the body must be at rest. According to Newton's first law, zero net force means the body is either at rest OR in uniform motion (constant velocity).",
        "<strong>Trap 4:</strong> Confusing momentum with kinetic energy. Momentum (p = mv) is a vector; kinetic energy (KE = ½mv²) is a scalar. A body can have kinetic energy but zero net momentum if two equal masses move in opposite directions."
    ]
}

deep_dive_en = [
    {
        "title": "1. Types of Motion & Frame of Reference",
        "content": """<p>Motion is a change in position of an object with respect to time and a reference point. Key types include:</p>

        <!-- SVG Mindmap: Types of Motion -->
        <svg viewBox="0 0 800 380" class="responsive-svg-diagram" style="margin:1rem 0; border-radius:10px; background:var(--bg-card,#ffffff); padding:10px;">
          <style>
            .mm-title{font-family:'Outfit',sans-serif;font-weight:bold;fill:var(--text-dark,#2c3e50);font-size:16px;}
            .mm-center{fill:var(--bg-card,#ffffff);stroke:var(--primary,#8e44ad);stroke-width:2.5px;}
            .mm-node{fill:var(--bg-card,#ffffff);stroke:var(--primary,#8e44ad);stroke-width:1.8px;}
            .mm-node-hl{fill:rgba(142,68,173,0.06);stroke:#9b59b6;stroke-width:2px;}
            .mm-text{font-family:'Inter',sans-serif;font-size:11px;fill:var(--text-dark,#2c3e50);font-weight:600;}
            .mm-text-sub{font-family:'Inter',sans-serif;font-size:10px;fill:#555;}
            .mm-line{stroke:#8e44ad;stroke-width:1.5px;fill:none;}
            body.dark-mode .mm-center{fill:#1e1e24;stroke:var(--primary,#c084fc);}
            body.dark-mode .mm-node{fill:#1e1e24;stroke:var(--primary,#c084fc);}
            body.dark-mode .mm-node-hl{fill:rgba(168,85,247,0.08);stroke:var(--primary,#c084fc);}
            body.dark-mode .mm-text{fill:#f1f5f9;}
            body.dark-mode .mm-text-sub{fill:#bbb;}
            body.dark-mode .mm-title{fill:#f1f5f9;}
          </style>
          <text x="400" y="28" class="mm-title" text-anchor="middle">Classification of Motion</text>
          <!-- Center -->
          <rect x="300" y="42" width="200" height="34" class="mm-center" rx="17" ry="17" />
          <text x="400" y="64" class="mm-text" text-anchor="middle" font-size="13">MOTION</text>
          <!-- Level 1 branches -->
          <line x1="400" y1="76" x2="150" y2="115" class="mm-line" />
          <line x1="400" y1="76" x2="400" y2="115" class="mm-line" />
          <line x1="400" y1="76" x2="650" y2="115" class="mm-line" />
          <!-- Translational -->
          <rect x="50" y="115" width="200" height="30" class="mm-node" rx="6" />
          <text x="150" y="135" class="mm-text" text-anchor="middle">Translational</text>
          <line x1="150" y1="145" x2="80" y2="175" class="mm-line" />
          <line x1="150" y1="145" x2="200" y2="175" class="mm-line" />
          <rect x="25" y="175" width="110" height="24" class="mm-node-hl" rx="4" />
          <text x="80" y="192" class="mm-text-sub" text-anchor="middle">Rectilinear</text>
          <rect x="145" y="175" width="100" height="24" class="mm-node-hl" rx="4" />
          <text x="195" y="192" class="mm-text-sub" text-anchor="middle">Curvilinear</text>
          <!-- Rotational -->
          <rect x="310" y="115" width="180" height="30" class="mm-node" rx="6" />
          <text x="400" y="135" class="mm-text" text-anchor="middle">Rotational</text>
          <line x1="355" y1="145" x2="340" y2="175" class="mm-line" />
          <line x1="445" y1="145" x2="460" y2="175" class="mm-line" />
          <rect x="285" y="175" width="110" height="24" class="mm-node-hl" rx="4" />
          <text x="340" y="192" class="mm-text-sub" text-anchor="middle">Rigid body rotation</text>
          <rect x="405" y="175" width="110" height="24" class="mm-node-hl" rx="4" />
          <text x="460" y="192" class="mm-text-sub" text-anchor="middle">Circular motion</text>
          <!-- Periodic/Oscillatory -->
          <rect x="560" y="115" width="180" height="30" class="mm-node" rx="6" />
          <text x="650" y="135" class="mm-text" text-anchor="middle">Periodic / Oscillatory</text>
          <line x1="590" y1="145" x2="570" y2="175" class="mm-line" />
          <line x1="650" y1="145" x2="650" y2="175" class="mm-line" />
          <line x1="710" y1="145" x2="730" y2="175" class="mm-line" />
          <rect x="520" y="175" width="100" height="24" class="mm-node-hl" rx="4" />
          <text x="570" y="192" class="mm-text-sub" text-anchor="middle">Simple Harmonic</text>
          <rect x="600" y="175" width="100" height="24" class="mm-node-hl" rx="4" />
          <text x="650" y="192" class="mm-text-sub" text-anchor="middle">Pendulum</text>
          <rect x="685" y="175" width="95" height="24" class="mm-node-hl" rx="4" />
          <text x="732" y="192" class="mm-text-sub" text-anchor="middle">Wave motion</text>
          <!-- Examples row -->
          <text x="400" y="235" class="mm-text-sub" text-anchor="middle" fill="#8e44ad" font-weight="600">Examples:</text>
          <text x="400" y="255" class="mm-text-sub" text-anchor="middle">Car on road (translational) | Earth spinning (rotational)</text>
          <text x="400" y="275" class="mm-text-sub" text-anchor="middle">Pendulum (oscillatory) | Satellite (circular)</text>
          <!-- Bottom note -->
          <text x="400" y="310" class="mm-text-sub" text-anchor="middle" font-style="italic">Frame of Reference: Inertial (non-accelerating) vs Non-inertial (requires pseudo-forces)</text>
          <text x="400" y="330" class="mm-text-sub" text-anchor="middle" font-style="italic">Example: A car accelerating is non-inertial; a car at constant speed is inertial.</text>
        </svg>

        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>Type of Motion</th>
                <th>Description</th>
                <th>Example</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Translational</strong></td>
                <td>All parts move the same distance in same direction</td>
                <td>A car moving on a straight road</td>
              </tr>
              <tr>
                <td><strong>Rotational</strong></td>
                <td>Body moves around a fixed axis</td>
                <td>Earth's rotation, spinning top</td>
              </tr>
              <tr>
                <td><strong>Oscillatory</strong></td>
                <td>To-and-fro motion about a mean position</td>
                <td>Simple pendulum, vibrating string</td>
              </tr>
              <tr>
                <td><strong>Periodic</strong></td>
                <td>Motion that repeats itself at regular intervals</td>
                <td>Motion of planets around the Sun</td>
              </tr>
              <tr>
                <td><strong>Uniform Circular</strong></td>
                <td>Motion along a circular path with constant speed</td>
                <td>Satellite orbiting Earth</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p><strong>Frame of Reference</strong>: A coordinate system relative to which motion is measured. Inertial frames are non-accelerating (Newton's laws hold directly); non-inertial frames require pseudo-forces.</p>"""
    },
    {
        "title": "2. Scalars & Vectors in Motion",
        "content": """<p>Understanding the difference between scalars and vectors is foundational for motion:</p>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>Quantity</th>
                <th>Type</th>
                <th>SI Unit</th>
                <th>Formula</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Distance</strong></td>
                <td>Scalar</td>
                <td>m</td>
                <td>Total path length traveled</td>
              </tr>
              <tr>
                <td><strong>Displacement</strong></td>
                <td>Vector</td>
                <td>m</td>
                <td>Shortest path from initial to final position</td>
              </tr>
              <tr>
                <td><strong>Speed</strong></td>
                <td>Scalar</td>
                <td>m/s</td>
                <td>Distance / Time</td>
              </tr>
              <tr>
                <td><strong>Velocity</strong></td>
                <td>Vector</td>
                <td>m/s</td>
                <td>Displacement / Time</td>
              </tr>
              <tr>
                <td><strong>Acceleration</strong></td>
                <td>Vector</td>
                <td>m/s²</td>
                <td>(v - u) / t</td>
              </tr>
              <tr>
                <td><strong>Momentum</strong></td>
                <td>Vector</td>
                <td>kg·m/s</td>
                <td>p = m × v</td>
              </tr>
              <tr>
                <td><strong>Force</strong></td>
                <td>Vector</td>
                <td>N (Newton)</td>
                <td>F = ma</td>
              </tr>
            </tbody>
          </table>
        </div>
        
        <p><strong>Equations of Motion (Constant Acceleration):</strong></p>
        <ul>
          <li><strong>v = u + at</strong> (Relation between velocities and time)</li>
          <li><strong>s = ut + ½at²</strong> (Relation between displacement and time)</li>
          <li><strong>v² = u² + 2as</strong> (Relation without time)</li>
          <li><strong>s<sub>n</sub> = u + a(2n - 1)/2</strong> (Distance traveled in n<sup>th</sup> second)</li>
        </ul>
        <p><em>Where: u = initial velocity, v = final velocity, a = acceleration, t = time, s = displacement</em></p>"""
    },
    {
        "title": "3. Newton's Laws of Motion",
        "content": """<p>Newton's three laws form the foundation of classical mechanics:</p>

        <!-- SVG Concept Map: Newton's Laws -->
        <svg viewBox="0 0 800 260" class="responsive-svg-diagram" style="margin:1rem 0; border-radius:10px; background:var(--bg-card,#ffffff); padding:10px;">
          <style>
            .nl-center{fill:var(--bg-card,#ffffff);stroke:#e74c3c;stroke-width:2.5px;}
            .nl-node{fill:var(--bg-card,#ffffff);stroke:#8e44ad;stroke-width:1.8px;}
            .nl-text{font-family:'Inter',sans-serif;font-size:11px;fill:var(--text-dark,#2c3e50);font-weight:600;}
            .nl-text-sub{font-family:'Inter',sans-serif;font-size:10px;fill:#555;}
            .nl-line{stroke:#8e44ad;stroke-width:1.5px;fill:none;}
            body.dark-mode .nl-center{fill:#1e1e24;stroke:#e74c3c;}
            body.dark-mode .nl-node{fill:#1e1e24;stroke:var(--primary,#c084fc);}
            body.dark-mode .nl-text{fill:#f1f5f9;}
            body.dark-mode .nl-text-sub{fill:#bbb;}
          </style>
          <text x="400" y="25" class="nl-text" text-anchor="middle" font-size="14">Newton's Three Laws of Motion</text>
          <!-- Center -->
          <rect x="300" y="40" width="200" height="36" class="nl-center" rx="18" ry="18" />
          <text x="400" y="63" class="nl-text" text-anchor="middle" font-size="13" fill="#e74c3c">NEWTON'S LAWS</text>
          <!-- Branches -->
          <line x1="400" y1="76" x2="120" y2="120" class="nl-line" />
          <line x1="400" y1="76" x2="400" y2="120" class="nl-line" />
          <line x1="400" y1="76" x2="680" y2="120" class="nl-line" />
          <!-- 1st Law -->
          <rect x="10" y="120" width="220" height="36" class="nl-node" rx="6" />
          <text x="120" y="142" class="nl-text" text-anchor="middle">1st Law — Law of Inertia</text>
          <line x1="120" y1="156" x2="120" y2="185" class="nl-line" />
          <rect x="10" y="185" width="220" height="50" class="nl-node" rx="4" />
          <text x="120" y="200" class="nl-text-sub" text-anchor="middle">Body at rest → stays at rest</text>
          <text x="120" y="218" class="nl-text-sub" text-anchor="middle">Body in motion → continues uniformly</text>
          <text x="120" y="235" class="nl-text-sub" text-anchor="middle" font-style="italic">Unless unbalanced external force acts</text>
          <!-- 2nd Law -->
          <rect x="290" y="120" width="220" height="36" class="nl-node" rx="6" />
          <text x="400" y="142" class="nl-text" text-anchor="middle">2nd Law — F = ma</text>
          <line x1="400" y1="156" x2="400" y2="185" class="nl-line" />
          <rect x="290" y="185" width="220" height="50" class="nl-node" rx="4" />
          <text x="400" y="200" class="nl-text-sub" text-anchor="middle">Force = Mass × Acceleration</text>
          <text x="400" y="218" class="nl-text-sub" text-anchor="middle">Rate of change of momentum = Force</text>
          <text x="400" y="235" class="nl-text-sub" text-anchor="middle" font-style="italic">1 N = 1 kg·m/s²</text>
          <!-- 3rd Law -->
          <rect x="570" y="120" width="220" height="36" class="nl-node" rx="6" />
          <text x="680" y="142" class="nl-text" text-anchor="middle">3rd Law — Action-Reaction</text>
          <line x1="680" y1="156" x2="680" y2="185" class="nl-line" />
          <rect x="570" y="185" width="220" height="50" class="nl-node" rx="4" />
          <text x="680" y="200" class="nl-text-sub" text-anchor="middle">For every action → Equal & opposite reaction</text>
          <text x="680" y="218" class="nl-text-sub" text-anchor="middle">Forces always occur in pairs</text>
          <text x="680" y="235" class="nl-text-sub" text-anchor="middle" font-style="italic">e.g., Gun recoil, rocket propulsion</text>
        </svg>

        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>Law</th>
                <th>Statement</th>
                <th>Key Concept</th>
                <th>Example</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>First Law</strong></td>
                <td>An object at rest stays at rest; an object in motion stays in motion with constant velocity, unless acted upon by an unbalanced external force.</td>
                <td><strong>Inertia</strong> — resistance to change in state of motion</td>
                <td>A book on a table remains at rest until pushed.</td>
              </tr>
              <tr>
                <td><strong>Second Law</strong></td>
                <td>The rate of change of momentum of a body is directly proportional to the applied force and takes place in the direction of the force. (F = ma)</td>
                <td><strong>Quantifies force</strong> — 1 N = 1 kg·m/s²</td>
                <td>A tennis racket applies force to accelerate the ball.</td>
              </tr>
              <tr>
                <td><strong>Third Law</strong></td>
                <td>Every action has an equal and opposite reaction. (Forces always occur in pairs.)</td>
                <td><strong>Action-Reaction</strong> — forces on different bodies</td>
                <td>When you jump, you push the Earth down (action) and Earth pushes you up (reaction).</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p><strong>Impulse:</strong> Impulse = Force × Time = Change in momentum. It is a vector quantity (SI unit: N·s or kg·m/s). Cricketer pulling his hands back while catching a ball increases the time of impact, reducing the force experienced.</p>"""
    },
    {
        "title": "4. Types of Forces",
        "content": """<p>Forces are broadly classified into <strong>Contact Forces</strong> and <strong>Non-Contact Forces</strong>:</p>

        <!-- SVG Mindmap: Forces Classification -->
        <svg viewBox="0 0 800 280" class="responsive-svg-diagram" style="margin:1rem 0; border-radius:10px; background:var(--bg-card,#ffffff); padding:10px;">
          <style>
            .fc-title{font-family:'Outfit',sans-serif;font-weight:bold;fill:var(--text-dark,#2c3e50);font-size:15px;}
            .fc-center{fill:var(--bg-card,#ffffff);stroke:#2ecc71;stroke-width:2.5px;}
            .fc-node{fill:var(--bg-card,#ffffff);stroke:var(--primary,#8e44ad);stroke-width:1.8px;}
            .fc-node-hl{fill:rgba(142,68,173,0.06);stroke:#9b59b6;stroke-width:1.5px;}
            .fc-text{font-family:'Inter',sans-serif;font-size:10.5px;fill:var(--text-dark,#2c3e50);font-weight:600;}
            .fc-text-sub{font-family:'Inter',sans-serif;font-size:9.5px;fill:#555;}
            .fc-line{stroke:#8e44ad;stroke-width:1.5px;fill:none;}
            body.dark-mode .fc-center{fill:#1e1e24;stroke:#2ecc71;}
            body.dark-mode .fc-node{fill:#1e1e24;stroke:var(--primary,#c084fc);}
            body.dark-mode .fc-node-hl{fill:rgba(168,85,247,0.06);stroke:var(--primary,#c084fc);}
            body.dark-mode .fc-text{fill:#f1f5f9;}
            body.dark-mode .fc-text-sub{fill:#bbb;}
            body.dark-mode .fc-title{fill:#f1f5f9;}
          </style>
          <text x="400" y="22" class="fc-title" text-anchor="middle">Classification of Forces</text>
          <!-- Center -->
          <rect x="325" y="35" width="150" height="32" class="fc-center" rx="16" ry="16" />
          <text x="400" y="55" class="fc-text" text-anchor="middle" fill="#2ecc71" font-size="12">FORCES</text>
          <!-- Two main branches -->
          <line x1="400" y1="67" x2="150" y2="105" class="fc-line" />
          <line x1="400" y1="67" x2="650" y2="105" class="fc-line" />
          <!-- Contact Forces -->
          <rect x="40" y="105" width="220" height="32" class="fc-node" rx="6" />
          <text x="150" y="125" class="fc-text" text-anchor="middle">CONTACT FORCES</text>
          <!-- Contact sub-branches -->
          <line x1="100" y1="137" x2="100" y2="165" class="fc-line" />
          <line x1="150" y1="137" x2="150" y2="165" class="fc-line" />
          <line x1="200" y1="137" x2="200" y2="165" class="fc-line" />
          <rect x="30" y="165" width="140" height="24" class="fc-node-hl" rx="4" />
          <text x="100" y="181" class="fc-text-sub" text-anchor="middle">Friction (F=μN)</text>
          <rect x="80" y="165" width="140" height="24" class="fc-node-hl" rx="4" />
          <text x="150" y="181" class="fc-text-sub" text-anchor="middle">Normal Reaction</text>
          <rect x="135" y="165" width="130" height="24" class="fc-node-hl" rx="4" />
          <text x="200" y="181" class="fc-text-sub" text-anchor="middle">Tension & Spring</text>
          <!-- Non-Contact Forces -->
          <rect x="540" y="105" width="220" height="32" class="fc-node" rx="6" />
          <text x="650" y="125" class="fc-text" text-anchor="middle">NON-CONTACT FORCES</text>
          <!-- Non-contact sub-branches -->
          <line x1="590" y1="137" x2="590" y2="165" class="fc-line" />
          <line x1="650" y1="137" x2="650" y2="165" class="fc-line" />
          <line x1="710" y1="137" x2="710" y2="165" class="fc-line" />
          <rect x="530" y="165" width="120" height="24" class="fc-node-hl" rx="4" />
          <text x="590" y="181" class="fc-text-sub" text-anchor="middle">Gravitational</text>
          <rect x="595" y="165" width="110" height="24" class="fc-node-hl" rx="4" />
          <text x="650" y="181" class="fc-text-sub" text-anchor="middle">Electromagnetic</text>
          <rect x="660" y="165" width="110" height="24" class="fc-node-hl" rx="4" />
          <text x="715" y="181" class="fc-text-sub" text-anchor="middle">Nuclear</text>
          <!-- Circular motion forces row -->
          <text x="400" y="225" class="fc-text" text-anchor="middle" fill="#8e44ad">Circular Motion Forces:</text>
          <rect x="200" y="240" width="180" height="24" class="fc-node-hl" rx="4" />
          <text x="290" y="256" class="fc-text-sub" text-anchor="middle">Centripetal (real, towards center)</text>
          <rect x="420" y="240" width="180" height="24" class="fc-node-hl" rx="4" />
          <text x="510" y="256" class="fc-text-sub" text-anchor="middle">Centrifugal (pseudo, outward)</text>
        </svg>

        <h4 style="margin-top: 1rem;">Contact Forces</h4>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>Force</th>
                <th>Description</th>
                <th>Key Fact for Exams</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Friction</strong></td>
                <td>Opposes relative motion between surfaces in contact</td>
                <td>F = μN (μ = coefficient of friction, N = normal reaction). Static > Kinetic > Rolling friction.</td>
              </tr>
              <tr>
                <td><strong>Normal Reaction</strong></td>
                <td>Perpendicular force exerted by a surface on an object</td>
                <td>Always acts perpendicular to the surface of contact.</td>
              </tr>
              <tr>
                <td><strong>Tension</strong></td>
                <td>Force transmitted through a string/rope when pulled</td>
                <td>Tension is the same throughout an ideal massless, inextensible string.</td>
              </tr>
              <tr>
                <td><strong>Spring Force</strong></td>
                <td>Restoring force proportional to displacement (Hooke's Law)</td>
                <td>F = -kx (k = spring constant, x = displacement from natural length)</td>
              </tr>
            </tbody>
          </table>
        </div>
        
        <h4 style="margin-top: 1.5rem;">Non-Contact Forces</h4>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>Force</th>
                <th>Description</th>
                <th>Key Fact for Exams</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Gravitational Force</strong></td>
                <td>Force of attraction between any two masses</td>
                <td>F = Gm₁m₂/r². g = 9.8 m/s² at Earth's surface. g decreases with altitude and depth.</td>
              </tr>
              <tr>
                <td><strong>Electromagnetic Force</strong></td>
                <td>Force between charged particles (electric & magnetic)</td>
                <td>Much stronger than gravity (~10³⁶ times). Governs atomic and molecular interactions.</td>
              </tr>
              <tr>
                <td><strong>Nuclear Forces</strong></td>
                <td>Strong and weak nuclear forces binding nucleus</td>
                <td>Strongest force in nature. Acts over extremely short range (~10⁻¹⁵ m).</td>
              </tr>
              <tr>
                <td><strong>Centripetal Force</strong></td>
                <td>Force required to keep a body moving in a circular path</td>
                <td>F<sub>c</sub> = mv²/r. Directed toward the center. Without it, the body would fly off tangentially.</td>
              </tr>
              <tr>
                <td><strong>Centrifugal Force</strong></td>
                <td>Pseudo-force felt in a rotating reference frame</td>
                <td>Directed outward, away from the center. It is a fictitious force experienced in non-inertial frames.</td>
              </tr>
            </tbody>
          </table>
        </div>"""
    },
    {
        "title": "5. Friction, Gravity & Conservation Laws",
        "content": """<p><strong>Friction</strong> is a resistive force that opposes relative motion between surfaces in contact. It is of three types:</p>
        <ul>
          <li><strong>Static Friction (f<sub>s</sub>)</strong>: Opposes the initiation of motion. Maximum static friction f<sub>s</sub>(max) = μ<sub>s</sub>N.</li>
          <li><strong>Kinetic/Sliding Friction (f<sub>k</sub>)</strong>: Opposes ongoing motion. f<sub>k</sub> = μ<sub>k</sub>N. Usually μ<sub>k</sub> < μ<sub>s</sub>.</li>
          <li><strong>Rolling Friction (f<sub>r</sub>)</strong>: Opposes rolling motion. Much smaller than static and kinetic friction. This is why wheels were invented.</li>
        </ul>
        <p><strong>Methods to reduce friction:</strong> Lubrication (oil/grease), polishing surfaces, using ball bearings, streamlining shapes, and using wheels/rollers.</p>
        
        <p><strong>Gravity (Universal Gravitation):</strong></p>
        <ul>
          <li>Every particle attracts every other particle with a force proportional to the product of their masses and inversely proportional to the square of the distance between them.</li>
          <li><strong>Acceleration due to gravity (g)</strong>: At Earth's surface, g = GM/R² ≈ 9.8 m/s².</li>
          <li><strong>Variation of g:</strong> 
            <ul>
              <li>With altitude: g' = g(1 - 2h/R) for h << R.</li>
              <li>With depth: g' = g(1 - d/R) inside Earth.</li>
              <li>Due to rotation of Earth: g is maximum at poles, minimum at the equator.</li>
            </ul>
          </li>
          <li><strong>Escape Velocity (v<sub>e</sub>)</strong>: Minimum velocity required to escape Earth's gravitational pull. v<sub>e</sub> = √(2GM/R) = √(2gR) ≈ 11.2 km/s.</li>
        </ul>
        
        <p><strong>Conservation Laws:</strong></p>
        <ul>
          <li><strong>Conservation of Linear Momentum</strong>: In the absence of external forces, the total momentum of an isolated system remains constant. (Momentum before = Momentum after)</li>
          <li><strong>Conservation of Energy</strong>: Energy can neither be created nor destroyed — it can only be converted from one form to another.</li>
          <li><strong>Conservation of Angular Momentum</strong>: In the absence of external torque, the angular momentum of a system remains constant. (Used to explain why a spinning ice skater spins faster by pulling arms in.)</li>
        </ul>"""
    }
]

# ----------------- HINDI DATA DEFINITIONS -----------------
breadcrumbs_hi = {
    "parent": "सामान्य विज्ञान",
    "parentUrl": "../",
    "current": "गति और बल"
}

hero_hi = {
    "title": "गति और बल",
    "description": "गति के नियमों, विभिन्न प्रकार के बलों—गुरुत्वाकर्षण, घर्षण, अभिकेंद्रीय, अपकेंद्रीय—न्यूटन के तीन नियमों, संवेग, जड़त्व, आवेग और संरक्षण सिद्धांतों में महारत हासिल करें।"
}

labels_hi = {
    "clickToExpand": "विवरण देखने के लिए क्लिक करें",
    "mockIntro": {
        "title": "इंटरएक्टिव गति और बल मॉक टेस्ट",
        "description": "गति, बल, न्यूटन के नियम, घर्षण, गुरुत्वाकर्षण, संवेग और संबंधित अवधारणाओं की अपनी समझ का परीक्षण करें। इस समयबद्ध मॉक टेस्ट में 15 प्रश्न शामिल हैं।",
        "startBtn": "मॉक टेस्ट शुरू करें"
    },
    "mockPlay": {
        "prevBtn": "पिछला प्रश्न",
        "nextBtn": "अगला प्रश्न",
        "submitBtn": "टेस्ट सबमिट करें"
    }
}

timeline_hi = {
    "title": "शास्त्रीय यांत्रिकी का ऐतिहासिक विकास",
    "description": "गति और बलों की समझ में प्रमुख मील के पत्थर।",
    "cards": [
        {
            "period": "अरस्तू की भौतिकी",
            "date": "लगभग 330 ई.पू.",
            "details": "अरस्तू ने प्रस्तावित किया कि भारी वस्तुएं तेजी से गिरती हैं, और गति बनाए रखने के लिए बल आवश्यक है (यह दृष्टिकोण बाद में गैलीलियो और न्यूटन द्वारा ख़ारिज किया गया)।"
        },
        {
            "period": "गैलीलियो के प्रयोग",
            "date": "लगभग 1590-1600",
            "details": "गैलीलियो गैलीलाई ने आनत तल और मुक्त रूप से गिरती वस्तुओं के साथ प्रयोग किए, जड़त्व और एकसमान त्वरण की अवधारणा स्थापित की।"
        },
        {
            "period": "न्यूटन का प्रिंसिपिया",
            "date": "1687",
            "details": "सर आइजैक न्यूटन ने 'फिलोसोफी नेचुरलिस प्रिंसिपिया मैथेमेटिका' प्रकाशित किया, जिसमें गति के तीन नियम और सार्वभौमिक गुरुत्वाकर्षण का नियम दिए गए।"
        },
        {
            "period": "आइंस्टीन का सापेक्षता सिद्धांत",
            "date": "1905-1915",
            "details": "अल्बर्ट आइंस्टीन के विशेष और सामान्य सापेक्षता सिद्धांतों ने उच्च वेगों और प्रबल गुरुत्वीय क्षेत्रों पर गति, गुरुत्व और अंतरिक्ष-समय की अवधारणाओं को पुनर्परिभाषित किया।"
        }
    ]
}

mnemonics_hi = {
    "title": "गति और बल के स्मृति सूत्र",
    "description": "परीक्षा के लिए प्रमुख अवधारणाओं, नियमों और सूत्रों को याद रखने के त्वरित सूत्र।",
    "items": [
        {
            "title": "स्मृति सूत्र 1: न्यूटन के तीन नियम (संख्या ट्रिक)",
            "phrase": "\"पहला — जड़त्व, दूसरा — F=ma, तीसरा — क्रिया-प्रतिक्रिया\"",
            "decryption": "इन्हें संख्या क्रम से याद रखें:<br>• **पहला नियम (जड़त्व का नियम)**: स्थिर वस्तु स्थिर रहती है, गतिमान वस्तु गतिमान रहती है।<br>• **दूसरा नियम**: F = ma — बल का सूत्र।<br>• **तीसरा नियम**: प्रत्येक क्रिया के बराबर और विपरीत प्रतिक्रिया होती है।"
        },
        {
            "title": "स्मृति सूत्र 2: घर्षण के प्रकार क्रम",
            "phrase": "\"S-K-R (स्थैतिक > गतिज > लोटनिक)\"",
            "decryption": "घर्षण के प्रकार अधिकतम से न्यूनतम क्रम में:<br>• <strong>S</strong> — स्थैतिक घर्षण (Static, सबसे अधिक, गति शुरू करने के लिए आवश्यक)<br>• <strong>K</strong> — गतिज घर्षण (Kinetic, मध्यम, गति का विरोध करता है)<br>• <strong>R</strong> — लोटनिक घर्षण (Rolling, सबसे कम, पहिए इसे कम करते हैं)"
        },
        {
            "title": "स्मृति सूत्र 3: घर्षण को प्रभावित करने वाले कारक",
            "phrase": "\"N-R-I (प्रकृति, खुरदरापन, स्वतंत्रता)\"",
            "decryption": "मुख्य कारक:<br>• <strong>N</strong> — संपर्क में सतहों की प्रकृति (Nature)<br>• <strong>R</strong> — सतहों का खुरदरापन (Roughness)<br>• <strong>I</strong> — क्षेत्रफल से स्वतंत्र (Independent of area)"
        }
    ]
}

flashcards_hi = {
    "title": "सक्रिय रिकॉल फ्लैशकार्ड",
    "description": "उत्तर देखने के लिए होवर करें या क्लिक करें। त्वरित याददाश्त बनाने के लिए इन कार्डों को दोबारा देखें।",
    "items": [
        {
            "question": "न्यूटन का गति का पहला नियम किस नाम से भी जाना जाता है?",
            "answer": "**जड़त्व का नियम (Law of Inertia)** — कोई वस्तु तब तक अपनी स्थिर या एकसमान गति की अवस्था में बनी रहती है जब तक उस पर कोई बाह्य असंतुलित बल न लगाया जाए।",
            "icon": "fa-bed"
        },
        {
            "question": "न्यूटन के गति के दूसरे नियम को गणितीय रूप में लिखें।",
            "answer": "**F = ma** (बल = द्रव्यमान × त्वरण)। किसी पिंड के संवेग में परिवर्तन की दर लगाए गए बल के समानुपाती होती है और बल की दिशा में होती है।",
            "icon": "fa-square-root-variable"
        },
        {
            "question": "संवेग (Momentum) का SI मात्रक क्या है?",
            "answer": "**kg·m/s** (किलोग्राम मीटर प्रति सेकंड)। संवेग = द्रव्यमान × वेग।",
            "icon": "fa-arrow-right"
        },
        {
            "question": "द्रव्यमान (Mass) और भार (Weight) में क्या अंतर है?",
            "answer": "**द्रव्यमान** पदार्थ की मात्रा है (अदिश, हर जगह स्थिर, kg में मापा जाता है)। **भार** वस्तु पर गुरुत्वाकर्षण बल है (सदिश, W = mg, गुरुत्व के साथ बदलता है)।",
            "icon": "fa-scale-balanced"
        }
    ]
}

traps_hi = {
    "title": "बचाव योग्य सामान्य परीक्षा भ्रम (Traps)",
    "items": [
        "<strong>भ्रम 1:</strong> द्रव्यमान और भार को भ्रमित करना। द्रव्यमान स्थान के साथ नहीं बदलता; भार गुरुत्वीय क्षेत्र के साथ बदलता है (जैसे चंद्रमा पर भार पृथ्वी का 1/6 है, पर द्रव्यमान वही रहता है)।",
        "<strong>भ्रम 2:</strong> यह सोचना कि एकसमान वृत्तीय गति में कोई त्वरण नहीं होता। एकसमान वृत्तीय गति में चाल स्थिर रहती है, लेकिन दिशा बदलती रहती है — अतः **अभिकेंद्रीय त्वरण (centripetal acceleration)** केंद्र की ओर होता है।",
        "<strong>भ्रम 3:</strong> यह सोचना कि शून्य नेट बल का अर्थ वस्तु विराम अवस्था में होनी चाहिए। न्यूटन के पहले नियम के अनुसार, शून्य नेट बल का अर्थ है कि वस्तु या तो विराम में है या एकसमान गति में है।",
        "<strong>भ्रम 4:</strong> संवेग और गतिज ऊर्जा को भ्रमित करना। संवेग (p = mv) एक सदिश है; गतिज ऊर्जा (KE = ½mv²) एक अदिश है। एक पिंड में गतिज ऊर्जा हो सकती है लेकिन शुद्ध संवेग शून्य हो सकता है (दो समान द्रव्यमान विपरीत दिशा में चलते हुए)।"
    ]
}

deep_dive_hi = [
    {
        "title": "1. गति के प्रकार और संदर्भ फ्रेम",
        "content": """<p>गति समय और एक संदर्भ बिंदु के सापेक्ष किसी वस्तु की स्थिति में परिवर्तन है। मुख्य प्रकार इस प्रकार हैं:</p>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>गति का प्रकार</th>
                <th>विवरण</th>
                <th>उदाहरण</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>स्थानांतरीय (Translational)</strong></td>
                <td>सभी भाग समान दिशा में समान दूरी तय करते हैं</td>
                <td>सीधी सड़क पर चलती कार</td>
              </tr>
              <tr>
                <td><strong>घूर्णन (Rotational)</strong></td>
                <td>पिंड एक निश्चित अक्ष के चारों ओर घूमता है</td>
                <td>पृथ्वी का घूर्णन, लट्टू</td>
              </tr>
              <tr>
                <td><strong>दोलन (Oscillatory)</strong></td>
                <td>माध्य स्थिति के चारों ओर आगे-पीछे गति</td>
                <td>सरल लोलक, कंपन करती डोरी</td>
              </tr>
              <tr>
                <td><strong>आवर्ती (Periodic)</strong></td>
                <td>गति जो नियमित अंतराल पर दोहराई जाती है</td>
                <td>सूर्य के चारों ओर ग्रहों की गति</td>
              </tr>
              <tr>
                <td><strong>एकसमान वृत्तीय</strong></td>
                <td>स्थिर चाल के साथ वृत्ताकार पथ पर गति</td>
                <td>पृथ्वी की परिक्रमा करता उपग्रह</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p><strong>संदर्भ फ्रेम (Frame of Reference)</strong>: एक निर्देशांक प्रणाली जिसके सापेक्ष गति मापी जाती है। जड़त्वीय फ्रेम त्वरित नहीं होते (न्यूटन के नियम सीधे लागू होते हैं); गैर-जड़त्वीय फ्रेम में छद्म बलों की आवश्यकता होती है।</p>"""
    },
    {
        "title": "2. गति में अदिश और सदिश राशियां",
        "content": """<p>गति के लिए अदिश और सदिश के बीच अंतर समझना मौलिक है:</p>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>राशि</th>
                <th>प्रकार</th>
                <th>SI मात्रक</th>
                <th>सूत्र</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>दूरी (Distance)</strong></td>
                <td>अदिश</td>
                <td>m</td>
                <td>तय किए गए पथ की कुल लंबाई</td>
              </tr>
              <tr>
                <td><strong>विस्थापन (Displacement)</strong></td>
                <td>सदिश</td>
                <td>m</td>
                <td>प्रारंभिक से अंतिम स्थिति तक की न्यूनतम दूरी</td>
              </tr>
              <tr>
                <td><strong>चाल (Speed)</strong></td>
                <td>अदिश</td>
                <td>m/s</td>
                <td>दूरी / समय</td>
              </tr>
              <tr>
                <td><strong>वेग (Velocity)</strong></td>
                <td>सदिश</td>
                <td>m/s</td>
                <td>विस्थापन / समय</td>
              </tr>
              <tr>
                <td><strong>त्वरण (Acceleration)</strong></td>
                <td>सदिश</td>
                <td>m/s²</td>
                <td>(v - u) / t</td>
              </tr>
              <tr>
                <td><strong>संवेग (Momentum)</strong></td>
                <td>सदिश</td>
                <td>kg·m/s</td>
                <td>p = m × v</td>
              </tr>
              <tr>
                <td><strong>बल (Force)</strong></td>
                <td>सदिश</td>
                <td>N (न्यूटन)</td>
                <td>F = ma</td>
              </tr>
            </tbody>
          </table>
        </div>
        
        <p><strong>गति के समीकरण (स्थिर त्वरण के लिए):</strong></p>
        <ul>
          <li><strong>v = u + at</strong> (वेग और समय में संबंध)</li>
          <li><strong>s = ut + ½at²</strong> (विस्थापन और समय में संबंध)</li>
          <li><strong>v² = u² + 2as</strong> (समय रहित संबंध)</li>
          <li><strong>s<sub>n</sub> = u + a(2n - 1)/2</strong> (nवें सेकंड में तय दूरी)</li>
        </ul>
        <p><em>जहाँ: u = प्रारंभिक वेग, v = अंतिम वेग, a = त्वरण, t = समय, s = विस्थापन</em></p>"""
    },
    {
        "title": "3. न्यूटन के गति के नियम",
        "content": """<p>न्यूटन के तीन नियम शास्त्रीय यांत्रिकी की नींव बनाते हैं:</p>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>नियम</th>
                <th>कथन</th>
                <th>मुख्य अवधारणा</th>
                <th>उदाहरण</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>पहला नियम</strong></td>
                <td>कोई वस्तु अपनी स्थिर अवस्था या एकसमान गति की अवस्था में तब तक बनी रहती है जब तक उस पर कोई बाहरी असंतुलित बल न लगाया जाए।</td>
                <td><strong>जड़त्व (Inertia)</strong> — गति की अवस्था में परिवर्तन का विरोध</td>
                <td>मेज पर रखी किताब तब तक स्थिर रहती है जब तक धक्का न लगे।</td>
              </tr>
              <tr>
                <td><strong>दूसरा नियम</strong></td>
                <td>किसी पिंड के संवेग परिवर्तन की दर लगाए गए बल के समानुपाती होती है और बल की दिशा में होती है। (F = ma)</td>
                <td><strong>बल का मापन</strong> — 1 N = 1 kg·m/s²</td>
                <td>टेनिस रैकेट गेंद को त्वरित करने के लिए बल लगाता है।</td>
              </tr>
              <tr>
                <td><strong>तीसरा नियम</strong></td>
                <td>प्रत्येक क्रिया के बराबर और विपरीत प्रतिक्रिया होती है। (बल हमेशा युग्म में होते हैं।)</td>
                <td><strong>क्रिया-प्रतिक्रिया</strong> — बल अलग-अलग पिंडों पर कार्य करते हैं</td>
                <td>जब आप कूदते हैं, आप पृथ्वी को नीचे धकेलते हैं (क्रिया) और पृथ्वी आपको ऊपर धकेलती है (प्रतिक्रिया)।</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p><strong>आवेग (Impulse):</strong> आवेग = बल × समय = संवेग में परिवर्तन। यह एक सदिश राशि है (SI मात्रक: N·s या kg·m/s)। क्रिकेटर गेंद पकड़ते समय हाथ पीछे खींचता है जिससे प्रभाव का समय बढ़ जाता है और बल कम हो जाता है।</p>"""
    },
    {
        "title": "4. बलों के प्रकार",
        "content": """<p>बलों को मोटे तौर पर <strong>संपर्क बल</strong> और <strong>असंपर्क बल</strong> में वर्गीकृत किया जाता है:</p>
        
        <h4 style="margin-top: 1rem;">संपर्क बल (Contact Forces)</h4>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>बल</th>
                <th>विवरण</th>
                <th>परीक्षा के लिए महत्वपूर्ण तथ्य</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>घर्षण (Friction)</strong></td>
                <td>संपर्क में सतहों के बीच सापेक्ष गति का विरोध करता है</td>
                <td>F = μN (μ = घर्षण गुणांक, N = अभिलंब प्रतिक्रिया)। स्थैतिक > गतिज > लोटनिक घर्षण।</td>
              </tr>
              <tr>
                <td><strong>अभिलंब प्रतिक्रिया</strong></td>
                <td>किसी सतह द्वारा वस्तु पर लगाया गया लंबवत बल</td>
                <td>हमेशा संपर्क सतह के लंबवत कार्य करता है।</td>
              </tr>
              <tr>
                <td><strong>तनाव (Tension)</strong></td>
                <td>रस्सी/डोरी में खिंचाव पर संचारित बल</td>
                <td>आदर्श द्रव्यमानहीन, अविभाज्य डोरी में तनाव हर जगह समान होता है।</td>
              </tr>
              <tr>
                <td><strong>स्प्रिंग बल</strong></td>
                <td>विस्थापन के समानुपाती प्रत्यावर्तन बल (हुक का नियम)</td>
                <td>F = -kx (k = स्प्रिंग स्थिरांक, x = प्राकृतिक लंबाई से विस्थापन)</td>
              </tr>
            </tbody>
          </table>
        </div>
        
        <h4 style="margin-top: 1.5rem;">असंपर्क बल (Non-Contact Forces)</h4>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>बल</th>
                <th>विवरण</th>
                <th>परीक्षा के लिए महत्वपूर्ण तथ्य</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>गुरुत्वाकर्षण बल</strong></td>
                <td>किन्हीं दो द्रव्यमानों के बीच आकर्षण बल</td>
                <td>F = Gm₁m₂/r². पृथ्वी की सतह पर g = 9.8 m/s². ऊंचाई और गहराई के साथ g घटता है।</td>
              </tr>
              <tr>
                <td><strong>विद्युत चुंबकीय बल</strong></td>
                <td>आवेशित कणों के बीच बल (विद्युत और चुंबकीय)</td>
                <td>गुरुत्वाकर्षण से बहुत अधिक शक्तिशाली (~10³⁶ गुना)। परमाणु और आणविक अंतःक्रियाओं को नियंत्रित करता है।</td>
              </tr>
              <tr>
                <td><strong>नाभिकीय बल</strong></td>
                <td>प्रबल और दुर्बल नाभिकीय बल नाभिक को बांधते हैं</td>
                <td>प्रकृति का सबसे शक्तिशाली बल। अत्यंत छोटी सीमा (~10⁻¹⁵ m) पर कार्य करता है।</td>
              </tr>
              <tr>
                <td><strong>अभिकेंद्रीय बल</strong></td>
                <td>वृत्ताकार पथ पर पिंड को बनाए रखने के लिए आवश्यक बल</td>
                <td>F<sub>c</sub> = mv²/r. केंद्र की ओर दिष्ट। इसके बिना पिंड स्पर्श रेखा की ओर उड़ जाएगा।</td>
              </tr>
              <tr>
                <td><strong>अपकेंद्रीय बल</strong></td>
                <td>घूर्णन संदर्भ फ्रेम में महसूस किया जाने वाला छद्म बल</td>
                <td>केंद्र से बाहर की ओर दिष्ट। यह गैर-जड़त्वीय फ्रेम में अनुभव किया जाने वाला काल्पनिक बल है।</td>
              </tr>
            </tbody>
          </table>
        </div>"""
    },
    {
        "title": "5. घर्षण, गुरुत्वाकर्षण और संरक्षण नियम",
        "content": """<p><strong>घर्षण (Friction)</strong> एक प्रतिरोधी बल है जो संपर्क में सतहों के बीच सापेक्ष गति का विरोध करता है। इसके तीन प्रकार हैं:</p>
        <ul>
          <li><strong>स्थैतिक घर्षण (f<sub>s</sub>)</strong>: गति की शुरुआत का विरोध करता है। अधिकतम स्थैतिक घर्षण f<sub>s</sub>(max) = μ<sub>s</sub>N.</li>
          <li><strong>गतिज/सर्पी घर्षण (f<sub>k</sub>)</strong>: चल रही गति का विरोध करता है। f<sub>k</sub> = μ<sub>k</sub>N. सामान्यतः μ<sub>k</sub> < μ<sub>s</sub>.</li>
          <li><strong>लोटनिक घर्षण (f<sub>r</sub>)</strong>: लुढ़कने की गति का विरोध करता है। स्थैतिक और गतिज घर्षण से बहुत कम। यही कारण है कि पहियों का आविष्कार हुआ।</li>
        </ul>
        <p><strong>घर्षण कम करने के उपाय:</strong> स्नेहन (तेल/ग्रीस), सतहों को पॉलिश करना, बॉल बेयरिंग का उपयोग, सुव्यवस्थित आकार और पहियों/रोलर्स का उपयोग।</p>
        
        <p><strong>गुरुत्वाकर्षण (सार्वभौमिक गुरुत्वाकर्षण):</strong></p>
        <ul>
          <li>प्रत्येक कण एक-दूसरे को उनके द्रव्यमानों के गुणनफल के समानुपाती और उनके बीच की दूरी के वर्ग के व्युत्क्रमानुपाती बल से आकर्षित करता है।</li>
          <li><strong>गुरुत्वीय त्वरण (g)</strong>: पृथ्वी की सतह पर, g = GM/R² ≈ 9.8 m/s².</li>
          <li><strong>g में परिवर्तन:</strong> 
            <ul>
              <li>ऊंचाई के साथ: g' = g(1 - 2h/R) (h << R के लिए)।</li>
              <li>गहराई के साथ: g' = g(1 - d/R) पृथ्वी के अंदर।</li>
              <li>पृथ्वी के घूर्णन के कारण: g ध्रुवों पर अधिकतम, भूमध्य रेखा पर न्यूनतम।</li>
            </ul>
          </li>
          <li><strong>पलायन वेग (v<sub>e</sub>)</strong>: पृथ्वी के गुरुत्वाकर्षण से बचने के लिए आवश्यक न्यूनतम वेग। v<sub>e</sub> = √(2GM/R) = √(2gR) ≈ 11.2 km/s.</li>
        </ul>
        
        <p><strong>संरक्षण नियम:</strong></p>
        <ul>
          <li><strong>रैखिक संवेग का संरक्षण</strong>: बाह्य बलों की अनुपस्थिति में, एक पृथक निकाय का कुल संवेग स्थिर रहता है।</li>
          <li><strong>ऊर्जा का संरक्षण</strong>: ऊर्जा न तो उत्पन्न की जा सकती है और न ही नष्ट — इसे केवल एक रूप से दूसरे रूप में परिवर्तित किया जा सकता है।</li>
          <li><strong>कोणीय संवेग का संरक्षण</strong>: बाह्य बल आघूर्ण की अनुपस्थिति में, किसी निकाय का कोणीय संवेग स्थिर रहता है।</li>
        </ul>"""
    }
]

# ----------------- PRACTICE QUESTIONS (50 Qs) -----------------
practice_questions = [
    {
        "q": "What is the SI unit of Force?",
        "q_hi": "बल का SI मात्रक क्या है?",
        "opts": ["Joule", "Newton", "Pascal", "Watt"],
        "opts_hi": ["जूल", "न्यूटन", "पास्कल", "वाट"],
        "ans": 1,
        "sol": "Newton is the SI derived unit of force (equivalent to kg·m/s²).",
        "sol_hi": "बल का व्युत्पन्न SI मात्रक न्यूटन है (किग्रा·मीटर/सेकंड² के बराबर)।"
    },
    {
        "q": "Newton's first law of motion is also known as:",
        "q_hi": "न्यूटन का गति का पहला नियम किस नाम से जाना जाता है?",
        "opts": ["Law of Gravitation", "Law of Inertia", "Law of Acceleration", "Law of Reaction"],
        "opts_hi": ["गुरुत्वाकर्षण का नियम", "जड़त्व का नियम", "त्वरण का नियम", "प्रतिक्रिया का नियम"],
        "ans": 1,
        "sol": "Newton's first law is called the Law of Inertia — an object resists change in its state of motion.",
        "sol_hi": "न्यूटन के पहले नियम को जड़त्व का नियम कहा जाता है — वस्तु अपनी गति की अवस्था में परिवर्तन का विरोध करती है।"
    },
    {
        "q": "What is the mathematical expression of Newton's second law?",
        "q_hi": "न्यूटन के दूसरे नियम का गणितीय सूत्र क्या है?",
        "opts": ["F = mv", "F = ma", "F = m/v", "F = m²a"],
        "opts_hi": ["F = mv", "F = ma", "F = m/v", "F = m²a"],
        "ans": 1,
        "sol": "F = ma (Force = Mass × Acceleration). The net force equals rate of change of momentum.",
        "sol_hi": "F = ma (बल = द्रव्यमान × त्वरण)। शुद्ध बल संवेग परिवर्तन की दर के बराबर होता है।"
    },
    {
        "q": "Which of the following is a vector quantity?",
        "q_hi": "निम्नलिखित में से कौन सी एक सदिश राशि है?",
        "opts": ["Speed", "Distance", "Velocity", "Mass"],
        "opts_hi": ["चाल", "दूरी", "वेग", "द्रव्यमान"],
        "ans": 2,
        "sol": "Velocity has both magnitude and direction, making it a vector. Speed, distance, and mass are scalars.",
        "sol_hi": "वेग में परिमाण और दिशा दोनों होते हैं, जिससे यह सदिश राशि है। चाल, दूरी और द्रव्यमान अदिश हैं।"
    },
    {
        "q": "What is the SI unit of momentum?",
        "q_hi": "संवेग का SI मात्रक क्या है?",
        "opts": ["Newton", "kg·m/s", "Joule", "Watt"],
        "opts_hi": ["न्यूटन", "kg·m/s", "जूल", "वाट"],
        "ans": 1,
        "sol": "Momentum = mass × velocity, so its SI unit is kg·m/s.",
        "sol_hi": "संवेग = द्रव्यमान × वेग, अतः इसका SI मात्रक kg·m/s है।"
    },
    {
        "q": "When a cricketer pulls his hands back while catching a ball, which principle is applied?",
        "q_hi": "क्रिकेटर गेंद पकड़ते समय हाथ पीछे खींचता है, यह किस सिद्धांत का अनुप्रयोग है?",
        "opts": ["Newton's first law", "Impulse-momentum theorem", "Conservation of energy", "Hooke's law"],
        "opts_hi": ["न्यूटन का पहला नियम", "आवेग-संवेग प्रमेय", "ऊर्जा संरक्षण", "हुक का नियम"],
        "ans": 1,
        "sol": "Pulling hands back increases impact time, reducing the force (Impulse = F × t = constant change in momentum).",
        "sol_hi": "हाथ पीछे खींचने से प्रभाव का समय बढ़ता है, जिससे बल कम होता है (आवेग = F × t = स्थिर संवेग परिवर्तन)।"
    },
    {
        "q": "The force that opposes the motion of an object through a fluid is called:",
        "q_hi": "किसी तरल पदार्थ में गति का विरोध करने वाला बल कहलाता है:",
        "opts": ["Friction", "Viscous drag", "Tension", "Normal reaction"],
        "opts_hi": ["घर्षण", "श्यान कर्षण", "तनाव", "अभिलंब प्रतिक्रिया"],
        "ans": 1,
        "sol": "Viscous drag (or fluid friction) opposes motion through liquids or gases.",
        "sol_hi": "श्यान कर्षण (या तरल घर्षण) द्रव या गैस में गति का विरोध करता है।"
    },
    {
        "q": "What is the value of acceleration due to gravity (g) at the Earth's surface?",
        "q_hi": "पृथ्वी की सतह पर गुरुत्वीय त्वरण (g) का मान क्या है?",
        "opts": ["8.9 m/s²", "9.8 m/s²", "10.8 m/s²", "7.8 m/s²"],
        "opts_hi": ["8.9 m/s²", "9.8 m/s²", "10.8 m/s²", "7.8 m/s²"],
        "ans": 1,
        "sol": "The standard value of g at Earth's surface is approximately 9.8 m/s².",
        "sol_hi": "पृथ्वी की सतह पर g का मानक मान लगभग 9.8 m/s² है।"
    },
    {
        "q": "Which of Newton's laws explains the recoil of a gun?",
        "q_hi": "बंदूक का पीछे हटना (recoil) न्यूटन के किस नियम द्वारा समझाया जाता है?",
        "opts": ["First law", "Second law", "Third law", "Law of gravitation"],
        "opts_hi": ["पहला नियम", "दूसरा नियम", "तीसरा नियम", "गुरुत्वाकर्षण का नियम"],
        "ans": 2,
        "sol": "The gun exerts forward force on the bullet (action), and the bullet exerts equal backward force on the gun (reaction), causing the recoil. This is Newton's third law.",
        "sol_hi": "बंदूक गोली पर आगे की ओर बल लगाती है (क्रिया), और गोली बंदूक पर बराबर पीछे की ओर बल लगाती है (प्रतिक्रिया), जिससे पीछे हटना होता है।"
    },
    {
        "q": "If the mass of a body is doubled and its velocity is halved, what happens to its momentum?",
        "q_hi": "यदि किसी पिंड का द्रव्यमान दोगुना और वेग आधा कर दिया जाए, तो उसके संवेग पर क्या प्रभाव पड़ेगा?",
        "opts": ["Doubled", "Halved", "Unchanged", "Quadrupled"],
        "opts_hi": ["दोगुना", "आधा", "अपरिवर्तित", "चार गुना"],
        "ans": 2,
        "sol": "Momentum p = m × v. New momentum = (2m) × (v/2) = mv = same. Momentum remains unchanged.",
        "sol_hi": "संवेग p = m × v. नया संवेग = (2m) × (v/2) = mv = समान रहता है।"
    },
    {
        "q": "Which type of friction is the largest in magnitude?",
        "q_hi": "कौन सा घर्षण परिमाण में सबसे बड़ा होता है?",
        "opts": ["Static friction", "Kinetic friction", "Rolling friction", "Fluid friction"],
        "opts_hi": ["स्थैतिक घर्षण", "गतिज घर्षण", "लोटनिक घर्षण", "तरल घर्षण"],
        "ans": 0,
        "sol": "Static friction is the strongest as it must overcome the interlocking of surface irregularities to start motion.",
        "sol_hi": "स्थैतिक घर्षण सबसे प्रबल होता है क्योंकि इसे गति शुरू करने के लिए सतह की अनियमितताओं को पार करना होता है।"
    },
    {
        "q": "What is the escape velocity of Earth?",
        "q_hi": "पृथ्वी का पलायन वेग कितना है?",
        "opts": ["7.2 km/s", "9.8 km/s", "11.2 km/s", "15 km/s"],
        "opts_hi": ["7.2 km/s", "9.8 km/s", "11.2 km/s", "15 km/s"],
        "ans": 2,
        "sol": "Escape velocity of Earth is approximately 11.2 km/s, the minimum speed needed to overcome Earth's gravity.",
        "sol_hi": "पृथ्वी का पलायन वेग लगभग 11.2 km/s है, जो पृथ्वी के गुरुत्वाकर्षण से बचने की न्यूनतम गति है।"
    },
    {
        "q": "A body moving in a circular path experiences which force directed towards the center?",
        "q_hi": "वृत्ताकार पथ पर चलने वाला पिंड केंद्र की ओर किस बल का अनुभव करता है?",
        "opts": ["Centrifugal force", "Centripetal force", "Gravitational force", "Frictional force"],
        "opts_hi": ["अपकेंद्रीय बल", "अभिकेंद्रीय बल", "गुरुत्वाकर्षण बल", "घर्षण बल"],
        "ans": 1,
        "sol": "Centripetal force (Fc = mv²/r) is directed towards the center of the circular path, keeping the body in circular motion.",
        "sol_hi": "अभिकेंद्रीय बल (Fc = mv²/r) वृत्ताकार पथ के केंद्र की ओर दिष्ट होता है, जो पिंड को वृत्तीय गति में रखता है।"
    },
    {
        "q": "Which law states that \"Energy can neither be created nor destroyed\"?",
        "q_hi": "कौन सा नियम कहता है कि \"ऊर्जा न तो उत्पन्न की जा सकती है और न ही नष्ट\"?",
        "opts": ["Law of conservation of mass", "Law of conservation of energy", "Newton's first law", "Newton's second law"],
        "opts_hi": ["द्रव्यमान संरक्षण का नियम", "ऊर्जा संरक्षण का नियम", "न्यूटन का पहला नियम", "न्यूटन का दूसरा नियम"],
        "ans": 1,
        "sol": "The law of conservation of energy states energy can only be transformed from one form to another, not created or destroyed.",
        "sol_hi": "ऊर्जा संरक्षण का नियम कहता है कि ऊर्जा को केवल एक रूप से दूसरे रूप में बदला जा सकता है, न उत्पन्न और न नष्ट।"
    },
    {
        "q": "F = μN is the formula for which type of force?",
        "q_hi": "F = μN किस बल का सूत्र है?",
        "opts": ["Gravitational force", "Frictional force", "Centripetal force", "Spring force"],
        "opts_hi": ["गुरुत्वाकर्षण बल", "घर्षण बल", "अभिकेंद्रीय बल", "स्प्रिंग बल"],
        "ans": 1,
        "sol": "F = μN is the formula for frictional force, where μ is the coefficient of friction and N is the normal reaction.",
        "sol_hi": "F = μN घर्षण बल का सूत्र है, जहाँ μ घर्षण गुणांक है और N अभिलंब प्रतिक्रिया है।"
    },
    {
        "q": "When a passenger in a bus is thrown forward when the bus suddenly stops, this is an example of:",
        "q_hi": "जब बस अचानक रुकती है तो यात्री आगे की ओर झुक जाता है, यह किसका उदाहरण है?",
        "opts": ["Newton's first law (inertia)", "Newton's second law", "Newton's third law", "Conservation of momentum"],
        "opts_hi": ["न्यूटन का पहला नियम (जड़त्व)", "न्यूटन का दूसरा नियम", "न्यूटन का तीसरा नियम", "संवेग संरक्षण"],
        "ans": 0,
        "sol": "Due to inertia, the passenger's body continues moving forward even when the bus stops suddenly (Newton's first law).",
        "sol_hi": "जड़त्व के कारण, बस अचानक रुकने पर भी यात्री का शरीर आगे बढ़ता रहता है (न्यूटन का पहला नियम)।"
    },
    {
        "q": "Which of the following is NOT a contact force?",
        "q_hi": "निम्नलिखित में से कौन संपर्क बल नहीं है?",
        "opts": ["Friction", "Normal reaction", "Tension", "Gravitational force"],
        "opts_hi": ["घर्षण", "अभिलंब प्रतिक्रिया", "तनाव", "गुरुत्वाकर्षण बल"],
        "ans": 3,
        "sol": "Gravitational force is a non-contact (field) force. Friction, normal reaction, and tension are contact forces.",
        "sol_hi": "गुरुत्वाकर्षण बल एक असंपर्क (क्षेत्र) बल है। घर्षण, अभिलंब प्रतिक्रिया और तनाव संपर्क बल हैं।"
    },
    {
        "q": "What is the formula for centripetal force?",
        "q_hi": "अभिकेंद्रीय बल का सूत्र क्या है?",
        "opts": ["F = mv²/r", "F = mvr", "F = mr/v²", "F = v²/mr"],
        "opts_hi": ["F = mv²/r", "F = mvr", "F = mr/v²", "F = v²/mr"],
        "ans": 0,
        "sol": "Centripetal force F = mv²/r, where m is mass, v is velocity, and r is the radius of the circular path.",
        "sol_hi": "अभिकेंद्रीय बल F = mv²/r, जहाँ m द्रव्यमान, v वेग और r वृत्ताकार पथ की त्रिज्या है।"
    },
    {
        "q": "Which of the following quantities remains constant in uniform circular motion?",
        "q_hi": "एकसमान वृत्तीय गति में निम्नलिखित में से कौन सी राशि स्थिर रहती है?",
        "opts": ["Velocity", "Acceleration", "Speed", "Displacement"],
        "opts_hi": ["वेग", "त्वरण", "चाल", "विस्थापन"],
        "ans": 2,
        "sol": "In uniform circular motion, speed remains constant but velocity changes due to changing direction.",
        "sol_hi": "एकसमान वृत्तीय गति में चाल स्थिर रहती है लेकिन दिशा बदलने के कारण वेग बदलता है।"
    },
    {
        "q": "The impulse-momentum theorem states that impulse equals:",
        "q_hi": "आवेग-संवेग प्रमेय के अनुसार आवेग किसके बराबर होता है?",
        "opts": ["Change in kinetic energy", "Change in momentum", "Change in velocity", "Change in acceleration"],
        "opts_hi": ["गतिज ऊर्जा में परिवर्तन", "संवेग में परिवर्तन", "वेग में परिवर्तन", "त्वरण में परिवर्तन"],
        "ans": 1,
        "sol": "Impulse = Force × Time = Change in momentum (Δp).",
        "sol_hi": "आवेग = बल × समय = संवेग में परिवर्तन (Δp)।"
    },
    {
        "q": "What happens to the value of 'g' as we go above the Earth's surface?",
        "q_hi": "पृथ्वी की सतह से ऊपर जाने पर 'g' के मान पर क्या प्रभाव पड़ता है?",
        "opts": ["Increases", "Decreases", "Remains constant", "First increases then decreases"],
        "opts_hi": ["बढ़ता है", "घटता है", "स्थिर रहता है", "पहले बढ़ता है फिर घटता है"],
        "ans": 1,
        "sol": "The value of g decreases with altitude: g' = g(1 - 2h/R).",
        "sol_hi": "ऊंचाई के साथ g का मान घटता है: g' = g(1 - 2h/R)।"
    },
    {
        "q": "Which force is responsible for holding the planets in orbit around the Sun?",
        "q_hi": "सूर्य के चारों ओर ग्रहों की कक्षा में रखने वाला बल कौन सा है?",
        "opts": ["Centripetal force", "Centrifugal force", "Gravitational force", "Magnetic force"],
        "opts_hi": ["अभिकेंद्रीय बल", "अपकेंद्रीय बल", "गुरुत्वाकर्षण बल", "चुंबकीय बल"],
        "ans": 2,
        "sol": "Gravitational force between the Sun and planets provides the necessary centripetal force for orbital motion.",
        "sol_hi": "सूर्य और ग्रहों के बीच गुरुत्वाकर्षण बल कक्षीय गति के लिए आवश्यक अभिकेंद्रीय बल प्रदान करता है।"
    },
    {
        "q": "The coefficient of friction depends on:",
        "q_hi": "घर्षण गुणांक निर्भर करता है:",
        "opts": ["Area of contact", "Nature of surfaces", "Relative speed", "All of the above"],
        "opts_hi": ["संपर्क क्षेत्रफल", "सतहों की प्रकृति", "सापेक्ष गति", "उपरोक्त सभी"],
        "ans": 1,
        "sol": "The coefficient of friction depends only on the nature (material and roughness) of the surfaces, NOT on area or speed.",
        "sol_hi": "घर्षण गुणांक केवल सतहों की प्रकृति (सामग्री और खुरदरापन) पर निर्भर करता है, क्षेत्र या गति पर नहीं।"
    },
    {
        "q": "What is inertia a measure of?",
        "q_hi": "जड़त्व (inertia) किसका माप है?",
        "opts": ["Weight of a body", "Mass of a body", "Velocity of a body", "Volume of a body"],
        "opts_hi": ["पिंड का भार", "पिंड का द्रव्यमान", "पिंड का वेग", "पिंड का आयतन"],
        "ans": 1,
        "sol": "Inertia is directly proportional to mass. Heavier objects have greater inertia and are harder to move or stop.",
        "sol_hi": "जड़त्व द्रव्यमान के समानुपाती होता है। भारी वस्तुओं में अधिक जड़त्व होता है और उन्हें चलाना/रोकना कठिन होता है।"
    },
    {
        "q": "When we jump off a boat, the boat moves backward. This is an example of:",
        "q_hi": "जब हम नाव से कूदते हैं, तो नाव पीछे चली जाती है। यह किसका उदाहरण है?",
        "opts": ["Newton's first law", "Newton's second law", "Newton's third law", "Law of gravitation"],
        "opts_hi": ["न्यूटन का पहला नियम", "न्यूटन का दूसरा नियम", "न्यूटन का तीसरा नियम", "गुरुत्वाकर्षण का नियम"],
        "ans": 2,
        "sol": "The person pushes the boat backward (action), and the boat pushes the person forward (reaction) — Newton's third law.",
        "sol_hi": "व्यक्ति नाव को पीछे धकेलता है (क्रिया), और नाव व्यक्ति को आगे धकेलती है (प्रतिक्रिया) — न्यूटन का तीसरा नियम।"
    },
    {
        "q": "How does the value of 'g' vary with depth inside the Earth?",
        "q_hi": "पृथ्वी के अंदर गहराई के साथ 'g' के मान में क्या परिवर्तन होता है?",
        "opts": ["Increases", "Decreases", "Remains constant", "Becomes zero at center"],
        "opts_hi": ["बढ़ता है", "घटता है", "स्थिर रहता है", "केंद्र पर शून्य हो जाता है"],
        "ans": 3,
        "sol": "g decreases linearly with depth and becomes zero at the center of the Earth.",
        "sol_hi": "g गहराई के साथ रैखिक रूप से घटता है और पृथ्वी के केंद्र पर शून्य हो जाता है।"
    },
    {
        "q": "A ball rolling on the ground stops after some time due to:",
        "q_hi": "जमीन पर लुढ़कती गेंद कुछ समय बाद रुक जाती है:",
        "opts": ["Gravitational force", "Frictional force", "Centripetal force", "Magnetic force"],
        "opts_hi": ["गुरुत्वाकर्षण बल", "घर्षण बल", "अभिकेंद्रीय बल", "चुंबकीय बल"],
        "ans": 1,
        "sol": "The ball stops due to frictional force between the ball and the ground, which opposes motion.",
        "sol_hi": "गेंद और जमीन के बीच घर्षण बल के कारण गेंद रुक जाती है, जो गति का विरोध करता है।"
    },
    {
        "q": "Which of the following is the equation for the distance traveled in the nth second?",
        "q_hi": "nवें सेकंड में तय की गई दूरी का सूत्र क्या है?",
        "opts": ["s = ut + ½at²", "s = u + a(2n-1)/2", "v = u + at", "v² = u² + 2as"],
        "opts_hi": ["s = ut + ½at²", "s = u + a(2n-1)/2", "v = u + at", "v² = u² + 2as"],
        "ans": 1,
        "sol": "Distance traveled in nth second: s_n = u + a(2n - 1)/2.",
        "sol_hi": "nवें सेकंड में तय दूरी: s_n = u + a(2n - 1)/2."
    },
    {
        "q": "Which force acts on a body moving in a circle when viewed from an inertial frame?",
        "q_hi": "एक जड़त्वीय फ्रेम से देखने पर वृत्ताकार पथ पर चलने वाले पिंड पर कौन सा बल कार्य करता है?",
        "opts": ["Only centripetal force", "Only centrifugal force", "Both centripetal and centrifugal force", "Neither"],
        "opts_hi": ["केवल अभिकेंद्रीय बल", "केवल अपकेंद्रीय बल", "अभिकेंद्रीय और अपकेंद्रीय दोनों", "कोई नहीं"],
        "ans": 0,
        "sol": "In an inertial frame, only centripetal force (real force) is present. Centrifugal force is a pseudo-force in non-inertial frames.",
        "sol_hi": "जड़त्वीय फ्रेम में केवल अभिकेंद्रीय बल (वास्तविक बल) मौजूद है। अपकेंद्रीय बल गैर-जड़त्वीय फ्रेम में छद्म बल है।"
    },
    {
        "q": "The mass of a body on the Moon is 60 kg. What is its weight on the Moon? (g_moon = 1.6 m/s²)",
        "q_hi": "चंद्रमा पर किसी पिंड का द्रव्यमान 60 kg है। चंद्रमा पर इसका भार क्या होगा? (g_चंद्रमा = 1.6 m/s²)",
        "opts": ["96 N", "60 N", "588 N", "9.8 N"],
        "opts_hi": ["96 N", "60 N", "588 N", "9.8 N"],
        "ans": 0,
        "sol": "Weight = mass × gravity = 60 × 1.6 = 96 N. Mass remains 60 kg.",
        "sol_hi": "भार = द्रव्यमान × गुरुत्व = 60 × 1.6 = 96 N. द्रव्यमान 60 kg ही रहेगा।"
    },
    {
        "q": "What is the unit of the coefficient of friction?",
        "q_hi": "घर्षण गुणांक का मात्रक क्या है?",
        "opts": ["Newton", "No unit (dimensionless)", "N/m", "kg/m"],
        "opts_hi": ["न्यूटन", "कोई मात्रक नहीं (विमीयहीन)", "N/m", "kg/m"],
        "ans": 1,
        "sol": "The coefficient of friction is a dimensionless quantity as it is a ratio of two forces.",
        "sol_hi": "घर्षण गुणांक एक विमीयहीन राशि है क्योंकि यह दो बलों का अनुपात है।"
    },
    {
        "q": "When a bullet is fired from a gun, the net momentum of the bullet-gun system is:",
        "q_hi": "जब बंदूक से गोली चलाई जाती है, तो गोली-बंदूक निकाय का कुल संवेग होता है:",
        "opts": ["More than zero", "Zero", "Depends on mass of bullet", "Depends on velocity of bullet"],
        "opts_hi": ["शून्य से अधिक", "शून्य", "गोली के द्रव्यमान पर निर्भर", "गोली के वेग पर निर्भर"],
        "ans": 1,
        "sol": "By conservation of momentum, initial momentum (zero) = final momentum of gun + bullet. So net = 0.",
        "sol_hi": "संवेग संरक्षण के अनुसार, प्रारंभिक संवेग (शून्य) = बंदूक + गोली का अंतिम संवेग। अतः कुल = 0।"
    },
    {
        "q": "If you apply the same force to two objects of different masses, the lighter object will have:",
        "q_hi": "यदि आप विभिन्न द्रव्यमानों की दो वस्तुओं पर समान बल लगाते हैं, तो हल्की वस्तु में होगा:",
        "opts": ["Greater acceleration", "Less acceleration", "Same acceleration", "Zero acceleration"],
        "opts_hi": ["अधिक त्वरण", "कम त्वरण", "समान त्वरण", "शून्य त्वरण"],
        "ans": 0,
        "sol": "Since F = ma, a = F/m. For same force, smaller mass gives greater acceleration.",
        "sol_hi": "चूँकि F = ma, a = F/m. समान बल के लिए, कम द्रव्यमान अधिक त्वरण देता है।"
    },
    {
        "q": "Which of the following devices is used to measure the force acting on an object?",
        "q_hi": "किसी वस्तु पर कार्य करने वाले बल को मापने के लिए किस उपकरण का उपयोग किया जाता है?",
        "opts": ["Dynamometer", "Barometer", "Thermometer", "Galvanometer"],
        "opts_hi": ["डायनेमोमीटर", "बैरोमीटर", "थर्मामीटर", "गैल्वेनोमीटर"],
        "ans": 0,
        "sol": "A dynamometer is a device that measures force, torque, or power.",
        "sol_hi": "डायनेमोमीटर वह उपकरण है जो बल, आघूर्ण या शक्ति मापता है।"
    },
    {
        "q": "A fruit falling from a tree is an example of motion under:",
        "q_hi": "पेड़ से गिरता फल किसके अंतर्गत गति का उदाहरण है?",
        "opts": ["Constant velocity", "Uniform acceleration", "Non-uniform acceleration", "Deceleration"],
        "opts_hi": ["स्थिर वेग", "एकसमान त्वरण", "असमान त्वरण", "मंदन"],
        "ans": 1,
        "sol": "A freely falling object experiences uniform acceleration due to gravity (g ≈ 9.8 m/s²).",
        "sol_hi": "मुक्त रूप से गिरने वाली वस्तु गुरुत्वाकर्षण के कारण एकसमान त्वरण (g ≈ 9.8 m/s²) का अनुभव करती है।"
    },
    {
        "q": "Hooke's law relates to:",
        "q_hi": "हुक का नियम (Hooke's law) किससे संबंधित है?",
        "opts": ["Friction", "Spring force", "Gravitational force", "Centripetal force"],
        "opts_hi": ["घर्षण", "स्प्रिंग बल", "गुरुत्वाकर्षण बल", "अभिकेंद्रीय बल"],
        "ans": 1,
        "sol": "Hooke's law: F = -kx, where F is restoring force, k is spring constant, and x is displacement.",
        "sol_hi": "हुक का नियम: F = -kx, जहाँ F प्रत्यावर्तन बल, k स्प्रिंग स्थिरांक और x विस्थापन है।"
    },
    {
        "q": "A person weighs less at the equator than at the poles because:",
        "q_hi": "एक व्यक्ति का भार ध्रुवों की तुलना में भूमध्य रेखा पर कम होता है क्योंकि:",
        "opts": ["Earth is flat at equator", "Centrifugal force due to Earth's rotation", "Equator is closer to the Sun", "Less gravity at equator"],
        "opts_hi": ["पृथ्वी भूमध्य रेखा पर चपटी है", "पृथ्वी के घूर्णन के कारण अपकेंद्रीय बल", "भूमध्य रेखा सूर्य के करीब है", "भूमध्य रेखा पर कम गुरुत्व"],
        "ans": 1,
        "sol": "At the equator, the centrifugal force due to Earth's rotation opposes gravity, reducing effective weight.",
        "sol_hi": "भूमध्य रेखा पर, पृथ्वी के घूर्णन के कारण अपकेंद्रीय बल गुरुत्व का विरोध करता है, जिससे प्रभावी भार कम होता है।"
    },
    {
        "q": "Which of the following has maximum inertia?",
        "q_hi": "निम्नलिखित में से किसमें सबसे अधिक जड़त्व होता है?",
        "opts": ["A bicycle", "A car", "A truck", "All have same inertia"],
        "opts_hi": ["साइकिल", "कार", "ट्रक", "सभी में समान जड़त्व"],
        "ans": 2,
        "sol": "Inertia is directly proportional to mass. A truck has the greatest mass, hence maximum inertia.",
        "sol_hi": "जड़त्व द्रव्यमान के समानुपाती होता है। ट्रक का द्रव्यमान सबसे अधिक होता है, अतः सबसे अधिक जड़त्व।"
    },
    {
        "q": "A rocket works on the principle of:",
        "q_hi": "रॉकेट किस सिद्धांत पर कार्य करता है?",
        "opts": ["Newton's first law", "Newton's second law", "Newton's third law", "Law of gravitation"],
        "opts_hi": ["न्यूटन का पहला नियम", "न्यूटन का दूसरा नियम", "न्यूटन का तीसरा नियम", "गुरुत्वाकर्षण का नियम"],
        "ans": 2,
        "sol": "Rockets expel gases downward (action), and the gases push the rocket upward (reaction) — Newton's third law.",
        "sol_hi": "रॉकेट गैसों को नीचे की ओर निष्कासित करता है (क्रिया), और गैसें रॉकेट को ऊपर धकेलती हैं (प्रतिक्रिया) — न्यूटन का तीसरा नियम।"
    },
    {
        "q": "What is the rate of change of momentum equal to?",
        "q_hi": "संवेग परिवर्तन की दर किसके बराबर होती है?",
        "opts": ["Impulse", "Applied force", "Acceleration", "Velocity"],
        "opts_hi": ["आवेग", "लगाया गया बल", "त्वरण", "वेग"],
        "ans": 1,
        "sol": "Rate of change of momentum = Applied force (Newton's second law: F = dp/dt).",
        "sol_hi": "संवेग परिवर्तन की दर = लगाया गया बल (न्यूटन का दूसरा नियम: F = dp/dt)।"
    },
    {
        "q": "A passenger feels a backward push when a vehicle suddenly starts. This is due to:",
        "q_hi": "जब वाहन अचानक चलता है तो यात्री पीछे की ओर धक्का महसूस करता है। यह किसके कारण होता है?",
        "opts": ["Inertia of rest", "Inertia of motion", "Inertia of direction", "Friction"],
        "opts_hi": ["विराम का जड़त्व", "गति का जड़त्व", "दिशा का जड़त्व", "घर्षण"],
        "ans": 0,
        "sol": "The passenger's lower body moves with the vehicle, but the upper body tends to remain at rest (inertia of rest), pushing backward.",
        "sol_hi": "यात्री का निचला भाग वाहन के साथ चलता है, लेकिन ऊपरी भाग विराम में रहना चाहता है (विराम का जड़त्व), पीछे की ओर धकेलता है।"
    },
    {
        "q": "If Earth were to suddenly stop rotating, what would happen to the weight of a body at the equator?",
        "q_hi": "यदि पृथ्वी अचानक घूमना बंद कर दे, तो भूमध्य रेखा पर किसी पिंड के भार पर क्या प्रभाव पड़ेगा?",
        "opts": ["Decrease", "Increase", "Remain same", "Become zero"],
        "opts_hi": ["घट जाएगा", "बढ़ जाएगा", "समान रहेगा", "शून्य हो जाएगा"],
        "ans": 1,
        "sol": "Weight would increase because the centrifugal force that opposed gravity at the equator would no longer exist.",
        "sol_hi": "भार बढ़ जाएगा क्योंकि भूमध्य रेखा पर गुरुत्व का विरोध करने वाला अपकेंद्रीय बल समाप्त हो जाएगा।"
    },
    {
        "q": "The first law of thermodynamics is an extension of which conservation law?",
        "q_hi": "ऊष्मागतिकी का पहला नियम किस संरक्षण नियम का विस्तार है?",
        "opts": ["Conservation of mass", "Conservation of energy", "Conservation of momentum", "Conservation of charge"],
        "opts_hi": ["द्रव्यमान संरक्षण", "ऊर्जा संरक्षण", "संवेग संरक्षण", "आवेश संरक्षण"],
        "ans": 1,
        "sol": "The first law of thermodynamics is a version of the law of conservation of energy for thermodynamic systems.",
        "sol_hi": "ऊष्मागतिकी का पहला नियम ऊष्मागतिक प्रणालियों के लिए ऊर्जा संरक्षण के नियम का एक रूप है।"
    },
    {
        "q": "A 50 kg object is moving with a velocity of 10 m/s. What is its momentum?",
        "q_hi": "50 kg की एक वस्तु 10 m/s के वेग से चल रही है। इसका संवेग क्या होगा?",
        "opts": ["5 kg·m/s", "60 kg·m/s", "500 kg·m/s", "0.2 kg·m/s"],
        "opts_hi": ["5 kg·m/s", "60 kg·m/s", "500 kg·m/s", "0.2 kg·m/s"],
        "ans": 2,
        "sol": "p = m × v = 50 × 10 = 500 kg·m/s.",
        "sol_hi": "p = m × v = 50 × 10 = 500 kg·m/s."
    },
    {
        "q": "Which of the following is the weakest fundamental force in nature?",
        "q_hi": "निम्नलिखित में से प्रकृति का सबसे दुर्बल मूलभूत बल कौन सा है?",
        "opts": ["Gravitational force", "Electromagnetic force", "Strong nuclear force", "Weak nuclear force"],
        "opts_hi": ["गुरुत्वाकर्षण बल", "विद्युत चुंबकीय बल", "प्रबल नाभिकीय बल", "दुर्बल नाभिकीय बल"],
        "ans": 0,
        "sol": "Gravitational force is the weakest fundamental force, though it has infinite range.",
        "sol_hi": "गुरुत्वाकर्षण बल सबसे दुर्बल मूलभूत बल है, हालांकि इसकी सीमा अनंत है।"
    },
    {
        "q": "An object of mass 20 kg is acted upon by a force of 60 N. What is its acceleration?",
        "q_hi": "20 kg द्रव्यमान की वस्तु पर 60 N का बल लगाया जाता है। इसका त्वरण क्या होगा?",
        "opts": ["2 m/s²", "3 m/s²", "4 m/s²", "1.5 m/s²"],
        "opts_hi": ["2 m/s²", "3 m/s²", "4 m/s²", "1.5 m/s²"],
        "ans": 1,
        "sol": "a = F/m = 60/20 = 3 m/s².",
        "sol_hi": "a = F/m = 60/20 = 3 m/s²."
    },
    {
        "q": "A cyclist leans inward while taking a turn on a curved road to:",
        "q_hi": "साइकिल सवार मोड़ लेते समय अंदर की ओर झुकता है ताकि:",
        "opts": ["Reduce air resistance", "Provide necessary centripetal force", "Increase speed", "Reduce friction"],
        "opts_hi": ["वायु प्रतिरोध कम करे", "आवश्यक अभिकेंद्रीय बल प्रदान करे", "गति बढ़ाए", "घर्षण कम करे"],
        "ans": 1,
        "sol": "Leaning inward provides the horizontal component of normal reaction needed as centripetal force for turning.",
        "sol_hi": "अंदर झुकने से अभिकेंद्रीय बल के रूप में आवश्यक अभिलंब प्रतिक्रिया का क्षैतिज घटक मिलता है।"
    },
    {
        "q": "How many dynes are equal to 1 Newton?",
        "q_hi": "1 न्यूटन कितने डाइन के बराबर होता है?",
        "opts": ["10⁵", "10³", "10⁶", "10⁷"],
        "opts_hi": ["10⁵", "10³", "10⁶", "10⁷"],
        "ans": 0,
        "sol": "1 Newton = 10⁵ dynes. Dyne is the CGS unit of force.",
        "sol_hi": "1 न्यूटन = 10⁵ डाइन। डाइन CGS प्रणाली में बल का मात्रक है।"
    },
    {
        "q": "Which of the following events demonstrates Newton's first law of motion?",
        "q_hi": "निम्नलिखित में से कौन सी घटना न्यूटन के गति के पहले नियम को प्रदर्शित करती है?",
        "opts": ["A rocket lifting off", "Collision of two cars", "Dust shaken from a carpet by beating it", "Bullet fired from a gun"],
        "opts_hi": ["रॉकेट का उड़ान भरना", "दो कारों की टक्कर", "कालीन को पीटने से धूल निकलना", "बंदूक से गोली चलना"],
        "ans": 2,
        "sol": "When a carpet is beaten, the carpet moves but the dust particles tend to remain at rest (inertia), separating from the carpet. This is Newton's first law.",
        "sol_hi": "जब कालीन को पीटा जाता है, कालीन चलता है लेकिन धूल के कण विराम में रहना चाहते हैं (जड़त्व), जिससे वे कालीन से अलग हो जाते हैं।"
    },
    {
        "q": "What happens to the kinetic energy of a body if its velocity is doubled?",
        "q_hi": "यदि किसी पिंड का वेग दोगुना कर दिया जाए तो उसकी गतिज ऊर्जा पर क्या प्रभाव पड़ेगा?",
        "opts": ["Doubled", "Halved", "Quadrupled", "Unchanged"],
        "opts_hi": ["दोगुनी", "आधी", "चार गुनी", "अपरिवर्तित"],
        "ans": 2,
        "sol": "KE = ½mv². If v is doubled, KE becomes ½m(2v)² = 4 × (½mv²) = 4 times original.",
        "sol_hi": "गतिज ऊर्जा = ½mv². यदि v दोगुना हो, तो KE = ½m(2v)² = 4 × (½mv²) = 4 गुना हो जाती है।"
    },
    {
        "q": "What is the dimensional formula of force?",
        "q_hi": "बल का विमीय सूत्र क्या है?",
        "opts": ["[M¹ L¹ T⁻¹]", "[M¹ L¹ T⁻²]", "[M¹ L² T⁻²]", "[M⁰ L¹ T⁻²]"],
        "opts_hi": ["[M¹ L¹ T⁻¹]", "[M¹ L¹ T⁻²]", "[M¹ L² T⁻²]", "[M⁰ L¹ T⁻²]"],
        "ans": 1,
        "sol": "Force = Mass × Acceleration = [M] × [LT⁻²] = [M¹ L¹ T⁻²].",
        "sol_hi": "बल = द्रव्यमान × त्वरण = [M] × [LT⁻²] = [M¹ L¹ T⁻²]."
    },
    {
        "q": "In the absence of external force, the total momentum of a system is conserved. This is:",
        "q_hi": "बाह्य बल की अनुपस्थिति में निकाय का कुल संवेग संरक्षित रहता है। यह है:",
        "opts": ["Law of conservation of momentum", "Newton's first law", "Newton's second law", "Law of conservation of energy"],
        "opts_hi": ["संवेग संरक्षण का नियम", "न्यूटन का पहला नियम", "न्यूटन का दूसरा नियम", "ऊर्जा संरक्षण का नियम"],
        "ans": 0,
        "sol": "The law of conservation of linear momentum follows from Newton's second and third laws.",
        "sol_hi": "रैखिक संवेग संरक्षण का नियम न्यूटन के दूसरे और तीसरे नियम से अनुसरण करता है।"
    },
    {
        "q": "If a bus suddenly takes a sharp turn, passengers tend to fall outward because of:",
        "q_hi": "यदि बस अचानक तीव्र मोड़ लेती है, तो यात्री बाहर की ओर गिरने लगते हैं:",
        "opts": ["Centripetal force", "Centrifugal force (inertia of direction)", "Frictional force", "Gravitational force"],
        "opts_hi": ["अभिकेंद्रीय बल", "अपकेंद्रीय बल (दिशा का जड़त्व)", "घर्षण बल", "गुरुत्वाकर्षण बल"],
        "ans": 1,
        "sol": "Passengers tend to continue in their straight-line motion (inertia of direction). From the bus frame, it appears as a centrifugal push outward.",
        "sol_hi": "यात्री अपनी सीधी रेखीय गति जारी रखना चाहते हैं (दिशा का जड़त्व)। बस के फ्रेम से, यह बाहर की ओर अपकेंद्रीय धक्का प्रतीत होता है।"
    }
]

# ----------------- MOCK TEST QUESTIONS (15 Qs) -----------------
mock_test_questions = [
    {
        "q": "Consider the following statements about friction:<br>1. Static friction is always greater than kinetic friction.<br>2. Rolling friction is greater than sliding friction.<br>Which of the statements given above is/are correct?",
        "q_hi": "घर्षण के बारे में निम्नलिखित कथनों पर विचार करें:<br>1. स्थैतिक घर्षण हमेशा गतिज घर्षण से अधिक होता है।<br>2. लोटनिक घर्षण सर्पी घर्षण से अधिक होता है।<br>उपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans": 0,
        "sol": "Statement 1 is correct (static > kinetic). Statement 2 is wrong because rolling friction is the smallest.",
        "sol_hi": "कथन 1 सही है (स्थैतिक > गतिज)। कथन 2 गलत है क्योंकि लोटनिक घर्षण सबसे छोटा होता है।"
    },
    {
        "q": "Match the following:<br>A. Newton's First Law &rarr; 1. F = ma<br>B. Newton's Second Law &rarr; 2. Action-Reaction<br>C. Newton's Third Law &rarr; 3. Law of Inertia",
        "q_hi": "सुमेलित करें:<br>A. न्यूटन का पहला नियम &rarr; 1. F = ma<br>B. न्यूटन का दूसरा नियम &rarr; 2. क्रिया-प्रतिक्रिया<br>C. न्यूटन का तीसरा नियम &rarr; 3. जड़त्व का नियम",
        "opts": ["A-1, B-2, C-3", "A-3, B-1, C-2", "A-2, B-3, C-1", "A-3, B-2, C-1"],
        "opts_hi": ["A-1, B-2, C-3", "A-3, B-1, C-2", "A-2, B-3, C-1", "A-3, B-2, C-1"],
        "ans": 1,
        "sol": "Newton's first law is Law of Inertia (A-3), second law is F=ma (B-1), third law is Action-Reaction (C-2).",
        "sol_hi": "न्यूटन का पहला नियम जड़त्व का नियम (A-3), दूसरा नियम F=ma (B-1), तीसरा नियम क्रिया-प्रतिक्रिया (C-2) है।"
    },
    {
        "q": "A 1000 kg car is moving at 20 m/s. It brakes and comes to rest in 5 seconds. What is the braking force?",
        "q_hi": "1000 kg की एक कार 20 m/s से चल रही है। यह ब्रेक लगाकर 5 सेकंड में रुक जाती है। ब्रेकिंग बल क्या है?",
        "opts": ["2000 N", "4000 N", "5000 N", "10000 N"],
        "opts_hi": ["2000 N", "4000 N", "5000 N", "10000 N"],
        "ans": 1,
        "sol": "a = (v-u)/t = (0-20)/5 = -4 m/s². F = ma = 1000 × 4 = 4000 N (magnitude).",
        "sol_hi": "a = (v-u)/t = (0-20)/5 = -4 m/s². F = ma = 1000 × 4 = 4000 N (परिमाण)।"
    },
    {
        "q": "In which of the following situations is there no net force on the body?",
        "q_hi": "निम्नलिखित में से किस स्थिति में पिंड पर कोई शुद्ध बल नहीं है?",
        "opts": ["A car accelerating on a straight road", "A satellite moving in a circular orbit", "A book lying on a table", "A ball falling freely"],
        "opts_hi": ["सीधी सड़क पर त्वरित होती कार", "वृत्ताकार कक्षा में चलता उपग्रह", "मेज पर रखी किताब", "मुक्त रूप से गिरती गेंद"],
        "ans": 2,
        "sol": "A book on a table has balanced forces (weight downward, normal reaction upward) — net force is zero.",
        "sol_hi": "मेज पर रखी किताब पर बल संतुलित हैं (भार नीचे, अभिलंब प्रतिक्रिया ऊपर) — शुद्ध बल शून्य है।"
    },
    {
        "q": "A 5 kg object accelerates from 2 m/s to 6 m/s in 2 seconds. What is the force applied?",
        "q_hi": "5 kg की वस्तु 2 सेकंड में 2 m/s से 6 m/s तक त्वरित होती है। लगाया गया बल क्या है?",
        "opts": ["5 N", "10 N", "15 N", "20 N"],
        "opts_hi": ["5 N", "10 N", "15 N", "20 N"],
        "ans": 1,
        "sol": "a = (6-2)/2 = 2 m/s². F = ma = 5 × 2 = 10 N.",
        "sol_hi": "a = (6-2)/2 = 2 m/s². F = ma = 5 × 2 = 10 N."
    },
    {
        "q": "Which of the following forces is responsible for a car being able to turn on a flat curved road?",
        "q_hi": "समतल घुमावदार सड़क पर कार के मुड़ने के लिए कौन सा बल जिम्मेदार है?",
        "opts": ["Engine force", "Frictional force between tires and road", "Gravitational force", "Air resistance"],
        "opts_hi": ["इंजन बल", "टायरों और सड़क के बीच घर्षण बल", "गुरुत्वाकर्षण बल", "वायु प्रतिरोध"],
        "ans": 1,
        "sol": "On a flat curved road, the centripetal force needed for turning is provided by the frictional force between the tires and the road.",
        "sol_hi": "समतल घुमावदार सड़क पर, मुड़ने के लिए आवश्यक अभिकेंद्रीय बल टायरों और सड़क के बीच घर्षण बल द्वारा प्रदान किया जाता है।"
    },
    {
        "q": "If an object is in a state of equilibrium, which of the following must be true?",
        "q_hi": "यदि कोई वस्तु संतुलन की अवस्था में है, तो निम्नलिखित में से क्या सत्य होना चाहिए?",
        "opts": ["It must be at rest", "It must be moving with constant velocity", "Net force on it is zero", "It must have zero momentum"],
        "opts_hi": ["वह विराम में होनी चाहिए", "वह स्थिर वेग से चल रही होनी चाहिए", "उस पर शुद्ध बल शून्य है", "उसका संवेग शून्य होना चाहिए"],
        "ans": 2,
        "sol": "Equilibrium means net force is zero. The body can be at rest OR moving with constant velocity.",
        "sol_hi": "संतुलन का अर्थ है शुद्ध बल शून्य। वस्तु विराम में या स्थिर वेग से चल रही हो सकती है।"
    },
    {
        "q": "Forces of 3 N and 4 N act at a point in perpendicular directions. What is the magnitude of the resultant force?",
        "q_hi": "3 N और 4 N के बल लंबवत दिशाओं में एक बिंदु पर कार्य करते हैं। परिणामी बल का परिमाण क्या है?",
        "opts": ["5 N", "6 N", "7 N", "12 N"],
        "opts_hi": ["5 N", "6 N", "7 N", "12 N"],
        "ans": 0,
        "sol": "Resultant = √(3² + 4²) = √(9 + 16) = √25 = 5 N (Pythagorean theorem).",
        "sol_hi": "परिणामी = √(3² + 4²) = √(9 + 16) = √25 = 5 N (पाइथागोरस प्रमेय)।"
    },
    {
        "q": "The tendency of an object to resist a change in its state of motion is known as:",
        "q_hi": "अपनी गति की अवस्था में परिवर्तन का विरोध करने की वस्तु की प्रवृत्ति कहलाती है:",
        "opts": ["Force", "Momentum", "Inertia", "Impulse"],
        "opts_hi": ["बल", "संवेग", "जड़त्व", "आवेग"],
        "ans": 2,
        "sol": "Inertia is the natural tendency of objects to resist changes in their state of motion.",
        "sol_hi": "जड़त्व वस्तुओं की अपनी गति की अवस्था में परिवर्तन का विरोध करने की स्वाभाविक प्रवृत्ति है।"
    },
    {
        "q": "When a batsman hits a cricket ball, in which direction should the ball go for maximum distance? (Ignoring air resistance)",
        "q_hi": "जब बल्लेबाज क्रिकेट गेंद को मारता है, तो अधिकतम दूरी के लिए गेंद किस दिशा में जानी चाहिए? (वायु प्रतिरोध को नजरअंदाज करते हुए)",
        "opts": ["30°", "45°", "60°", "90°"],
        "opts_hi": ["30°", "45°", "60°", "90°"],
        "ans": 1,
        "sol": "For maximum horizontal range in projectile motion, the angle of projection should be 45°.",
        "sol_hi": "प्रक्षेप्य गति में अधिकतम क्षैतिज परास के लिए प्रक्षेपण कोण 45° होना चाहिए।"
    },
    {
        "q": "Which of the following statements regarding Newton's law of gravitation is correct?",
        "q_hi": "न्यूटन के गुरुत्वाकर्षण नियम के बारे में निम्नलिखित में से कौन सा कथन सही है?",
        "opts": ["Gravitational force is repulsive", "Gravitational force is independent of the medium", "Gravitational force depends on the square of the distance", "Both B and C"],
        "opts_hi": ["गुरुत्वाकर्षण बल प्रतिकर्षी है", "गुरुत्वाकर्षण बल माध्यम से स्वतंत्र है", "गुरुत्वाकर्षण बल दूरी के वर्ग पर निर्भर करता है", "B और C दोनों"],
        "ans": 3,
        "sol": "Gravitational force is always attractive (not repulsive), independent of medium, and follows inverse square law.",
        "sol_hi": "गुरुत्वाकर्षण बल हमेशा आकर्षी है (प्रतिकर्षी नहीं), माध्यम से स्वतंत्र है, और व्युत्क्रम वर्ग नियम का पालन करता है।"
    },
    {
        "q": "A body weighs 600 N on Earth. What will be its weight on a planet where g = 4.9 m/s²?",
        "q_hi": "एक पिंड का पृथ्वी पर भार 600 N है। उस ग्रह पर इसका भार क्या होगा जहाँ g = 4.9 m/s²?",
        "opts": ["150 N", "300 N", "600 N", "1200 N"],
        "opts_hi": ["150 N", "300 N", "600 N", "1200 N"],
        "ans": 1,
        "sol": "Mass = W/g = 600/9.8 = 61.22 kg. New weight = m × g_new = 61.22 × 4.9 = 300 N.",
        "sol_hi": "द्रव्यमान = W/g = 600/9.8 = 61.22 kg. नया भार = m × g_नया = 61.22 × 4.9 = 300 N."
    },
    {
        "q": "During a collision between two objects, what is always conserved?",
        "q_hi": "दो वस्तुओं के बीच टक्कर के दौरान हमेशा क्या संरक्षित रहता है?",
        "opts": ["Kinetic energy only", "Linear momentum only", "Both kinetic energy and linear momentum", "Neither"],
        "opts_hi": ["केवल गतिज ऊर्जा", "केवल रैखिक संवेग", "गतिज ऊर्जा और रैखिक संवेग दोनों", "कोई नहीं"],
        "ans": 1,
        "sol": "In all types of collisions (elastic and inelastic), linear momentum is always conserved. Kinetic energy is conserved only in elastic collisions.",
        "sol_hi": "सभी प्रकार की टक्करों (प्रत्यास्थ और अप्रत्यास्थ) में, रैखिक संवेग हमेशा संरक्षित रहता है। गतिज ऊर्जा केवल प्रत्यास्थ टक्करों में संरक्षित होती है।"
    },
    {
        "q": "An astronaut inside a freely orbiting satellite feels weightlessness because:",
        "q_hi": "मुक्त रूप से परिक्रमा करने वाले उपग्रह के अंदर अंतरिक्ष यात्री भारहीनता महसूस करता है क्योंकि:",
        "opts": ["Gravity is zero in space", "The satellite is falling freely with the astronaut", "The astronaut is far from Earth", "The satellite's speed cancels gravity"],
        "opts_hi": ["अंतरिक्ष में गुरुत्व शून्य है", "उपग्रह अंतरिक्ष यात्री के साथ मुक्त रूप से गिर रहा है", "अंतरिक्ष यात्री पृथ्वी से दूर है", "उपग्रह की गति गुरुत्व को रद्द करती है"],
        "ans": 1,
        "sol": "Weightlessness occurs because both the satellite and the astronaut are in free fall toward Earth at the same rate, with no normal reaction force.",
        "sol_hi": "भारहीनता इसलिए होती है क्योंकि उपग्रह और अंतरिक्ष यात्री दोनों पृथ्वी की ओर समान दर से मुक्त रूप से गिर रहे हैं, कोई अभिलंब प्रतिक्रिया नहीं है।"
    },
    {
        "q": "A car of mass 1500 kg is moving on a circular track of radius 50 m at a speed of 10 m/s. What is the centripetal force required?",
        "q_hi": "1500 kg द्रव्यमान की कार 50 m त्रिज्या के वृत्ताकार ट्रैक पर 10 m/s की चाल से चल रही है। आवश्यक अभिकेंद्रीय बल क्या है?",
        "opts": ["1500 N", "3000 N", "4500 N", "6000 N"],
        "opts_hi": ["1500 N", "3000 N", "4500 N", "6000 N"],
        "ans": 1,
        "sol": "Fc = mv²/r = 1500 × (10)² / 50 = 1500 × 100 / 50 = 1500 × 2 = 3000 N.",
        "sol_hi": "Fc = mv²/r = 1500 × (10)² / 50 = 1500 × 100 / 50 = 1500 × 2 = 3000 N."
    }
]

# ----------------- BUILD FINAL JSON OBJECTS -----------------
def build_theory():
    return {
        "breadcrumbs": breadcrumbs_en,
        "hero": hero_en,
        "labels": labels_en,
        "timeline": timeline_en,
        "mnemonics": mnemonics_en,
        "flashcards": flashcards_en,
        "traps": traps_en,
        "deepDive": {"title": f"{TOPIC_DISPLAY} Core Study Notes", "description": "Thoroughly review the fundamental concepts, laws, forces, and conservation principles.", "sections": deep_dive_en}
    }

def build_practice():
    practice_obj = {"practiceQuestions": practice_questions, "mockTestQuestions": mock_test_questions}
    return practice_obj

def build_mastery():
    return {
        "sections": [
            {
                "title": "1. Newton's Laws of Motion",
                "masteryZone": [
                    {"type": "MCQ", "q": "A passenger in a bus is thrown forward when the bus suddenly stops. Which law explains this?", "opts": ["Newton's First Law (Inertia)", "Newton's Second Law (F=ma)", "Newton's Third Law (Action-Reaction)", "Law of Gravitation"], "ans": 0, "sol": "Newton's First Law (Law of Inertia) — the passenger's body continues moving forward due to inertia even after the bus stops."},
                    {"type": "MCQ", "q": "What is the SI unit of Force?", "opts": ["Joule", "Newton", "Pascal", "Watt"], "ans": 1, "sol": "Newton (N) is the SI unit of force. 1 N = 1 kg·m/s²."},
                    {"type": "True/False", "q": "True or False: Newton's first law is also called the Law of Acceleration.", "ans": False, "sol": "False. Newton's first law is the Law of Inertia. The second law (F = ma) is the Law of Acceleration."},
                    {"type": "MCQ", "q": "When a bullet is fired from a gun, the gun recoils backward. This is an example of:", "opts": ["First Law", "Second Law", "Third Law", "Law of Conservation of Energy"], "ans": 2, "sol": "Newton's Third Law — the gun exerts forward force on bullet (action), bullet exerts equal backward force on gun (reaction), causing recoil."}
                ]
            },
            {
                "title": "2. Types of Forces",
                "masteryZone": [
                    {"type": "MCQ", "q": "Which force is responsible for the motion of planets around the Sun?", "opts": ["Centripetal force", "Centrifugal force", "Gravitational force", "Magnetic force"], "ans": 2, "sol": "Gravitational force between the Sun and planets provides the necessary centripetal force for orbital motion."},
                    {"type": "MCQ", "q": "Which of the following is NOT a contact force?", "opts": ["Friction", "Normal reaction", "Tension", "Gravitational force"], "ans": 3, "sol": "Gravitational force is a non-contact (field) force. Friction, normal reaction, and tension require physical contact between objects."},
                    {"type": "MCQ", "q": "What is the formula for centripetal force?", "opts": ["F = mv²/r", "F = mvr", "F = mr/v²", "F = v²/mr"], "ans": 0, "sol": "Centripetal force F = mv²/r, where m = mass, v = velocity, r = radius of circular path."},
                    {"type": "One-Liner", "q": "What is the SI unit of force?", "sol": "Newton (N). 1 N = 1 kg·m/s²."}
                ]
            },
            {
                "title": "3. Friction",
                "masteryZone": [
                    {"type": "MCQ", "q": "Which type of friction has the LARGEST magnitude?", "opts": ["Static friction", "Kinetic friction", "Rolling friction", "Fluid friction"], "ans": 0, "sol": "Static friction is the strongest — it must overcome interlocking of surface irregularities to start motion."},
                    {"type": "MCQ", "q": "Which type of friction has the SMALLEST magnitude?", "opts": ["Static friction", "Kinetic friction", "Rolling friction", "Fluid friction"], "ans": 2, "sol": "Rolling friction is the smallest. This is why wheels and ball bearings are used to reduce friction."},
                    {"type": "True/False", "q": "True or False: The coefficient of friction depends on the area of contact between surfaces.", "ans": False, "sol": "False. The coefficient of friction depends only on the nature (material and roughness) of the surfaces, NOT on the area of contact."},
                    {"type": "True/False", "q": "True or False: Lubrication reduces friction by creating a thin layer between surfaces.", "ans": True, "sol": "True. Oils and greases create a thin film that separates surfaces, converting dry friction into fluid friction which is much smaller."}
                ]
            },
            {
                "title": "4. Gravity & Gravitation",
                "masteryZone": [
                    {"type": "MCQ", "q": "The value of acceleration due to gravity (g) at Earth's surface is approximately:", "opts": ["8.9 m/s²", "9.8 m/s²", "10.8 m/s²", "7.8 m/s²"], "ans": 1, "sol": "Standard value of g at Earth's surface = 9.8 m/s²."},
                    {"type": "MCQ", "q": "What happens to the value of 'g' as we go above the Earth's surface?", "opts": ["Increases", "Decreases", "Remains constant", "First increases then decreases"], "ans": 1, "sol": "g decreases with altitude: g' = g(1 - 2h/R) where h = height above surface and R = Earth's radius."},
                    {"type": "MCQ", "q": "The value of g at the center of Earth is:", "opts": ["9.8 m/s²", "4.9 m/s²", "0 m/s²", "Infinite"], "ans": 2, "sol": "At Earth's center, depth d = R, so g' = g(1 - R/R) = 0 m/s²."},
                    {"type": "MCQ", "q": "Escape velocity of Earth is approximately:", "opts": ["7.2 km/s", "9.8 km/s", "11.2 km/s", "15 km/s"], "ans": 2, "sol": "Escape velocity ve = √(2gR) ≈ 11.2 km/s — minimum speed needed to overcome Earth's gravity."}
                ]
            },
            {
                "title": "5. Motion Equations & Conservation Laws",
                "masteryZone": [
                    {"type": "MCQ", "q": "Which equation relates final velocity (v), initial velocity (u), acceleration (a), and time (t)?", "opts": ["v = u + at", "s = ut + ½at²", "v² = u² + 2as", "s = (v+u)t/2"], "ans": 0, "sol": "v = u + at — the first equation of motion for constant acceleration."},
                    {"type": "MCQ", "q": "In an elastic collision, which of the following is conserved?", "opts": ["Only momentum", "Only kinetic energy", "Both momentum and kinetic energy", "Neither"], "ans": 2, "sol": "In elastic collisions, both momentum and kinetic energy are conserved. In inelastic collisions, only momentum is conserved."},
                    {"type": "MCQ", "q": "If the mass of a body is doubled and velocity is halved, momentum becomes:", "opts": ["Doubled", "Halved", "Unchanged", "Quadrupled"], "ans": 2, "sol": "p = m × v. New p = (2m) × (v/2) = mv = same. Momentum remains unchanged."},
                    {"type": "True/False", "q": "True or False: According to the law of conservation of linear momentum, the total momentum of an isolated system remains constant if no external force acts.", "ans": True, "sol": "True. In the absence of external forces, total linear momentum is always conserved."}
                ]
            }
        ]
    }


def build_theory_hi():
    return {
        "breadcrumbs": breadcrumbs_hi,
        "hero": hero_hi,
        "labels": labels_hi,
        "timeline": timeline_hi,
        "mnemonics": mnemonics_hi,
        "flashcards": flashcards_hi,
        "traps": traps_hi,
        "deepDive": {"title": f"{TOPIC_DISPLAY_HI} के मुख्य अध्ययन नोट्स", "description": "मौलिक अवधारणाओं, नियमों, बलों और संरक्षण सिद्धांतों की गहन समीक्षा करें।", "sections": deep_dive_hi}
    }

def build_practice_hi():
    practice_obj = {
        "practiceQuestions": [
            {"q": pq["q_hi"], "opts": pq["opts_hi"], "ans": pq["ans"], "sol": pq["sol_hi"]} for pq in practice_questions
        ],
        "mockTestQuestions": [
            {"q": mtq["q_hi"], "opts": mtq["opts_hi"], "ans": mtq["ans"], "sol": mtq["sol_hi"]} for mtq in mock_test_questions
        ]
    }
    return practice_obj

def build_mastery_hi():
    return {
        "sections": [
            {
                "title": "1. न्यूटन के गति के नियम",
                "masteryZone": [
                    {"type": "MCQ", "q": "बस अचानक रुकने पर यात्री आगे की ओर झुक जाता है। यह किस नियम द्वारा समझाया जाता है?", "opts": ["न्यूटन का पहला नियम (जड़त्व)", "न्यूटन का दूसरा नियम (F=ma)", "न्यूटन का तीसरा नियम (क्रिया-प्रतिक्रिया)", "गुरुत्वाकर्षण का नियम"], "ans": 0, "sol": "न्यूटन का पहला नियम (जड़त्व का नियम) — बस रुकने के बाद भी यात्री का शरीर जड़त्व के कारण आगे बढ़ता रहता है।"},
                    {"type": "MCQ", "q": "बल का SI मात्रक क्या है?", "opts": ["जूल", "न्यूटन", "पास्कल", "वाट"], "ans": 1, "sol": "न्यूटन (N) बल का SI मात्रक है। 1 N = 1 kg·m/s²."},
                    {"type": "True/False", "q": "सही या गलत: न्यूटन का पहला नियम त्वरण का नियम भी कहलाता है।", "ans": False, "sol": "गलत। न्यूटन का पहला नियम जड़त्व का नियम है। दूसरा नियम (F = ma) त्वरण का नियम है।"},
                    {"type": "MCQ", "q": "बंदूक से गोली चलाने पर बंदूक पीछे हटती है। यह किसका उदाहरण है?", "opts": ["पहला नियम", "दूसरा नियम", "तीसरा नियम", "ऊर्जा संरक्षण का नियम"], "ans": 2, "sol": "न्यूटन का तीसरा नियम — बंदूक गोली पर आगे का बल लगाती है (क्रिया), गोली बंदूक पर बराबर पीछे का बल लगाती है (प्रतिक्रिया)।"}
                ]
            },
            {
                "title": "2. बलों के प्रकार",
                "masteryZone": [
                    {"type": "MCQ", "q": "सूर्य के चारों ओर ग्रहों की गति के लिए कौन सा बल जिम्मेदार है?", "opts": ["अभिकेंद्रीय बल", "अपकेंद्रीय बल", "गुरुत्वाकर्षण बल", "चुंबकीय बल"], "ans": 2, "sol": "सूर्य और ग्रहों के बीच गुरुत्वाकर्षण बल कक्षीय गति के लिए आवश्यक अभिकेंद्रीय बल प्रदान करता है।"},
                    {"type": "MCQ", "q": "निम्नलिखित में से कौन संपर्क बल नहीं है?", "opts": ["घर्षण", "अभिलंब प्रतिक्रिया", "तनाव", "गुरुत्वाकर्षण बल"], "ans": 3, "sol": "गुरुत्वाकर्षण बल एक असंपर्क (क्षेत्र) बल है। घर्षण, अभिलंब प्रतिक्रिया और तनाव में वस्तुओं के बीच भौतिक संपर्क आवश्यक है।"},
                    {"type": "MCQ", "q": "अभिकेंद्रीय बल का सूत्र क्या है?", "opts": ["F = mv²/r", "F = mvr", "F = mr/v²", "F = v²/mr"], "ans": 0, "sol": "अभिकेंद्रीय बल F = mv²/r, जहाँ m = द्रव्यमान, v = वेग, r = वृत्तीय पथ की त्रिज्या।"},
                    {"type": "One-Liner", "q": "बल का SI मात्रक क्या है?", "sol": "न्यूटन (N)। 1 N = 1 kg·m/s²।"}
                ]
            },
            {
                "title": "3. घर्षण",
                "masteryZone": [
                    {"type": "MCQ", "q": "किस घर्षण का परिमाण सबसे अधिक होता है?", "opts": ["स्थैतिक घर्षण", "गतिज घर्षण", "लोटनिक घर्षण", "तरल घर्षण"], "ans": 0, "sol": "स्थैतिक घर्षण सबसे प्रबल होता है — इसे गति शुरू करने के लिए सतह की अनियमितताओं को पार करना होता है।"},
                    {"type": "MCQ", "q": "किस घर्षण का परिमाण सबसे छोटा होता है?", "opts": ["स्थैतिक घर्षण", "गतिज घर्षण", "लोटनिक घर्षण", "तरल घर्षण"], "ans": 2, "sol": "लोटनिक घर्षण सबसे छोटा होता है। यही कारण है कि पहियों और बॉल बेयरिंग का उपयोग घर्षण कम करने के लिए किया जाता है।"},
                    {"type": "True/False", "q": "सही या गलत: घर्षण गुणांक सतहों के बीच संपर्क क्षेत्रफल पर निर्भर करता है।", "ans": False, "sol": "गलत। घर्षण गुणांक केवल सतहों की प्रकृति (सामग्री और खुरदरापन) पर निर्भर करता है, क्षेत्रफल पर नहीं।"},
                    {"type": "True/False", "q": "सही या गलत: स्नेहन (तेल/ग्रीस) सतहों के बीच एक पतली परत बनाकर घर्षण कम करता है।", "ans": True, "sol": "सही। तेल और ग्रीस सतहों को अलग करने वाली एक पतली फिल्म बनाते हैं, जो शुष्क घर्षण को बहुत छोटे तरल घर्षण में बदल देता है।"}
                ]
            },
            {
                "title": "4. गुरुत्वाकर्षण",
                "masteryZone": [
                    {"type": "MCQ", "q": "पृथ्वी की सतह पर गुरुत्वीय त्वरण (g) का मान लगभग कितना होता है?", "opts": ["8.9 m/s²", "9.8 m/s²", "10.8 m/s²", "7.8 m/s²"], "ans": 1, "sol": "पृथ्वी की सतह पर g का मानक मान = 9.8 m/s²."},
                    {"type": "MCQ", "q": "पृथ्वी की सतह से ऊपर जाने पर 'g' के मान पर क्या प्रभाव पड़ता है?", "opts": ["बढ़ता है", "घटता है", "स्थिर रहता है", "पहले बढ़ता है फिर घटता है"], "ans": 1, "sol": "ऊंचाई के साथ g घटता है: g' = g(1 - 2h/R) जहाँ h = ऊंचाई, R = पृथ्वी की त्रिज्या।"},
                    {"type": "MCQ", "q": "पृथ्वी के केंद्र पर g का मान क्या है?", "opts": ["9.8 m/s²", "4.9 m/s²", "0 m/s²", "अनंत"], "ans": 2, "sol": "पृथ्वी के केंद्र पर, गहराई d = R, अतः g' = g(1 - R/R) = 0 m/s²."},
                    {"type": "MCQ", "q": "पृथ्वी का पलायन वेग लगभग कितना है?", "opts": ["7.2 km/s", "9.8 km/s", "11.2 km/s", "15 km/s"], "ans": 2, "sol": "पलायन वेग ve = √(2gR) ≈ 11.2 km/s — पृथ्वी के गुरुत्वाकर्षण से बचने के लिए न्यूनतम गति।"}
                ]
            },
            {
                "title": "5. गति के समीकरण और संरक्षण नियम",
                "masteryZone": [
                    {"type": "MCQ", "q": "कौन सा समीकरण अंतिम वेग (v), प्रारंभिक वेग (u), त्वरण (a) और समय (t) में संबंध बताता है?", "opts": ["v = u + at", "s = ut + ½at²", "v² = u² + 2as", "s = (v+u)t/2"], "ans": 0, "sol": "v = u + at — स्थिर त्वरण के लिए गति का पहला समीकरण।"},
                    {"type": "MCQ", "q": "प्रत्यास्थ टक्कर में निम्नलिखित में से क्या संरक्षित रहता है?", "opts": ["केवल संवेग", "केवल गतिज ऊर्जा", "संवेग और गतिज ऊर्जा दोनों", "कोई नहीं"], "ans": 2, "sol": "प्रत्यास्थ टक्करों में संवेग और गतिज ऊर्जा दोनों संरक्षित रहते हैं। अप्रत्यास्थ टक्करों में केवल संवेग संरक्षित होता है।"},
                    {"type": "MCQ", "q": "यदि किसी पिंड का द्रव्यमान दोगुना और वेग आधा कर दिया जाए, तो संवेग होगा:", "opts": ["दोगुना", "आधा", "अपरिवर्तित", "चार गुना"], "ans": 2, "sol": "p = m × v. नया p = (2m) × (v/2) = mv = समान। संवेग अपरिवर्तित रहता है।"},
                    {"type": "True/False", "q": "सही या गलत: रैखिक संवेग संरक्षण नियम के अनुसार, बाह्य बल की अनुपस्थिति में एक पृथक निकाय का कुल संवेग स्थिर रहता है।", "ans": True, "sol": "सही। बाह्य बलों की अनुपस्थिति में, कुल रैखिक संवेग हमेशा संरक्षित रहता है।"}
                ]
            }
        ]
    }


# ----------------- FILE GENERATION -----------------
def write_json(filepath, data):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Written: {filepath}")

# Write English files
write_json(os.path.join(BASE_DIR, "theory.json"), build_theory())
write_json(os.path.join(BASE_DIR, "practice.json"), build_practice())
write_json(os.path.join(BASE_DIR, "mastery.json"), build_mastery())

# Write Hindi files
write_json(os.path.join(HI_DIR, "theory.json"), build_theory_hi())
write_json(os.path.join(HI_DIR, "practice.json"), build_practice_hi())
write_json(os.path.join(HI_DIR, "mastery.json"), build_mastery_hi())