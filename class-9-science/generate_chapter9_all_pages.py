from pathlib import Path
import re
import json
import html


# ================================================================
# SJMaths — Class 9 Science — Chapter 9 Generator
# "Atomic Foundations of Matter"
#
# IMPORTANT:
# Chapter 1 is the MASTER UI/UX.
#
# This generator does NOT recreate the Quiz/Test UI.
# It takes the ACTUAL Chapter 1 HTML files and changes only:
#
#   • Chapter-specific metadata
#   • Breadcrumb / navigation text
#   • Chapter 9 content
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
# Therefore Chapter 9 inherits the EXACT Chapter 1 UI/UX.
# ================================================================


BASE = Path(__file__).resolve().parent

CH1_FOLDER = "chapter-1-exploration-entering-world-of-secondary-science"
CH8_FOLDER = "chapter-9-atomic-foundations-of-matter"

CH1 = BASE / CH1_FOLDER
CH8 = BASE / CH8_FOLDER


TITLE = "Atomic Foundations of Matter"
CHAPTER = 9

NEXT_FOLDER = "chapter-10-sound-waves-characteristics-and-applications"
NEXT_TITLE = "Ch 10: Sound Waves"


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
# CHAPTER 9 — CONCEPTS
#
# Content only.
# UI wrappers remain Chapter 1-compatible.
# ================================================================


CONCEPTS = [
    ("1","fa-scale-balanced","Law of Conservation of Mass","""
        <p>In a chemical reaction, matter is neither created nor destroyed. The total mass of the reactants is equal to the total mass of the products. This is the <strong>Law of Conservation of Mass</strong>, proposed by <strong>Antoine Lavoisier</strong> in 1789.</p>
        <div class="sj-grid">
            <div class="sj-grid-card"><h4>Closed System</h4><p>If no matter escapes, the measured mass before and after a reaction remains constant.</p></div>
            <div class="sj-grid-card"><h4>Open System</h4><p>If a gas escapes, the measured mass of the apparatus may decrease even though total matter is conserved.</p></div>
            <div class="sj-grid-card"><h4>Exam Formula</h4><p><strong>Total mass of reactants = Total mass of products</strong></p></div>
        </div>
        <div class="sj-ibox info"><i class="fas fa-flask" style="color:#0284c7;font-size:1.4rem;"></i><div><strong style="display:block;margin-bottom:4px;color:#0369a1;">Example</strong><p style="font-size:.9rem;margin-bottom:0;">4.0 g CaCO<sub>3</sub> + 2.92 g HCl gives products of 1.76 g CO<sub>2</sub> + 0.72 g H<sub>2</sub>O + 4.44 g CaCl<sub>2</sub>. Both sides total <strong>6.92 g</strong>.</p></div></div>

        <div class="sj-example">
        <h3>Given Example — Conservation of Mass</h3>
        <p><strong>Question:</strong> 4.0 g calcium carbonate reacts with 2.92 g hydrochloric acid. The products are 1.76 g carbon dioxide, 0.72 g water and 4.44 g calcium chloride. Verify the law.</p>
        <p><strong>Step 1:</strong> Total reactant mass = 4.0 + 2.92 = <strong>6.92 g</strong>.</p>
        <p><strong>Step 2:</strong> Total product mass = 1.76 + 0.72 + 4.44 = <strong>6.92 g</strong>.</p>
        <p><strong>Conclusion:</strong> Reactant mass = product mass, so the law is obeyed.</p>
        <p><strong>Exam trap:</strong> In an open vessel, an escaping gas can make the measured mass appear smaller. The law is not violated—the system was not closed.</p>
        </div>
    """),
    ("2","fa-balance-scale","Law of Constant Proportions","""
        <p>A pure compound always contains the same elements combined in a <strong>fixed ratio by mass</strong>, irrespective of its source or method of preparation. This is also called the <strong>Law of Definite Proportions</strong> or <strong>Proust's Law</strong>.</p>
        <table class="sj-table"><thead><tr><th>Compound</th><th>Mass ratio</th><th>Meaning</th></tr></thead><tbody>
        <tr><td>Water</td><td>H : O = 1 : 8</td><td>9 g water always contains 1 g H and 8 g O.</td></tr>
        <tr><td>NaCl</td><td>Na : Cl = 23 : 35.5</td><td>The ratio remains fixed in pure sodium chloride.</td></tr>
        </tbody></table>
        <div class="sj-ibox discovery"><i class="fas fa-lightbulb" style="color:#0f9d8a;font-size:1.4rem;"></i><div><strong style="display:block;margin-bottom:4px;color:#0f9d8a;">Compound vs Mixture</strong><p style="font-size:.9rem;margin-bottom:0;">The fixed mass ratio applies to a <strong>compound</strong>, not to a mixture whose components can be present in variable proportions.</p></div></div>

        <div class="sj-example">
        <h3>Given Example — Fixed Mass Ratio</h3>
        <p><strong>Water:</strong> hydrogen : oxygen = <strong>1 : 8</strong> by mass. Therefore, 9 g pure water contains 1 g H and 8 g O, regardless of whether the water came from a river, borewell or ocean after purification.</p>
        <p><strong>Numerical example:</strong> NaCl has Na : Cl = 23 : 35.5. For 46 g Na, chlorine required = (35.5/23) × 46 = <strong>71 g</strong>.</p>
        <p><strong>Exam trick:</strong> First identify the fixed ratio, then multiply/divide both terms by the same factor.</p>
        </div>
    """),
    ("3","fa-atom","Dalton's Atomic Theory","""
        <p><strong>John Dalton</strong> used the two laws above to develop an atomic theory in which chemical reactions involve the rearrangement of atoms.</p>
        <div class="sj-grid">
            <div class="sj-grid-card"><h4>Atoms</h4><p>All matter is made of very tiny particles called atoms.</p></div>
            <div class="sj-grid-card"><h4>Conservation</h4><p>Atoms are not created or destroyed in a chemical reaction.</p></div>
            <div class="sj-grid-card"><h4>Elements</h4><p>Atoms of a given element were proposed to have identical mass and chemical properties; different elements have different masses and properties.</p></div>
            <div class="sj-grid-card"><h4>Compounds</h4><p>Atoms combine in simple whole-number ratios and the relative number and kinds of atoms are constant in a compound.</p></div>
        </div>
        <div class="sj-ibox caution"><i class="fas fa-circle-exclamation" style="color:#b91c1c;font-size:1.4rem;"></i><div><strong style="display:block;margin-bottom:4px;color:#991b1b;">Modern perspective</strong><p style="font-size:.9rem;margin-bottom:0;">The chapter presents Dalton's postulates as the historical basis of modern atomic theory. Later discoveries show that atoms contain subatomic particles and that atoms of an element can differ in mass.</p></div></div>

        <div class="sj-example">
        <h3>Given Example — Dalton's Theory in Action</h3>
        <p>Hydrogen and oxygen atoms combine to form water. The atoms are rearranged during the reaction; they are not simply created or destroyed. Similarly, magnesium atoms combine with oxygen atoms when magnesium burns to form magnesium oxide.</p>
        <p><strong>Exam focus:</strong> Dalton explains conservation through rearrangement of atoms and explains definite composition through fixed/simple whole-number combinations.</p>
        </div>
    """),
    ("4","fa-link","How Atoms Combine","""
        <p>Atoms combine because a more stable arrangement can result when their valence electrons are <strong>shared</strong> or <strong>transferred</strong>. The force holding atoms together is called a <strong>chemical bond</strong>.</p>
        <div class="sj-grid">
            <div class="sj-grid-card"><h4>Sharing</h4><p>Atoms share some or all valence electrons. This forms a <strong>covalent bond</strong>.</p></div>
            <div class="sj-grid-card"><h4>Transfer</h4><p>One atom loses electrons and another gains them. This forms ions and an <strong>ionic bond</strong>.</p></div>
            <div class="sj-grid-card"><h4>Molecule</h4><p>A molecule is an electrically neutral entity containing more than one atom, capable of independent existence and showing the properties of that substance.</p></div>
        </div>

        <div class="sj-example">
        <h3>Given Examples — Why Atoms Combine</h3>
        <p><strong>H + H → H₂:</strong> each H needs one more electron, so they share one pair.</p>
        <p><strong>Na + Cl → NaCl:</strong> Na transfers one electron to Cl; ions form and attract.</p>
        <p><strong>Key distinction:</strong> sharing → covalent bond; transfer → ionic bond.</p>
        </div>
    """),
    ("5","fa-share-nodes","Covalent Bonding: Molecules of Elements","""
        <p>A <strong>covalent bond</strong> forms when atoms share electron pairs. A single shared pair gives a <strong>single covalent bond</strong>; two shared pairs give a <strong>double bond</strong>.</p>
        <table class="sj-table"><thead><tr><th>Molecule</th><th>Valence idea</th><th>Structure</th><th>Bond</th></tr></thead><tbody>
        <tr><td>H<sub>2</sub></td><td>Each H needs one more electron for a duplet.</td><td><strong>H—H</strong></td><td>Single</td></tr>
        <tr><td>Cl<sub>2</sub></td><td>Each Cl has 7 valence electrons and needs 1.</td><td><strong>Cl—Cl</strong></td><td>Single</td></tr>
        <tr><td>O<sub>2</sub></td><td>Each O has 6 valence electrons and needs 2.</td><td><strong>O=O</strong></td><td>Double</td></tr>
        </tbody></table>

        <div class="sj-example">
        <h3>Given Examples — Single, Double and Triple Bond Logic</h3>
        <p><strong>H₂:</strong> H—H → one shared pair → single bond.</p>
        <p><strong>Cl₂:</strong> Cl—Cl → one shared pair → single bond.</p>
        <p><strong>O₂:</strong> O=O → two shared pairs → double bond.</p>
        <p><strong>N₂:</strong> N≡N → three shared pairs → triple bond. Nitrogen has five valence electrons and needs three more.</p>
        <p><strong>Shortcut:</strong> Number of shared electron pairs = bond order.</p>
        </div>
    """),
    ("6","fa-droplet","Covalent Compounds and Naming","""
        <p>Atoms of different elements can share electrons to form covalent compounds such as HCl and H<sub>2</sub>O. The formula shows the number of atoms of each element.</p>
        <p>Binary covalent compounds use prefixes such as <strong>mono-, di-, tri-, tetra-, penta-, hexa-</strong>. The first element keeps its usual name; the second generally ends in <strong>-ide</strong>.</p>
        <table class="sj-table"><thead><tr><th>Formula</th><th>Name</th></tr></thead><tbody>
        <tr><td>CO</td><td>carbon monoxide</td></tr>
        <tr><td>CO<sub>2</sub></td><td>carbon dioxide</td></tr>
        <tr><td>CS<sub>2</sub></td><td>carbon disulfide</td></tr>
        <tr><td>PCl<sub>3</sub></td><td>phosphorus trichloride</td></tr>
        <tr><td>SF<sub>6</sub></td><td>sulfur hexafluoride</td></tr>
        <tr><td>N<sub>2</sub>O<sub>4</sub></td><td>dinitrogen tetroxide</td></tr>
        </tbody></table>
        <div class="sj-ibox info"><i class="fas fa-language" style="color:#0284c7;font-size:1.4rem;"></i><div><strong style="display:block;margin-bottom:4px;color:#0369a1;">Special cases</strong><p style="font-size:.9rem;margin-bottom:0;">H<sub>2</sub>O is commonly called <strong>water</strong>, and NH<sub>3</sub> is commonly called <strong>ammonia</strong>.</p></div></div>

        <div class="sj-example">
        <h3>Given Examples — Covalent Naming</h3>
        <p>CO → <strong>carbon monoxide</strong>; CO₂ → <strong>carbon dioxide</strong>; CS₂ → <strong>carbon disulfide</strong>; PCl₃ → <strong>phosphorus trichloride</strong>; SF₆ → <strong>sulfur hexafluoride</strong>; N₂O₄ → <strong>dinitrogen tetroxide</strong>.</p>
        <p><strong>Rules:</strong> mono = 1, di = 2, tri = 3, tetra = 4, penta = 5, hexa = 6. Mono is usually omitted for the first element but used for the second. Drop the final vowel of a prefix before a vowel in cases such as <strong>monoxide</strong> and <strong>tetroxide</strong>.</p>
        <p><strong>Special:</strong> H₂O is commonly called water and NH₃ is commonly called ammonia.</p>
        </div>
    """),
    ("7","fa-bolt","Ionic Bonding: Electron Transfer","""
        <p>Atoms with fewer than four valence electrons generally tend to lose electrons, while atoms with more than four often gain or share electrons. Electron transfer can produce oppositely charged ions.</p>
        <div class="sj-grid">
            <div class="sj-grid-card"><h4>Cation</h4><p>Sodium loses one electron: Na → Na<sup>+</sup>. A cation is positively charged.</p></div>
            <div class="sj-grid-card"><h4>Anion</h4><p>Chlorine gains one electron: Cl → Cl<sup>−</sup>. An anion is negatively charged.</p></div>
            <div class="sj-grid-card"><h4>Ionic Bond</h4><p>The electrostatic attraction between oppositely charged ions.</p></div>
        </div>
        <p><strong>NaCl formation:</strong> Na transfers one electron to Cl, producing Na<sup>+</sup> and Cl<sup>−</sup>. Their attraction forms sodium chloride.</p>

        <div class="sj-example">
        <h3>Given Example — Formation of NaCl</h3>
        <p>Sodium has electronic configuration 2,8,1. It loses one electron:</p>
        <p><strong>Na → Na⁺ + e⁻</strong></p>
        <p>Chlorine has configuration 2,8,7. It gains that electron:</p>
        <p><strong>Cl + e⁻ → Cl⁻</strong></p>
        <p>Na⁺ and Cl⁻ attract electrostatically to form NaCl. The compound is electrically neutral because +1 + (−1) = 0.</p>
        <p><strong>Remember:</strong> loss of electron → positive ion; gain of electron → negative ion.</p>
        </div>
    """),
    ("8","fa-cubes-stacked","Ionic Crystal Structure and Ions","""
        <p>Ionic compounds generally form <strong>three-dimensional crystals</strong>, not individual molecules. In sodium chloride, each Na<sup>+</sup> is surrounded by six Cl<sup>−</sup> ions and each Cl<sup>−</sup> by six Na<sup>+</sup> ions in a repeating arrangement.</p>
        <table class="sj-table"><thead><tr><th>Ion type</th><th>Examples</th><th>Charge/valency</th></tr></thead><tbody>
        <tr><td>Monatomic cations</td><td>Na<sup>+</sup>, Mg<sup>2+</sup>, Al<sup>3+</sup>, Fe<sup>2+</sup>, Fe<sup>3+</sup></td><td>Positive</td></tr>
        <tr><td>Monatomic anions</td><td>F<sup>−</sup>, Cl<sup>−</sup>, O<sup>2−</sup>, S<sup>2−</sup></td><td>Negative</td></tr>
        <tr><td>Polyatomic ions</td><td>OH<sup>−</sup>, NO<sub>3</sub><sup>−</sup>, CO<sub>3</sub><sup>2−</sup>, SO<sub>4</sub><sup>2−</sup>, NH<sub>4</sub><sup>+</sup></td><td>Group charge</td></tr>
        </tbody></table>

        <div class="sj-example">
        <h3>Given Examples — Ions and Crystal Lattice</h3>
        <p>In NaCl, each Na⁺ is surrounded by six Cl⁻ ions and each Cl⁻ by six Na⁺ ions in a repeating 3-D pattern. Therefore, NaCl is represented by a <strong>formula unit</strong>, not an individual molecule.</p>
        <p>Examples of common ions from the chapter: Na⁺, K⁺, Ag⁺; Ca²⁺, Mg²⁺, Zn²⁺; Al³⁺; Fe²⁺/Fe³⁺; OH⁻, NO₃⁻, HCO₃⁻, CO₃²⁻, SO₄²⁻ and NH₄⁺.</p>
        </div>
    """),
    ("9","fa-pen-ruler","Writing Chemical Formulae","""
        <p>For both covalent and ionic compounds, the chapter gives a quick <strong>valency/charge crossover</strong> method. Always write the simplest whole-number ratio.</p>
        <div class="sj-grid">
            <div class="sj-grid-card"><h4>Covalent</h4><p>Write element symbols → write valencies → crossover the valencies as subscripts → omit subscript 1.</p></div>
            <div class="sj-grid-card"><h4>Ionic</h4><p>Write cation first → write anion → crossover charge numbers → simplify common factors.</p></div>
            <div class="sj-grid-card"><h4>Polyatomic ions</h4><p>Use brackets when two or more identical polyatomic ions occur, e.g. Mg(OH)<sub>2</sub> and Al(OH)<sub>3</sub>.</p></div>
        </div>
        <table class="sj-table"><thead><tr><th>Compound</th><th>Formula</th><th>Reason</th></tr></thead><tbody>
        <tr><td>Calcium chloride</td><td>CaCl<sub>2</sub></td><td>Ca<sup>2+</sup> needs two Cl<sup>−</sup>.</td></tr>
        <tr><td>Aluminium oxide</td><td>Al<sub>2</sub>O<sub>3</sub></td><td>Al<sup>3+</sup> and O<sup>2−</sup> balance in 2:3.</td></tr>
        <tr><td>Magnesium hydroxide</td><td>Mg(OH)<sub>2</sub></td><td>Mg<sup>2+</sup> needs two OH<sup>−</sup>.</td></tr>
        <tr><td>Calcium carbonate</td><td>CaCO<sub>3</sub></td><td>Ca<sup>2+</sup> and CO<sub>3</sub><sup>2−</sup> simplify to 1:1.</td></tr>
        </tbody></table>

        <div class="sj-example">
        <h3>Given Examples — Formula Writing</h3>
        <p><strong>CaCl₂:</strong> Ca²⁺ and Cl⁻ → crossover 2 and 1 → CaCl₂.</p>
        <p><strong>Al₂O₃:</strong> Al³⁺ and O²⁻ → crossover → Al₂O₃.</p>
        <p><strong>MgO:</strong> Mg²⁺ and O²⁻ initially gives Mg₂O₂, then divide by 2 → <strong>MgO</strong>.</p>
        <p><strong>Al(OH)₃:</strong> Al³⁺ needs three OH⁻ ions, so brackets are essential: <strong>Al(OH)₃</strong>, not AlOH₃.</p>
        <p><strong>CaCO₃:</strong> Ca²⁺ and CO₃²⁻ simplify to 1:1.</p>
        <p><strong>Exam check:</strong> Multiply charge × subscript. Total positive charge must equal total negative charge.</p>
        </div>
    """),
    ("10","fa-vial","Properties of Ionic and Covalent Compounds","""
        <p>The chapter compares ionic and covalent compounds through solubility, electrical conductivity and melting/boiling behaviour.</p>
        <table class="sj-table"><thead><tr><th>Property</th><th>Ionic compounds</th><th>Covalent compounds</th></tr></thead><tbody>
        <tr><td>Water solubility</td><td>Generally soluble</td><td>Many are insoluble; some such as sugar are soluble</td></tr>
        <tr><td>Kerosene/petrol</td><td>Generally insoluble</td><td>Many dissolve</td></tr>
        <tr><td>Solid-state conduction</td><td>No, ions are fixed</td><td>Generally do not conduct</td></tr>
        <tr><td>Aqueous conduction</td><td>Generally conduct because ions can move</td><td>Usually do not provide ions</td></tr>
        <tr><td>Melting/boiling points</td><td>Generally high</td><td>Usually low</td></tr>
        </tbody></table>

        <div class="sj-example">
        <h3>Given Example — Property Comparison</h3>
        <p>Sodium chloride and copper sulfate are generally soluble in water but insoluble in kerosene/petrol. Camphor and naphthalene are generally insoluble in water but dissolve in kerosene/petrol.</p>
        <p>Solid NaCl does not conduct because its ions are fixed. When dissolved in water, the ions can move and conduct electricity. Sugar may dissolve in water but does not produce ions, so its solution does not conduct electricity.</p>
        <p><strong>Exam trap:</strong> Solubility alone does not decide conductivity. Ask whether <strong>mobile charged particles</strong> are present.</p>
        </div>
    """),
    ("11","fa-calculator","Molecular Mass of Covalent Compounds","""
        <p><strong>Molecular mass</strong> is the total mass of all atoms present in one molecule, expressed in atomic mass units (u).</p>
        <div class="sj-grid">
            <div class="sj-grid-card"><h4>Water</h4><p>H<sub>2</sub>O = (1 × 2) + 16 = <strong>18 u</strong></p></div>
            <div class="sj-grid-card"><h4>Carbon dioxide</h4><p>CO<sub>2</sub> = 12 + (16 × 2) = <strong>44 u</strong></p></div>
            <div class="sj-grid-card"><h4>Nitric acid</h4><p>HNO<sub>3</sub> = 1 + 14 + (16 × 3) = <strong>63 u</strong></p></div>
        </div>
        <div class="sj-ibox caution"><i class="fas fa-circle-exclamation" style="color:#b91c1c;font-size:1.4rem;"></i><div><strong style="display:block;margin-bottom:4px;color:#991b1b;">Important distinction</strong><p style="font-size:.9rem;margin-bottom:0;">Ionic compounds do not form molecules; therefore their corresponding quantity is called <strong>formula unit mass</strong>.</p></div></div>

        <div class="sj-example">
        <h3>Given Examples — Molecular Mass</h3>
        <p><strong>H₂O:</strong> (1 × 2) + 16 = <strong>18 u</strong>.</p>
        <p><strong>CO₂:</strong> 12 + (16 × 2) = <strong>44 u</strong>.</p>
        <p><strong>HNO₃:</strong> 1 + 14 + (16 × 3) = <strong>63 u</strong>.</p>
        <p><strong>CH₄:</strong> 12 + (1 × 4) = <strong>16 u</strong>.</p>
        <p><strong>Method:</strong> multiply each atomic mass by its subscript, then add all contributions.</p>
        </div>
    """),
    ("12","fa-weight-hanging","Formula Unit Mass of Ionic Compounds","""
        <p>The <strong>formula unit</strong> is the simplest whole-number ratio of ions in an ionic compound. Its mass is the <strong>formula unit mass</strong>, found by adding the atomic masses represented in the formula unit.</p>
        <div class="sj-grid">
            <div class="sj-grid-card"><h4>Na<sub>2</sub>O</h4><p>(23 × 2) + 16 = <strong>62 u</strong></p></div>
            <div class="sj-grid-card"><h4>Ca(NO<sub>3</sub>)<sub>2</sub></h4><p>40 + 2(14 + 16 × 3) = <strong>164 u</strong></p></div>
            <div class="sj-grid-card"><h4>KCl</h4><p>39 + 35.5 = <strong>74.5 u</strong></p></div>
        </div>

        <div class="sj-example">
        <h3>Given Examples — Formula Unit Mass</h3>
        <p><strong>Na₂O:</strong> (23 × 2) + 16 = <strong>62 u</strong>.</p>
        <p><strong>Ca(NO₃)₂:</strong> 40 + 2(14 + 3×16) = <strong>164 u</strong>.</p>
        <p><strong>KCl:</strong> 39 + 35.5 = <strong>74.5 u</strong>.</p>
        <p><strong>Mg(OH)₂:</strong> 24 + 2(16 + 1) = <strong>58 u</strong>.</p>
        <p><strong>Rule:</strong> expand brackets carefully; the outside subscript multiplies every atom inside the bracket.</p>
        </div>
    """),
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
# NCERT — COMPLETE SOURCE COVERAGE: Questions 1–24 from the supplied Chapter 9 source.
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
(1,"A particular element A has one electron in its third shell. Another element B has six electrons in its second shell. Determine their electron gain/loss tendency, ions, bond and formula.",[], "<p>A has configuration 2,8,1, so it tends to <strong>lose one electron</strong> and forms A<sup>+</sup>. B has configuration 2,6, so it tends to <strong>gain two electrons</strong> and forms B<sup>2−</sup>. Their combination is by <strong>ionic bonding</strong>. Two A<sup>+</sup> ions combine with one B<sup>2−</sup>, so the formula is <strong>A<sub>2</sub>B</strong>.</p>","5"),
(2,"An element X has six electrons in its outer shell and forms a diatomic molecule. Explain why, state the bond, draw its structure, and describe the molecule formed with element Y having two electrons in its second shell.",[], "<p>X has six valence electrons and needs two more to complete its octet, so two X atoms share two pairs of electrons and form a diatomic molecule <strong>X=X</strong> with a double covalent bond. Y has configuration 2, so it tends to lose two electrons. With X, electron transfer gives an ionic compound with the simplest ratio <strong>YX</strong>.</p>","5"),
(3,"Which combination gives total positive charge 6+ and total negative charge 6−: (i) 2 Al3+ and 3 Cl−; (ii) 3 Mg2+ and 1 PO4 3−; (iii) 2 Fe3+ and 3 O2−; (iv) 3 Ca2+ and 2 SO4 2−?",["2 Al3+ and 3 Cl−","3 Mg2+ and 1 PO4 3−","2 Fe3+ and 3 O2−","3 Ca2+ and 2 SO4 2−"], "<p><strong>(i), (iii) and (iv)</strong> each give total positive charge 6+ and total negative charge 6−. In (ii), the positive charge is 6+ but the negative charge is only 3−.</p>","3"),
(4,"Choose the correct statement(s) and correct the false statements: (i) Elements are made up of molecules and compounds are made up of atoms. (ii) A compound molecule is always made of atoms of the same kind. (iii) One molecule of nitrogen gas contains three nitrogen atoms. (iv) Water contains two H atoms covalently bonded with one O atom.",[], "<p><strong>(iv) is correct.</strong> (i) is false: elements may exist as atoms or molecules, while compounds consist of atoms of different elements chemically combined. (ii) is false: a compound molecule contains atoms of different elements. (iii) is false: N<sub>2</sub> contains <strong>two</strong> nitrogen atoms.</p>","4"),
(5,"Write the chemical formulae for aluminium nitrate, calcium oxide and ferric oxide.",[], "<p>Al<sup>3+</sup> and NO<sub>3</sub><sup>−</sup> give <strong>Al(NO<sub>3</sub>)<sub>3</sub></strong>. Ca<sup>2+</sup> and O<sup>2−</sup> simplify to <strong>CaO</strong>. Fe<sup>3+</sup> and O<sup>2−</sup> give <strong>Fe<sub>2</sub>O<sub>3</sub></strong>.</p>","3"),
(6,"Write the formulae formed from Ca2+ and Br−; Al3+ and CO3 2−; K+ and SO4 2−; NH4+ and Cl−.",[], "<p>(i) <strong>CaBr<sub>2</sub></strong>; (ii) <strong>Al<sub>2</sub>(CO<sub>3</sub>)<sub>3</sub></strong>; (iii) <strong>K<sub>2</sub>SO<sub>4</sub></strong>; (iv) <strong>NH<sub>4</sub>Cl</strong>.</p>","4"),
(7,"Assertion: 2 g hydrogen combines with 16 g oxygen to form 18 g water. Reason: Dalton's theory states atoms combine in simple whole-number ratios by mass.",[], "<p>Both Assertion and Reason are true, and the Reason gives the basic atomic-theory explanation for fixed combination ratios. Therefore the correct option is <strong>(i)</strong>.</p>","2"),
(8,"Nitrogen has five valence electrons. Draw the structure of the nitrogen molecule N2.",[], "<p>Each nitrogen atom has five valence electrons and needs three more for an octet. Two nitrogen atoms therefore share three pairs of electrons, forming a <strong>triple covalent bond</strong>: <strong>N≡N</strong>.</p>","2"),
(9,"The atomic number of fluorine is 9. Explain the formation of the fluorine molecule F2.",[], "<p>Fluorine has configuration 2,7 and needs one electron to complete its octet. Two F atoms share one electron each, forming one shared pair and hence a <strong>single covalent bond</strong>: <strong>F—F</strong>.</p>","2"),
(10,"Show the formation of carbon dioxide CO2, hydrogen sulfide H2S and ammonia NH3.",[], "<p>Carbon has valency 4 and each oxygen has valency 2, giving <strong>O=C=O</strong>. Sulfur has valency 2 and two H atoms each contribute one shared electron pair, giving <strong>H—S—H</strong>. Nitrogen has valency 3 and forms three N—H bonds, giving <strong>NH<sub>3</sub></strong>.</p>","4"),
(11,"Neon has atomic number 10 and neither transfers nor shares its valence electrons. Explain.",[], "<p>Neon has electronic configuration <strong>2,8</strong>. Its valence shell is already complete, so it has no tendency to gain, lose or share electrons under ordinary conditions. Hence it is stable and does not normally form covalent or ionic bonds.</p>","2"),
(12,"What kind of ion will oxygen form?",[], "<p>Oxygen has six valence electrons and needs two more to complete its octet. It gains two electrons and forms the <strong>oxide ion O<sup>2−</sup></strong>.</p>","1"),
(13,"Complete: magnesium can give two electrons to become Mg2+. Chlorine can take only one electron to become _____. Now, _____ ion of magnesium and _____ ions of chlorine combine to give magnesium chloride.",[], "<p>Chlorine becomes <strong>Cl<sup>−</sup></strong>. One <strong>Mg<sup>2+</sup></strong> ion combines with <strong>two Cl<sup>−</sup></strong> ions, giving magnesium chloride, <strong>MgCl<sub>2</sub></strong>.</p>","2"),
(14,"Show the formation of cations of potassium and calcium and the formation of their chlorides.",[], "<p>K has one valence electron and loses it: <strong>K → K<sup>+</sup> + e<sup>−</sup></strong>; therefore its chloride is <strong>KCl</strong>. Ca has two valence electrons and loses both: <strong>Ca → Ca<sup>2+</sup> + 2e<sup>−</sup></strong>; therefore two Cl<sup>−</sup> ions combine with Ca<sup>2+</sup>, giving <strong>CaCl<sub>2</sub></strong>.</p>","4"),
(15,"Illustrate how sodium sulfide Na2S is formed.",[], "<p>Each Na atom loses one electron to form Na<sup>+</sup>. Sulfur gains two electrons to form S<sup>2−</sup>. Therefore <strong>two Na<sup>+</sup></strong> ions combine with one S<sup>2−</sup> ion, producing <strong>Na<sub>2</sub>S</strong>.</p>","3"),
(16,"Name CO2, NO2, SF6 and PCl3.",[], "<p>(i) <strong>carbon dioxide</strong>; (ii) <strong>nitrogen dioxide</strong>; (iii) <strong>sulfur hexafluoride</strong>; (iv) <strong>phosphorus trichloride</strong>.</p>","2"),
(17,"Write formulae for sodium hydrogencarbonate, sulfur dioxide, ferric chloride and cuprous oxide.",[], "<p>(i) <strong>NaHCO<sub>3</sub></strong>; (ii) <strong>SO<sub>2</sub></strong>; (iii) <strong>FeCl<sub>3</sub></strong>; (iv) <strong>Cu<sub>2</sub>O</strong>.</p>","3"),
(18,"Write formulae for compounds formed from Fe3+ and OH−; K+ and CO3 2−.",[], "<p>Fe<sup>3+</sup> requires three OH<sup>−</sup>: <strong>Fe(OH)<sub>3</sub></strong>. K<sup>+</sup> requires two ions for CO<sub>3</sub><sup>2−</sup>: <strong>K<sub>2</sub>CO<sub>3</sub></strong>.</p>","2"),
(19,"What type of chemical bond is present in a solid compound that does not conduct electricity in the solid state but conducts electricity when dissolved in water?",[], "<p>The compound is typically <strong>ionic</strong>. Its ions are fixed in the solid lattice, so it does not conduct in the solid state. When dissolved in water, ions become free to move and conduct electricity.</p>","2"),
(20,"A metal M has two electrons in its valence shell and reacts with oxygen to form a compound slightly soluble in water. Predict its formula, bond type and conductivity of its aqueous solution.",[], "<p>M tends to form <strong>M<sup>2+</sup></strong>, while oxygen forms O<sup>2−</sup>. The simplest formula is <strong>MO</strong>. The bond is <strong>ionic</strong>. Its aqueous solution is expected to conduct electricity because mobile ions are present.</p>","3"),
(21,"Find the molecular mass of nitric acid HNO3 using H = 1 u, N = 14 u and O = 16 u.",[], "<p>Molecular mass = 1 + 14 + (16 × 3) = 1 + 14 + 48 = <strong>63 u</strong>.</p>","2"),
(22,"Find the molecular mass of methane CH4 using C = 12 u and H = 1 u.",[], "<p>Molecular mass = 12 + (1 × 4) = <strong>16 u</strong>.</p>","1"),
(23,"Find the formula unit mass of potassium chloride KCl using K = 39 u and Cl = 35.5 u.",[], "<p>Formula unit mass = 39 + 35.5 = <strong>74.5 u</strong>.</p>","1"),
(24,"Find the formula unit mass of magnesium hydroxide Mg(OH)2 using Mg = 24 u, O = 16 u and H = 1 u.",[], "<p>Formula unit mass = 24 + 2(16 + 1) = 24 + 34 = <strong>58 u</strong>.</p>","2"),
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
        Chapter 9. Expand each question to view the detailed model
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
        "question": "Q1. Which law states that mass is neither created nor destroyed in a chemical reaction?",
        "options": [
            "Law of Conservation of Mass",
            "Law of Constant Proportions",
            "Boyle's Law",
            "Ohm's Law"
        ],
        "correctIdx": 0,
        "hint": "Apply the definition or calculation rule from this chapter.",
        "explanations": [
            "Correct: the law says total mass is conserved.",
            "Incorrect: constant proportions concerns fixed mass ratios within a compound.",
            "Incorrect: Boyle's Law relates pressure and volume of a gas.",
            "Incorrect: Ohm's Law relates voltage, current and resistance."
        ]
    },
    {
        "question": "Q2. Who proposed the Law of Conservation of Mass?",
        "options": [
            "Joseph Proust",
            "John Dalton",
            "Antoine Lavoisier",
            "J. J. Thomson"
        ],
        "correctIdx": 2,
        "hint": "Apply the definition or calculation rule from this chapter.",
        "explanations": [
            "Incorrect: Proust is associated with constant proportions.",
            "Incorrect: Dalton proposed Atomic Theory.",
            "Correct: Antoine Lavoisier proposed the Law of Conservation of Mass.",
            "Incorrect: Thomson is associated with the electron."
        ]
    },
    {
        "question": "Q3. The mass ratio of hydrogen to oxygen in pure water is:",
        "options": [
            "1:2",
            "1:8",
            "2:1",
            "8:1"
        ],
        "correctIdx": 1,
        "hint": "Apply the definition or calculation rule from this chapter.",
        "explanations": [
            "Incorrect: 1:2 is not the mass ratio in water.",
            "Correct: pure water has H:O = 1:8 by mass.",
            "Incorrect: 2:1 is not the required ratio.",
            "Incorrect: 8:1 is the reverse ratio."
        ]
    },
    {
        "question": "Q4. The Law of Constant Proportions is also called:",
        "options": [
            "Proust's Law",
            "Dalton's Law",
            "Lavoisier's Law",
            "Avogadro's Law"
        ],
        "correctIdx": 0,
        "hint": "Apply the definition or calculation rule from this chapter.",
        "explanations": [
            "Correct: it is also called Proust's Law.",
            "Incorrect: Dalton is associated with Atomic Theory.",
            "Incorrect: Lavoisier is associated with conservation of mass.",
            "Incorrect: Avogadro's Law is not the law described here."
        ]
    },
    {
        "question": "Q5. Who proposed Dalton's Atomic Theory?",
        "options": [
            "Lavoisier",
            "Proust",
            "John Dalton",
            "Chadwick"
        ],
        "correctIdx": 2,
        "hint": "Apply the definition or calculation rule from this chapter.",
        "explanations": [
            "Incorrect: Lavoisier proposed conservation of mass.",
            "Incorrect: Proust proposed constant proportions.",
            "Correct: John Dalton proposed Dalton's Atomic Theory.",
            "Incorrect: Chadwick discovered the neutron."
        ]
    },
    {
        "question": "Q6. Atoms of a given element were stated by Dalton to be identical in:",
        "options": [
            "mass and chemical properties",
            "number of shells only",
            "mass number only",
            "charge only"
        ],
        "correctIdx": 0,
        "hint": "Apply the definition or calculation rule from this chapter.",
        "explanations": [
            "Correct: Dalton stated that atoms of a given element have identical mass and chemical properties in his original postulate.",
            "Incorrect: the postulate is not limited to number of shells.",
            "Incorrect: it is not limited to mass number.",
            "Incorrect: charge alone is not the stated property."
        ]
    },
    {
        "question": "Q7. A molecule is best described as:",
        "options": [
            "a charged ion only",
            "an electrically neutral entity of more than one atom capable of independent existence",
            "a single proton",
            "a crystal lattice"
        ],
        "correctIdx": 1,
        "hint": "Apply the definition or calculation rule from this chapter.",
        "explanations": [
            "Incorrect: an ion is charged, while a molecule is electrically neutral.",
            "Correct: a molecule is an electrically neutral entity of more than one atom capable of independent existence.",
            "Incorrect: a proton is a subatomic particle.",
            "Incorrect: a crystal lattice is an extended ionic arrangement."
        ]
    },
    {
        "question": "Q8. A covalent bond is formed by:",
        "options": [
            "transfer of protons",
            "sharing of electrons",
            "loss of neutrons",
            "sharing of nuclei"
        ],
        "correctIdx": 1,
        "hint": "Apply the definition or calculation rule from this chapter.",
        "explanations": [
            "Incorrect: covalent bonding does not involve proton transfer.",
            "Correct: covalent bonds form through sharing of electrons.",
            "Incorrect: neutrons are not lost to form a covalent bond.",
            "Incorrect: nuclei are not shared."
        ]
    },
    {
        "question": "Q9. How many shared electron pairs form a double bond?",
        "options": [
            "One",
            "Two",
            "Three",
            "Four"
        ],
        "correctIdx": 1,
        "hint": "Apply the definition or calculation rule from this chapter.",
        "explanations": [
            "Incorrect: one shared pair gives a single bond.",
            "Correct: two shared electron pairs form a double bond.",
            "Incorrect: three shared pairs form a triple bond.",
            "Incorrect: four shared pairs are not the definition of a double bond."
        ]
    },
    {
        "question": "Q10. The structure of an oxygen molecule is represented as:",
        "options": [
            "O—O",
            "O=O",
            "O≡O",
            "O+O−"
        ],
        "correctIdx": 1,
        "hint": "Apply the definition or calculation rule from this chapter.",
        "explanations": [
            "Incorrect: O—O represents a single bond.",
            "Correct: O=O represents two shared electron pairs, a double bond.",
            "Incorrect: O≡O would represent a triple bond.",
            "Incorrect: O+O− represents ions, not covalent O₂."
        ]
    },
    {
        "question": "Q11. The covalent molecule formed by two chlorine atoms is:",
        "options": [
            "Cl",
            "Cl2",
            "Cl3",
            "Cl−"
        ],
        "correctIdx": 1,
        "hint": "Apply the definition or calculation rule from this chapter.",
        "explanations": [
            "Incorrect: one Cl atom is not the diatomic molecule.",
            "Correct: two chlorine atoms form Cl₂.",
            "Incorrect: Cl₃ is not the molecule described.",
            "Incorrect: Cl− is a chloride ion."
        ]
    },
    {
        "question": "Q12. Carbon dioxide is named using which prefixes/form?",
        "options": [
            "carbon monoxide",
            "carbon dioxide",
            "dicarbon monoxide",
            "carbon trioxide"
        ],
        "correctIdx": 1,
        "hint": "Apply the definition or calculation rule from this chapter.",
        "explanations": [
            "Incorrect: CO is carbon monoxide.",
            "Correct: CO₂ is carbon dioxide; di- indicates two oxygen atoms.",
            "Incorrect: the first element is not named dicarbon here.",
            "Incorrect: CO₂ has two oxygen atoms, not three."
        ]
    },
    {
        "question": "Q13. Which compound is commonly called water?",
        "options": [
            "HCl",
            "H2O",
            "NH3",
            "CO2"
        ],
        "correctIdx": 1,
        "hint": "Apply the definition or calculation rule from this chapter.",
        "explanations": [
            "Incorrect: HCl is hydrogen chloride.",
            "Correct: H₂O is commonly called water.",
            "Incorrect: NH₃ is commonly called ammonia.",
            "Incorrect: CO₂ is carbon dioxide."
        ]
    },
    {
        "question": "Q14. Sodium loses one electron to form:",
        "options": [
            "Na−",
            "Na+",
            "Na2+",
            "Na"
        ],
        "correctIdx": 1,
        "hint": "Apply the definition or calculation rule from this chapter.",
        "explanations": [
            "Incorrect: losing one electron leaves sodium positively charged.",
            "Correct: Na loses one electron to form Na⁺.",
            "Incorrect: one electron lost gives +1, not +2.",
            "Incorrect: sodium becomes Na⁺, not neutral."
        ]
    },
    {
        "question": "Q15. Chlorine gains one electron to form:",
        "options": [
            "Cl+",
            "Cl2+",
            "Cl−",
            "Cl2−"
        ],
        "correctIdx": 2,
        "hint": "Apply the definition or calculation rule from this chapter.",
        "explanations": [
            "Incorrect: gaining an electron makes chlorine negative.",
            "Incorrect: one gained electron gives −1, not +2.",
            "Correct: Cl gains one electron to form Cl⁻.",
            "Incorrect: chlorine does not gain two electrons here."
        ]
    },
    {
        "question": "Q16. The electrostatic attraction between oppositely charged ions is called:",
        "options": [
            "covalent bond",
            "ionic bond",
            "metallic bond",
            "hydrogen bond"
        ],
        "correctIdx": 1,
        "hint": "Apply the definition or calculation rule from this chapter.",
        "explanations": [
            "Incorrect: sharing electrons gives a covalent bond.",
            "Correct: attraction between oppositely charged ions is an ionic bond.",
            "Incorrect: metallic bonding is a different type.",
            "Incorrect: hydrogen bonding is not the ionic bond defined here."
        ]
    },
    {
        "question": "Q17. In solid sodium chloride, ions:",
        "options": [
            "move freely",
            "are fixed in a repeating lattice",
            "do not exist",
            "share electrons equally"
        ],
        "correctIdx": 1,
        "hint": "Apply the definition or calculation rule from this chapter.",
        "explanations": [
            "Incorrect: solid NaCl ions are not free to move.",
            "Correct: ions occupy fixed positions in a repeating crystal lattice.",
            "Incorrect: ions are present in solid NaCl.",
            "Incorrect: NaCl forms by electron transfer, not equal sharing."
        ]
    },
    {
        "question": "Q18. Which ion has charge 2−?",
        "options": [
            "Na+",
            "Cl−",
            "O2−",
            "Al3+"
        ],
        "correctIdx": 2,
        "hint": "Apply the definition or calculation rule from this chapter.",
        "explanations": [
            "Incorrect: Na⁺ is +1.",
            "Incorrect: Cl⁻ is −1.",
            "Correct: O²⁻ has charge −2.",
            "Incorrect: Al³⁺ is +3."
        ]
    },
    {
        "question": "Q19. Which is a polyatomic ion?",
        "options": [
            "Na+",
            "Cl−",
            "SO4 2−",
            "Mg2+"
        ],
        "correctIdx": 2,
        "hint": "Apply the definition or calculation rule from this chapter.",
        "explanations": [
            "Incorrect: Na⁺ is monatomic.",
            "Incorrect: Cl⁻ is monatomic.",
            "Correct: SO₄²⁻ contains multiple atoms and is polyatomic.",
            "Incorrect: Mg²⁺ is monatomic."
        ]
    },
    {
        "question": "Q20. The correct formula for calcium chloride is:",
        "options": [
            "CaCl",
            "CaCl2",
            "Ca2Cl",
            "Ca2Cl2"
        ],
        "correctIdx": 1,
        "hint": "Apply the definition or calculation rule from this chapter.",
        "explanations": [
            "Incorrect: Ca²⁺ requires two Cl⁻ ions.",
            "Correct: CaCl₂ gives +2 and −2 overall.",
            "Incorrect: Ca₂Cl gives an unbalanced charge.",
            "Incorrect: Ca₂Cl₂ must be simplified, but CaCl would still be unbalanced; the correct formula is CaCl₂."
        ]
    },
    {
        "question": "Q21. The correct formula for aluminium oxide is:",
        "options": [
            "AlO",
            "Al2O3",
            "Al3O2",
            "AlO2"
        ],
        "correctIdx": 1,
        "hint": "Apply the definition or calculation rule from this chapter.",
        "explanations": [
            "Incorrect: Al³⁺ and O²⁻ balance in a 2:3 ratio.",
            "Correct: Al₂O₃ gives +6 and −6.",
            "Incorrect: Al₃O₂ gives +9 and −4.",
            "Incorrect: AlO₂ gives +3 and −4."
        ]
    },
    {
        "question": "Q22. The correct formula for magnesium hydroxide is:",
        "options": [
            "MgOH",
            "Mg(OH)2",
            "Mg2OH",
            "Mg2(OH)"
        ],
        "correctIdx": 1,
        "hint": "Apply the definition or calculation rule from this chapter.",
        "explanations": [
            "Incorrect: Mg²⁺ needs two OH⁻ ions.",
            "Correct: Mg(OH)₂ contains one Mg²⁺ and two OH⁻ ions.",
            "Incorrect: Mg₂OH is not charge balanced.",
            "Incorrect: Mg₂(OH) is not charge balanced."
        ]
    },
    {
        "question": "Q23. Ionic compounds generally have:",
        "options": [
            "low melting points",
            "high melting points",
            "no fixed composition",
            "only molecular structures"
        ],
        "correctIdx": 1,
        "hint": "Apply the definition or calculation rule from this chapter.",
        "explanations": [
            "Incorrect: strong inter-ionic attraction generally raises melting point.",
            "Correct: ionic compounds generally have high melting points.",
            "Incorrect: ionic compounds have definite composition.",
            "Incorrect: ionic compounds form crystal lattices rather than individual molecules."
        ]
    },
    {
        "question": "Q24. Molecular mass of H2O is:",
        "options": [
            "16 u",
            "17 u",
            "18 u",
            "20 u"
        ],
        "correctIdx": 2,
        "hint": "Apply the definition or calculation rule from this chapter.",
        "explanations": [
            "Incorrect: 16 u is only the oxygen contribution.",
            "Incorrect: 17 u is not the molecular mass of H₂O.",
            "Correct: H₂O = 2(1) + 16 = 18 u.",
            "Incorrect: 20 u is not the correct sum."
        ]
    },
    {
        "question": "Q25. Formula unit mass of KCl is:",
        "options": [
            "39 u",
            "35.5 u",
            "74.5 u",
            "75.5 u"
        ],
        "correctIdx": 2,
        "hint": "Apply the definition or calculation rule from this chapter.",
        "explanations": [
            "Incorrect: 39 u is only the potassium contribution.",
            "Incorrect: 35.5 u is only the chlorine contribution.",
            "Correct: KCl = 39 + 35.5 = 74.5 u.",
            "Incorrect: the correct sum is 74.5 u."
        ]
    },
    {
        "question": "Q26. Which statement is correct?",
        "options": [
            "Ionic compounds form individual molecules",
            "Covalent compounds always conduct electricity in water",
            "Ionic compounds generally conduct when their ions are free to move",
            "Mass ratios in mixtures are always fixed"
        ],
        "correctIdx": 2,
        "hint": "Apply the definition or calculation rule from this chapter.",
        "explanations": [
            "Incorrect: ionic compounds form crystal structures, not individual molecules.",
            "Incorrect: covalent compounds generally do not conduct; 'always' is false.",
            "Correct: ionic compounds conduct when ions are free to move, such as in solution.",
            "Incorrect: mixtures can have variable composition."
        ]
    }
]

# ================================================================
# REVISION
# ================================================================

REVISION = """
<section class="sj-card"><div class="sj-cheader"><div class="sj-cicon"><i class="fas fa-bolt"></i></div><div>
<small style="font-weight:800;text-transform:uppercase;font-size:.65rem;display:block;">Rapid Revision</small><h2>60-Second Chapter Summary</h2></div></div>
<div class="sj-ibox info"><ul>
<li><strong>Conservation of Mass:</strong> total mass of reactants = total mass of products.</li>
<li><strong>Constant Proportions:</strong> elements in a pure compound occur in a fixed ratio by mass.</li>
<li><strong>Dalton:</strong> atoms rearrange during reactions; compounds form by simple whole-number ratios.</li>
<li><strong>Covalent:</strong> sharing of electron pairs. <strong>Ionic:</strong> electron transfer forms ions; opposite ions attract.</li>
<li><strong>Cation:</strong> positive. <strong>Anion:</strong> negative.</li>
<li><strong>Molecular mass:</strong> for molecules. <strong>Formula unit mass:</strong> for ionic compounds.</li>
</ul></div></section>
<section class="sj-card"><div class="sj-cheader"><div class="sj-cicon"><i class="fas fa-brain"></i></div><div>
<small style="font-weight:800;text-transform:uppercase;font-size:.65rem;display:block;">Memory Tools</small><h2>Mnemonics & Smart Tricks</h2></div></div>
<h3>1. Two Laws — “Conserve, then Compare”</h3>
<p><strong>Conservation = before vs after.</strong> Add reactant masses and product masses.<br><strong>Constant Proportions = inside one compound.</strong> Compare the masses of its elements.</p>
<h3>2. Scientists — “LCP”</h3><p><strong>L = Lavoisier → Law of conservation.</strong><br><strong>P = Proust → Proportion fixed.</strong><br><strong>D = Dalton → Described atoms.</strong></p>
<h3>3. Ionic vs Covalent — “Transfer or Share?”</h3>
<div class="sj-grid"><div class="sj-grid-card"><h4>TRANSFER → IONIC</h4><p>Electron transfer → cation + anion → electrostatic attraction.</p></div>
<div class="sj-grid-card"><h4>SHARE → COVALENT</h4><p>Electron sharing → shared pair(s) → covalent bond.</p></div></div>
<h3>4. “Lose = Plus, Gain = Minus”</h3><p>Lose electrons → <strong>cation (+)</strong>. Gain electrons → <strong>anion (−)</strong>.</p>
<h3>5. Bond-order trick</h3><p><strong>1 pair = single</strong> → H—H, Cl—Cl<br><strong>2 pairs = double</strong> → O=O<br><strong>3 pairs = triple</strong> → N≡N</p>
<h3>6. Formula-writing trick — “Write, Charge, Cross, Cancel, Check”</h3>
<ol><li>Write cation then anion.</li><li>Write charges/valencies.</li><li>Cross the numbers as subscripts.</li><li>Cancel common factors.</li><li>Check total positive charge = total negative charge.</li></ol>
<p><strong>Example:</strong> Al³⁺ + O²⁻ → Al₂O₃; 2(+3) + 3(−2) = 0.</p>
<h3>7. Bracket trick</h3><p><strong>One polyatomic ion:</strong> CaCO₃. <strong>Two or more:</strong> Mg(OH)₂, Al(OH)₃, Al₂(SO₄)₃.</p>
<h3>8. Covalent prefixes — “1-2-3-4-5-6”</h3><p><strong>mono, di, tri, tetra, penta, hexa</strong>. Mono is normally omitted for the first element but used for the second.</p>
</section>
<section class="sj-card"><div class="sj-cheader"><div class="sj-cicon"><i class="fas fa-triangle-exclamation"></i></div><div>
<small style="font-weight:800;text-transform:uppercase;font-size:.65rem;display:block;">Exam Defence</small><h2>Common Traps</h2></div></div>
<ul><li>Open-system mass decrease can occur because gas escapes; conservation is not violated.</li><li>Do not confuse mass ratio with number ratio.</li><li>Do not call NaCl a molecule; use formula unit.</li><li>Do not write AlOH₃; write <strong>Al(OH)₃</strong>.</li><li>After criss-crossing, simplify Mg₂O₂ to <strong>MgO</strong>.</li><li>Water solubility does not automatically mean conductivity; sugar dissolves but does not provide ions.</li><li>Use formula unit mass for ionic compounds.</li></ul></section>
<section class="sj-card"><div class="sj-cheader"><div class="sj-cicon"><i class="fas fa-table"></i></div><div>
<small style="font-weight:800;text-transform:uppercase;font-size:.65rem;display:block;">Last-Minute Values</small><h2>Must-Know Values</h2></div></div>
<table class="sj-table"><thead><tr><th>Item</th><th>Value / Rule</th></tr></thead><tbody>
<tr><td>Water mass ratio</td><td>H : O = 1 : 8</td></tr><tr><td>NaCl mass ratio</td><td>Na : Cl = 23 : 35.5</td></tr><tr><td>H₂O molecular mass</td><td>18 u</td></tr><tr><td>CO₂ molecular mass</td><td>44 u</td></tr><tr><td>HNO₃ molecular mass</td><td>63 u</td></tr><tr><td>Na₂O formula unit mass</td><td>62 u</td></tr><tr><td>Ca(NO₃)₂ formula unit mass</td><td>164 u</td></tr><tr><td>KCl formula unit mass</td><td>74.5 u</td></tr><tr><td>Mg(OH)₂ formula unit mass</td><td>58 u</td></tr>
</tbody></table></section>
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
            "question": "Q1. Which law states that total mass remains constant in a chemical reaction?",
            "options": [
                "Conservation of Mass",
                "Constant Proportions",
                "Periodic Law",
                "Gas Law"
            ],
            "correctIdx": 0
        },
        {
            "type": "mcq",
            "marks": 1,
            "question": "Q2. Water contains hydrogen and oxygen in which mass ratio?",
            "options": [
                "1:8",
                "8:1",
                "1:2",
                "2:1"
            ],
            "correctIdx": 0
        },
        {
            "type": "mcq",
            "marks": 1,
            "question": "Q3. Which bond is formed by transfer of electrons?",
            "options": [
                "Covalent",
                "Ionic",
                "Double covalent",
                "Triple covalent"
            ],
            "correctIdx": 1
        },
        {
            "type": "ar",
            "marks": 1,
            "question": "Q4. Assertion & Reasoning:\n\nAssertion (A): Sodium chloride conducts electricity when dissolved in water.\n\nReason (R): Dissolving frees its ions so they can move.",
            "options": [
                "(A) Both Assertion (A) and Reason (R) are true and Reason (R) is the correct explanation of Assertion (A).",
                "(B) Both Assertion (A) and Reason (R) are true but Reason (R) is not the correct explanation of Assertion (A).",
                "(C) Assertion (A) is true but Reason (R) is false.",
                "(D) Assertion (A) is false but Reason (R) is true."
            ],
            "correctIdx": 0
        },
        {
            "type": "subjective",
            "marks": 2,
            "question": "State the Law of Conservation of Mass.",
            "sampleAnswer": "Matter is neither created nor destroyed in a chemical reaction. Total mass of reactants equals total mass of products."
        },
        {
            "type": "subjective",
            "marks": 2,
            "question": "Write the formulae of calcium chloride and aluminium oxide.",
            "sampleAnswer": "Calcium chloride = CaCl2. Aluminium oxide = Al2O3."
        },
        {
            "type": "subjective",
            "marks": 3,
            "question": "Explain how NaCl is formed by electron transfer.",
            "sampleAnswer": "Na loses one electron to form Na+. Cl gains one electron to form Cl−. The oppositely charged ions attract electrostatically to form NaCl."
        },
        {
            "type": "subjective",
            "marks": 3,
            "question": "Calculate the molecular mass of CO2.",
            "sampleAnswer": "Molecular mass = 12 + (16 × 2) = 44 u."
        },
        {
            "type": "subjective",
            "marks": 5,
            "question": "Explain the difference between covalent and ionic bonding.",
            "sampleAnswer": "Covalent bonding involves sharing electron pairs between atoms. Ionic bonding involves transfer of electrons, producing cations and anions held together by electrostatic attraction."
        },
        {
            "type": "case",
            "marks": 5,
            "question": "Q10. Case-Based Passage:\n\nA compound contains Ca2+ and Cl− ions.\n\nSub-Questions:\n1. What is the charge on calcium? (1 Mark)\n2. What is the charge on chloride? (1 Mark)\n3. How many chloride ions are required for one calcium ion? (1 Mark)\n4. Write the formula. (1 Mark)\n5. Is the bond ionic or covalent? (1 Mark)",
            "sampleAnswer": "1. Calcium has charge 2+.\n2. Chloride has charge 1−.\n3. Two chloride ions are required.\n4. Formula = CaCl2.\n5. The bond is ionic."
        }
    ],
    "standard": [
        {
            "type": "mcq",
            "marks": 1,
            "question": "Q1. Who proposed the Law of Constant Proportions?",
            "options": [
                "Lavoisier",
                "Proust",
                "Dalton",
                "Chadwick"
            ],
            "correctIdx": 1
        },
        {
            "type": "mcq",
            "marks": 1,
            "question": "Q2. Which molecule contains a double covalent bond?",
            "options": [
                "H2",
                "Cl2",
                "O2",
                "N2"
            ],
            "correctIdx": 2
        },
        {
            "type": "mcq",
            "marks": 1,
            "question": "Q3. Which is the correct formula for magnesium hydroxide?",
            "options": [
                "MgOH",
                "Mg(OH)2",
                "Mg2OH",
                "Mg2(OH)2"
            ],
            "correctIdx": 1
        },
        {
            "type": "ar",
            "marks": 1,
            "question": "Q4. Assertion & Reasoning:\n\nAssertion (A): Ionic compounds generally have high melting points.\n\nReason (R): Strong electrostatic attractions hold oppositely charged ions together.",
            "options": [
                "(A) Both Assertion (A) and Reason (R) are true and Reason (R) is the correct explanation of Assertion (A).",
                "(B) Both Assertion (A) and Reason (R) are true but Reason (R) is not the correct explanation of Assertion (A).",
                "(C) Assertion (A) is true but Reason (R) is false.",
                "(D) Assertion (A) is false but Reason (R) is true."
            ],
            "correctIdx": 0
        },
        {
            "type": "subjective",
            "marks": 2,
            "question": "Differentiate molecular mass and formula unit mass.",
            "sampleAnswer": "Molecular mass is the sum of atomic masses in a molecule of a covalent compound. Formula unit mass is the sum for the simplest whole-number ratio of ions in an ionic compound."
        },
        {
            "type": "subjective",
            "marks": 2,
            "question": "Why does an open experiment with a gas-producing reaction appear to lose mass?",
            "sampleAnswer": "The gas may escape from the open apparatus. The measured mass of the apparatus decreases, although total matter is conserved when all products are considered."
        },
        {
            "type": "subjective",
            "marks": 3,
            "question": "Write the formulae for Fe3+ with OH− and K+ with CO3 2−.",
            "sampleAnswer": "Fe3+ requires three OH− ions: Fe(OH)3. K+ requires two ions for CO3 2−: K2CO3."
        },
        {
            "type": "subjective",
            "marks": 3,
            "question": "Find the formula unit mass of Ca(NO3)2 using Ca=40, N=14, O=16.",
            "sampleAnswer": "40 + 2(14 + 16×3) = 40 + 2(62) = 164 u."
        },
        {
            "type": "subjective",
            "marks": 5,
            "question": "Explain the naming of binary covalent compounds with examples.",
            "sampleAnswer": "The first element keeps its name and the second generally ends in -ide. Prefixes indicate atom numbers: mono-, di-, tri-, tetra-, penta-, hexa-. Examples: CO carbon monoxide, CO2 carbon dioxide, PCl3 phosphorus trichloride, SF6 sulfur hexafluoride."
        },
        {
            "type": "case",
            "marks": 5,
            "question": "Q10. Case-Based Passage:\n\nAn element X has configuration 2,8,2 and reacts with element Y having configuration 2,7.\n\nSub-Questions:\n1. How many valence electrons does X have? (1 Mark)\n2. What ion does X tend to form? (1 Mark)\n3. What ion does Y tend to form? (1 Mark)\n4. What is the formula of the compound? (1 Mark)\n5. What type of bond is present? (1 Mark)",
            "sampleAnswer": "1. X has 2 valence electrons.\n2. X tends to form X2+.\n3. Y tends to form Y−.\n4. Formula = XY2.\n5. The bond is ionic."
        }
    ],
    "advanced": [
        {
            "type": "mcq",
            "marks": 1,
            "question": "Q1. Which statement correctly explains the Law of Constant Proportions?",
            "options": [
                "A mixture always has a fixed mass ratio",
                "A pure compound contains its elements in a fixed mass ratio",
                "Atoms can combine in any mass ratio",
                "Only gases obey the law"
            ],
            "correctIdx": 1
        },
        {
            "type": "mcq",
            "marks": 1,
            "question": "Q2. Which species is a polyatomic ion?",
            "options": [
                "Na+",
                "Cl−",
                "SO4 2−",
                "Mg2+"
            ],
            "correctIdx": 2
        },
        {
            "type": "mcq",
            "marks": 1,
            "question": "Q3. The formula unit mass of KCl is (K=39, Cl=35.5):",
            "options": [
                "39 u",
                "35.5 u",
                "74.5 u",
                "75 u"
            ],
            "correctIdx": 2
        },
        {
            "type": "ar",
            "marks": 1,
            "question": "Q4. Assertion & Reasoning:\n\nAssertion (A): Mg(OH)2 contains brackets around OH.\n\nReason (R): More than one hydroxide ion occurs in the formula.",
            "options": [
                "(A) Both Assertion (A) and Reason (R) are true and Reason (R) is the correct explanation of Assertion (A).",
                "(B) Both Assertion (A) and Reason (R) are true but Reason (R) is not the correct explanation of Assertion (A).",
                "(C) Assertion (A) is true but Reason (R) is false.",
                "(D) Assertion (A) is false but Reason (R) is true."
            ],
            "correctIdx": 0
        },
        {
            "type": "subjective",
            "marks": 2,
            "question": "Why must ionic formulae be written in the simplest whole-number ratio?",
            "sampleAnswer": "The chemical formula of an ionic compound represents the simplest whole-number ratio of its ions and must give overall electrical neutrality."
        },
        {
            "type": "subjective",
            "marks": 2,
            "question": "Why does sugar solution generally not conduct electricity although sugar dissolves in water?",
            "sampleAnswer": "Sugar is a covalent compound. It dissolves without producing free ions, so the solution generally does not conduct electricity."
        },
        {
            "type": "subjective",
            "marks": 3,
            "question": "An element has 6 valence electrons. Explain why it can form X2 and state the bond.",
            "sampleAnswer": "It needs two electrons to complete its octet. Two atoms share two electron pairs, so X2 is formed with a double covalent bond, represented X=X."
        },
        {
            "type": "subjective",
            "marks": 3,
            "question": "A compound contains 40% sulfur and 60% oxygen by mass. How much oxygen is present with 20 g sulfur?",
            "sampleAnswer": "If sulfur is 40% and oxygen is 60%, O:S = 60:40 = 3:2. For 20 g sulfur, oxygen = 20 × 3/2 = 30 g."
        },
        {
            "type": "subjective",
            "marks": 5,
            "question": "Compare ionic and covalent compounds using conductivity, solubility and melting/boiling points.",
            "sampleAnswer": "Ionic compounds generally dissolve in water, are insoluble in kerosene/petrol, do not conduct in the solid state but conduct when ions are free in aqueous/molten states, and generally have high melting/boiling points. Covalent compounds generally have low melting/boiling points, many are insoluble in water and soluble in organic solvents, and usually do not conduct because they do not provide mobile ions."
        },
        {
            "type": "case",
            "marks": 5,
            "question": "Q10. Case-Based Passage:\n\nA sample of a compound contains 46 g sodium and 71 g chlorine.\n\nSub-Questions:\n1. State the Na:Cl mass ratio. (1 Mark)\n2. Does this support a fixed composition? (1 Mark)\n3. If 23 g Na is used, how much Cl is needed? (1 Mark)\n4. Name the compound. (1 Mark)\n5. State the law illustrated. (1 Mark)",
            "sampleAnswer": "1. Na:Cl = 46:71 = 23:35.5.\n2. Yes, it supports fixed composition for the pure compound.\n3. 35.5 g chlorine is needed.\n4. Sodium chloride.\n5. Law of Constant Proportions (Definite Proportions)."
        }
    ]
}

# ================================================================
# Metadata
# ================================================================

DESCRIPTIONS = {

    "concepts":
        "Detailed concepts for Class 9 Science Chapter 9 Atomic Foundations of Matter covering atomic models, subatomic particles, atomic number, mass number, electronic configuration, valency, isotopes and isobars.",

    "ncert-exercises":
        "NCERT exercise solutions for Class 9 Science Chapter 9 Atomic Foundations of Matter with model answers and marking guidance.",

    "quiz":
        "Interactive MCQ quiz for Class 9 Science Chapter 9 Atomic Foundations of Matter covering atomic models, subatomic particles, electronic configuration, valency, isotopes and isobars.",

    "tests":
        "Basic, Standard and Advanced chapter tests for Class 9 Science Chapter 9 Atomic Foundations of Matter.",

    "revision-notes":
        "Quick revision notes, formulas, comparisons and common exam traps for Class 9 Science Chapter 9 Atomic Foundations of Matter."
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
        "Atomic Foundations of Matter: Interactive Quiz | Class 9 Science Ch 9"
    )

    doc = doc.replace(
        "Exploration: Interactive Quiz MCQs | Class 9 Science Chapter 1",
        "Atomic Foundations of Matter: Interactive Quiz MCQs | Class 9 Science Chapter 9"
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
        "Atomic Foundations of Matter: Chapter Tests | Class 9 Science Ch 9"
    )

    doc = doc.replace(
        "Chapter tests for Exploration with Basic, Standard and Advanced difficulty levels.",
        "Chapter tests for Atomic Foundations of Matter with Basic, Standard and Advanced difficulty levels."
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
        f" Chapter 9: Atomic Foundations of Matter\n"
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
        " Chapter 9: Atomic Foundations of Matter\n"
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
        " Chapter 9: Atomic Foundations of Matter\n"
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
                f"QUIZ VALIDATION FAILED: custom Chapter 9 "
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

    # These are genuinely old/custom Chapter 9 identifiers.
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
                f"Chapter 9 UI detected: {item}"
            )

    # These MUST exist because Chapter 9 is supposed to use
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
    print(" SJMaths — Class 9 Science Chapter 9")
    print(" Atomic Foundations of Matter")
    print()
    print(" MASTER UI/UX: Chapter 1")
    print(" CONTENT:     Chapter 9")
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
            f"Chapter 9 folder not found:\n{CH8}\n\n"
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
    print("✓ CHAPTER 9 COMPLETE")
    print("=" * 76)
    print()

    print("Generated:")
    print("  chapter-9-atomic-foundations-of-matter/")
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
    print("  Chapter 9 Quiz/Test engines come directly from Chapter 1.")
    print()


if __name__ == "__main__":
    main()