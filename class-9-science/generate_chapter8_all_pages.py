from pathlib import Path
import re
import json
import html


# ================================================================
# SJMaths — Class 9 Science — Chapter 8 Generator
# "Journey Inside the Atom"
#
# IMPORTANT:
# Chapter 1 is the MASTER UI/UX.
#
# This generator does NOT recreate the Quiz/Test UI.
# It takes the ACTUAL Chapter 1 HTML files and changes only:
#
#   • Chapter-specific metadata
#   • Breadcrumb / navigation text
#   • Chapter 8 content
#   • NCERT question content
#   • Quiz data
#   • Test data
#   • Revision content
#
# It DOES NOT:
#   • remove Chapter 1 CSS
#   • remove Chapter 1 JavaScript
#   • create a new quiz engine
#   • create a new test engine
#   • create new quiz classes
#   • create new test classes
#
# Therefore Chapter 8 inherits the EXACT Chapter 1 UI/UX.
# ================================================================


BASE = Path(__file__).resolve().parent

CH1_FOLDER = "chapter-1-exploration-entering-world-of-secondary-science"
CH8_FOLDER = "chapter-8-journey-inside-atom"

CH1 = BASE / CH1_FOLDER
CH8 = BASE / CH8_FOLDER


TITLE = "Journey Inside the Atom"
CHAPTER = 8

NEXT_FOLDER = "chapter-9-atomic-foundations-of-matter"
NEXT_TITLE = "Ch 9: Atomic Foundations"


TEMPLATES = {
    "concepts": CH1 / "concepts" / "index.html",
    "ncert-exercises": CH1 / "ncert-exercises" / "index.html",
    "quiz": CH1 / "quiz" / "index.html",
    "tests": CH1 / "tests" / "index.html",
    "revision-notes": CH1 / "revision-notes" / "index.html",
}


# ================================================================
# Utility
# ================================================================

def esc(value):
    return html.escape(str(value), quote=True)


def js(value):
    """
    Convert Python objects to safe JSON/JavaScript literals.
    """
    return json.dumps(
        value,
        ensure_ascii=False,
        indent=12
    )


# ================================================================
# Navigation
#
# Structure deliberately follows Chapter 1.
# ================================================================

PAGE_NAV = {
    "concepts": (
        '<a href="../index.html" class="sj-btn">'
        '<i class="fas fa-arrow-left"></i> OVERVIEW</a>',
        '<a href="../ncert-exercises/" class="sj-btn next">'
        'NCERT <i class="fas fa-arrow-right"></i></a>',
    ),

    "ncert-exercises": (
        '<a href="../concepts/" class="sj-btn">'
        '<i class="fas fa-arrow-left"></i> CONCEPTS</a>',
        '<a href="../quiz/" class="sj-btn next">'
        'Quiz <i class="fas fa-arrow-right"></i></a>',
    ),

    "quiz": (
        '<a href="../ncert-exercises/" class="sj-btn">'
        '<i class="fas fa-arrow-left"></i> NCERT</a>',
        '<a href="../tests/" class="sj-btn next">'
        'Tests <i class="fas fa-arrow-right"></i></a>',
    ),

    "tests": (
        '<a href="../quiz/" class="sj-btn">'
        '<i class="fas fa-arrow-left"></i> Quiz</a>',
        '<a href="../revision-notes/" class="sj-btn next">'
        'Revision <i class="fas fa-arrow-right"></i></a>',
    ),

    "revision-notes": (
        '<a href="../tests/" class="sj-btn">'
        '<i class="fas fa-arrow-left"></i> Tests</a>',
        f'<a href="../../{NEXT_FOLDER}/" class="sj-btn next">'
        f'{NEXT_TITLE} <i class="fas fa-arrow-right"></i></a>',
    ),
}


BOTTOM_NAV = {
    "concepts": (
        '<a href="../index.html" class="prev">'
        '<i class="fas fa-arrow-left"></i> Overview</a>',
        '<a href="../ncert-exercises/" class="next">'
        'NCERT Exercises <i class="fas fa-arrow-right"></i></a>',
    ),

    "ncert-exercises": (
        '<a href="../concepts/" class="prev">'
        '<i class="fas fa-arrow-left"></i> Concepts</a>',
        '<a href="../quiz/" class="next">'
        'Interactive Quiz <i class="fas fa-arrow-right"></i></a>',
    ),

    "quiz": (
        '<a href="../ncert-exercises/" class="prev">'
        '<i class="fas fa-arrow-left"></i> NCERT Exercises</a>',
        '<a href="../tests/" class="next">'
        'Tests <i class="fas fa-arrow-right"></i></a>',
    ),

    "tests": (
        '<a href="../quiz/" class="prev">'
        '<i class="fas fa-arrow-left"></i> Quiz</a>',
        '<a href="../revision-notes/" class="next">'
        'Revision <i class="fas fa-arrow-right"></i></a>',
    ),

    "revision-notes": (
        '<a href="../tests/" class="prev">'
        '<i class="fas fa-arrow-left"></i> Tests</a>',
        f'<a href="../../{NEXT_FOLDER}/" class="next">'
        f'{NEXT_TITLE} <i class="fas fa-arrow-right"></i></a>',
    ),
}


# ================================================================
# CHAPTER 8 — CONCEPTS
#
# Content only.
# UI wrappers remain Chapter 1-compatible.
# ================================================================

CONCEPTS = [

    (
        "1",
        "fa-history",
        "Rediscovering the Roots of Atomic Theory",
        """
        <p>
            Ideas about atoms developed over more than two thousand years.
            <strong>Acharya Kanada</strong> proposed that matter could be divided
            repeatedly until reaching extremely small particles called
            <em>parmanus</em>. He described combinations such as dyads and triads
            in the <em>Vaisesika Sutras</em>.
        </p>

        <p>
            In ancient Greece, <strong>Leucippus and Democritus</strong>
            proposed a similar idea and used the word
            <em>atomos</em>, meaning indivisible.
            These early ideas were philosophical rather than experimental.
        </p>

        <div class="sj-grid">

            <div class="sj-grid-card">
                <h4>
                    <i class="fas fa-om"></i>
                    Acharya Kanada
                </h4>
                <p>
                    Proposed the idea of indivisible
                    <strong>parmanus</strong> and combinations of particles.
                </p>
            </div>

            <div class="sj-grid-card">
                <h4>
                    <i class="fas fa-landmark"></i>
                    Greek Atomism
                </h4>
                <p>
                    Leucippus and Democritus used the term
                    <strong>atomos</strong> for indivisible particles.
                </p>
            </div>

            <div class="sj-grid-card">
                <h4>
                    <i class="fas fa-flask"></i>
                    Dalton, 1808
                </h4>
                <p>
                    John Dalton gave the first scientific description of
                    matter as being composed of atoms, based on experiments.
                </p>
            </div>

        </div>

        <div class="sj-ibox discovery">
            <i class="fas fa-lightbulb"
               style="color:#0f9d8a;font-size:1.4rem;"></i>

            <div>
                <strong style="display:block;margin-bottom:4px;color:#0f9d8a;">
                    Key Idea
                </strong>

                <p style="font-size:.9rem;margin-bottom:0;">
                    Atomic theory did not appear fully formed.
                    Scientific models changed as new experiments
                    produced new evidence.
                </p>
            </div>
        </div>
        """
    ),

    (
        "2",
        "fa-atom",
        "Thomson’s Model and the Discovery of the Electron",
        """
        <p>
            In 1897, <strong>J. J. Thomson</strong> studied cathode rays
            in a low-pressure gas discharge tube.
            The rays were streams of negatively charged particles
            later called <strong>electrons</strong>.
        </p>

        <div class="sj-grid">

            <div class="sj-grid-card">
                <h4>
                    <i class="fas fa-minus"></i>
                    Electron
                </h4>
                <p>
                    Relative charge: <strong>−1</strong>.
                    Charge is approximately
                    −1.602 × 10<sup>−19</sup> C.
                </p>
            </div>

            <div class="sj-grid-card">
                <h4>
                    <i class="fas fa-circle"></i>
                    Thomson Model
                </h4>
                <p>
                    The atom was pictured as a positively charged sphere
                    with electrons embedded throughout it.
                </p>
            </div>

            <div class="sj-grid-card">
                <h4>
                    <i class="fas fa-watermelon"></i>
                    Textbook Analogy
                </h4>
                <p>
                    The model is compared with a watermelon:
                    positive pulp and electrons represented by seeds.
                </p>
            </div>

        </div>

        <div class="sj-ibox info">
            <i class="fas fa-user-tie"
               style="color:#0284c7;font-size:1.4rem;"></i>

            <div>
                <strong style="display:block;margin-bottom:4px;color:#0369a1;">
                    Meet a Scientist: J. J. Thomson
                </strong>

                <p style="font-size:.9rem;margin-bottom:0;">
                    Thomson’s discovery of the electron showed that
                    atoms were not indivisible and led to new models
                    of atomic structure.
                </p>
            </div>
        </div>
        """
    ),

    (
        "3",
        "fa-bullseye",
        "Rutherford’s Gold Foil Experiment and Nuclear Model",
        """
        <p>
            In 1911, Geiger and Marsden, working under
            <strong>Ernest Rutherford</strong>, directed a narrow beam
            of positively charged alpha particles at a very thin
            sheet of gold foil.
        </p>

        <table class="sj-table">
            <thead>
                <tr>
                    <th>Observation</th>
                    <th>Conclusion</th>
                </tr>
            </thead>

            <tbody>
                <tr>
                    <td>Most alpha particles passed straight through.</td>
                    <td>
                        Most of the atom is
                        <strong>empty space</strong>.
                    </td>
                </tr>

                <tr>
                    <td>Some alpha particles were deflected.</td>
                    <td>
                        Positive charge is concentrated in
                        a small region.
                    </td>
                </tr>

                <tr>
                    <td>A very few bounced back sharply.</td>
                    <td>
                        The central region is extremely small,
                        dense and massive.
                    </td>
                </tr>
            </tbody>
        </table>

        <div class="sj-ibox caution">

            <i class="fas fa-circle-exclamation"
               style="color:#b91c1c;font-size:1.4rem;"></i>

            <div>
                <strong style="display:block;margin-bottom:4px;color:#991b1b;">
                    Rutherford’s Nuclear Model
                </strong>

                <p style="font-size:.9rem;margin-bottom:0;">
                    The atom contains a tiny, dense, positively charged
                    <strong>nucleus</strong>.
                    Most of the atom is empty space.
                </p>
            </div>

        </div>
        """
    ),

    (
        "4",
        "fa-circle-radiation",
        "Limitation of Rutherford’s Model and Bohr’s Model",
        """
        <p>
            Rutherford’s model could explain the nucleus but could not
            explain <strong>atomic stability</strong>.
            A charged electron moving in a curved path would be accelerating
            and, according to the classical picture, should lose energy.
        </p>

        <p>
            In 1913, <strong>Niels Bohr</strong> proposed that electrons
            occupy fixed circular paths called stationary states,
            orbits or shells. Each allowed shell has a definite energy.
        </p>

        <div class="sj-grid">

            <div class="sj-grid-card">
                <h4>
                    <i class="fas fa-circle-dot"></i>
                    K-shell
                </h4>
                <p>
                    First shell, n = 1, closest to the nucleus
                    and lowest in energy.
                </p>
            </div>

            <div class="sj-grid-card">
                <h4>
                    <i class="fas fa-layer-group"></i>
                    L, M, N
                </h4>
                <p>
                    Higher shells have higher energy:
                    K, L, M, N or n = 1, 2, 3, 4...
                </p>
            </div>

            <div class="sj-grid-card">
                <h4>
                    <i class="fas fa-bolt"></i>
                    Energy Change
                </h4>
                <p>
                    An electron changes shell by absorbing or releasing
                    energy equal to the difference between levels.
                </p>
            </div>

        </div>
        """
    ),

    (
        "5",
        "fa-scale-balanced",
        "Subatomic Particles and the Neutron",
        """
        <p>
            The nucleus contains almost all of an atom’s mass.
            Electrons are extremely light in comparison.
            In 1932, <strong>James Chadwick</strong> discovered
            the <strong>neutron</strong>, a neutral particle whose
            mass is nearly equal to that of a proton.
        </p>

        <table class="sj-table">
            <thead>
                <tr>
                    <th>Particle</th>
                    <th>Symbol</th>
                    <th>Relative Charge</th>
                    <th>Location</th>
                </tr>
            </thead>

            <tbody>
                <tr>
                    <td>Electron</td>
                    <td>e<sup>−</sup></td>
                    <td>−1</td>
                    <td>Outside nucleus</td>
                </tr>

                <tr>
                    <td>Proton</td>
                    <td>p<sup>+</sup></td>
                    <td>+1</td>
                    <td>Nucleus</td>
                </tr>

                <tr>
                    <td>Neutron</td>
                    <td>n<sup>0</sup></td>
                    <td>0</td>
                    <td>Nucleus</td>
                </tr>
            </tbody>
        </table>
        """
    ),

    (
        "6",
        "fa-hashtag",
        "Atomic Number and Mass Number",
        """
        <p>
            The <strong>atomic number (Z)</strong> is the number of
            protons in the nucleus. It uniquely identifies an element.
        </p>

        <p>
            The <strong>mass number (A)</strong> is the total number
            of protons and neutrons in the nucleus.
        </p>

        <div class="sj-grid">

            <div class="sj-grid-card">
                <h4>Atomic Number</h4>
                <p>
                    <strong>Z = number of protons</strong>
                </p>
                <p>
                    For a neutral atom:
                    electrons = protons = Z.
                </p>
            </div>

            <div class="sj-grid-card">
                <h4>Mass Number</h4>
                <p>
                    <strong>A = protons + neutrons</strong>
                </p>
                <p>
                    Therefore:
                    neutrons = A − Z.
                </p>
            </div>

            <div class="sj-grid-card">
                <h4>Standard Notation</h4>
                <p>
                    Carbon-12:
                    <strong><sup>12</sup><sub>6</sub>C</strong>
                </p>
                <p>
                    A is written above and Z below the symbol.
                </p>
            </div>

        </div>
        """
    ),

    (
        "7",
        "fa-layer-group",
        "Electronic Configuration: Bohr–Bury Rules",
        """
        <p>
            Bohr and Bury suggested rules for distributing electrons
            among shells. The maximum number of electrons in shell n is
            <strong>2n²</strong>.
        </p>

        <table class="sj-table">
            <thead>
                <tr>
                    <th>Shell</th>
                    <th>n</th>
                    <th>Maximum electrons</th>
                </tr>
            </thead>

            <tbody>
                <tr>
                    <td>K</td>
                    <td>1</td>
                    <td>2</td>
                </tr>

                <tr>
                    <td>L</td>
                    <td>2</td>
                    <td>8</td>
                </tr>

                <tr>
                    <td>M</td>
                    <td>3</td>
                    <td>18</td>
                </tr>

                <tr>
                    <td>N</td>
                    <td>4</td>
                    <td>32</td>
                </tr>
            </tbody>
        </table>

        <div class="sj-ibox info">

            <i class="fas fa-code-branch"
               style="color:#0284c7;font-size:1.4rem;"></i>

            <div>

                <strong style="display:block;margin-bottom:4px;color:#0369a1;">
                    Examples
                </strong>

                <p style="font-size:.9rem;margin-bottom:0;">
                    Na (Z = 11) → <strong>2, 8, 1</strong>;
                    Mg (Z = 12) → <strong>2, 8, 2</strong>;
                    Cl (Z = 17) → <strong>2, 8, 7</strong>;
                    Ar (Z = 18) → <strong>2, 8, 8</strong>.
                </p>

            </div>
        </div>
        """
    ),

    (
        "8",
        "fa-link",
        "Valency and Combining Capacity",
        """
        <p>
            The outermost shell is the <strong>valence shell</strong>.
            Its electrons are called <strong>valence electrons</strong>.
        </p>

        <p>
            <strong>Valency</strong> is the combining capacity of an atom.
            It is related to the number of electrons gained, lost or shared
            to achieve a stable configuration.
        </p>

        <div class="sj-grid">

            <div class="sj-grid-card">
                <h4>Sodium: 2,8,1</h4>
                <p>
                    Loses one electron →
                    valency <strong>1</strong>.
                </p>
            </div>

            <div class="sj-grid-card">
                <h4>Oxygen: 2,6</h4>
                <p>
                    Gains two electrons →
                    valency <strong>2</strong>.
                </p>
            </div>

            <div class="sj-grid-card">
                <h4>Carbon: 2,4</h4>
                <p>
                    Shares four electrons →
                    valency <strong>4</strong>.
                </p>
            </div>

        </div>
        """
    ),

    (
        "9",
        "fa-clone",
        "Isotopes and Isobars",
        """
        <p>
            <strong>Isotopes</strong> are atoms of the same element
            having the same atomic number but different mass numbers.
        </p>

        <table class="sj-table">

            <thead>
                <tr>
                    <th>Example</th>
                    <th>Same</th>
                    <th>Different</th>
                </tr>
            </thead>

            <tbody>

                <tr>
                    <td>¹H, ²H, ³H</td>
                    <td>Atomic number = 1</td>
                    <td>Neutrons / mass number</td>
                </tr>

                <tr>
                    <td>¹²C, ¹³C, ¹⁴C</td>
                    <td>Atomic number = 6</td>
                    <td>Neutrons / mass number</td>
                </tr>

            </tbody>

        </table>

        <div class="sj-ibox discovery">

            <i class="fas fa-radiation"
               style="color:#0f9d8a;font-size:1.4rem;"></i>

            <div>

                <strong style="display:block;margin-bottom:4px;color:#0f9d8a;">
                    Isobars
                </strong>

                <p style="font-size:.9rem;margin-bottom:0;">
                    Atoms of different elements having the same mass number
                    but different atomic numbers are called
                    <strong>isobars</strong>.
                    Ca, K and Ar can have mass number 40.
                </p>

            </div>

        </div>
        """
    ),
]


def concepts_html():

    blocks = []

    for num, icon, title, body in CONCEPTS:

        blocks.append(
            f"""
<section class="sj-card">

    <div class="sj-cheader">

        <div class="sj-cicon">
            <i class="fas {icon}"></i>
        </div>

        <div>

            <small
                style="
                    color:#0f9d8a;
                    font-weight:800;
                    text-transform:uppercase;
                    font-size:.65rem;
                    display:block;
                "
            >
                Concept {num}
            </small>

            <h2>{title}</h2>

        </div>

    </div>

    {body}

</section>
"""
        )

    return "\n".join(blocks)


# ================================================================
# NCERT
#
# IMPORTANT:
# The structure intentionally follows Chapter 1:
#
# sj-card
#   sj-cheader
#   intro
#   sj-faq-item
#      question + marks
#      details
#         Model Answer
#         Marking Scheme Tips
#
# ================================================================

NCERT = [

    (
        1,
        "Choose the correct options related to Rutherford’s gold foil experiment.",
        [
            "The experiment clearly showed the existence of neutrons in the nucleus.",
            "The results disproved the plum pudding model and led to the idea of a nucleus.",
            "Large deflections indicated that positive charge and most of the mass are concentrated in a tiny region.",
            "The experiment directly established the fixed orbits of electrons."
        ],
        """
        <p>
            The correct statements are <strong>(ii)</strong> and
            <strong>(iii)</strong>.
        </p>

        <p>
            Rutherford’s experiment showed that the atom has a tiny,
            dense, positively charged nucleus and that most of the atom
            is empty space. It did not discover the neutron and did not
            establish Bohr’s fixed electron orbits.
        </p>
        """,
        "4"
    ),

    (
        2,
        "Which statement is correct according to Bohr’s atomic model?",
        [
            "Electrons continuously lose energy and fall into the nucleus.",
            "Electrons can exist at any arbitrary energy.",
            "Electrons occupy allowed stationary energy levels without continuously losing energy.",
            "Electrons must remain between two energy levels."
        ],
        """
        <p>
            Only <strong>(iii)</strong> is correct.
        </p>

        <p>
            In Bohr’s model, electrons occupy specific allowed energy
            levels. While remaining in a stationary state they do not
            continuously lose energy.
        </p>
        """,
        "4"
    ),

    (
        3,
        "The nuclei of X, Y and Z contain X = 18 protons, 19 neutrons; Y = 17 protons, 18 neutrons; Z = 17 protons, 20 neutrons. Find the relation between Y and Z and between Z and X.",
        [],
        """
        <p>
            For Y:
            A = 17 + 18 = <strong>35</strong>.
        </p>

        <p>
            For Z:
            A = 17 + 20 = <strong>37</strong>.
        </p>

        <p>
            Y and Z have the same atomic number but different mass
            numbers. Therefore, they are <strong>isotopes</strong>.
        </p>

        <p>
            X has A = 18 + 19 = <strong>37</strong>.
            Z also has A = 37, but their atomic numbers differ.
            Therefore, Z and X are <strong>isobars</strong>.
        </p>
        """,
        "3"
    ),

    (
        4,
        "What conclusion did Rutherford draw from the alpha particles that were deflected through large angles or bounced back?",
        [],
        """
        <p>
            The positive charge and almost all the mass of the atom are
            concentrated in an extremely small, dense central region
            called the <strong>nucleus</strong>.
        </p>
        """,
        "2"
    ),

    (
        5,
        "Arrange the atomic models chronologically: Dalton, Thomson, Rutherford and Bohr.",
        [],
        """
        <p>
            The correct chronological order is:
        </p>

        <p>
            <strong>
                Dalton → Thomson → Rutherford → Bohr
            </strong>
        </p>

        <p>
            Dalton proposed the indivisible atom, Thomson proposed the
            plum pudding model, Rutherford proposed the nuclear model,
            and Bohr introduced fixed energy levels.
        </p>
        """,
        "2"
    ),

    (
        6,
        "Electrons move around the nucleus. Why do they not fly away from the atom?",
        [],
        """
        <p>
            The negatively charged electron is attracted towards the
            positively charged nucleus.
        </p>

        <p>
            In Bohr’s model, electrons remain in permitted stationary
            energy levels rather than continuously losing energy and
            collapsing into the nucleus.
        </p>
        """,
        "2"
    ),

    (
        7,
        "Assertion (A): The discovery of subatomic particles helped in understanding atomic structure. Reason (R): The number of electrons is equal to the number of protons in a neutral atom.",
        [],
        """
        <p>
            Both A and R are true for a neutral atom, but R is not the
            correct explanation of A.
        </p>

        <p>
            Therefore, the correct option is
            <strong>(ii)</strong>.
        </p>
        """,
        "2"
    ),

    (
        8,
        "For magnesium with mass number 24 and atomic number 12, determine protons, neutrons, electrons and electronic arrangement.",
        [],
        """
        <p>
            Atomic number Z = 12, therefore:
        </p>

        <p>
            Protons = <strong>12</strong>
        </p>

        <p>
            For a neutral atom:
            Electrons = <strong>12</strong>
        </p>

        <p>
            Neutrons = A − Z
            = 24 − 12
            = <strong>12</strong>
        </p>

        <p>
            Electronic configuration:
            <strong>2, 8, 2</strong>
        </p>
        """,
        "3"
    ),

    (
        9,
        "For the elements shown in Fig. 8.17, identify their name, symbol, electrons, valence electrons, valency, protons and atomic number.",
        [],
        """
        <p>
            For a neutral atom:
        </p>

        <p>
            <strong>
                electrons = protons = atomic number
            </strong>
        </p>

        <p>
            The valence electrons are the electrons in the outermost
            occupied shell. Use the electron configuration shown in
            Fig. 8.17 to determine the valency.
        </p>
        """,
        "4"
    ),

    (
        10,
        "Why did Rutherford’s model fail to explain atomic stability while Bohr’s model succeeded?",
        [],
        """
        <p>
            Rutherford’s model did not explain why an accelerating
            electron would not continuously lose energy and spiral
            into the nucleus.
        </p>

        <p>
            Bohr introduced <strong>stationary energy levels</strong>.
            Electrons could remain in allowed energy levels without
            continuously losing energy.
        </p>
        """,
        "3"
    ),

    (
        11,
        "An atom ⁷⁰X has 31 electrons. How many neutrons are present?",
        [],
        """
        <p>
            For a neutral atom:
            protons = electrons = 31.
        </p>

        <p>
            Neutrons = A − Z
            = 70 − 31
            = <strong>39</strong>.
        </p>
        """,
        "2"
    ),

    (
        12,
        "An atom has 79 protons and mass number 197. Find the number of neutrons and electrons.",
        [],
        """
        <p>
            Neutrons:
            197 − 79 = <strong>118</strong>.
        </p>

        <p>
            For a neutral atom:
            electrons = protons = <strong>79</strong>.
        </p>
        """,
        "2"
    ),

    (
        13,
        "Complete Table 8.5 using atomic number, mass number, neutrons, protons, electrons and element name.",
        [],
        """
        <p>
            Use:
        </p>

        <p>
            <strong>Z = protons = electrons</strong>
        </p>

        <p>
            and
        </p>

        <p>
            <strong>A = protons + neutrons</strong>.
        </p>

        <p>
            The missing quantities can therefore be obtained directly
            from the given entries.
        </p>
        """,
        "4"
    ),

    (
        14,
        "An element X has mass number 35 and contains 18 neutrons. Find its electrons, protons, atomic number, identity, electronic configuration, valence electrons and the relation of the new atom formed by adding two neutrons.",
        [],
        """
        <p>
            Protons:
            35 − 18 = <strong>17</strong>.
        </p>

        <p>
            For a neutral atom, electrons = <strong>17</strong>.
        </p>

        <p>
            Atomic number = <strong>17</strong>, so X is
            <strong>chlorine (Cl)</strong>.
        </p>

        <p>
            Electronic configuration:
            <strong>2, 8, 7</strong>.
        </p>

        <p>
            Valence electrons = <strong>7</strong>.
        </p>

        <p>
            Adding two neutrons gives mass number:
            35 + 2 = <strong>37</strong>.
        </p>

        <p>
            The new atom is an <strong>isotope</strong> of X.
        </p>
        """,
        "5"
    ),

    (
        15,
        "An atom has 12 protons and 12 neutrons. If all electrons are replaced by hypothetical particles having the same charge as electrons but 500 times greater mass, what changes?",
        [],
        """
        <p>
            Atomic number remains <strong>12</strong> because atomic
            number depends only on the number of protons.
        </p>

        <p>
            Mass number remains <strong>24</strong> because mass number
            counts protons and neutrons.
        </p>

        <p>
            The actual mass of the atom would increase because the
            replacement particles are much heavier than electrons.
        </p>

        <p>
            Overall charge remains neutral because the replacement
            particles have the same charge as electrons.
        </p>
        """,
        "4"
    ),

    (
        16,
        "Find the number of electrons in the outermost shell of ¹²₆C, ¹⁹₉F and ²⁸₁₄Si.",
        [],
        """
        <p>
            Carbon:
            Z = 6 → configuration 2,4 →
            <strong>4</strong> outermost electrons.
        </p>

        <p>
            Fluorine:
            Z = 9 → configuration 2,7 →
            <strong>7</strong> outermost electrons.
        </p>

        <p>
            Silicon:
            Z = 14 → configuration 2,8,4 →
            <strong>4</strong> outermost electrons.
        </p>
        """,
        "3"
    ),

    (
        17,
        "Write the electronic configuration of the elements having atomic numbers 12, 16 and 18.",
        [],
        """
        <p>
            Z = 12:
            <strong>2, 8, 2</strong>
        </p>

        <p>
            Z = 16:
            <strong>2, 8, 6</strong>
        </p>

        <p>
            Z = 18:
            <strong>2, 8, 8</strong>
        </p>
        """,
        "3"
    ),

    (
        18,
        "An atom has mass number 23 and 11 protons. It is a soft metal that reacts vigorously with water. Identify it and find its neutrons.",
        [],
        """
        <p>
            Atomic number = 11.
            Therefore the element is
            <strong>sodium (Na)</strong>.
        </p>

        <p>
            Neutrons:
            23 − 11 = <strong>12</strong>.
        </p>

        <p>
            The clue about a soft metal reacting vigorously with water
            also agrees with sodium.
        </p>
        """,
        "3"
    ),
]


def ncert_html():

    blocks = []

    for qno, question, options, answer, marks in NCERT:

        option_html = ""

        if options:

            lis = "\n".join(
                f"<li>{esc(option)}</li>"
                for option in options
            )

            option_html = f"""
<div style="
    background:#f8fafc;
    padding:12px 15px;
    border-radius:8px;
    margin-top:10px;
">
    <strong>Statements / Options:</strong>
    <ol>
        {lis}
    </ol>
</div>
"""

        blocks.append(
            f"""
<div class="sj-faq-item"
     style="
        border-bottom:1px solid #e2e8f0;
        padding:20px 0;
     ">

    <div style="
        display:flex;
        justify-content:space-between;
        align-items:center;
        gap:12px;
    ">

        <h3 style="
            font-size:1.05rem;
            margin:0;
            font-family:'Outfit',sans-serif;
        ">
            Q{qno}. {question}
        </h3>

        <span class="marks-badge"
              style="
                background:#fef2f2;
                border:1px solid #fca5a5;
                color:#b91c1c;
                white-space:nowrap;
              ">
            {marks} Marks
        </span>

    </div>

    {option_html}

    <details style="margin-top:10px;cursor:pointer;">

        <summary style="
            color:#0ea5e9;
            font-weight:600;
            font-size:.9rem;
        ">
            View Ideal Answer & Marking Scheme
        </summary>

        <div style="
            background:#f8fafc;
            padding:15px;
            border-radius:8px;
            margin-top:10px;
            font-size:.95rem;
            line-height:1.5;
        ">

            <strong style="
                color:#0f172a;
                display:block;
                margin-bottom:6px;
            ">
                Model Answer:
            </strong>

            {answer}

            <strong style="
                color:#10b981;
                display:block;
                margin-top:10px;
            ">
                <i class="fas fa-check-circle"></i>
                Marking Scheme Tips:
            </strong>

            <p style="
                margin:4px 0 0 0;
                color:#065f46;
            ">
                Award marks for the correct scientific principle,
                logical reasoning, calculation and appropriate units
                according to the question.
            </p>

        </div>

    </details>

</div>
"""
        )

    return f"""
<section class="sj-card">

    <div class="sj-cheader">

        <div class="sj-cicon"
             style="color:#ef4444;">
            <i class="fas fa-pencil-ruler"></i>
        </div>

        <div>

            <small style="
                color:#ef4444;
                font-weight:800;
                text-transform:uppercase;
                font-size:.65rem;
                display:block;
            ">
                NCERT Exercises
            </small>

            <h2>Textbook Question Solutions</h2>

        </div>

    </div>

    <p>
        Verify your answers against standard solutions curated for
        Chapter 8. Expand each question to view the detailed model
        answer and marking guidance.
    </p>

    {''.join(blocks)}

</section>
"""


# ================================================================
# QUIZ DATA
#
# IMPORTANT:
# The Chapter 1 quiz ENGINE is retained.
# Only quizData is replaced.
# ================================================================

QUIZ = [

    {
        "question": "Q1. Who proposed the idea of extremely small particles called parmanus?",
        "options": [
            "Acharya Kanada",
            "J. J. Thomson",
            "Rutherford",
            "Bohr"
        ],
        "correctIdx": 0,
        "hint": "Think of the ancient Indian ideas discussed at the beginning of the chapter.",
        "explanations": [
            "Correct! Acharya Kanada described extremely small particles called parmanus.",
            "Incorrect. Thomson discovered the electron much later.",
            "Incorrect. Rutherford proposed the nuclear model.",
            "Incorrect. Bohr proposed fixed energy levels."
        ]
    },

    {
        "question": "Q2. Who discovered the electron through cathode-ray experiments?",
        "options": [
            "Dalton",
            "J. J. Thomson",
            "James Chadwick",
            "Niels Bohr"
        ],
        "correctIdx": 1,
        "hint": "Think of the scientist associated with cathode rays.",
        "explanations": [
            "Incorrect. Dalton proposed an early atomic theory.",
            "Correct! J. J. Thomson identified the electron in 1897.",
            "Incorrect. Chadwick discovered the neutron.",
            "Incorrect. Bohr developed the shell model."
        ]
    },

    {
        "question": "Q3. What did most alpha particles passing through gold foil indicate?",
        "options": [
            "The atom is completely solid",
            "Most of the atom is empty space",
            "The nucleus contains no charge",
            "Electrons are positively charged"
        ],
        "correctIdx": 1,
        "hint": "Most alpha particles passed through the foil without large deflections.",
        "explanations": [
            "Incorrect. The atom is not completely solid.",
            "Correct! Most of the atom is empty space.",
            "Incorrect. The nucleus is positively charged.",
            "Incorrect. Electrons carry negative charge."
        ]
    },

    {
        "question": "Q4. What did the few sharply deflected alpha particles suggest?",
        "options": [
            "A tiny dense nucleus",
            "A completely uniform atom",
            "No positive charge",
            "Electrons have most of the mass"
        ],
        "correctIdx": 0,
        "hint": "Large deflection requires strong repulsion from a concentrated positive region.",
        "explanations": [
            "Correct! The observations supported a tiny, dense, positively charged nucleus.",
            "Incorrect. A uniform charge distribution could not explain the observations.",
            "Incorrect. Positive charge is concentrated in the nucleus.",
            "Incorrect. Most of the mass is associated with the nucleus."
        ]
    },

    {
        "question": "Q5. Which model introduced electrons embedded in a positively charged sphere?",
        "options": [
            "Dalton",
            "Thomson",
            "Rutherford",
            "Bohr"
        ],
        "correctIdx": 1,
        "hint": "This is commonly called the plum pudding model.",
        "explanations": [
            "Incorrect. Dalton considered atoms indivisible.",
            "Correct! Thomson proposed the plum pudding model.",
            "Incorrect. Rutherford proposed the nuclear model.",
            "Incorrect. Bohr proposed fixed energy levels."
        ]
    },

    {
        "question": "Q6. Who discovered the neutron?",
        "options": [
            "Thomson",
            "Rutherford",
            "James Chadwick",
            "Dalton"
        ],
        "correctIdx": 2,
        "hint": "The neutron was discovered in 1932.",
        "explanations": [
            "Incorrect. Thomson discovered the electron.",
            "Incorrect. Rutherford established the nuclear model.",
            "Correct! James Chadwick discovered the neutron.",
            "Incorrect. Dalton proposed an early atomic theory."
        ]
    },

    {
        "question": "Q7. Atomic number Z is equal to the number of:",
        "options": [
            "Neutrons",
            "Protons",
            "Nucleons",
            "Shells"
        ],
        "correctIdx": 1,
        "hint": "Atomic number identifies an element.",
        "explanations": [
            "Incorrect. Neutrons can vary among isotopes.",
            "Correct! Atomic number is the number of protons.",
            "Incorrect. Nucleons are protons plus neutrons.",
            "Incorrect. Shell number is unrelated to atomic number."
        ]
    },

    {
        "question": "Q8. For a neutral atom, the number of electrons equals the number of:",
        "options": [
            "Neutrons",
            "Protons",
            "Mass number",
            "Shells"
        ],
        "correctIdx": 1,
        "hint": "A neutral atom has zero overall charge.",
        "explanations": [
            "Incorrect. Neutrons carry no charge.",
            "Correct! Positive proton charge balances negative electron charge.",
            "Incorrect. Mass number counts protons and neutrons.",
            "Incorrect. Shell count does not determine neutrality."
        ]
    },

    {
        "question": "Q9. Mass number A is equal to:",
        "options": [
            "p − n",
            "p + n",
            "e + n",
            "p + e"
        ],
        "correctIdx": 1,
        "hint": "Mass number counts nucleons.",
        "explanations": [
            "Incorrect. Mass number is not a difference.",
            "Correct! A = protons + neutrons.",
            "Incorrect. Electrons are not included in mass number.",
            "Incorrect. Mass number does not count electrons."
        ]
    },

    {
        "question": "Q10. Which formula gives the maximum number of electrons in shell n?",
        "options": [
            "n²",
            "2n",
            "2n²",
            "n/2"
        ],
        "correctIdx": 2,
        "hint": "Use the Bohr–Bury rule.",
        "explanations": [
            "Incorrect.",
            "Incorrect.",
            "Correct! Maximum electrons = 2n².",
            "Incorrect."
        ]
    },

    {
        "question": "Q11. The maximum number of electrons in the K shell is:",
        "options": [
            "1",
            "2",
            "8",
            "18"
        ],
        "correctIdx": 1,
        "hint": "For K shell, n = 1.",
        "explanations": [
            "Incorrect.",
            "Correct! 2(1)² = 2.",
            "Incorrect.",
            "Incorrect."
        ]
    },

    {
        "question": "Q12. The electronic configuration of sodium (Z = 11) is:",
        "options": [
            "2,7,2",
            "2,8,1",
            "8,2,1",
            "2,9"
        ],
        "correctIdx": 1,
        "hint": "Distribute 11 electrons beginning from the K shell.",
        "explanations": [
            "Incorrect.",
            "Correct! Sodium has configuration 2,8,1.",
            "Incorrect.",
            "Incorrect."
        ]
    },

    {
        "question": "Q13. The outermost occupied shell is called the:",
        "options": [
            "Nuclear shell",
            "Valence shell",
            "Mass shell",
            "Atomic shell"
        ],
        "correctIdx": 1,
        "hint": "It contains the valence electrons.",
        "explanations": [
            "Incorrect.",
            "Correct! The outermost occupied shell is the valence shell.",
            "Incorrect.",
            "Incorrect."
        ]
    },

    {
        "question": "Q14. Atoms of the same element with the same atomic number but different mass numbers are:",
        "options": [
            "Isobars",
            "Isotopes",
            "Ions",
            "Molecules"
        ],
        "correctIdx": 1,
        "hint": "Think of hydrogen-1, hydrogen-2 and hydrogen-3.",
        "explanations": [
            "Incorrect. Isobars have the same mass number.",
            "Correct! Same Z but different A means isotopes.",
            "Incorrect.",
            "Incorrect."
        ]
    },

    {
        "question": "Q15. Atoms of different elements having the same mass number are:",
        "options": [
            "Isotopes",
            "Isobars",
            "Ions",
            "Nucleons"
        ],
        "correctIdx": 1,
        "hint": "Calcium, potassium and argon can all have mass number 40.",
        "explanations": [
            "Incorrect.",
            "Correct! Same A but different Z means isobars.",
            "Incorrect.",
            "Incorrect."
        ]
    },

    {
        "question": "Q16. An atom has mass number 56 and atomic number 26. How many neutrons does it have?",
        "options": [
            "26",
            "30",
            "56",
            "82"
        ],
        "correctIdx": 1,
        "hint": "Use n = A − Z.",
        "explanations": [
            "Incorrect. 26 is the proton number.",
            "Correct! 56 − 26 = 30 neutrons.",
            "Incorrect.",
            "Incorrect."
        ]
    },

    {
        "question": "Q17. Which isotope is commonly associated with carbon dating?",
        "options": [
            "C-12",
            "C-13",
            "C-14",
            "C-16"
        ],
        "correctIdx": 2,
        "hint": "It is the radioactive carbon isotope used for dating ancient materials.",
        "explanations": [
            "Incorrect.",
            "Incorrect.",
            "Correct! Carbon-14 is used for dating ancient fossils and artefacts.",
            "Incorrect."
        ]
    },

    {
        "question": "Q18. Which shell has the lowest energy in Bohr’s model?",
        "options": [
            "K",
            "L",
            "M",
            "N"
        ],
        "correctIdx": 0,
        "hint": "The shell closest to the nucleus has the lowest energy.",
        "explanations": [
            "Correct! K is the first and lowest-energy shell.",
            "Incorrect.",
            "Incorrect.",
            "Incorrect."
        ]
    },

    {
        "question": "Q19. An atom has 17 protons and 18 neutrons. What are its atomic number and mass number?",
        "options": [
            "Z = 18, A = 35",
            "Z = 17, A = 35",
            "Z = 17, A = 18",
            "Z = 35, A = 17"
        ],
        "correctIdx": 1,
        "hint": "Z = protons and A = protons + neutrons.",
        "explanations": [
            "Incorrect.",
            "Correct! Z = 17 and A = 17 + 18 = 35.",
            "Incorrect.",
            "Incorrect."
        ]
    },

    {
        "question": "Q20. What is the electronic configuration of chlorine (Z = 17)?",
        "options": [
            "2,8,7",
            "2,7,8",
            "8,8,1",
            "2,9,6"
        ],
        "correctIdx": 0,
        "hint": "Distribute 17 electrons shell by shell.",
        "explanations": [
            "Correct! Chlorine has configuration 2,8,7.",
            "Incorrect.",
            "Incorrect.",
            "Incorrect."
        ]
    },

    {
        "question": "Q21. Which statement about isotopes is correct?",
        "options": [
            "They have different atomic numbers.",
            "They have the same atomic number but different mass numbers.",
            "They always have different chemical properties.",
            "They have the same number of neutrons."
        ],
        "correctIdx": 1,
        "hint": "The defining feature is same element but different neutron count.",
        "explanations": [
            "Incorrect. Isotopes have the same atomic number.",
            "Correct!",
            "Incorrect. Their chemical properties are generally similar because their electron configurations are the same.",
            "Incorrect. Their neutron numbers differ."
        ]
    },

    {
        "question": "Q22. What is the relation between ⁴⁰₂₀Ca and ⁴⁰₁₈Ar?",
        "options": [
            "Isotopes",
            "Isobars",
            "Ions",
            "Same element"
        ],
        "correctIdx": 1,
        "hint": "Compare A and Z.",
        "explanations": [
            "Incorrect.",
            "Correct! Same mass number but different atomic numbers means isobars.",
            "Incorrect.",
            "Incorrect."
        ]
    },

    {
        "question": "Q23. What happens to the mass number when two neutrons are added to an atom?",
        "options": [
            "It decreases by 2.",
            "It remains unchanged.",
            "It increases by 2.",
            "It doubles."
        ],
        "correctIdx": 2,
        "hint": "Mass number counts protons and neutrons.",
        "explanations": [
            "Incorrect.",
            "Incorrect.",
            "Correct! Adding two neutrons increases A by 2.",
            "Incorrect."
        ]
    },

    {
        "question": "Q24. Why do isotopes of an element generally have similar chemical properties?",
        "options": [
            "They have the same mass.",
            "They have the same electron configuration in neutral atoms.",
            "They have different atomic numbers.",
            "They have identical neutron numbers."
        ],
        "correctIdx": 1,
        "hint": "Chemical behaviour mainly depends on electrons, especially valence electrons.",
        "explanations": [
            "Incorrect. Their masses differ.",
            "Correct! Their neutral atoms have the same electron configuration.",
            "Incorrect.",
            "Incorrect."
        ]
    },

    {
        "question": "Q25. Which particle has no electrical charge?",
        "options": [
            "Electron",
            "Proton",
            "Neutron",
            "Positron"
        ],
        "correctIdx": 2,
        "hint": "It is located in the nucleus and is electrically neutral.",
        "explanations": [
            "Incorrect. Electron has charge −1.",
            "Incorrect. Proton has charge +1.",
            "Correct! The neutron has zero relative charge.",
            "Incorrect."
        ]
    },

    {
        "question": "Q26. Which sequence correctly represents the development of the major atomic models?",
        "options": [
            "Bohr → Dalton → Thomson → Rutherford",
            "Dalton → Thomson → Rutherford → Bohr",
            "Thomson → Dalton → Bohr → Rutherford",
            "Rutherford → Thomson → Dalton → Bohr"
        ],
        "correctIdx": 1,
        "hint": "Start with the indivisible atom and move toward energy levels.",
        "explanations": [
            "Incorrect.",
            "Correct! Dalton → Thomson → Rutherford → Bohr.",
            "Incorrect.",
            "Incorrect."
        ]
    },
]


# ================================================================
# REVISION
# ================================================================

REVISION = """
<section class="sj-card">

    <div class="sj-cheader">

        <div class="sj-cicon"
             style="color:#9333ea;">
            <i class="fas fa-bolt"></i>
        </div>

        <div>

            <small style="
                color:#9333ea;
                font-weight:800;
                text-transform:uppercase;
                font-size:.65rem;
                display:block;
            ">
                Summary
            </small>

            <h2>60-Second Chapter Summary</h2>

        </div>

    </div>

    <p>
        Revise the essential ideas of Journey Inside the Atom quickly.
    </p>

    <div class="sj-ibox info">

        <ul style="
            margin:0;
            padding-left:20px;
            font-size:.95rem;
            line-height:1.6;
        ">

            <li>
                Matter is made of extremely small particles called atoms.
            </li>

            <li>
                Acharya Kanada described <strong>parmanus</strong>;
                Greek thinkers used <strong>atomos</strong>.
            </li>

            <li>
                Dalton proposed an early scientific atomic theory.
            </li>

            <li>
                Thomson discovered the electron and proposed the
                plum pudding model.
            </li>

            <li>
                Rutherford’s gold foil experiment led to the nuclear model.
            </li>

            <li>
                Bohr introduced fixed energy levels or shells.
            </li>

            <li>
                Chadwick discovered the neutron.
            </li>

            <li>
                <strong>Z = number of protons.</strong>
            </li>

            <li>
                For a neutral atom:
                <strong>electrons = protons = Z.</strong>
            </li>

            <li>
                <strong>A = protons + neutrons.</strong>
            </li>

            <li>
                Therefore:
                <strong>neutrons = A − Z.</strong>
            </li>

            <li>
                Maximum electrons in shell n:
                <strong>2n².</strong>
            </li>

            <li>
                Isotopes:
                <strong>same Z, different A.</strong>
            </li>

            <li>
                Isobars:
                <strong>same A, different Z.</strong>
            </li>

        </ul>

    </div>

</section>


<section class="sj-card">

    <div class="sj-cheader">

        <div class="sj-cicon"
             style="color:#ef4444;">
            <i class="fas fa-brain"></i>
        </div>

        <div>

            <small style="
                color:#ef4444;
                font-weight:800;
                text-transform:uppercase;
                font-size:.65rem;
                display:block;
            ">
                Memory Hooks
            </small>

            <h2>Exam Memory Formulae</h2>

        </div>

    </div>

    <div class="sj-grid">

        <div class="sj-grid-card">
            <h4>Z = p = e</h4>
            <p>
                For a neutral atom, atomic number equals
                protons and electrons.
            </p>
        </div>

        <div class="sj-grid-card">
            <h4>A = p + n</h4>
            <p>
                Mass number equals protons plus neutrons.
            </p>
        </div>

        <div class="sj-grid-card">
            <h4>n = A − Z</h4>
            <p>
                Neutrons are obtained by subtracting atomic number
                from mass number.
            </p>
        </div>

        <div class="sj-grid-card">
            <h4>2n²</h4>
            <p>
                Maximum electrons permitted in shell n
                according to the stated Bohr–Bury rule.
            </p>
        </div>

    </div>

</section>


<section class="sj-card">

    <div class="sj-cheader">

        <div class="sj-cicon"
             style="color:#0f9d8a;">
            <i class="fas fa-table"></i>
        </div>

        <div>

            <small style="
                color:#0f9d8a;
                font-weight:800;
                text-transform:uppercase;
                font-size:.65rem;
                display:block;
            ">
                Quick Comparison
            </small>

            <h2>Atomic Models at a Glance</h2>

        </div>

    </div>

    <table class="sj-table">

        <thead>
            <tr>
                <th>Model</th>
                <th>Main Idea</th>
                <th>Major Limitation / Next Step</th>
            </tr>
        </thead>

        <tbody>

            <tr>
                <td>Dalton</td>
                <td>Atom as indivisible particle</td>
                <td>Subatomic particles were later discovered</td>
            </tr>

            <tr>
                <td>Thomson</td>
                <td>Positive sphere with embedded electrons</td>
                <td>Could not explain gold-foil scattering</td>
            </tr>

            <tr>
                <td>Rutherford</td>
                <td>Dense nucleus; mostly empty space</td>
                <td>Could not explain atomic stability</td>
            </tr>

            <tr>
                <td>Bohr</td>
                <td>Fixed shells / energy levels</td>
                <td>Later replaced by quantum mechanical model</td>
            </tr>

        </tbody>

    </table>

</section>


<section class="sj-card">

    <div class="sj-cheader">

        <div class="sj-cicon"
             style="color:#f59e0b;">
            <i class="fas fa-triangle-exclamation"></i>
        </div>

        <div>

            <small style="
                color:#f59e0b;
                font-weight:800;
                text-transform:uppercase;
                font-size:.65rem;
                display:block;
            ">
                Common Traps
            </small>

            <h2>Do Not Confuse These</h2>

        </div>

    </div>

    <div class="sj-ibox caution">

        <ul style="
            margin:0;
            padding-left:20px;
            line-height:1.7;
        ">

            <li>
                Atomic number is not the number of neutrons.
            </li>

            <li>
                Mass number is not the number of electrons.
            </li>

            <li>
                Isotopes have the same atomic number,
                not the same mass number.
            </li>

            <li>
                Isobars have the same mass number,
                not the same atomic number.
            </li>

            <li>
                Rutherford’s experiment did not discover the neutron.
            </li>

            <li>
                Bohr’s shell model is not identical to the modern
                quantum-mechanical electron-cloud model.
            </li>

        </ul>

    </div>

</section>
"""


# ================================================================
# TEST DATABASE
#
# THIS USES THE EXACT Chapter 1 TEST ENGINE.
#
# Required structure:
#   basic
#   standard
#   advanced
#
# Each:
#   3 MCQ × 1M
#   1 Assertion Reason × 1M
#   2 subjective × 2M
#   2 subjective × 3M
#   1 subjective × 5M
#   1 case × 5M
#
# Total = 24 marks.
# ================================================================

AR_OPTIONS = [
    "(A) Both Assertion (A) and Reason (R) are true and Reason (R) is the correct explanation of Assertion (A).",
    "(B) Both Assertion (A) and Reason (R) are true but Reason (R) is not the correct explanation of Assertion (A).",
    "(C) Assertion (A) is true but Reason (R) is false.",
    "(D) Assertion (A) is false but Reason (R) is true."
]


TESTS = {

    "basic": [

        {
            "type": "mcq",
            "marks": 1,
            "question": "Q1. What is the relative charge of an electron?",
            "options": ["−1", "0", "+1", "+2"],
            "correctIdx": 0
        },

        {
            "type": "mcq",
            "marks": 1,
            "question": "Q2. Who discovered the neutron?",
            "options": ["Dalton", "Chadwick", "Bohr", "Thomson"],
            "correctIdx": 1
        },

        {
            "type": "mcq",
            "marks": 1,
            "question": "Q3. Atomic number is equal to the number of:",
            "options": ["neutrons", "protons", "nucleons", "shells"],
            "correctIdx": 1
        },

        {
            "type": "ar",
            "marks": 1,
            "question": """Q4. Assertion & Reasoning:

Assertion (A): Rutherford’s experiment showed that most of the atom is empty space.

Reason (R): Most alpha particles passed through the gold foil without significant deflection.""",
            "options": AR_OPTIONS,
            "correctIdx": 0
        },

        {
            "type": "subjective",
            "marks": 2,
            "question": "Q5. What is atomic number? State its relation with protons.",
            "sampleAnswer": "Atomic number Z is the number of protons present in the nucleus of an atom. Therefore Z = number of protons."
        },

        {
            "type": "subjective",
            "marks": 2,
            "question": "Q6. Find the number of neutrons in an atom having A = 23 and Z = 11.",
            "sampleAnswer": "Neutrons = A − Z = 23 − 11 = 12."
        },

        {
            "type": "subjective",
            "marks": 3,
            "question": "Q7. Explain the main conclusion of Rutherford’s gold foil experiment.",
            "sampleAnswer": "Most of the atom is empty space. Positive charge and most of the mass are concentrated in a tiny, dense nucleus. A small number of alpha particles undergo large deflections because of strong repulsion from the concentrated positive nucleus."
        },

        {
            "type": "subjective",
            "marks": 3,
            "question": "Q8. Write the electronic configurations of Mg (Z = 12) and Cl (Z = 17).",
            "sampleAnswer": "Mg has 12 electrons: 2,8,2. Cl has 17 electrons: 2,8,7."
        },

        {
            "type": "subjective",
            "marks": 5,
            "question": "Q9. Explain isotopes and isobars with one example of each.",
            "sampleAnswer": "Isotopes are atoms of the same element having the same atomic number but different mass numbers, e.g. chlorine-35 and chlorine-37. Isobars are atoms of different elements having the same mass number but different atomic numbers, e.g. calcium-40 and argon-40."
        },

        {
            "type": "case",
            "marks": 5,
            "question": """Q10. Case-Based Passage:

An atom X has mass number 35 and contains 18 neutrons.

Sub-Questions:
1. Find the number of protons. (1 Mark)
2. Find the number of electrons in a neutral atom. (1 Mark)
3. Find its atomic number. (1 Mark)
4. Identify the element. (1 Mark)
5. Write its electronic configuration. (1 Mark)""",
            "sampleAnswer": """1. Protons = 35 − 18 = 17.
2. Electrons = 17 for a neutral atom.
3. Atomic number = 17.
4. Element = chlorine (Cl).
5. Electronic configuration = 2,8,7."""
        }
    ],


    "standard": [

        {
            "type": "mcq",
            "marks": 1,
            "question": "Q1. Which statement correctly describes Bohr’s model?",
            "options": [
                "Electrons can have any energy.",
                "Electrons occupy allowed stationary energy levels.",
                "The nucleus has no positive charge.",
                "Electrons are embedded in a positive sphere."
            ],
            "correctIdx": 1
        },

        {
            "type": "mcq",
            "marks": 1,
            "question": "Q2. An atom has A = 56 and Z = 26. How many neutrons does it contain?",
            "options": ["26", "30", "56", "82"],
            "correctIdx": 1
        },

        {
            "type": "mcq",
            "marks": 1,
            "question": "Q3. Which pair represents isobars?",
            "options": [
                "³⁵Cl and ³⁷Cl",
                "⁴⁰Ca and ⁴⁰Ar",
                "¹²C and ¹³C",
                "¹H and ²H"
            ],
            "correctIdx": 1
        },

        {
            "type": "ar",
            "marks": 1,
            "question": """Q4. Assertion & Reasoning:

Assertion (A): Isotopes of an element generally have similar chemical properties.

Reason (R): Neutral isotopes of an element have the same number of electrons and the same electronic configuration.""",
            "options": AR_OPTIONS,
            "correctIdx": 0
        },

        {
            "type": "subjective",
            "marks": 2,
            "question": "Q5. Differentiate between atomic number and mass number.",
            "sampleAnswer": "Atomic number Z is the number of protons. Mass number A is the total number of protons and neutrons. Thus Z identifies the element, while A gives the number of nucleons."
        },

        {
            "type": "subjective",
            "marks": 2,
            "question": "Q6. Explain why Rutherford’s model could not explain atomic stability.",
            "sampleAnswer": "According to classical physics, an accelerating charged electron should radiate energy and spiral into the nucleus. Rutherford’s model did not explain why this does not happen."
        },

        {
            "type": "subjective",
            "marks": 3,
            "question": "Q7. An atom has 17 protons and 18 neutrons. Find Z, A and the number of electrons in a neutral atom.",
            "sampleAnswer": "Z = 17. A = 17 + 18 = 35. A neutral atom has 17 electrons."
        },

        {
            "type": "subjective",
            "marks": 3,
            "question": "Q8. Explain why ³⁵Cl and ³⁷Cl are isotopes but ⁴⁰Ca and ⁴⁰Ar are isobars.",
            "sampleAnswer": "³⁵Cl and ³⁷Cl have the same atomic number 17 but different mass numbers, so they are isotopes. ⁴⁰Ca and ⁴⁰Ar have the same mass number 40 but different atomic numbers 20 and 18, so they are isobars."
        },

        {
            "type": "subjective",
            "marks": 5,
            "question": "Q9. Explain the development from Dalton’s model to Bohr’s model.",
            "sampleAnswer": """Dalton described atoms as indivisible particles. Thomson discovered electrons and proposed a positive sphere containing electrons. Rutherford’s experiment showed that positive charge and most mass are concentrated in a tiny nucleus. Rutherford’s model could not explain atomic stability. Bohr therefore proposed fixed energy levels or shells in which electrons could remain without continuously losing energy."""
        },

        {
            "type": "case",
            "marks": 5,
            "question": """Q10. Case-Based Passage:

An atom has atomic number 12 and mass number 24.

Sub-Questions:
1. Find the number of protons. (1 Mark)
2. Find the number of electrons in the neutral atom. (1 Mark)
3. Find the number of neutrons. (1 Mark)
4. Write the electronic configuration. (1 Mark)
5. State its common valency. (1 Mark)""",
            "sampleAnswer": """1. Protons = 12.
2. Electrons = 12.
3. Neutrons = 24 − 12 = 12.
4. Electronic configuration = 2,8,2.
5. Magnesium tends to lose two electrons, so its common valency is 2."""
        }
    ],


    "advanced": [

        {
            "type": "mcq",
            "marks": 1,
            "question": "Q1. Why does a very small number of alpha particles undergo large deflection in Rutherford’s experiment?",
            "options": [
                "They encounter a tiny, dense, positively charged nucleus.",
                "They collide with electrons having large mass.",
                "The entire atom is positively charged uniformly.",
                "Gold foil contains no empty space."
            ],
            "correctIdx": 0
        },

        {
            "type": "mcq",
            "marks": 1,
            "question": "Q2. An atom has 79 protons and mass number 197. How many neutrons does it have?",
            "options": ["79", "118", "197", "276"],
            "correctIdx": 1
        },

        {
            "type": "mcq",
            "marks": 1,
            "question": "Q3. An element has Z = 14. Which is its configuration and common valency?",
            "options": [
                "2,8,4; valency 4",
                "2,8,3; valency 3",
                "2,6,6; valency 2",
                "2,8,6; valency 2"
            ],
            "correctIdx": 0
        },

        {
            "type": "ar",
            "marks": 1,
            "question": """Q4. Assertion & Reasoning:

Assertion (A): Bohr’s model improved the explanation of atomic stability.

Reason (R): Bohr proposed that electrons could occupy specific stationary energy levels.""",
            "options": AR_OPTIONS,
            "correctIdx": 0
        },

        {
            "type": "subjective",
            "marks": 2,
            "question": "Q5. Explain why the atomic number remains unchanged when neutrons are added to an atom.",
            "sampleAnswer": "Atomic number is defined by the number of protons. Adding neutrons changes the mass number but does not change the number of protons. Therefore atomic number remains unchanged."
        },

        {
            "type": "subjective",
            "marks": 2,
            "question": "Q6. Why do isotopes have different physical properties but generally similar chemical properties?",
            "sampleAnswer": "Isotopes have different numbers of neutrons and therefore different masses, leading to differences in physical properties. Neutral isotopes have the same number and arrangement of electrons, so their chemical properties are generally similar."
        },

        {
            "type": "subjective",
            "marks": 3,
            "question": "Q7. Y has 17 protons and 20 neutrons while X has 18 protons and 19 neutrons. Determine their mass numbers and relationship.",
            "sampleAnswer": "Y: A = 17 + 20 = 37. X: A = 18 + 19 = 37. Their mass numbers are equal but their atomic numbers differ, so X and Y are isobars."
        },

        {
            "type": "subjective",
            "marks": 3,
            "question": "Q8. Explain why the discovery of subatomic particles forced scientists to modify Dalton’s atomic model.",
            "sampleAnswer": "Dalton considered atoms indivisible. Thomson discovered electrons, showing atoms contain smaller charged particles. Later Rutherford and Chadwick established the nucleus, protons and neutrons. Therefore the indivisible-atom picture had to be replaced by models describing internal atomic structure."
        },

        {
            "type": "subjective",
            "marks": 5,
            "question": "Q9. Compare Thomson, Rutherford and Bohr models with respect to charge distribution, electron arrangement and major limitation.",
            "sampleAnswer": """Thomson: positive charge was distributed through a sphere with electrons embedded in it; it could not explain the gold-foil observations.

Rutherford: positive charge and most mass were concentrated in a tiny nucleus and electrons surrounded it; it could not explain atomic stability.

Bohr: electrons occupied fixed energy levels or shells; this improved the explanation of atomic stability, although the model was later superseded by the quantum-mechanical model."""
        },

        {
            "type": "case",
            "marks": 5,
            "question": """Q10. Case-Based Passage:

Element X has mass number 37 and atomic number 17.

Sub-Questions:
1. Find the number of protons. (1 Mark)
2. Find the number of electrons in a neutral atom. (1 Mark)
3. Find the number of neutrons. (1 Mark)
4. Write its electronic configuration. (1 Mark)
5. If another atom has Z = 17 and A = 35, state the relationship between the two atoms. (1 Mark)""",
            "sampleAnswer": """1. Protons = 17.
2. Electrons = 17.
3. Neutrons = 37 − 17 = 20.
4. Configuration = 2,8,7.
5. Both atoms have Z = 17 but different mass numbers, so they are isotopes."""
        }
    ]
}


# ================================================================
# Metadata
# ================================================================

DESCRIPTIONS = {

    "concepts":
        "Detailed concepts for Class 9 Science Chapter 8 Journey Inside the Atom covering atomic models, subatomic particles, atomic number, mass number, electronic configuration, valency, isotopes and isobars.",

    "ncert-exercises":
        "NCERT exercise solutions for Class 9 Science Chapter 8 Journey Inside the Atom with model answers and marking guidance.",

    "quiz":
        "Interactive MCQ quiz for Class 9 Science Chapter 8 Journey Inside the Atom covering atomic models, subatomic particles, electronic configuration, valency, isotopes and isobars.",

    "tests":
        "Basic, Standard and Advanced chapter tests for Class 9 Science Chapter 8 Journey Inside the Atom.",

    "revision-notes":
        "Quick revision notes, formulas, comparisons and common exam traps for Class 9 Science Chapter 8 Journey Inside the Atom."
}


# ================================================================
# Basic metadata replacement
# ================================================================

def update_metadata(doc, page_type):

    canonical = (
        f"https://sjmaths.com/class-9-science/"
        f"{CH8_FOLDER}/{page_type}/"
    )

    description = DESCRIPTIONS[page_type]

    doc = re.sub(
        r"<title>.*?</title>",
        (
            f"<title>"
            f"{esc(TITLE)} | Class 9 Science Ch {CHAPTER} | SJMaths"
            f"</title>"
        ),
        doc,
        count=1,
        flags=re.S
    )

    doc = re.sub(
        r'<meta name="description" content=".*?">',
        f'<meta name="description" content="{esc(description)}">',
        doc,
        count=1,
        flags=re.S
    )

    doc = re.sub(
        r'<link rel="canonical" href=".*?">',
        f'<link rel="canonical" href="{canonical}">',
        doc,
        count=1,
        flags=re.S
    )

    # JSON-LD headline
    doc = re.sub(
        r'"headline"\s*:\s*".*?"',
        (
            f'"headline": '
            f'"{esc(TITLE)} | Class 9 Science Chapter {CHAPTER}"'
        ),
        doc,
        count=1,
        flags=re.S
    )

    # JSON-LD description
    doc = re.sub(
        r'"description"\s*:\s*".*?"',
        (
            '"description": '
            f'"{esc(description)}"'
        ),
        doc,
        count=1,
        flags=re.S
    )

    # JSON-LD URL
    doc = re.sub(
        r'"url"\s*:\s*"https://sjmaths\.com/class-9-science/.*?"',
        f'"url": "{canonical}"',
        doc,
        count=1,
        flags=re.S
    )

    return doc


# ================================================================
# Breadcrumb / top navigation
#
# Same Chapter 1 classes.
# ================================================================

def replace_tbar(doc, page_type):

    prev, nxt = PAGE_NAV[page_type]

    label_map = {
        "concepts": "Concepts",
        "ncert-exercises": "NCERT Solutions",
        "quiz": "Quiz",
        "tests": "Tests",
        "revision-notes": "Revision"
    }

    label = label_map[page_type]

    tbar = f"""
<nav class="sj-tbar">

    <div class="sj-bcrumb">

        <a href="/">Home</a>

        <i class="fas fa-chevron-right"
           style="font-size:0.4rem;"></i>

        <a href="/class-9-science/">
            Class 9 Science
        </a>

        <i class="fas fa-chevron-right"
           style="font-size:0.4rem;"></i>

        <a href="../index.html">
            {TITLE}
        </a>

        <i class="fas fa-chevron-right"
           style="font-size:0.4rem;"></i>

        <span style="color:#0f9d8a;">
            {label}
        </span>

    </div>

    <div class="sj-nav">
        {prev}
        {nxt}
    </div>

</nav>
"""

    doc = re.sub(
        r'<nav class="sj-tbar">.*?</nav>',
        tbar.strip(),
        doc,
        count=1,
        flags=re.S
    )

    # Chapter 1 uses exactly six section links.
    section_nav = f"""
<nav class="sj-section-nav">

    <a href="../index.html"
       class="sj-section-link">
        Overview
    </a>

    <a href="../concepts/"
       class="sj-section-link{' active' if page_type == 'concepts' else ''}">
        Concepts
    </a>

    <a href="../ncert-exercises/"
       class="sj-section-link{' active' if page_type == 'ncert-exercises' else ''}">
        NCERT
    </a>

    <a href="../quiz/"
       class="sj-section-link{' active' if page_type == 'quiz' else ''}">
        Quiz
    </a>

    <a href="../tests/"
       class="sj-section-link{' active' if page_type == 'tests' else ''}">
        Tests
    </a>

    <a href="../revision-notes/"
       class="sj-section-link{' active' if page_type == 'revision-notes' else ''}">
        Revision
    </a>

</nav>
"""

    doc = re.sub(
        r'<nav class="sj-section-nav">.*?</nav>',
        section_nav.strip(),
        doc,
        count=1,
        flags=re.S
    )

    return doc


# ================================================================
# Replace only sj-page-content
#
# IMPORTANT:
# We do NOT remove body scripts.
# ================================================================

def replace_page_content(doc, content, page_type):

    marker = '<div class="sj-page-content">'

    start = doc.find(marker)

    if start == -1:
        raise RuntimeError(
            f"Could not find sj-page-content in {page_type} template."
        )

    # Find bottom navigation.
    bottom = doc.find('<div class="sj-bottom-nav">', start)

    # Some Chapter 1 files may not contain bottom nav.
    if bottom == -1:
        footer = doc.find('<div id="footer-container">', start)

        if footer == -1:
            raise RuntimeError(
                f"Could not locate page boundary in {page_type}."
            )

        prefix = doc[:start]

        return (
            prefix
            + '<div class="sj-page-content">\n'
            + content
            + '\n</div>\n'
            + doc[footer:]
        )

    prefix = doc[:start]

    bottom_nav = (
        '<div class="sj-bottom-nav">\n'
        f'    {BOTTOM_NAV[page_type][0]}\n'
        f'    {BOTTOM_NAV[page_type][1]}\n'
        '</div>'
    )

    # Find closing sj-container immediately after bottom nav.
    after_bottom = doc.find("</div>", bottom)

    if after_bottom == -1:
        raise RuntimeError(
            f"Could not find closing container after bottom nav: {page_type}"
        )

    suffix = doc[after_bottom + len("</div>"):]

    return (
        prefix
        + '<div class="sj-page-content">\n'
        + content
        + '\n</div>\n\n'
        + bottom_nav
        + '\n</div>'
        + suffix
    )


# ================================================================
# QUIZ
#
# Do NOT replace page HTML.
#
# Keep the EXACT Chapter 1 quiz page.
# Only replace:
#
#       var quizData = [...]
#
# ================================================================

def replace_quiz_data(doc):

    start_token = "var quizData = ["
    start = doc.find(start_token)

    if start == -1:
        raise RuntimeError(
            "Chapter 1 quiz template does not contain "
            "'var quizData = ['."
        )

    end_token = "\n            ];"
    end = doc.find(end_token, start)

    if end == -1:
        # fallback
        end = doc.find("];", start)

        if end == -1:
            raise RuntimeError(
                "Could not find end of Chapter 1 quizData array."
            )

        end += 2

    else:
        end += len(end_token)

    replacement = (
        "var quizData = "
        + js(QUIZ)
        + ";"
    )

    return doc[:start] + replacement + doc[end:]


def update_quiz_visible_text(doc):

    # Keep Chapter 1's exact quiz UI wording:
    # Chapter Quiz / Quick Practice Quiz /
    # Instant feedback / Short hints.

    # Replace metadata-like text only.
    doc = doc.replace(
        "Exploration: Interactive Quiz - MCQs | Class 9 Science Ch 1",
        "Journey Inside the Atom: Interactive Quiz | Class 9 Science Ch 8"
    )

    doc = doc.replace(
        "Exploration: Interactive Quiz MCQs | Class 9 Science Chapter 1",
        "Journey Inside the Atom: Interactive Quiz MCQs | Class 9 Science Chapter 8"
    )

    # Change breadcrumb only.
    doc = re.sub(
        r'<a href="\.\./index\.html">Exploration</a>',
        f'<a href="../index.html">{TITLE}</a>',
        doc,
        count=1
    )

    return doc


# ================================================================
# TESTS
#
# Keep EXACT Chapter 1 HTML, CSS and JS engine.
# Only replace testsDatabase.
# ================================================================

def replace_tests_database(doc):

    start_token = "var testsDatabase = {"
    start = doc.find(start_token)

    if start == -1:
        raise RuntimeError(
            "Chapter 1 test template does not contain testsDatabase."
        )

    end_token = "\n        var activeTestLevel"

    end = doc.find(end_token, start)

    if end == -1:
        raise RuntimeError(
            "Could not find end of Chapter 1 testsDatabase."
        )

    replacement = (
        "var testsDatabase = "
        + js(TESTS)
        + ";\n\n"
    )

    return doc[:start] + replacement + doc[end:]


def update_tests_visible_text(doc):

    doc = doc.replace(
        "Exploration: Chapter Tests | Class 9 Science Ch 1",
        "Journey Inside the Atom: Chapter Tests | Class 9 Science Ch 8"
    )

    doc = doc.replace(
        "Chapter tests for Exploration with Basic, Standard and Advanced difficulty levels.",
        "Chapter tests for Journey Inside the Atom with Basic, Standard and Advanced difficulty levels."
    )

    doc = re.sub(
        r'<a href="\.\./index\.html">Exploration</a>',
        f'<a href="../index.html">{TITLE}</a>',
        doc,
        count=1
    )

    # Keep Chapter 1's test-selection layout.
    # Only change the introductory content.
    doc = re.sub(
        r'(<div id="selection-area">.*?<p>).*?(</p>)',
        (
            r'\1'
            'Choose a test difficulty level. '
            'Each test is out of <strong>24 Marks</strong> and contains '
            '10 structured questions: 3 MCQs, 1 Assertion-Reasoning, '
            '2 Short Answer (2M), 2 Short Answer (3M), '
            '1 Long Answer (5M), and 1 Case-Based Question (5M).'
            r'\2'
        ),
        doc,
        count=1,
        flags=re.S
    )

    return doc


# ================================================================
# Page-specific builders
# ================================================================

def build_content_page(page_type, content):

    template = TEMPLATES[page_type]

    if not template.exists():
        raise FileNotFoundError(
            f"Missing Chapter 1 template:\n{template}"
        )

    doc = template.read_text(encoding="utf-8")

    doc = update_metadata(doc, page_type)

    doc = replace_tbar(doc, page_type)

    doc = replace_page_content(
        doc,
        content,
        page_type
    )

    marker = (
        f"\n<!-- ==================================================\n"
        f" SJMaths Class 9 Science\n"
        f" Chapter 8: Journey Inside the Atom\n"
        f" Page: {page_type}\n"
        f" UI source: Chapter 1 master template\n"
        f" ================================================== -->\n"
    )

    doc = doc.replace(
        "<body>",
        "<body>" + marker,
        1
    )

    output_dir = CH8 / page_type
    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    output = output_dir / "index.html"

    output.write_text(
        doc,
        encoding="utf-8"
    )

    print(f"✓ {output}")


# ================================================================
# QUIZ PAGE BUILDER
# ================================================================

def build_quiz_page():

    template = TEMPLATES["quiz"]

    if not template.exists():
        raise FileNotFoundError(
            f"Missing Chapter 1 quiz template:\n{template}"
        )

    doc = template.read_text(
        encoding="utf-8"
    )

    # Metadata.
    doc = update_metadata(
        doc,
        "quiz"
    )

    # Breadcrumb + section navigation.
    doc = replace_tbar(
        doc,
        "quiz"
    )

    # ONLY replace quizData.
    doc = replace_quiz_data(doc)

    doc = update_quiz_visible_text(doc)

    marker = (
        "\n<!-- ==================================================\n"
        " SJMaths Class 9 Science\n"
        " Chapter 8: Journey Inside the Atom\n"
        " Page: quiz\n"
        " UI ENGINE: COPIED DIRECTLY FROM CHAPTER 1\n"
        " ================================================== -->\n"
    )

    doc = doc.replace(
        "<body>",
        "<body>" + marker,
        1
    )

    output_dir = CH8 / "quiz"

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    output = output_dir / "index.html"

    output.write_text(
        doc,
        encoding="utf-8"
    )

    print(f"✓ {output}")


# ================================================================
# TEST PAGE BUILDER
# ================================================================

def build_tests_page():

    template = TEMPLATES["tests"]

    if not template.exists():
        raise FileNotFoundError(
            f"Missing Chapter 1 tests template:\n{template}"
        )

    doc = template.read_text(
        encoding="utf-8"
    )

    # Metadata.
    doc = update_metadata(
        doc,
        "tests"
    )

    # Breadcrumb + section navigation.
    doc = replace_tbar(
        doc,
        "tests"
    )

    # ONLY replace testsDatabase.
    doc = replace_tests_database(doc)

    doc = update_tests_visible_text(doc)

    marker = (
        "\n<!-- ==================================================\n"
        " SJMaths Class 9 Science\n"
        " Chapter 8: Journey Inside the Atom\n"
        " Page: tests\n"
        " UI ENGINE: COPIED DIRECTLY FROM CHAPTER 1\n"
        " ================================================== -->\n"
    )

    doc = doc.replace(
        "<body>",
        "<body>" + marker,
        1
    )

    output_dir = CH8 / "tests"

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    output = output_dir / "index.html"

    output.write_text(
        doc,
        encoding="utf-8"
    )

    print(f"✓ {output}")


# ================================================================
# Validation
#
# These checks make sure we did not accidentally introduce
# the previous custom UI.
# ================================================================

def validate_quiz(doc):

    forbidden = [
        "atom-quiz-option",
        "atom-quiz-exp",
        "atom-quiz-question",
        "atom-progress",
        "atom-score"
    ]

    for item in forbidden:
        if item in doc:
            raise RuntimeError(
                f"QUIZ VALIDATION FAILED: custom Chapter 8 "
                f"class detected: {item}"
            )

    required = [
        "quizData",
        "notebook-progress-bar",
        "notebook-q-indicator",
        "notebook-option-container",
        "notebook-action-btn",
        "Finish & See Insights"
    ]

    for item in required:
        if item not in doc:
            raise RuntimeError(
                f"QUIZ VALIDATION FAILED: Chapter 1 "
                f"element missing: {item}"
            )

    print("✓ Quiz UI validation passed.")


def validate_tests(doc):

    # These are genuinely old/custom Chapter 8 identifiers.
    # DO NOT flag Chapter 1's legitimate UI classes.
    forbidden = [
        "gradeAtomTest",
        "atom-test-card",
        "atom-test-option",
        "atom-test-question",
        "atom-test-scorecard",
    ]

    for item in forbidden:
        if item in doc:
            raise RuntimeError(
                f"TEST VALIDATION FAILED: old custom "
                f"Chapter 8 UI detected: {item}"
            )

    # These MUST exist because Chapter 8 is supposed to use
    # the actual Chapter 1 test engine.
    required = [
        "testsDatabase",
        "test-selection-grid",
        "sj-test-card",
        "startTest",
        "question-content-root",
        "interactive-test-card",
        "renderDynamicScorecard",
        "gradeSubjectiveFromScorecard",
        "finishAndShowScorecard",
    ]

    for item in required:
        if item not in doc:
            raise RuntimeError(
                f"TEST VALIDATION FAILED: Chapter 1 "
                f"engine element missing: {item}"
            )

    print("✓ Tests UI validation passed.")


# ================================================================
# MAIN
# ================================================================

def main():

    print()
    print("=" * 76)
    print(" SJMaths — Class 9 Science Chapter 8")
    print(" Journey Inside the Atom")
    print()
    print(" MASTER UI/UX: Chapter 1")
    print(" CONTENT:     Chapter 8")
    print("=" * 76)
    print()

    # ------------------------------------------------------------
    # Verify folders.
    # ------------------------------------------------------------

    if not CH1.exists():
        raise FileNotFoundError(
            f"Chapter 1 folder not found:\n{CH1}"
        )

    if not CH8.exists():
        raise FileNotFoundError(
            f"Chapter 8 folder not found:\n{CH8}\n\n"
            f"Expected folder:\n{CH8_FOLDER}"
        )

    # ------------------------------------------------------------
    # Verify every Chapter 1 template.
    # ------------------------------------------------------------

    print("Checking Chapter 1 master templates...")
    print()

    for page_type, path in TEMPLATES.items():

        if not path.exists():

            raise FileNotFoundError(
                f"Missing Chapter 1 template for "
                f"'{page_type}':\n{path}"
            )

        print(f"✓ {page_type}: {path}")

    print()

    # ------------------------------------------------------------
    # Concepts
    # ------------------------------------------------------------

    print("STEP 1 — Concepts")
    print("-" * 76)

    build_content_page(
        "concepts",
        concepts_html()
    )

    print()

    # ------------------------------------------------------------
    # NCERT
    # ------------------------------------------------------------

    print("STEP 2 — NCERT Exercises")
    print("-" * 76)

    build_content_page(
        "ncert-exercises",
        ncert_html()
    )

    print()

    # ------------------------------------------------------------
    # Quiz
    #
    # IMPORTANT:
    # No custom HTML engine.
    # Chapter 1 HTML + CSS + JS retained.
    # ------------------------------------------------------------

    print("STEP 3 — Quiz")
    print("-" * 76)

    quiz_template = TEMPLATES["quiz"].read_text(
        encoding="utf-8"
    )

    quiz_template = update_metadata(
        quiz_template,
        "quiz"
    )

    quiz_template = replace_tbar(
        quiz_template,
        "quiz"
    )

    quiz_template = replace_quiz_data(
        quiz_template
    )

    quiz_template = update_quiz_visible_text(
        quiz_template
    )

    validate_quiz(
        quiz_template
    )

    output_dir = CH8 / "quiz"

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    output = output_dir / "index.html"

    output.write_text(
        quiz_template,
        encoding="utf-8"
    )

    print(f"✓ {output}")

    print()

    # ------------------------------------------------------------
    # Revision
    # ------------------------------------------------------------

    print("STEP 4 — Revision Notes")
    print("-" * 76)

    build_content_page(
        "revision-notes",
        REVISION
    )

    print()

    # ------------------------------------------------------------
    # Tests
    #
    # IMPORTANT:
    # No custom test engine.
    # Chapter 1 HTML + CSS + JS retained.
    # ------------------------------------------------------------

    print("STEP 5 — Tests")
    print("-" * 76)

    tests_template = TEMPLATES["tests"].read_text(
        encoding="utf-8"
    )

    tests_template = update_metadata(
        tests_template,
        "tests"
    )

    tests_template = replace_tbar(
        tests_template,
        "tests"
    )

    tests_template = replace_tests_database(
        tests_template
    )

    tests_template = update_tests_visible_text(
        tests_template
    )

    validate_tests(
        tests_template
    )

    output_dir = CH8 / "tests"

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    output = output_dir / "index.html"

    output.write_text(
        tests_template,
        encoding="utf-8"
    )

    print(f"✓ {output}")

    # ------------------------------------------------------------
    # Final validation
    # ------------------------------------------------------------

    print()
    print("=" * 76)
    print("✓ CHAPTER 8 COMPLETE")
    print("=" * 76)
    print()

    print("Generated:")
    print("  chapter-8-journey-inside-atom/")
    print("      concepts/index.html")
    print("      ncert-exercises/index.html")
    print("      quiz/index.html")
    print("      tests/index.html")
    print("      revision-notes/index.html")
    print()

    print("MASTER UI/UX:")
    print("  ✓ Chapter 1 NCERT structure")
    print("  ✓ Chapter 1 Quiz HTML")
    print("  ✓ Chapter 1 Quiz CSS")
    print("  ✓ Chapter 1 Quiz JavaScript")
    print("  ✓ Chapter 1 Tests HTML")
    print("  ✓ Chapter 1 Tests CSS")
    print("  ✓ Chapter 1 Tests JavaScript")
    print("  ✓ Chapter 1 scorecard")
    print("  ✓ Chapter 1 subjective grading")
    print("  ✓ Chapter 1 responsive behaviour")
    print()

    print("IMPORTANT:")
    print("  Chapter 1 files were NOT modified.")
    print("  No custom atom-quiz-* UI was generated.")
    print("  No custom test engine was generated.")
    print("  Chapter 8 Quiz/Test engines come directly from Chapter 1.")
    print()


if __name__ == "__main__":
    main()