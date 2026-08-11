from pathlib import Path
import re
import html

BASE = Path(__file__).resolve().parent

CH1_FOLDER = "chapter-1-exploration-entering-world-of-secondary-science"
CH7_FOLDER = "chapter-7-work-energy-and-simple-machines"

CH1 = BASE / CH1_FOLDER
CH7 = BASE / CH7_FOLDER

TITLE = "Work, Energy, and Simple Machines"
CHAPTER = 7

TEMPLATES = {
    "concepts": CH1 / "concepts" / "index.html",
    "ncert-exercises": CH1 / "ncert-exercises" / "index.html",
    "revision-notes": CH1 / "revision-notes" / "index.html",
}


# ================================================================
# IMPORTANT ARCHITECTURE
# ================================================================
#
# FULL NCERT CHAPTER 7 HIERARCHY
#
# 7.1 Work Done by a Constant Force
#   7.1.1 When is work done equal to zero?
#   7.1.2 Positive and negative work done
#
# 7.2 The Work-Energy Theorem
#
# 7.3 Forms of Energy
#
# 7.4 Mechanical Energy
#   7.4.1 Kinetic energy
#   7.4.2 Potential energy
#       General potential energy
#       Elastic potential energy
#       Magnetic potential energy
#       Electrostatic potential energy
#       Gravitational potential energy
#       Activity 7.1
#   7.4.3 Conservation of mechanical energy
#       Activity 7.2
#
# 7.5 Power
#
# 7.6 Simple Machines
#   7.6.1 Pulley
#   7.6.2 Inclined plane
#       Activity 7.3
#   7.6.3 Lever
#       Activity 7.4
#       Activity 7.5
#       Lever classes I, II, III
#
# CLICK-TO-REVEAL RULE
# --------------------
# ONLY:
#   - NCERT Examples
#   - NCERT Pause and Ponder
# may contain hidden answers.
#
# NCERT Exercises:
#   QUESTIONS ONLY.
#   No answer button.
#   No answer text embedded in the page.
#
# Concept Check:
#   prompt only.
#
# ================================================================


def esc(value):
    return html.escape(str(value), quote=True)


CSS = r"""
<style id="sj-ch7-v2-ui">
.sj-ch7-page {
    --ink:#172033;
    --muted:#64748b;
    --border:#e5e7eb;
    --soft:#f8fafc;
    --red:#e74c3c;
    --orange:#f39c12;
    --green:#059669;
    --blue:#0284c7;
    color:var(--ink);
}

.sj-ch7-page .ch7-section-card,
.sj-ch7-page .ch7-concept-card,
.sj-ch7-page .ch7-exercise-card {
    background:#fff;
    border:1px solid var(--border);
    border-radius:18px;
    margin:0 0 22px;
    overflow:hidden;
    box-shadow:0 7px 22px rgba(15,23,42,.05);
}

.sj-ch7-page .ch7-section-card {
    padding:22px;
}

.sj-ch7-page .ch7-concept-header {
    display:flex;
    gap:14px;
    align-items:flex-start;
    padding:19px 21px;
    border-bottom:1px solid var(--border);
    background:linear-gradient(180deg,#fff,#fafafa);
}

.sj-ch7-page .ch7-number {
    flex:0 0 auto;
    min-width:44px;
    height:44px;
    display:grid;
    place-items:center;
    border-radius:12px;
    background:#fff4f2;
    color:var(--red);
    font-weight:900;
    font-size:.9rem;
}

.sj-ch7-page .ch7-kicker {
    display:block;
    margin:0 0 4px;
    color:var(--red);
    font-size:.67rem;
    font-weight:900;
    letter-spacing:.08em;
    text-transform:uppercase;
}

.sj-ch7-page h2 {
    line-height:1.3;
}

.sj-ch7-page .ch7-concept-header h2 {
    margin:0;
    font-size:1.28rem;
}

.sj-ch7-page .ch7-body {
    padding:21px;
}

.sj-ch7-page .ch7-subsection {
    margin:26px 0 10px;
    font-size:1.05rem;
    font-weight:850;
    color:#263247;
}

.sj-ch7-page .ch7-formula {
    margin:15px 0;
    padding:15px 18px;
    border:1px solid #fed7aa;
    border-left:4px solid var(--orange);
    border-radius:12px;
    background:#fffaf2;
    text-align:center;
    overflow-x:auto;
}

.sj-ch7-page .ch7-example,
.sj-ch7-page .ch7-pause {
    margin:20px 0;
    border-radius:15px;
    overflow:hidden;
}

.sj-ch7-page .ch7-example {
    border:1px solid #bfdbfe;
    background:#f8fbff;
}

.sj-ch7-page .ch7-pause {
    border:1px solid #bbf7d0;
    background:#f0fdf4;
}

.sj-ch7-page .ch7-box-head {
    padding:12px 16px;
    font-weight:900;
    border-bottom:1px solid;
}

.sj-ch7-page .ch7-example .ch7-box-head {
    color:#0369a1;
    background:#eff6ff;
    border-color:#bfdbfe;
}

.sj-ch7-page .ch7-pause .ch7-box-head {
    color:#047857;
    background:#ecfdf5;
    border-color:#bbf7d0;
}

.sj-ch7-page .ch7-box-body {
    padding:16px;
}

.sj-ch7-page details.ch7-reveal {
    margin-top:14px;
    border-top:1px dashed #cbd5e1;
}

.sj-ch7-page details.ch7-reveal summary {
    cursor:pointer;
    padding:13px 0 4px;
    color:var(--blue);
    font-weight:900;
    list-style:none;
}

.sj-ch7-page details.ch7-reveal summary::-webkit-details-marker {
    display:none;
}

.sj-ch7-page details.ch7-reveal summary::before {
    content:"▸";
    display:inline-block;
    margin-right:8px;
    transition:.15s ease;
}

.sj-ch7-page details.ch7-reveal[open] summary::before {
    transform:rotate(90deg);
}

.sj-ch7-page .ch7-answer {
    margin-top:10px;
    padding:15px;
    border:1px solid #dbeafe;
    border-radius:12px;
    background:#fff;
}

.sj-ch7-page .ch7-answer-label {
    margin-bottom:8px;
    color:#0f172a;
    font-size:.78rem;
    font-weight:900;
    text-transform:uppercase;
    letter-spacing:.06em;
}

.sj-ch7-page .ch7-concept-check {
    margin:20px 0 0;
    padding:15px 16px;
    border:1px solid #e2e8f0;
    border-radius:13px;
    background:#f8fafc;
}

.sj-ch7-page .ch7-check-label {
    margin-bottom:7px;
    color:#334155;
    font-size:.78rem;
    font-weight:900;
    text-transform:uppercase;
    letter-spacing:.06em;
}

.sj-ch7-page .ch7-exercise-card {
    padding:0;
}

.sj-ch7-page .ch7-question-header {
    display:flex;
    justify-content:space-between;
    gap:14px;
    padding:17px 19px 12px;
    border-bottom:1px solid #eef2f7;
}

.sj-ch7-page .ch7-question-number {
    color:var(--red);
    font-weight:900;
}

.sj-ch7-page .ch7-question-type {
    margin-left:7px;
    color:#64748b;
    font-size:.72rem;
    font-weight:800;
    text-transform:uppercase;
    letter-spacing:.06em;
}

.sj-ch7-page .ch7-marks {
    flex:0 0 auto;
    align-self:flex-start;
    padding:5px 8px;
    border:1px solid #fecaca;
    border-radius:8px;
    background:#fff5f5;
    color:#b91c1c;
    font-size:.73rem;
    font-weight:900;
    white-space:nowrap;
}

.sj-ch7-page .ch7-question-body {
    padding:16px 19px 19px;
}

.sj-ch7-page .ch7-question-body > p:first-child {
    margin-top:0;
}

.sj-ch7-page .ch7-options {
    margin:12px 0;
    padding:13px 16px 13px 37px;
    border:1px solid #e2e8f0;
    border-radius:12px;
    background:#f8fafc;
}

.sj-ch7-page .ch7-table-wrap {
    overflow-x:auto;
    margin:15px 0;
}

.sj-ch7-page table.ch7-table {
    width:100%;
    min-width:560px;
    border-collapse:collapse;
}

.sj-ch7-page table.ch7-table th,
.sj-ch7-page table.ch7-table td {
    padding:10px 12px;
    border:1px solid #e2e8f0;
    text-align:left;
}

.sj-ch7-page table.ch7-table th {
    background:#f8fafc;
    font-weight:900;
}

.sj-ch7-page mjx-container {
    max-width:100%;
    overflow-x:auto;
    overflow-y:hidden;
}

@media(max-width:700px){
    .sj-ch7-page .ch7-concept-header,
    .sj-ch7-page .ch7-body,
    .sj-ch7-page .ch7-section-card {
        padding:16px;
    }

    .sj-ch7-page .ch7-question-header {
        display:block;
        padding:15px 16px 11px;
    }

    .sj-ch7-page .ch7-marks {
        display:inline-block;
        margin-top:9px;
    }

    .sj-ch7-page .ch7-question-body {
        padding:15px 16px 16px;
    }
}
</style>
"""

MATHJAX = r"""
<script>
window.MathJax = {
  tex: {
    inlineMath: [['\\(', '\\)']],
    displayMath: [['\\[', '\\]']]
  },
  svg: { fontCache: 'global' }
};
</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
"""


# ================================================================
# FULL CONCEPT DATA
# ================================================================

CONCEPTS = [
{
"no":"7.1",
"title":"Work Done by a Constant Force",
"body":r"""
<p>
Work is said to be done on an object when a force acting on it produces
displacement in the direction of the force. For a constant force, work
depends on the force and the displacement in the direction of that force.
</p>

<div class="ch7-formula">
\[
W=F\times s
\]
</div>

<p>
The scientific definition is important: while describing work, always
identify <strong>the force/agency doing the work</strong> and
<strong>the object on which the work is done</strong>.
</p>

<p>
The SI unit of work is the <strong>joule (J)</strong):
\[
1\,\mathrm{J}=1\,\mathrm{N}\times1\,\mathrm{m}.
\]
</p>

<p>
For a force–displacement graph, work done is represented by the
<strong>area under the graph</strong>. This remains useful even when the
force is not constant.
</p>

<div class="ch7-subsection">NCERT Example 7.1</div>
<div class="ch7-example">
<div class="ch7-box-head">Example 7.1 · Positive and Negative Work</div>
<div class="ch7-box-body">
<p>
While exercising, a girl lifts a dumbbell and slowly lowers it down.
Identify when the girl does positive work on the dumbbell and when she does
negative work on it.
</p>
<details class="ch7-reveal">
<summary>Show Answer</summary>
<div class="ch7-answer">
<div class="ch7-answer-label">NCERT Answer</div>
<p>
While moving the dumbbell up, the applied force and displacement are in the
same direction, so the work done by the girl is positive. While lowering it,
the force applied by the girl to hold it is opposite to the displacement, so
her work on the dumbbell is negative.
</p>
</div>
</details>
</div>
</div>

<div class="ch7-subsection">NCERT Example 7.2</div>
<div class="ch7-example">
<div class="ch7-box-head">Example 7.2 · Numerical</div>
<div class="ch7-box-body">
<p>
A goalkeeper's hand moved back by \(15\,\mathrm{cm}\) while stopping a ball
with a force of \(200\,\mathrm{N}\). How much work did the goalkeeper do on
the ball?
</p>
<details class="ch7-reveal">
<summary>Show Answer</summary>
<div class="ch7-answer">
<div class="ch7-answer-label">NCERT Answer</div>
<p>
The force is opposite to the ball's displacement, so the displacement in the
direction of the force is \(-0.15\,\mathrm{m}\).
</p>
<div class="ch7-formula">
\[
W=200(-0.15)=-30\,\mathrm{J}
\]
</div>
</div>
</details>
</div>
</div>

<div class="ch7-concept-check">
<div class="ch7-check-label">Concept Check</div>
<p>
Three identical bags are lifted through the same height. Explain why the
work done is three times the work needed for one bag.
</p>
</div>
"""
},
{
"no":"7.1.1",
"title":"When Is Work Done Equal to Zero?",
"body":r"""
<p>
From \(W=Fs\), work is zero in several important situations.
</p>
<ul>
<li><strong>No force:</strong> \(F=0\).</li>
<li><strong>No displacement:</strong> \(s=0\), even if a force is applied.</li>
<li>
<strong>Force perpendicular to displacement:</strong> there is no
displacement in the direction of the force.
</li>
</ul>

<p>
For example, pushing a rigid wall does not produce displacement of the wall,
so no work is done on the wall in the scientific sense. A person may still
feel tired because the body uses internal energy while maintaining force.
</p>

<p>
Similarly, when a girl carries a box horizontally, the upward force she
applies to balance the weight is perpendicular to the horizontal displacement,
so that force does zero work on the box.
</p>

<div class="ch7-pause">
<div class="ch7-box-head">NCERT · Pause and Ponder</div>
<div class="ch7-box-body">
<ol>
<li>
A weightlifter is holding a barbell steady. Is she doing any work on the
barbell while holding it steady?
</li>
<li>
Is the work done by friction on a stack of coins travelling on a rough
surface positive, negative or zero?
</li>
</ol>
<details class="ch7-reveal">
<summary>Show Answer</summary>
<div class="ch7-answer">
<div class="ch7-answer-label">Answer</div>
<p>
For the stationary barbell, displacement is zero, so the work done on the
barbell by the weightlifter is zero.
</p>
<p>
Friction opposes the motion of the coins, so its work is negative.
</p>
</div>
</details>
</div>
</div>

<div class="ch7-concept-check">
<div class="ch7-check-label">Concept Check</div>
<p>
A student pushes a wall with a large force but the wall does not move.
Distinguish between the student's physical effort and scientific work done
on the wall.
</p>
</div>
"""
},
{
"no":"7.1.2",
"title":"Positive and Negative Work Done",
"body":r"""
<p>
Work can be positive or negative depending on the relative directions of
force and displacement. Work itself has no direction; its sign indicates
the energy effect of the force.
</p>

<ul>
<li><strong>Positive work:</strong> force and displacement are in the same direction.</li>
<li><strong>Negative work:</strong> force and displacement are in opposite directions.</li>
</ul>

<p>
Pushing a wheelchair forward gives positive work by the applied force.
Stopping a moving ball involves negative work by the stopping force.
</p>

<p>
Remember that different forces acting during the same event can do different
amounts and signs of work.
</p>

<div class="ch7-concept-check">
<div class="ch7-check-label">Concept Check</div>
<p>
During upward motion of a thrown ball, compare the signs of the work done by
gravity and by an upward applied force.
</p>
</div>
"""
},
{
"no":"7.2",
"title":"The Work–Energy Theorem",
"body":r"""
<p>
An object having the capacity to do work is said to possess
<strong>energy</strong>. When positive work is done on an object, it gains
energy. That energy can subsequently be transferred to another object.
</p>

<div class="ch7-formula">
\[
\text{Work done on an object}=\text{change in its energy}
\]
</div>

<p>
This is the <strong>work–energy theorem</strong>. It also applies to a system
of objects and remains useful even when the forces involved are not constant.
The SI unit of energy is the joule (J).
</p>

<p>
Energy can be transferred by mechanical work, heat, radiation, electric
circuits, sound waves and nuclear processes. Mechanical work is therefore
one important mode of energy transfer, not the only one.
</p>

<div class="ch7-example">
<div class="ch7-box-head">Example 7.3 · Carrom Collision</div>
<div class="ch7-box-body">
<p>
In a game of carrom, a player plays a shot to pocket the black coin.
Identify who does work and describe the changes in energy at each collision.
</p>
<details class="ch7-reveal">
<summary>Show Answer</summary>
<div class="ch7-answer">
<div class="ch7-answer-label">NCERT Answer</div>
<p>
The moving striker does positive work on the white coin, increasing its
energy. The white coin does negative work on the striker, decreasing its
energy. The white coin then does positive work on the black coin, increasing
its energy, while the black coin does negative work on the white coin.
</p>
</div>
</details>
</div>
</div>

<div class="ch7-pause">
<div class="ch7-box-head">NCERT · Pause and Ponder</div>
<div class="ch7-box-body">
<p>
When you pedal a bicycle on a flat road, your muscles supply energy. In what
forms does this muscular energy appear as you ride?
</p>
<details class="ch7-reveal">
<summary>Show Answer</summary>
<div class="ch7-answer">
<div class="ch7-answer-label">Answer</div>
<p>
Chemical energy stored in the body is converted into mechanical energy of
the moving bicycle and rider, with some energy also appearing as thermal
energy and other losses such as sound.
</p>
</div>
</details>
</div>
</div>

<div class="ch7-concept-check">
<div class="ch7-check-label">Concept Check</div>
<p>
If a force does negative work on a moving object, explain what happens to
the object's kinetic energy when that force is responsible for slowing it.
</p>
</div>
"""
},
{
"no":"7.3",
"title":"Forms of Energy",
"body":r"""
<p>
Energy is the capacity to do work and can exist in many forms. The chapter
introduces mechanical, thermal, light, sound, nuclear, chemical and
electrical energy.
</p>

<div class="ch7-table-wrap">
<table class="ch7-table">
<thead><tr><th>Form</th><th>Idea / Example</th></tr></thead>
<tbody>
<tr><td>Mechanical</td><td>Energy due to motion or position.</td></tr>
<tr><td>Thermal</td><td>Energy associated with temperature and heating.</td></tr>
<tr><td>Light</td><td>Energy that enables vision.</td></tr>
<tr><td>Sound</td><td>Energy associated with vibrations.</td></tr>
<tr><td>Nuclear</td><td>Energy stored in atomic nuclei.</td></tr>
<tr><td>Chemical</td><td>Energy stored in chemical bonds, such as in food and fuels.</td></tr>
<tr><td>Electrical</td><td>Energy associated with electric charges and circuits.</td></tr>
</tbody>
</table>
</div>

<p>
Energy can be transformed from one form into another. For example, electrical
energy can become light and thermal energy in a bulb; chemical energy in food
can power muscles and become mechanical energy; and mechanical energy in a
ringing bell becomes sound energy.
</p>

<div class="ch7-concept-check">
<div class="ch7-check-label">Concept Check</div>
<p>
Identify the principal energy transformation in a watermill and in a solar
panel.
</p>
</div>
"""
},
{
"no":"7.4",
"title":"Mechanical Energy",
"body":r"""
<p>
Mechanical energy is the energy an object possesses due to its
<strong>motion or position</strong>. In this chapter it is studied through
kinetic energy and potential energy.
</p>

<div class="ch7-formula">
\[
E_{\text{mechanical}}=K+U
\]
</div>

<p>
Kinetic energy is associated with motion, while potential energy is associated
with deformation or the relative positions of objects in a system.
</p>

<div class="ch7-concept-check">
<div class="ch7-check-label">Concept Check</div>
<p>
A moving object is brought to rest by friction. Which part of its mechanical
energy changes first, and where does the transferred energy go?
</p>
</div>
"""
},
{
"no":"7.4.1",
"title":"Kinetic Energy",
"body":r"""
<p>
The energy possessed by an object due to its motion is called
<strong>kinetic energy</strong>. Starting from the work–energy theorem and
using the kinematic relation for constant acceleration gives the general
work expression
</p>

<div class="ch7-formula">
\[
W=\frac12m(v^2-u^2)
\]
</div>

<p>
For an object starting from rest, \(u=0\), so its kinetic energy is
</p>

<div class="ch7-formula">
\[
K=\frac12mv^2
\]
</div>

<p>
Kinetic energy is a scalar quantity and its SI unit is joule. Positive work
that increases speed increases kinetic energy; negative work that decreases
speed decreases kinetic energy.
</p>

<div class="ch7-example">
<div class="ch7-box-head">Example 7.4 · Velocity Scaling</div>
<div class="ch7-box-body">
<p>
If the velocity of a vehicle doubles in magnitude, what will its kinetic
energy be compared to its original value?
</p>
<details class="ch7-reveal">
<summary>Show Answer</summary>
<div class="ch7-answer">
<div class="ch7-answer-label">NCERT Answer</div>
<div class="ch7-formula">
\[
K_1=\frac12mv^2,\qquad
K_2=\frac12m(2v)^2=4K_1
\]
</div>
<p>The new kinetic energy is four times the original.</p>
</div>
</details>
</div>
</div>

<div class="ch7-example">
<div class="ch7-box-head">Example 7.5 · Cricket Ball</div>
<div class="ch7-box-body">
<p>
A cricket ball of approximate mass \(0.2\,\mathrm{kg}\) is bowled at about
\(154.8\,\mathrm{km\,h^{-1}}\). Calculate its kinetic energy.
</p>
<details class="ch7-reveal">
<summary>Show Answer</summary>
<div class="ch7-answer">
<div class="ch7-answer-label">NCERT Answer</div>
<p>
\(154.8\,\mathrm{km\,h^{-1}}=43\,\mathrm{m\,s^{-1}}\).
</p>
<div class="ch7-formula">
\[
K=\frac12(0.2)(43)^2\approx184.9\,\mathrm{J}
\]
</div>
</div>
</details>
</div>
</div>

<div class="ch7-example">
<div class="ch7-box-head">Example 7.6 · Jet Aircraft</div>
<div class="ch7-box-body">
<p>
A \(15000\,\mathrm{kg}\) jet is stopped within \(100\,\mathrm{m}\) by a
wire exerting an approximately constant backward force of \(367500\,\mathrm{N}\).
Find its velocity just before the wire catches it.
</p>
<details class="ch7-reveal">
<summary>Show Answer</summary>
<div class="ch7-answer">
<div class="ch7-answer-label">NCERT Answer</div>
<p>
The wire does negative work:
\[
W=367500(-100)=-36,750,000\,\mathrm{J}.
\]
By the work–energy theorem this equals the change in kinetic energy:
\[
-36,750,000=0-\frac12(15000)v^2.
\]
Hence
\[
v=70\,\mathrm{m\,s^{-1}}.
\]
</p>
</div>
</details>
</div>
</div>

<div class="ch7-pause">
<div class="ch7-box-head">NCERT · Pause and Ponder</div>
<div class="ch7-box-body">
<ol>
<li>
Two objects A and B of masses \(m\) and \(4m\) have the same kinetic energy.
What is the ratio of their speeds?
</li>
<li>
Does the kinetic energy of an object moving with constant velocity change
with its position?
</li>
</ol>
<details class="ch7-reveal">
<summary>Show Answer</summary>
<div class="ch7-answer">
<div class="ch7-answer-label">Answer</div>
<p>
Since \(K=\frac12mv^2\), equal kinetic energies give
\(mv^2=\text{constant}\). Thus
\[
v_A:v_B=2:1.
\]
For constant velocity and constant mass, kinetic energy remains unchanged
regardless of position.
</p>
</div>
</details>
</div>
</div>

<div class="ch7-concept-check">
<div class="ch7-check-label">Concept Check</div>
<p>
If the mass is doubled and the speed is halved, compare the new kinetic
energy with the original kinetic energy.
</p>
</div>
"""
},
{
"no":"7.4.2",
"title":"Potential Energy",
"body":r"""
<p>
Potential energy is the energy stored by an object because of its
<strong>deformation</strong> or by a system because of the
<strong>relative positions</strong> of its objects.
</p>

<p>
A stretched rubber band, a bent bow and a compressed spring can store energy
because work has been done to deform them. A system of separated magnets or
electric charges can store energy because of their relative positions.
Similarly, the Earth–ball system stores gravitational potential energy when
the ball is raised.
</p>

<div class="ch7-subsection">Gravitational Potential Energy</div>

<p>
Near the Earth's surface, potential energy usually refers to gravitational
potential energy. Taking the ground as the zero reference level, raising an
object of mass \(m\) through height \(h\) requires work against gravity:
</p>

<div class="ch7-formula">
\[
W=mgh
\qquad\Rightarrow\qquad
U=mgh
\]
</div>

<p>
The expression \(U=mgh\) is valid near the Earth's surface where \(g\) can be
treated as approximately constant.
</p>

<div class="ch7-subsection">Activity 7.1 · Investigating Potential Energy</div>
<p>
Raise a heavy ball above loose sand and drop it. Repeat from a greater height.
The deeper depression produced from the greater height shows that the ball
has more potential energy at greater height.
</p>

<div class="ch7-example">
<div class="ch7-box-head">Example 7.7 · Gravitational Potential Energy</div>
<div class="ch7-box-body">
<p>
A fielder throws a \(200\,\mathrm{g}\) cricket ball about \(10\,\mathrm{m}\)
above the ground. How much potential energy does it have at maximum height?
Take \(g=10\,\mathrm{m\,s^{-2}}\).
</p>
<details class="ch7-reveal">
<summary>Show Answer</summary>
<div class="ch7-answer">
<div class="ch7-answer-label">NCERT Answer</div>
<div class="ch7-formula">
\[
U=mgh=(0.2)(10)(10)=20\,\mathrm{J}
\]
</div>
</div>
</details>
</div>
</div>

<div class="ch7-pause">
<div class="ch7-box-head">NCERT · Pause and Ponder</div>
<div class="ch7-box-body">
<p>
Does the potential energy of an object near the Earth's surface change if it
moves with constant velocity horizontally? What if it is gradually raised
vertically?
</p>
<details class="ch7-reveal">
<summary>Show Answer</summary>
<div class="ch7-answer">
<div class="ch7-answer-label">Answer</div>
<p>
Horizontal motion at constant height does not change gravitational potential
energy. Raising the object vertically increases its gravitational potential
energy because its height increases.
</p>
</div>
</details>
</div>
</div>

<div class="ch7-concept-check">
<div class="ch7-check-label">Concept Check</div>
<p>
Explain why gravitational potential energy belongs naturally to the
Earth–object system rather than being treated as a property of the object
alone.
</p>
</div>
"""
},
{
"no":"7.4.3",
"title":"Conservation of Mechanical Energy",
"body":r"""
<p>
The sum of kinetic energy and potential energy is called mechanical energy.
For an object moving under gravity, if no other external forces act and
energy losses such as friction are absent, mechanical energy remains constant.
</p>

<div class="ch7-formula">
\[
E_{\text{mechanical}}=K+U=\text{constant}
\]
</div>

<p>
During free fall, potential energy decreases while kinetic energy increases
by an equal amount. Thus, potential energy is converted into kinetic energy
while the total mechanical energy remains \(mgh\) for an object released from
height \(h\).
</p>

<div class="ch7-subsection">Activity 7.2 · Simple Pendulum</div>
<p>
At one extreme position the bob has mainly potential energy. At the lowest
point, potential energy is minimum and kinetic energy is maximum. At the
other extreme, kinetic energy again becomes zero and potential energy is
restored. In a real pendulum, friction and air resistance gradually convert
mechanical energy into other forms, so the oscillations die out.
</p>

<div class="ch7-example">
<div class="ch7-box-head">Example 7.8 · Child on a Slide</div>
<div class="ch7-box-body">
<p>
What will be the magnitude of velocity of a child on reaching the bottom of
a frictionless slide of height \(h\)?
</p>
<details class="ch7-reveal">
<summary>Show Answer</summary>
<div class="ch7-answer">
<div class="ch7-answer-label">NCERT Answer</div>
<div class="ch7-formula">
\[
mgh=\frac12mv^2
\Rightarrow
v=\sqrt{2gh}
\]
</div>
<p>
The result depends on height \(h\), not on the mass of the child or the shape
of the frictionless slide.
</p>
</div>
</details>
</div>
</div>

<div class="ch7-example">
<div class="ch7-box-head">Example 7.9 · Escape Ramp</div>
<div class="ch7-box-body">
<p>
A \(10000\,\mathrm{kg}\) truck moving at \(72\,\mathrm{km\,h^{-1}}\) enters
a \(30^\circ\) escape ramp. Sand exerts \(50000\,\mathrm{N}\) opposite to
motion. Find the minimum ramp length needed to stop it. Take
\(g=10\,\mathrm{m\,s^{-2}}\).
</p>
<details class="ch7-reveal">
<summary>Show Answer</summary>
<div class="ch7-answer">
<div class="ch7-answer-label">NCERT Answer</div>
<p>
\(72\,\mathrm{km\,h^{-1}}=20\,\mathrm{m\,s^{-1}}\), so the initial kinetic
energy is
\[
K_i=\frac12(10000)(20)^2=2,000,000\,\mathrm{J}.
\]
For a \(30^\circ\) ramp, height gained is \(d/2\), giving final gravitational
potential energy \(50000d\). Sand does work \(-50000d\).
</p>
<div class="ch7-formula">
\[
-50000d=50000d-2000000
\]
\[
d=20\,\mathrm{m}
\]
</div>
</div>
</details>
</div>
</div>

<div class="ch7-pause">
<div class="ch7-box-head">NCERT · Pause and Ponder</div>
<div class="ch7-box-body">
<ol>
<li>
For the situation in Fig. 7.19, calculate the mechanical energy of the ball
just before it hits the ground and show that it is \(mgh\).
</li>
<li>
For the roller-coaster exhibit in Fig. 7.22, describe how kinetic and
potential energy change at A, B and C. Why are later points such as C, D and E
usually lower because of frictional energy loss?
</li>
</ol>
<details class="ch7-reveal">
<summary>Show Answer</summary>
<div class="ch7-answer">
<div class="ch7-answer-label">Answer</div>
<p>
Just before reaching the ground, the potential energy is zero if the ground
is chosen as the zero level, while the kinetic energy has increased by the
same amount by which potential energy decreased. Therefore the total
mechanical energy is still \(mgh\).
</p>
<p>
At higher points the ball has more potential and less kinetic energy. As it
moves downward, potential energy decreases and kinetic energy increases.
Friction and air resistance convert part of the mechanical energy into
thermal energy and sound, so later maximum heights are generally lower.
</p>
</div>
</details>
</div>
</div>

<div class="ch7-concept-check">
<div class="ch7-check-label">Concept Check</div>
<p>
What additional condition is required for mechanical energy to remain
constant when an object is moving under gravity?
</p>
</div>
"""
},
{
"no":"7.5",
"title":"Power",
"body":r"""
<p>
Power describes how quickly work is done. Doing the same work in a shorter
time requires greater power.
</p>

<div class="ch7-formula">
\[
P=\frac{W}{t}
\]
</div>

<p>
The SI unit of power is the watt:
\[
1\,\mathrm{W}=1\,\mathrm{J\,s^{-1}}.
\]
Another unit used for engines and pumps is horsepower:
\[
1\,\mathrm{hp}=746\,\mathrm{W}.
\]
</p>

<div class="ch7-example">
<div class="ch7-box-head">Example 7.10 · Weightlifter</div>
<div class="ch7-box-body">
<p>
A weightlifter lifts a \(75\,\mathrm{kg}\) mass by \(2\,\mathrm{m}\) in
\(5\,\mathrm{s}\). How much power is required? Take \(g=10\,\mathrm{m\,s^{-2}}\).
</p>
<details class="ch7-reveal">
<summary>Show Answer</summary>
<div class="ch7-answer">
<div class="ch7-answer-label">NCERT Answer</div>
\[
W=mgh=(75)(10)(2)=1500\,\mathrm{J}
\]
\[
P=\frac{1500}{5}=300\,\mathrm{W}
\]
</div>
</details>
</div>
</div>

<div class="ch7-example">
<div class="ch7-box-head">Example 7.11 · Car Engine</div>
<div class="ch7-box-body">
<p>
A \(1000\,\mathrm{kg}\) car starts from rest and reaches
\(72\,\mathrm{km\,h^{-1}}\) in \(10\,\mathrm{s}\). Calculate the power
required to achieve this start.
</p>
<details class="ch7-reveal">
<summary>Show Answer</summary>
<div class="ch7-answer">
<div class="ch7-answer-label">NCERT Answer</div>
<p>
\(72\,\mathrm{km\,h^{-1}}=20\,\mathrm{m\,s^{-1}}\).
</p>
<div class="ch7-formula">
\[
W=\Delta K=\frac12(1000)(20)^2=200000\,\mathrm{J}
\]
\[
P=\frac{200000}{10}=20000\,\mathrm{W}
\]
</div>
</div>
</details>
</div>
</div>

<div class="ch7-concept-check">
<div class="ch7-check-label">Concept Check</div>
<p>
Two students do the same work, but one takes half the time. Compare their
powers.
</p>
</div>
"""
},
{
"no":"7.6",
"title":"Simple Machines",
"body":r"""
<p>
Simple machines make tasks easier by changing the magnitude or direction of
the force that needs to be applied. They do <strong>not</strong> reduce the
total work required when friction is ignored.
</p>

<p>
The force applied to a machine is called the <strong>effort</strong>, and
the force that must be overcome is called the <strong>load</strong>.
Mechanical advantage is
</p>

<div class="ch7-formula">
\[
\mathrm{MA}=\frac{\text{Load}}{\text{Effort}}
\]
</div>

<p>
This chapter studies three simple machines: pulley, inclined plane and lever.
</p>
"""
},
{
"no":"7.6.1",
"title":"Pulley",
"body":r"""
<p>
A pulley is a wheel with a groove that guides a rope. A fixed pulley does not
reduce the magnitude of effort; it changes the direction of the effort.
For an ideal fixed pulley:
</p>

<div class="ch7-formula">
\[
\mathrm{MA}=1
\]
</div>

<p>
A movable pulley or a system of pulleys can have mechanical advantage greater
than 1, allowing a heavier load to be lifted with smaller effort. Such systems
are used in devices such as elevators and cranes.
</p>

<div class="ch7-subsection">Key comparison</div>
<ul>
<li>Fixed pulley → mainly changes direction of effort.</li>
<li>Movable/system pulley → can provide mechanical advantage greater than 1.</li>
<li>Ideal machine → does not create energy.</li>
</ul>

<div class="ch7-concept-check">
<div class="ch7-check-label">Concept Check</div>
<p>
Why is pulling downward with a fixed pulley more convenient than directly
lifting the same load upward, even though the ideal mechanical advantage is 1?
</p>
</div>
"""
},
{
"no":"7.6.2",
"title":"Inclined Plane",
"body":r"""
<p>
An inclined plane allows a heavy load to be moved to a higher or lower level
with a smaller effort applied over a larger distance.
</p>

<div class="ch7-subsection">Activity 7.3</div>
<p>
Compare lifting a cart vertically with pulling it along an inclined plank.
Then reduce the steepness of the plank. The required force decreases as the
plank becomes less steep, but the distance over which the force acts increases.
</p>

<p>
For a load \(mg\), effort \(F'\), height \(h\) and inclined-plane length \(L\),
ignoring friction:
</p>

<div class="ch7-formula">
\[
F'L=mgh
\]
\[
\mathrm{MA}
=\frac{mg}{F'}
=\frac{L}{h}
\]
</div>

<p>
Since \(L>h\), the ideal mechanical advantage is greater than 1. Increasing
the length of the ramp for the same height reduces the effort further.
</p>

<div class="ch7-example">
<div class="ch7-box-head">Example 7.12 · Inclined Ramp</div>
<div class="ch7-box-body">
<p>
A ramp raises an object over a \(30\,\mathrm{cm}\) step and has a width of
\(40\,\mathrm{cm}\). Find its mechanical advantage.
</p>
<details class="ch7-reveal">
<summary>Show Answer</summary>
<div class="ch7-answer">
<div class="ch7-answer-label">NCERT Answer</div>
<p>
The ramp length is \(50\,\mathrm{cm}\) by the right-angled triangle property.
</p>
<div class="ch7-formula">
\[
\mathrm{MA}=\frac{L}{h}
=\frac{50}{30}
\approx1.67
\]
</div>
</div>
</details>
</div>
</div>

<div class="ch7-pause">
<div class="ch7-box-head">NCERT · Pause and Ponder</div>
<div class="ch7-box-body">
<ol>
<li>Why are roads on hills built to wind around in gentle slopes?</li>
<li>Why is an inclined ladder easier to climb than a vertical ladder to reach the same floor?</li>
</ol>
<details class="ch7-reveal">
<summary>Show Answer</summary>
<div class="ch7-answer">
<div class="ch7-answer-label">Answer</div>
<p>
A longer, gentler slope reduces the effort required by increasing the
distance over which the force is applied. The same principle makes an
inclined ladder easier than a vertical climb.
</p>
</div>
</details>
</div>
</div>

<div class="ch7-concept-check">
<div class="ch7-check-label">Concept Check</div>
<p>
If the ramp length is doubled while the height remains the same, what happens
to its ideal mechanical advantage and the required effort?
</p>
</div>
"""
},
{
"no":"7.6.3",
"title":"Lever",
"body":r"""
<p>
A lever is a rigid bar that can rotate about a fixed point called the
<strong>fulcrum</strong>. Its three main parts are fulcrum, load and effort.
The distance of the load from the fulcrum is the <strong>load arm</strong>;
the distance of the effort from the fulcrum is the <strong>effort arm</strong>.
</p>

<div class="ch7-formula">
\[
F_1d_1=F_2d_2
\]
\[
\mathrm{MA}
=
\frac{\text{effort arm}}{\text{load arm}}
\]
</div>

<p>
Increasing the effort arm allows a smaller effort to produce a larger force
on the load. The effort moves through a larger distance, so the lever does
not reduce total work when friction is ignored.
</p>

<div class="ch7-subsection">Activity 7.4 · Lever Investigation</div>
<p>
Using a scale over a pencil as a fulcrum, place a heavy stapler near the
fulcrum and lighter objects farther away. A small effort can lift a larger
load when the geometry gives sufficient mechanical advantage.
</p>

<div class="ch7-subsection">Activity 7.5 · Beam Balance</div>
<p>
A beam balance demonstrates the lever principle. Balance occurs when
</p>

<div class="ch7-formula">
\[
\text{effort}\times\text{effort arm}
=
\text{load}\times\text{load arm}
\]
</div>

<div class="ch7-example">
<div class="ch7-box-head">Example 7.13 · Seesaw</div>
<div class="ch7-box-body">
<p>
For a seesaw with fulcrum at C, \(AC=EC=2\,\mathrm{m}\) and
\(BC=DC=1\,\mathrm{m}\), where should children of masses \(15\,\mathrm{kg}\)
and \(30\,\mathrm{kg}\) sit to balance it?
</p>
<details class="ch7-reveal">
<summary>Show Answer</summary>
<div class="ch7-answer">
<div class="ch7-answer-label">NCERT Answer</div>
<p>
Let the \(15\,\mathrm{kg}\) child sit at A. If the \(30\,\mathrm{kg}\) child
is at distance \(L\):
</p>
<div class="ch7-formula">
\[
15\times2=30\times L
\Rightarrow L=1\,\mathrm{m}
\]
</div>
<p>
Therefore the \(30\,\mathrm{kg}\) child should sit at D.</p>
</div>
</details>
</div>
</div>

<div class="ch7-subsection">Classes of Levers</div>
<div class="ch7-table-wrap">
<table class="ch7-table">
<thead>
<tr><th>Class</th><th>Arrangement</th><th>Examples</th></tr>
</thead>
<tbody>
<tr>
<td>Class I</td>
<td>Fulcrum between load and effort</td>
<td>Tongs, scissors, crowbar, pliers, balance scale, seesaw</td>
</tr>
<tr>
<td>Class II</td>
<td>Load between fulcrum and effort</td>
<td>Lemon squeezer, wheelbarrow, bottle opener</td>
</tr>
<tr>
<td>Class III</td>
<td>Effort between fulcrum and load</td>
<td>Tongs, tweezers, broom, hammer, oar</td>
</tr>
</tbody>
</table>
</div>

<div class="ch7-pause">
<div class="ch7-box-head">NCERT · Pause and Ponder</div>
<div class="ch7-box-body">
<ol>
<li>Why is it easier to open the lid of a can using a spoon?</li>
<li>Why do you push an object closer to the scissors' fulcrum when cutting a hard object?</li>
<li>
Why do real machines eventually slow down and stop? Explain in terms of work
and energy.
</li>
</ol>
<details class="ch7-reveal">
<summary>Show Answer</summary>
<div class="ch7-answer">
<div class="ch7-answer-label">Answer</div>
<p>
A spoon can provide a long effective effort arm, so a relatively small effort
produces a larger turning effect on the lid.
</p>
<p>
Moving a hard object closer to the fulcrum reduces the load arm. For the same
load, this reduces the effort needed.
</p>
<p>
Real machines experience friction and other energy losses. Mechanical energy
is transferred mainly into thermal energy and sometimes sound, so the machine
cannot continue doing useful work indefinitely without an energy input.
</p>
</div>
</details>
</div>
</div>

<div class="ch7-concept-check">
<div class="ch7-check-label">Concept Check</div>
<p>
A lever has an effort arm twice the load arm. What ideal mechanical advantage
does it provide?
</p>
</div>
"""
},
]


# ================================================================
# NCERT EXERCISES — QUESTIONS ONLY
# ================================================================

EXERCISES = [
(1,"True / False",r"""
<p>State whether the following statements are <strong>True or False</strong>.</p>
<ol>
<li>Work is said to be done when a force is applied, even if the object does not move.</li>
<li>Lifting a bucket vertically upward results in positive work done on the bucket.</li>
<li>The SI unit for both work and energy is joule (J).</li>
<li>A motionless stretched rubber band has kinetic energy.</li>
<li>Energy can change from one form to another.</li>
</ol>
"""),
(2,"Fill in the Blanks",r"""
<p>Fill in the blanks.</p>
<ol>
<li>Work done = ______ × ______ (in the direction of force).</li>
<li>1 joule of work is done when a force of ______ newton displaces an object by 1 metre in the direction of the force.</li>
<li>The expression for kinetic energy of a body of mass \(m\) and velocity \(v\) is ______.</li>
<li>The potential energy of an object of mass \(m\) at a small height \(h\) from the Earth's surface is ______.</li>
<li>Power is defined as the ______ at which work is done.</li>
</ol>
"""),
(3,"Multiple Correct",r"""
<p>When a ball thrown upwards reaches its highest point, tick the correct statement(s).</p>
<ol class="ch7-options">
<li>The force acting on the ball is zero.</li>
<li>The acceleration of the ball is zero.</li>
<li>Its kinetic energy is zero.</li>
<li>Its potential energy is maximum.</li>
</ol>
"""),
(4,"Energy Transformation",r"""
<p>Identify the energy transformation in each situation:
truck moving uphill; unwinding of a watch spring; photosynthesis in green leaves;
water flowing from a dam; burning of a matchstick; explosion of a fire cracker;
speaking into a microphone; a glowing electric bulb; a solar panel.</p>
"""),
(5,"Potential Energy",r"""
<p>
A student is slowly lifted straight up in an elevator from the ground level
to the top floor and later climbs the staircase to the same top. Given
\(h=72.5\,\mathrm{m}\), \(g=10\,\mathrm{m\,s^{-2}}\), \(m=50\,\mathrm{kg}\):
</p>
<ol>
<li>Find the gain in potential energy when lifted straight up.</li>
<li>Find the gain when the student climbs the stairs.</li>
<li>What do you conclude about dependence of potential energy on path?</li>
</ol>
"""),
(6,"Energy and Power",r"""
<p>
A crane lifts a mass \(m\) to the 10th floor in a certain time and then raises
the same mass to the 20th floor in double the time. How much more energy and
power are required? Assume equal floor heights.
</p>
"""),
(7,"Power Application",r"""
<p>
Which factors determine the energy required to raise a flag from the ground
to the top of a tall flagpole using a pulley? Does raising it slowly or
quickly change the work done? If the speed is doubled, how does the power
requirement change? Explain.
</p>
"""),
(8,"Kinetic Energy Ratio",r"""
<p>
A man of mass \(60\,\mathrm{kg}\) rides a scooter of mass \(100\,\mathrm{kg}\).
His \(40\,\mathrm{kg}\) son later joins him. If the scooter reaches the same
speed on both days in the same time and fuel supplies all the energy without
other losses, find the ratio of fuel used.
</p>
"""),
(9,"Lever / Seesaw Diagram",r"""
<p>
On a seesaw, an adult weighs twice as much as a child, yet the seesaw is
balanced. Draw a figure showing the distances from the fulcrum where the
child and adult should sit.
</p>
"""),
(10,"Work by Gravity",r"""
<p>
A \(2\,\mathrm{kg}\) ball is thrown upward at \(20\,\mathrm{m\,s^{-1}}\).
</p>
<ol>
<li>Identify the sign of work done by gravity during upward and downward motion.</li>
<li>If it reaches \(19.4\,\mathrm{m}\), find the work done by air resistance. Take \(g=10\,\mathrm{m\,s^{-2}}\).</li>
</ol>
"""),
(11,"Variable Force Graph",r"""
<p>
A \(10.0\,\mathrm{kg}\) block moves on a horizontal floor with negligible
friction. A variable force acts in the direction of motion from \(0\) to
\(4\,\mathrm{m}\) as shown in Fig. 7.37. If the block has kinetic energy
\(180\,\mathrm{J}\) at \(0\,\mathrm{m}\), find its speed at \(0\,\mathrm{m}\)
and \(4\,\mathrm{m}\). Does it have negative acceleration in any portion?
</p>
"""),
(12,"Moon Gravity",r"""
<p>
The Moon's surface gravity is about \(1/6\) of Earth's. An astronaut can throw
a ball to \(8\,\mathrm{m}\) on Earth. How high will the same upward velocity
take it on the Moon?
</p>
"""),
(13,"Braking Graph",r"""
<p>
A \(1000\,\mathrm{kg}\) car moves at constant speed and then brakes to stop,
as represented in Fig. 7.38.
</p>
<ol>
<li>Describe the motion between A and B.</li>
<li>Calculate the kinetic energy at A.</li>
<li>State the work done by the brakes between B and C.</li>
<li>What does the kinetic energy transform into?</li>
</ol>
"""),
(14,"Potential Energy Graph",r"""
<p>
The potential-energy/displacement graph of a \(0.5\,\mathrm{kg}\) ball on a
frictionless track is shown in Fig. 7.39. At O, its velocity is
\(0\,\mathrm{m\,s^{-1}}\) and potential energy is \(30\,\mathrm{J}\).
Calculate the velocity at P, Q and R.
</p>
"""),
(15,"Energy Dissipation",r"""
<p>
A \(1.5\,\mathrm{kg}\) coconut falls from a \(10\,\mathrm{m}\) tree onto wet
sand and comes to rest while making a depression.
</p>
<ol>
<li>Calculate its velocity just before impact.</li>
<li>
If the average resistive force is \(3000\,\mathrm{N}\) and all its energy is
used to create the depression, calculate the depression depth. Take
\(g=10\,\mathrm{m\,s^{-2}}\).
</li>
</ol>
"""),
]


def render_concept(c):
    return f"""
<section class="ch7-concept-card" id="section-{c['no'].replace('.','-')}">
<div class="ch7-concept-header">
<div class="ch7-number">{c['no']}</div>
<div>
<span class="ch7-kicker">NCERT Concept</span>
<h2>{c['title']}</h2>
</div>
</div>
<div class="ch7-body">
{c['body']}
</div>
</section>
"""


def render_exercise(q):
    no, typ, body = q
    return f"""
<article class="ch7-exercise-card" id="question-{no}">
<div class="ch7-question-header">
<div>
<span class="ch7-question-number">Q{no}</span>
<span class="ch7-question-type">{esc(typ)}</span>
</div>
<span class="ch7-marks">NCERT</span>
</div>
<div class="ch7-question-body">
{body}
</div>
</article>
"""


REVISION = r"""
<div class="sj-ch7-page">

<section class="ch7-section-card">
<span class="ch7-kicker">Master Revision</span>
<h2>Work, Energy, and Simple Machines — Complete Revision</h2>
<p>
This is a <strong>full revision chapter</strong>, not a compressed formula sheet.
It covers the complete chapter concepts, definitions, relationships, activities,
formulae, mnemonics, shortcuts, comparisons, common traps and numerical
approaches.
</p>
</section>

<section class="ch7-section-card">
<span class="ch7-kicker">01 · Concept Map</span>
<h2>Chapter at a Glance</h2>
<div class="ch7-table-wrap">
<table class="ch7-table">
<thead><tr><th>Concept</th><th>Core idea</th><th>Must remember</th></tr></thead>
<tbody>
<tr><td>Work</td><td>Force produces displacement in its direction</td><td>\(W=Fs\)</td></tr>
<tr><td>Zero work</td><td>No displacement / no force / perpendicular force</td><td>Check displacement in force direction</td></tr>
<tr><td>Positive work</td><td>Force and displacement same direction</td><td>Usually increases kinetic energy</td></tr>
<tr><td>Negative work</td><td>Force opposes displacement</td><td>Usually removes kinetic energy</td></tr>
<tr><td>Energy</td><td>Capacity to do work</td><td>SI unit: joule</td></tr>
<tr><td>Work–energy theorem</td><td>Work changes energy</td><td>\(W=\Delta E\)</td></tr>
<tr><td>Kinetic energy</td><td>Energy due to motion</td><td>\(K=\frac12mv^2\)</td></tr>
<tr><td>Potential energy</td><td>Energy due to deformation or relative position</td><td>Near Earth: \(U=mgh\)</td></tr>
<tr><td>Mechanical energy</td><td>Kinetic + potential energy</td><td>\(E_m=K+U\)</td></tr>
<tr><td>Conservation</td><td>Mechanical energy remains constant under ideal stated conditions</td><td>\(K+U=\text{constant}\)</td></tr>
<tr><td>Power</td><td>Rate of doing work</td><td>\(P=W/t\)</td></tr>
<tr><td>Simple machine</td><td>Changes force magnitude/direction, not ideal total work</td><td>\(\mathrm{MA}=L/E\)</td></tr>
<tr><td>Fixed pulley</td><td>Changes direction of effort</td><td>Ideal MA \(=1\)</td></tr>
<tr><td>Inclined plane</td><td>Smaller force over larger distance</td><td>\(\mathrm{MA}=L/h\)</td></tr>
<tr><td>Lever</td><td>Rotates about fulcrum</td><td>\(F_ed_e=F_ld_l\)</td></tr>
</tbody>
</table>
</div>
</section>

<section class="ch7-section-card">
<span class="ch7-kicker">02 · Work</span>
<h2>Work — Complete Revision</h2>
<div class="ch7-formula">\[W=F\times s\]</div>
<p>
Work is done when a force acting on an object produces displacement in the
direction of that force. \(F\) is force and \(s\) is displacement in the
direction of the force.
</p>
<ul>
<li>SI unit: joule (J).</li>
<li>\(1\,\mathrm{J}=1\,\mathrm{N\,m}\).</li>
<li>Work is a scalar quantity; its sign describes the energy effect.</li>
</ul>
<div class="ch7-subsection">The F–D–D Work Test</div>
<p><strong>Mnemonic: “F–D–D” → Force → Displacement → Direction.</strong></p>
<ol>
<li>Is a force acting?</li>
<li>Is there displacement?</li>
<li>Is there displacement in the direction of that particular force?</li>
</ol>
<div class="ch7-subsection">When Is Work Zero?</div>
<ul>
<li>No force: \(F=0\).</li>
<li>No displacement: \(s=0\).</li>
<li>Force is perpendicular to displacement.</li>
</ul>
<p>
<strong>Classic trap:</strong> A person can feel tired while holding a heavy
object stationary, but the mechanical work done on that stationary object is
zero because its displacement is zero.
</p>
<div class="ch7-subsection">Positive, Negative and Zero Work</div>
<div class="ch7-table-wrap">
<table class="ch7-table">
<thead><tr><th>Type</th><th>Direction</th><th>Typical effect</th></tr></thead>
<tbody>
<tr><td>Positive</td><td>Force and displacement same direction</td><td>Energy transferred to object</td></tr>
<tr><td>Negative</td><td>Force opposite displacement</td><td>Energy removed from motion</td></tr>
<tr><td>Zero</td><td>No displacement along force</td><td>No work by that force</td></tr>
</tbody>
</table>
</div>
<p><strong>Mnemonic: “Same = +, Against = −, Across = 0.”</strong></p>
<div class="ch7-subsection">Variable Force / Graph Trick</div>
<p>
When force varies with displacement, work is represented by the area under
the force–displacement graph:
\[
W=\text{area under the }F\text{–}s\text{ graph}.
\]
</p>
<div class="ch7-subsection">Exam Traps</div>
<ul>
<li>Force alone does not guarantee work.</li>
<li>Displacement alone does not guarantee work by a particular force.</li>
<li>Always identify which force is being considered.</li>
<li>Do not confuse physical effort/fatigue with mechanical work on an object.</li>
</ul>
</section>

<section class="ch7-section-card">
<span class="ch7-kicker">03 · Work–Energy Theorem</span>
<h2>Work–Energy Theorem</h2>
<div class="ch7-formula">\[W=\Delta E\]</div>
<p>
Work done on an object or system equals the change in its energy. For
translational motion:
\[
W_{\rm net}=\Delta K=K_f-K_i.
\]
</p>
<ul>
<li>Positive net work → kinetic energy increases.</li>
<li>Negative net work → kinetic energy decreases.</li>
<li>Zero net work → kinetic energy remains unchanged.</li>
</ul>
<p>
<strong>Numerical trick:</strong> If force/displacement and initial/final
speeds are involved, the work–energy theorem can often solve the problem
directly without a long sequence of kinematic steps.
</p>
<p><strong>Stopping trick:</strong> If an object finally stops, \(K_f=0\),
so \(W_{\rm net}=-K_i\).</p>
</section>

<section class="ch7-section-card">
<span class="ch7-kicker">04 · Forms of Energy</span>
<h2>Forms and Transformations</h2>
<div class="ch7-table-wrap">
<table class="ch7-table">
<thead><tr><th>Form</th><th>Typical idea / example</th></tr></thead>
<tbody>
<tr><td>Mechanical</td><td>Motion or position</td></tr>
<tr><td>Thermal</td><td>Heating</td></tr>
<tr><td>Light</td><td>Sun, lamp</td></tr>
<tr><td>Sound</td><td>Vibrations</td></tr>
<tr><td>Nuclear</td><td>Atomic nuclei</td></tr>
<tr><td>Chemical</td><td>Food, fuels</td></tr>
<tr><td>Electrical</td><td>Electric charges/circuits</td></tr>
</tbody>
</table>
</div>
<p><strong>Transformation trick: “Input → Conversion → Useful output + losses.”</strong></p>
<ul>
<li>Dam: gravitational potential → kinetic → mechanical/electrical.</li>
<li>Bulb: electrical → light + thermal.</li>
<li>Solar panel: light → electrical.</li>
<li>Microphone: sound → electrical signal.</li>
<li>Matchstick: chemical → thermal + light.</li>
<li>Food: chemical → mechanical + thermal.</li>
</ul>
</section>

<section class="ch7-section-card">
<span class="ch7-kicker">05 · Mechanical Energy</span>
<h2>Mechanical Energy</h2>
<div class="ch7-formula">\[E_m=K+U\]</div>
<p>Mechanical energy is the combination of kinetic and potential energy.</p>
<p><strong>Mnemonic: “Move = K; Position/Shape = U.”</strong></p>
</section>

<section class="ch7-section-card">
<span class="ch7-kicker">06 · Kinetic Energy</span>
<h2>Kinetic Energy — Formula, Dependence and Tricks</h2>
<div class="ch7-formula">\[K=\frac12mv^2\]</div>
<p>Kinetic energy is the energy possessed by an object because of its motion.</p>
<div class="ch7-subsection">Dependence</div>
<ul>
<li>\(K\propto m\): double mass → double KE.</li>
<li>\(K\propto v^2\): double speed → four times KE.</li>
<li>Triple speed → nine times KE.</li>
<li>Half speed → one-fourth KE.</li>
</ul>
<p><strong>Mnemonic: “Mass once, Speed square.”</strong></p>
<div class="ch7-subsection">Ratio Shortcut</div>
<div class="ch7-formula">
\[
\frac{K_1}{K_2}
=
\frac{m_1}{m_2}
\left(\frac{v_1}{v_2}\right)^2
\]
</div>
<div class="ch7-subsection">Equal Kinetic Energy</div>
<div class="ch7-formula">\[m_1v_1^2=m_2v_2^2\]</div>
<p>For equal KE, the lighter body has the greater speed.</p>
<div class="ch7-subsection">Unit Conversion Trap</div>
<div class="ch7-formula">\[v(\mathrm{m/s})=\frac5{18}v(\mathrm{km/h})\]</div>
<p><strong>Mnemonic: km/h → m/s = ×5/18.</strong></p>
<div class="ch7-subsection">Stopping</div>
<div class="ch7-formula">\[W_{\rm stopping}=-K_i\]</div>
</section>

<section class="ch7-section-card">
<span class="ch7-kicker">07 · Potential Energy</span>
<h2>Potential Energy — Complete Classification</h2>
<p>
Potential energy is stored by deformation or by the relative positions of
objects in a system.
</p>
<div class="ch7-table-wrap">
<table class="ch7-table">
<thead><tr><th>Type</th><th>Stored because of</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Elastic</td><td>Deformation</td><td>Stretched rubber band, compressed spring, bent bow</td></tr>
<tr><td>Magnetic</td><td>Relative positions of magnets</td><td>Separated magnetic poles</td></tr>
<tr><td>Electrostatic</td><td>Relative positions of charges</td><td>Separated electric charges</td></tr>
<tr><td>Gravitational</td><td>Relative position in gravitational field</td><td>Raised object near Earth</td></tr>
</tbody>
</table>
</div>
<div class="ch7-subsection">Gravitational Potential Energy</div>
<div class="ch7-formula">\[U=mgh\]</div>
<p>
Near Earth's surface, \(g\) is treated as approximately constant. \(h\) is
measured relative to the chosen reference level.
</p>
<p><strong>Mnemonic: “m-g-h = mass × gravity × height.”</strong></p>
<div class="ch7-subsection">Path Independence</div>
<p>
For gravitational potential energy near Earth's surface:
\[
\Delta U=mg\Delta h.
\]
The change depends on vertical height change, not whether the object travels
vertically, along stairs or along a ramp, when initial and final heights are
the same.
</p>
<p><strong>Exam trick:</strong> Same \(m\), same \(g\), same height change →
same gravitational PE change.</p>
</section>

<section class="ch7-section-card">
<span class="ch7-kicker">08 · Conservation</span>
<h2>Conservation of Mechanical Energy</h2>
<div class="ch7-formula">\[K_i+U_i=K_f+U_f\]</div>
<p>
When the stated ideal conditions hold—no frictional/mechanical-energy loss
and no other relevant non-conservative work changing the mechanical energy—
the sum \(K+U\) remains constant.
</p>
<div class="ch7-subsection">Free-Fall Pattern</div>
<div class="ch7-table-wrap">
<table class="ch7-table">
<thead><tr><th>Position</th><th>Potential Energy</th><th>Kinetic Energy</th></tr></thead>
<tbody>
<tr><td>Top</td><td>Maximum</td><td>Minimum / zero if released from rest</td></tr>
<tr><td>Middle</td><td>Decreasing</td><td>Increasing</td></tr>
<tr><td>Bottom</td><td>Minimum relative to zero level</td><td>Maximum</td></tr>
</tbody>
</table>
</div>
<p><strong>Mnemonic: “Down U, Up K.”</strong></p>
<div class="ch7-subsection">Free-Fall Speed Shortcut</div>
<div class="ch7-formula">\[mgh=\frac12mv^2\Rightarrow v=\sqrt{2gh}\]</div>
<p>Mass cancels, so ideal free-fall speed from a given height is independent of mass.</p>
<div class="ch7-subsection">Friction</div>
<p>
With friction, mechanical energy is transferred partly into thermal energy
and possibly sound. Total energy remains accounted for, but mechanical
energy \(K+U\) is not constant.
</p>
<p><strong>Exam distinction:</strong> Total energy conservation is broader
than mechanical-energy conservation.</p>
</section>

<section class="ch7-section-card">
<span class="ch7-kicker">09 · Power</span>
<h2>Power — Rate of Doing Work</h2>
<div class="ch7-formula">\[P=\frac{W}{t}\]</div>
<ul>
<li>SI unit: watt (W).</li>
<li>\(1\,\mathrm{W}=1\,\mathrm{J\,s^{-1}}\).</li>
<li>\(1\,\mathrm{hp}=746\,\mathrm{W}\).</li>
</ul>
<p><strong>Mnemonic: “Power = Work per Time.”</strong></p>
<p>
Same work in less time means greater power. For fixed work,
\(P\propto1/t\). For fixed time, \(P\propto W\).
</p>
<div class="ch7-subsection">Lifting</div>
<div class="ch7-formula">\[W=mgh,\qquad P=\frac{mgh}{t}\]</div>
<div class="ch7-subsection">Acceleration</div>
<div class="ch7-formula">\[W=\Delta K=\frac12m(v^2-u^2),\qquad P=\frac{\Delta K}{t}\]</div>
</section>

<section class="ch7-section-card">
<span class="ch7-kicker">10 · Simple Machines</span>
<h2>Simple Machines — Master Framework</h2>
<p>
Simple machines make tasks easier by changing the magnitude or direction of
the applied force. They do not reduce total work in the ideal case.
</p>
<div class="ch7-formula">\[\mathrm{MA}=\frac{\text{Load}}{\text{Effort}}\]</div>
<p><strong>Mnemonic: “L over E” → Load on top, Effort below.</strong></p>
<div class="ch7-table-wrap">
<table class="ch7-table">
<thead><tr><th>Machine</th><th>Main advantage</th><th>Key relation</th></tr></thead>
<tbody>
<tr><td>Fixed pulley</td><td>Changes direction</td><td>Ideal MA = 1</td></tr>
<tr><td>Movable/system pulley</td><td>Can reduce effort</td><td>MA can exceed 1</td></tr>
<tr><td>Inclined plane</td><td>Reduces effort by increasing distance</td><td>\(MA=L/h\)</td></tr>
<tr><td>Lever</td><td>Uses arm lengths to multiply force</td><td>\(F_ed_e=F_ld_l\)</td></tr>
</tbody>
</table>
</div>
<p><strong>Golden machine rule:</strong> “Gain force, lose distance; save force,
spend distance.”</p>
</section>

<section class="ch7-section-card">
<span class="ch7-kicker">11 · Pulley</span>
<h2>Pulley — Fixed and Movable</h2>
<div class="ch7-subsection">Fixed Pulley</div>
<ul>
<li>Ideal effort equals load.</li>
<li>Ideal mechanical advantage = 1.</li>
<li>Main benefit is changing the direction of effort.</li>
</ul>
<p><strong>Mnemonic: “Fixed = Direction.”</strong></p>
<div class="ch7-subsection">Movable / Pulley System</div>
<ul>
<li>Can have mechanical advantage greater than 1.</li>
<li>Can lift heavier loads with smaller effort.</li>
<li>Used in practical systems such as cranes and elevators.</li>
</ul>
<p><strong>Trap:</strong> Do not say every pulley automatically gives MA greater
than 1; a fixed pulley has ideal MA 1.</p>
</section>

<section class="ch7-section-card">
<span class="ch7-kicker">12 · Inclined Plane</span>
<h2>Inclined Plane — Formula + Geometry</h2>
<p>
An inclined plane trades force for distance. A gentler and longer ramp
requires less effort over a greater distance.
</p>
<div class="ch7-formula">
\[F'L=mgh\]
\[\mathrm{MA}=\frac{mg}{F'}=\frac{L}{h}\]
</div>
<div class="ch7-subsection">Geometry Shortcut</div>
<p>If vertical height \(h\) and horizontal base \(b\) are given:</p>
<div class="ch7-formula">\[L=\sqrt{h^2+b^2}\]</div>
<p>Then use \(MA=L/h\).</p>
<p><strong>Mnemonic: “Ramp MA = Long / Height.”</strong></p>
<div class="ch7-subsection">Making the Ramp Gentler</div>
<ul>
<li>Ramp length increases.</li>
<li>Height remains the same.</li>
<li>Mechanical advantage increases.</li>
<li>Required effort decreases.</li>
<li>Distance through which effort acts increases.</li>
</ul>
</section>

<section class="ch7-section-card">
<span class="ch7-kicker">13 · Lever</span>
<h2>Lever — Complete Revision</h2>
<p>
A lever is a rigid bar rotating about a fixed point called the fulcrum.
The three parts are fulcrum, load and effort. Their distances from the
fulcrum are the load arm and effort arm.
</p>
<div class="ch7-formula">
\[F_ed_e=F_ld_l\]
\[\mathrm{MA}=\frac{F_l}{F_e}=\frac{d_e}{d_l}\]
</div>
<p><strong>Mnemonic: “Longer effort arm = easier lifting.”</strong></p>
<div class="ch7-subsection">Seesaw / Balance Trick</div>
<div class="ch7-formula">\[m_1d_1=m_2d_2\]</div>
<p>
Do not compare masses alone. Compare mass × distance from the fulcrum.
A heavier person must sit closer to the fulcrum to balance a lighter person.
</p>
<div class="ch7-subsection">Three Classes of Lever</div>
<div class="ch7-table-wrap">
<table class="ch7-table">
<thead><tr><th>Class</th><th>Middle part</th><th>Examples</th></tr></thead>
<tbody>
<tr><td>I</td><td>Fulcrum</td><td>Scissors, crowbar, pliers, balance scale, seesaw</td></tr>
<tr><td>II</td><td>Load</td><td>Lemon squeezer, wheelbarrow, bottle opener</td></tr>
<tr><td>III</td><td>Effort</td><td>Tongs, tweezers, broom, hammer, oar</td></tr>
</tbody>
</table>
</div>
<p><strong>Mnemonic: “1-F, 2-L, 3-E.”</strong><br>
Class I → Fulcrum in middle.<br>
Class II → Load in middle.<br>
Class III → Effort in middle.</p>
<p><strong>Second cue: F-L-E = 1-2-3.</strong></p>
</section>

<section class="ch7-section-card">
<span class="ch7-kicker">14 · Activities</span>
<h2>Activities — What Each One Proves</h2>
<div class="ch7-table-wrap">
<table class="ch7-table">
<thead><tr><th>Activity</th><th>Observation</th><th>Concept</th></tr></thead>
<tbody>
<tr><td>7.1</td><td>Ball dropped from greater height makes a deeper depression</td><td>Greater height → greater gravitational PE</td></tr>
<tr><td>7.2</td><td>Pendulum moves between high and low positions</td><td>Potential ↔ kinetic energy transformation</td></tr>
<tr><td>7.3</td><td>Gentler ramp needs less force over more distance</td><td>Inclined plane trades force for distance</td></tr>
<tr><td>7.4</td><td>Small effort can lift larger load with lever arrangement</td><td>Mechanical advantage from effort/load arms</td></tr>
<tr><td>7.5</td><td>Beam balances when force × arm matches on both sides</td><td>Lever balance / moments</td></tr>
</tbody>
</table>
</div>
<p><strong>Activity mnemonic: “Ball → Pendulum → Ramp → Lever → Balance.”</strong></p>
</section>

<section class="ch7-section-card">
<span class="ch7-kicker">15 · Formula Bank</span>
<h2>All Important Formulae</h2>
<div class="ch7-table-wrap">
<table class="ch7-table">
<thead><tr><th>Topic</th><th>Formula</th><th>Typical use</th></tr></thead>
<tbody>
<tr><td>Work</td><td>\(W=Fs\)</td><td>Constant force along displacement</td></tr>
<tr><td>Work–energy</td><td>\(W=\Delta E\)</td><td>Energy change due to work</td></tr>
<tr><td>Net work</td><td>\(W_{\rm net}=\Delta K\)</td><td>Speed changes</td></tr>
<tr><td>Kinetic energy</td><td>\(K=\frac12mv^2\)</td><td>Moving body</td></tr>
<tr><td>Gravitational PE</td><td>\(U=mgh\)</td><td>Near Earth</td></tr>
<tr><td>Mechanical energy</td><td>\(E_m=K+U\)</td><td>Mechanical energy total</td></tr>
<tr><td>Conservation</td><td>\(K_i+U_i=K_f+U_f\)</td><td>Ideal mechanical-energy conservation</td></tr>
<tr><td>Free-fall speed</td><td>\(v=\sqrt{2gh}\)</td><td>Starts from rest, ideal fall</td></tr>
<tr><td>Power</td><td>\(P=W/t\)</td><td>Rate of work</td></tr>
<tr><td>Horsepower</td><td>\(1\,hp=746\,W\)</td><td>Power conversion</td></tr>
<tr><td>Mechanical advantage</td><td>\(MA=L/E\)</td><td>Simple machines</td></tr>
<tr><td>Inclined plane</td><td>\(MA=L/h\)</td><td>Ideal ramp</td></tr>
<tr><td>Inclined plane work</td><td>\(F'L=mgh\)</td><td>Ideal ramp</td></tr>
<tr><td>Lever balance</td><td>\(F_ed_e=F_ld_l\)</td><td>Lever / seesaw</td></tr>
<tr><td>Lever MA</td><td>\(MA=d_e/d_l\)</td><td>Ideal lever</td></tr>
</tbody>
</table>
</div>
</section>

<section class="ch7-section-card">
<span class="ch7-kicker">16 · Numerical Tricks</span>
<h2>Fast Problem-Solving Toolkit</h2>
<div class="ch7-subsection">A. Work Questions</div>
<p>
Write \(W=Fs\), then determine direction. Opposite direction means negative
work; perpendicular means zero work by that force.
</p>
<div class="ch7-subsection">B. Speed / Force / Displacement</div>
<div class="ch7-formula">\[W_{\rm net}=\frac12m(v^2-u^2)\]</div>
<p>Use this directly when the question links work and speed change.</p>
<div class="ch7-subsection">C. Height / Speed</div>
<div class="ch7-formula">\[
mgh+\frac12mu^2=mgh'+\frac12mv^2
\]</div>
<p>For ideal motion between heights, cancel \(m\) early.</p>
<div class="ch7-subsection">D. Power</div>
<p>First find work/energy change, then divide by time: \(P=W/t\).</p>
<div class="ch7-subsection">E. Ramp</div>
<ol>
<li>Draw the right triangle.</li>
<li>Find ramp length \(L\) using Pythagoras if needed.</li>
<li>Use \(MA=L/h\).</li>
<li>If effort is required, use \(MA=Load/Effort\).</li>
</ol>
<div class="ch7-subsection">F. Seesaw / Lever</div>
<div class="ch7-formula">\[
\text{force}\times\text{distance}
=
\text{force}\times\text{distance}
\]</div>
<p>For masses in the same gravitational field: \(m_1d_1=m_2d_2\).</p>
<div class="ch7-subsection">G. Graphs</div>
<ul>
<li>Force–displacement graph → area gives work.</li>
<li>Potential-energy graph on a frictionless track → use mechanical-energy conservation.</li>
</ul>
</section>

<section class="ch7-section-card">
<span class="ch7-kicker">17 · Comparisons</span>
<h2>Frequently Confused Ideas</h2>
<div class="ch7-table-wrap">
<table class="ch7-table">
<thead><tr><th>Confusion</th><th>Correct distinction</th></tr></thead>
<tbody>
<tr><td>Work vs Power</td><td>Work is amount of energy transfer; power is rate of transfer.</td></tr>
<tr><td>Energy vs Power</td><td>Energy is an amount/capacity; power tells how quickly work is done.</td></tr>
<tr><td>Kinetic vs Potential</td><td>Kinetic → motion; potential → deformation/relative position.</td></tr>
<tr><td>Total vs Mechanical energy</td><td>Total energy can remain conserved while mechanical energy changes into thermal/sound energy.</td></tr>
<tr><td>Fixed vs movable pulley</td><td>Fixed mainly changes direction; movable/system can provide MA &gt; 1.</td></tr>
<tr><td>Load arm vs effort arm</td><td>Load arm = load-to-fulcrum distance; effort arm = effort-to-fulcrum distance.</td></tr>
<tr><td>Force vs Work</td><td>Applying force does not automatically mean work is done.</td></tr>
<tr><td>Mass vs weight</td><td>Mass is \(m\); gravitational force/weight near Earth is \(mg\).</td></tr>
<tr><td>Height vs path length</td><td>Gravitational PE change depends on vertical height change.</td></tr>
</tbody>
</table>
</div>
</section>

<section class="ch7-section-card">
<span class="ch7-kicker">18 · Mnemonics</span>
<h2>Master Mnemonics</h2>
<ul>
<li><strong>F–D–D:</strong> Force → Displacement → Direction.</li>
<li><strong>Same + / Against − / Across 0:</strong> sign of work.</li>
<li><strong>Mass once, Speed square:</strong> \(K\propto mv^2\).</li>
<li><strong>Move = K, Position/Shape = U.</strong></li>
<li><strong>Down U, Up K:</strong> falling object.</li>
<li><strong>Power = Work per Time.</strong></li>
<li><strong>L over E:</strong> \(MA=Load/Effort\).</li>
<li><strong>Fixed = Direction.</strong></li>
<li><strong>Ramp = Long/Height.</strong></li>
<li><strong>Longer effort arm = easier lifting.</strong></li>
<li><strong>1-F, 2-L, 3-E:</strong> lever classes.</li>
<li><strong>F-L-E = 1-2-3:</strong> second lever-class cue.</li>
<li><strong>Ball → Pendulum → Ramp → Lever → Balance:</strong> Activities 7.1–7.5.</li>
<li><strong>km/h → m/s = ×5/18.</strong></li>
</ul>
</section>

<section class="ch7-section-card">
<span class="ch7-kicker">19 · Error Check</span>
<h2>Top Exam Mistakes</h2>
<ol>
<li>Using \(W=Fs\) without checking direction.</li>
<li>Thinking force alone guarantees work.</li>
<li>Thinking tiredness automatically means mechanical work on the object.</li>
<li>Forgetting the square on velocity in KE.</li>
<li>Using km/h directly in \(K=\frac12mv^2\).</li>
<li>Forgetting the chosen reference level for potential energy.</li>
<li>Assuming mechanical energy is always conserved even with friction.</li>
<li>Confusing power with work.</li>
<li>Writing \(MA=Effort/Load\) instead of \(Load/Effort\).</li>
<li>Using horizontal base instead of ramp length in \(MA=L/h\).</li>
<li>Confusing effort arm with load arm.</li>
<li>Balancing a seesaw by mass alone instead of mass × distance.</li>
<li>Assuming every pulley has MA greater than 1.</li>
<li>Thinking a machine creates energy.</li>
<li>Ignoring friction in real-machine or roller-coaster questions.</li>
</ol>
</section>

<section class="ch7-section-card">
<span class="ch7-kicker">20 · Final Checklist</span>
<h2>Last-Minute 60-Second Revision</h2>
<ol>
<li>Define work and write \(W=Fs\).</li>
<li>State the three zero-work situations.</li>
<li>Distinguish positive and negative work.</li>
<li>State the work–energy theorem.</li>
<li>Name the major forms of energy in the chapter.</li>
<li>Define KE and write \(K=\frac12mv^2\).</li>
<li>Explain KE dependence on mass and speed.</li>
<li>Define potential energy and its types.</li>
<li>Use \(U=mgh\) correctly.</li>
<li>Explain mechanical energy \(K+U\).</li>
<li>State the conditions for mechanical-energy conservation.</li>
<li>Explain PE ↔ KE conversion.</li>
<li>Define power and watt.</li>
<li>Convert horsepower.</li>
<li>Define mechanical advantage.</li>
<li>Distinguish fixed and movable pulleys.</li>
<li>Use inclined-plane \(MA=L/h\).</li>
<li>Use lever balance \(F_ed_e=F_ld_l\).</li>
<li>Remember lever classes 1-F, 2-L, 3-E.</li>
<li>Explain why machines trade force for distance.</li>
</ol>
<div class="ch7-formula">
\[
\boxed{
W=Fs,\quad
W_{\rm net}=\Delta K,\quad
K=\frac12mv^2,\quad
U=mgh,\quad
K+U=\text{constant},\quad
P=\frac{W}{t},\quad
MA=\frac{L}{E}
}
\]
</div>
<p>
<strong>Final memory sentence:</strong>
“Work transfers energy; motion gives kinetic energy; position/deformation
stores potential energy; conservation shifts energy between forms; power tells
how fast the transfer happens; machines trade force for distance.”
</p>
</section>

</div>
"""


DESCRIPTIONS = {
"concepts":"Complete NCERT-aligned concepts for Class 9 Science Chapter 7 Work, Energy, and Simple Machines, including examples and Pause and Ponder answers.",
"ncert-exercises":"Class 9 Science Chapter 7 NCERT exercise questions for practice.",
"revision-notes":"Quick revision formulas and key ideas for Class 9 Science Chapter 7."
}


def update_metadata(doc, page_type):
    desc = DESCRIPTIONS[page_type]
    doc = re.sub(r"<title>.*?</title>",
                 f"<title>{esc(TITLE)} | Class 9 Science Ch 7 | SJMaths</title>",
                 doc, count=1, flags=re.S)
    doc = re.sub(r'<meta name="description" content=".*?">',
                 f'<meta name="description" content="{esc(desc)}">',
                 doc, count=1, flags=re.S)
    return doc


def replace_nav(doc, page_type):
    prev_next = {
        "concepts": (
            '<a href="../index.html" class="sj-btn"><i class="fas fa-arrow-left"></i> OVERVIEW</a>',
            '<a href="../ncert-exercises/" class="sj-btn next">NCERT <i class="fas fa-arrow-right"></i></a>'
        ),
        "ncert-exercises": (
            '<a href="../concepts/" class="sj-btn"><i class="fas fa-arrow-left"></i> CONCEPTS</a>',
            '<a href="../quiz/" class="sj-btn next">QUIZ <i class="fas fa-arrow-right"></i></a>'
        ),
        "revision-notes": (
            '<a href="../tests/" class="sj-btn"><i class="fas fa-arrow-left"></i> TESTS</a>',
            '<a href="../../chapter-8-journey-inside-atom/" class="sj-btn next">CH 8 <i class="fas fa-arrow-right"></i></a>'
        )
    }

    p, n = prev_next[page_type]

    tbar = f"""
<nav class="sj-tbar">
<div class="sj-bcrumb">
<a href="/">Home</a>
<i class="fas fa-chevron-right" style="font-size:.4rem;"></i>
<a href="/class-9-science/">Class 9 Science</a>
<i class="fas fa-chevron-right" style="font-size:.4rem;"></i>
<a href="../index.html">{esc(TITLE)}</a>
<i class="fas fa-chevron-right" style="font-size:.4rem;"></i>
<span style="color:#0f9d8a;">{page_type.replace("-", " ").title()}</span>
</div>
<div class="sj-nav">{p}{n}</div>
</nav>
"""
    doc = re.sub(r'<nav class="sj-tbar">.*?</nav>',
                 tbar.strip(), doc, count=1, flags=re.S)

    links = [
        ("Overview","../index.html",""),
        ("Concepts","../concepts/"," active" if page_type=="concepts" else ""),
        ("NCERT","../ncert-exercises/"," active" if page_type=="ncert-exercises" else ""),
        ("Quiz","../quiz/",""),
        ("Tests","../tests/",""),
        ("Revision","../revision-notes/"," active" if page_type=="revision-notes" else ""),
    ]

    section_nav = '<nav class="sj-section-nav">' + "".join(
        f'<a href="{href}" class="sj-section-link{active}">{label}</a>'
        for label, href, active in links
    ) + '</nav>'

    doc = re.sub(r'<nav class="sj-section-nav">.*?</nav>',
                 section_nav, doc, count=1, flags=re.S)
    return doc


def replace_content(doc, content, page_type):
    marker = '<div class="sj-page-content">'
    start = doc.find(marker)
    if start < 0:
        raise RuntimeError(f"Missing sj-page-content in {page_type} template.")

    bottom = doc.find('<div class="sj-bottom-nav">', start)
    if bottom >= 0:
        close = doc.find("</div>", bottom)
        if close < 0:
            raise RuntimeError("Cannot find bottom-nav closing tag.")

        return (
            doc[:start]
            + marker + "\n" + content + "\n</div>\n"
            + doc[bottom:close+len("</div>")]
            + doc[close+len("</div>"):]
        )

    footer = doc.find('<div id="footer-container">', start)
    if footer < 0:
        raise RuntimeError(f"Cannot find page boundary in {page_type}.")
    return doc[:start] + marker + "\n" + content + "\n</div>\n" + doc[footer:]


def prepare(page_type, content):
    template = TEMPLATES[page_type]
    if not template.exists():
        raise FileNotFoundError(template)

    doc = template.read_text(encoding="utf-8")
    doc = update_metadata(doc, page_type)
    doc = replace_nav(doc, page_type)
    doc = replace_content(doc, content, page_type)

    if 'id="sj-ch7-v2-ui"' not in doc:
        doc = doc.replace("</head>", CSS + "\n</head>", 1)

    if "cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js" not in doc:
        doc = doc.replace("</head>", MATHJAX + "\n</head>", 1)

    marker = (
        f'\n<!-- SJMaths Chapter 7 v3 rebuild: {page_type} -->\n'
    )
    doc = doc.replace("<body>", "<body>" + marker, 1)
    return doc


def build(page_type, content):
    out = CH7 / page_type / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(prepare(page_type, content), encoding="utf-8")
    print("✓", out)


def validate():
    expected = {
        "7.1","7.1.1","7.1.2","7.2","7.3","7.4","7.4.1",
        "7.4.2","7.4.3","7.5","7.6","7.6.1","7.6.2","7.6.3"
    }
    found = {c["no"] for c in CONCEPTS}
    missing = expected - found
    if missing:
        raise RuntimeError("Missing concepts: " + ", ".join(sorted(missing)))

    source = "\n".join(c["body"] for c in CONCEPTS)
    for i in range(1,14):
        if f"Example 7.{i}" not in source:
            raise RuntimeError(f"Missing Example 7.{i}")

    if len(EXERCISES) != 15:
        raise RuntimeError("Expected 15 NCERT exercises.")

    # Critical UX validation:
    # Answers must exist only in concept examples / Pause & Ponder,
    # never in exercise cards.
    exercise_source = "\n".join(x[2] for x in EXERCISES)
    forbidden = ["Show Answer", "Ideal Answer", "Marking Scheme", "ch7-reveal"]
    for token in forbidden:
        if token in exercise_source:
            raise RuntimeError(
                f"Answer/reveal UI leaked into NCERT Exercise Qs: {token}"
            )

    print("✓ Full concept hierarchy validated: 14 sections.")
    print("✓ NCERT Examples 7.1–7.13 validated.")
    print("✓ 15 NCERT exercises validated.")
    print("✓ Exercise pages contain QUESTIONS ONLY.")
    print("✓ Click-to-reveal exists only for Examples and Pause & Ponder.")


def main():
    print("=" * 78)
    print("SJMaths — Class 9 Science Chapter 7 v3")
    print("Work, Energy, and Simple Machines")
    print("=" * 78)

    if not CH1.exists():
        raise FileNotFoundError("Chapter 1 master template folder not found: " + str(CH1))
    if not CH7.exists():
        raise FileNotFoundError("Chapter 7 folder not found: " + str(CH7))

    validate()

    concepts_content = f"""
<div class="sj-ch7-page">
<section class="ch7-section-card">
<span class="ch7-kicker">Complete NCERT-aligned learning</span>
<h2>{esc(TITLE)}</h2>
<p>
This rebuild follows the complete NCERT hierarchy. Examples and Pause and
Ponder answers are hidden until clicked. NCERT Exercises remain question-only
for independent practice.
</p>
</section>
{"".join(render_concept(c) for c in CONCEPTS)}
</div>
"""

    exercises_content = f"""
<div class="sj-ch7-page">
<section class="ch7-section-card">
<span class="ch7-kicker">Practice</span>
<h2>NCERT Exercises</h2>
<p>
Attempt every question independently. This page intentionally contains
<strong>questions only</strong>; there is no answer/reveal control here.
</p>
</section>
{"".join(render_exercise(q) for q in EXERCISES)}
</div>
"""

    build("concepts", concepts_content)
    build("ncert-exercises", exercises_content)
    build("revision-notes", REVISION)

    print()
    print("✓ CHAPTER 7 v2 REBUILD COMPLETE")
    print("✓ Concepts: complete hierarchy")
    print("✓ Examples: click → answer")
    print("✓ Pause & Ponder: click → answer")
    print("✓ NCERT Exercises: questions only")
    print("✓ Quiz/Tests: untouched")


if __name__ == "__main__":
    main()