
'''
SJMaths — Class 9 Science — Chapter 11 Generator
"Reproduction: How Life Continues"

Final UI/UX rebuild:
- Uses the proven Chapter 1 master templates through a DIRECT Chapter 9 engine import.
- Concepts page contains detailed teaching content and only the relevant
  textbook-embedded Think It Over / Pause and Ponder checks.
- NCERT Exercises page contains ONLY the official Revise, Reflect, Refine
  end-of-chapter questions Q1–Q13.
- No AI/meta wording such as "Why this is here", "Important distinction",
  "How to read this page", or "In-concept checks vs NCERT exercises".
- Final CSS is explicitly injected into every generated content page.
'''
from pathlib import Path
import importlib.util
import html
import builtins

BASE = Path(__file__).resolve().parent

# IMPORTANT: load the proven Chapter 9 engine DIRECTLY.
# Do not import Chapter 10 -> Chapter 9 -> Chapter 11 recursively.
# The previous version did that and therefore its main() ultimately ran
# Chapter 10's engine globals, producing Chapter 10/9 output paths.
_ENGINE_CANDIDATES = [
    BASE / "generate_chapter9_all_pages_detailed.py",
    BASE / "generate_chapter9_all_pages.py",
    BASE / "generate_chapter8_all_pages.py",
]
ENGINE_PATH = next((p for p in _ENGINE_CANDIDATES if p.exists()), None)
if ENGINE_PATH is None:
    raise FileNotFoundError(
        "Could not find a direct Chapter 8/9 engine beside this file. "
        "Expected one of: " + ", ".join(p.name for p in _ENGINE_CANDIDATES)
    )

spec = importlib.util.spec_from_file_location("chapter11_base_engine", ENGINE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Could not load engine: {ENGINE_PATH}")
_engine = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_engine)

# ---------------------------------------------------------------------------
# Chapter identity
# ---------------------------------------------------------------------------
CH1_FOLDER = "chapter-1-exploration-entering-world-of-secondary-science"
CH11_FOLDER = "chapter-11-reproduction-how-life-continues"
CH1 = BASE / CH1_FOLDER
CH11 = BASE / CH11_FOLDER

# Patch the DIRECT engine with Chapter 11 identity and Chapter 1 master templates.
_engine.CH1 = CH1
_engine.CH8 = CH11
_engine.CH8_FOLDER = CH11_FOLDER
_engine.TITLE = "Reproduction: How Life Continues"
_engine.CHAPTER = 11
_engine.NEXT_FOLDER = "chapter-12-patterns-in-life-diversity-and-change"
_engine.NEXT_TITLE = "Ch 12"
_engine.TEMPLATES = {
    "concepts": CH1 / "concepts" / "index.html",
    "ncert-exercises": CH1 / "ncert-exercises" / "index.html",
    "quiz": CH1 / "quiz" / "index.html",
    "tests": CH1 / "tests" / "index.html",
    "revision-notes": CH1 / "revision-notes" / "index.html",
}

_engine.PAGE_NAV = {
    "concepts": (
        '<a href="../index.html" class="sj-btn"><i class="fas fa-arrow-left"></i> OVERVIEW</a>',
        '<a href="../ncert-exercises/" class="sj-btn next">NCERT EXERCISES <i class="fas fa-arrow-right"></i></a>'),
    "ncert-exercises": (
        '<a href="../concepts/" class="sj-btn"><i class="fas fa-arrow-left"></i> CONCEPTS</a>',
        '<a href="../quiz/" class="sj-btn next">QUIZ <i class="fas fa-arrow-right"></i></a>'),
    "quiz": (
        '<a href="../ncert-exercises/" class="sj-btn"><i class="fas fa-arrow-left"></i> NCERT EXERCISES</a>',
        '<a href="../tests/" class="sj-btn next">TESTS <i class="fas fa-arrow-right"></i></a>'),
    "tests": (
        '<a href="../quiz/" class="sj-btn"><i class="fas fa-arrow-left"></i> QUIZ</a>',
        '<a href="../revision-notes/" class="sj-btn next">REVISION <i class="fas fa-arrow-right"></i></a>'),
    "revision-notes": (
        '<a href="../tests/" class="sj-btn"><i class="fas fa-arrow-left"></i> TESTS</a>',
        '<a href="../index.html" class="sj-btn next">OVERVIEW <i class="fas fa-arrow-right"></i></a>')
}
_engine.BOTTOM_NAV = {
    "concepts": ('<a href="../index.html" class="prev"><i class="fas fa-arrow-left"></i> Overview</a>',
                 '<a href="../ncert-exercises/" class="next">NCERT Exercises <i class="fas fa-arrow-right"></i></a>'),
    "ncert-exercises": ('<a href="../concepts/" class="prev"><i class="fas fa-arrow-left"></i> Concepts</a>',
                        '<a href="../quiz/" class="next">Interactive Quiz <i class="fas fa-arrow-right"></i></a>'),
    "quiz": ('<a href="../ncert-exercises/" class="prev"><i class="fas fa-arrow-left"></i> NCERT Exercises</a>',
             '<a href="../tests/" class="next">Tests <i class="fas fa-arrow-right"></i></a>'),
    "tests": ('<a href="../quiz/" class="prev"><i class="fas fa-arrow-left"></i> Quiz</a>',
              '<a href="../revision-notes/" class="next">Revision <i class="fas fa-arrow-right"></i></a>'),
    "revision-notes": ('<a href="../tests/" class="prev"><i class="fas fa-arrow-left"></i> Tests</a>',
                       '<a href="../index.html" class="next">Overview <i class="fas fa-arrow-right"></i></a>')
}

# ---------------------------------------------------------------------------
# Final textbook-first content styling
# ---------------------------------------------------------------------------
FINAL_UI_CSS = r'''
.sj-card{background:#fff!important;border:1px solid #e3e9ef!important;border-radius:18px!important;box-shadow:0 4px 18px rgba(20,35,55,.055)!important;margin:0 0 24px!important;padding:28px 30px!important}
.sj-cheader{display:flex!important;align-items:center!important;gap:16px!important;padding-bottom:18px!important;margin-bottom:22px!important;border-bottom:1px dashed #dce4ea!important}
.sj-cicon{width:52px!important;height:52px!important;border-radius:14px!important;display:grid!important;place-items:center!important;background:#eaf7f4!important;color:#0f9f8b!important;font-size:21px!important;flex:0 0 52px!important}
.sj-cheader h2{margin:0!important;color:#09233f!important;font-size:1.55rem!important;line-height:1.25!important}
.sj-section-subtitle{margin:5px 0 0!important;color:#68788a!important;font-size:.94rem!important}
.sj-card p,.sj-card li{color:#243b53!important;font-size:1rem!important;line-height:1.72!important}
.sj-card h3{color:#09233f!important;margin-top:25px!important}.sj-card h4{color:#163c5b!important}
.sj-grid{display:grid!important;grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:14px!important;margin:20px 0!important}
.sj-grid-card{background:#f7fafc!important;border:1px solid #e5ebf0!important;border-radius:12px!important;padding:16px!important}
.sj-grid-card h4{margin:0 0 7px!important}
.sj-detail{margin:20px 0!important;padding:17px 18px!important;background:#f8fbfd!important;border-left:4px solid #0f9f8b!important;border-radius:0 10px 10px 0!important}
.sj-detail h4{margin:0 0 8px!important}
.sj-table{width:100%!important;border-collapse:collapse!important;margin:18px 0!important;font-size:.95rem!important}
.sj-table th{background:#f3f7f9!important;color:#17324d!important;font-weight:800!important}
.sj-table th,.sj-table td{padding:10px 12px!important;border:1px solid #dfe7ec!important;text-align:left!important;vertical-align:top!important}
.sj-exercise-q{margin:18px 0!important;padding:17px 18px!important;background:#fbfcfd!important;border:1px solid #e1e8ed!important;border-radius:13px!important}
.sj-q-header{display:flex!important;gap:10px!important;align-items:flex-start!important}
.sj-q-badge{flex:0 0 auto!important;background:#eaf7f4!important;color:#087f70!important;border-radius:7px!important;padding:5px 9px!important;font-size:.78rem!important;font-weight:800!important}
.sj-q-text{font-weight:700!important;color:#122f49!important;line-height:1.55!important}
.sj-ideal-answer summary,.sj-textbook-check summary{list-style:none!important;cursor:pointer!important;color:#087f70!important;font-weight:750!important;margin-top:12px!important}
.sj-ideal-answer summary::-webkit-details-marker,.sj-textbook-check summary::-webkit-details-marker{display:none!important}
.sj-ideal-answer summary:before,.sj-textbook-check summary:before{content:"▸";display:inline-block;margin-right:7px!important}
.sj-ideal-answer[open] summary:before,.sj-textbook-check[open] summary:before{content:"▾"}
.sj-answer-content{margin-top:11px!important;padding:14px 15px!important;background:#fff!important;border:1px solid #e4eaee!important;border-radius:9px!important;line-height:1.68!important}
.sj-textbook-check{margin:22px 0!important;padding:18px 19px 15px!important;border:1px solid #dbe7e4!important;border-radius:13px!important;background:linear-gradient(180deg,#f4fbf9,#fff)!important}
.sj-textbook-check .check-label{display:inline-block!important;margin-bottom:8px!important;color:#087f70!important;font-weight:850!important;font-size:.8rem!important;text-transform:uppercase!important;letter-spacing:.04em!important}
.sj-textbook-check .check-question{font-size:1rem!important;line-height:1.65!important;color:#17324d!important}
.sj-ncert-card{padding-bottom:18px!important}.sj-ncert-question{padding:20px 4px 22px!important;border-bottom:1px solid #e2e8ed!important}
.sj-ncert-question:last-child{border-bottom:0!important}
.sj-ncert-qtop{display:flex!important;justify-content:space-between!important;align-items:center!important;gap:15px!important}
.sj-ncert-qnumber{color:#09233f!important;font-weight:850!important;font-size:1.05rem!important}
.marks-badge{border:1px solid #ef8b8b!important;color:#c74444!important;background:#fffafa!important;padding:4px 8px!important;font-size:.78rem!important;border-radius:5px!important;white-space:nowrap!important}
.sj-ncert-qtext{margin:9px 0 11px!important;color:#17324d!important;font-size:1rem!important;line-height:1.65!important}
.sj-ncert-options{margin:12px 0!important;padding:13px 15px!important;background:#f7f9fb!important;border-radius:10px!important}
.sj-ncert-options ol{margin:7px 0 0 22px!important}
.sj-ncert-answer summary{color:#087f70!important;font-weight:750!important;cursor:pointer!important;list-style:none!important}
.sj-ncert-answer summary::-webkit-details-marker{display:none!important}
.sj-ncert-answer summary:before{content:"▸";display:inline-block;margin-right:7px!important}
.sj-ncert-answer[open] summary:before{content:"▾"}
@media(max-width:720px){.sj-card{padding:20px 16px!important;border-radius:14px!important}.sj-cheader h2{font-size:1.28rem!important}.sj-grid{grid-template-columns:1fr!important}.sj-ncert-question{padding:17px 0 19px!important}.sj-q-header{display:block!important}.sj-q-badge{display:inline-block!important;margin-bottom:8px!important}}
'''

def inject_css(doc):
    return doc.replace("</head>", '<style id="sj-ch11-final-ui">'+FINAL_UI_CSS+"</style>\n</head>", 1)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def check_block(label, question, answer):
    return f'''
<div class="sj-textbook-check">
  <span class="check-label">{label}</span>
  <div class="check-question">{question}</div>
  <details class="sj-ideal-answer">
    <summary>View Answer</summary>
    <div class="sj-answer-content">{answer}</div>
  </details>
</div>
'''

def nq(n,q,answer,marks="2",options=None):
    return (n,q,options or [],answer,marks)

# ---------------------------------------------------------------------------
# Detailed concepts. Embedded questions are kept with their relevant concept.
# ---------------------------------------------------------------------------
CONCEPTS = [
("1","fa-seedling","Reproduction and Continuity of Life",r'''
<p><strong>Reproduction</strong> is the biological process by which living organisms produce new individuals of their own kind. An organism is born, grows, matures, reproduces and eventually dies; reproduction allows life to continue across generations.</p>
<div class="sj-grid">
<div class="sj-grid-card"><h4>Asexual reproduction</h4><p>Usually involves one parent and produces offspring that are genetically identical or nearly identical to the parent.</p></div>
<div class="sj-grid-card"><h4>Sexual reproduction</h4><p>Involves genetic contributions from two individuals and produces variation among offspring.</p></div>
</div>
<div class="sj-detail"><h4>Why variation matters</h4><p>Small differences among offspring can accumulate over generations. Variation may help some individuals survive and reproduce when environmental conditions change, contributing to adaptation and evolution.</p></div>
''' + check_block("Think It Over","When does a farmer prefer asexual or sexual methods of reproduction for crop production?","Asexual methods are useful when a farmer wants many plants with the same desirable characters quickly. Sexual reproduction is useful when variation is desired, for example while developing or combining desirable characters through breeding.") +
check_block("Think It Over","Why do most complex animals and flowering plants use sexual reproduction, while organisms such as yeast and hydra mainly reproduce asexually?","Sexual reproduction creates genetic variation and is important for maintaining variation in complex organisms. Simpler organisms can often increase their numbers rapidly by asexual methods because a single parent can produce offspring without finding a mate.")),
("2","fa-leaf","Asexual Reproduction and Vegetative Propagation",r'''
<p><strong>Asexual reproduction</strong> involves a single parent. Examples in the chapter include bacteria, amoeba, yeast, hydra, sponge and many plants. Because there is no mixing of genetic material from two parents, the offspring are generally genetically identical to the parent.</p>
<p>In plants, new individuals may arise from vegetative parts such as stems or leaves. This is called <strong>vegetative propagation</strong>.</p>
<table class="sj-table"><thead><tr><th>Example</th><th>What happens?</th></tr></thead><tbody>
<tr><td>Potato and ginger</td><td>New plants arise from vegetative structures.</td></tr>
<tr><td>Sugarcane and money plant</td><td>Stem cuttings can grow into new plants.</td></tr>
<tr><td>Bryophyllum</td><td>Leaf plantlets develop into new plants.</td></tr>
</tbody></table>
<p>Vegetative propagation has been adapted through <strong>cutting, grafting, layering and tissue culture</strong>. It allows rapid multiplication of plants with desirable characteristics.</p>
'''),
("3","fa-scissors","Methods of Vegetative Propagation",r'''
<div class="sj-grid">
<div class="sj-grid-card"><h4>Cutting</h4><p>A suitable stem cutting is inserted into soil; under suitable conditions it develops roots and grows into a new plant.</p></div>
<div class="sj-grid-card"><h4>Grafting</h4><p>A stem piece from one plant is fitted into a slit or wound on a rooted plant so that the two parts grow together.</p></div>
<div class="sj-grid-card"><h4>Layering</h4><p>A flexible twig is bent and a middle portion is buried. Roots develop there before the twig is separated from the parent.</p></div>
<div class="sj-grid-card"><h4>Tissue culture</h4><p>Plant material such as shoot tips can be used to produce large numbers of healthy plantlets.</p></div>
</div>
<div class="sj-detail"><h4>Agricultural importance</h4><p>These methods help farmers multiply desirable varieties on a large scale. The chapter describes tissue culture in banana farming and the role of Krishi Vigyan Kendras in supporting modern grafting skills.</p></div>
'''),
("4","fa-dna","Budding, Spore Formation and Clones",r'''
<p>In <strong>budding</strong>, repeated cell division at a particular site produces a small outgrowth called a bud. The bud grows and may separate from the parent. Yeast shows budding, and hydra can develop several buds on its body.</p>
<p>Fungi can reproduce by <strong>spore formation</strong>. Spores are produced in very large numbers and are light enough to be carried by air. When a spore lands where moisture and nutrients are suitable, it can germinate and form a new individual.</p>
<div class="sj-detail"><h4>Role of mitosis</h4><p>The chapter identifies mitosis as the central cell-division process behind the asexual examples discussed. It produces daughter cells with the same chromosome number as the parent. Genetically identical offspring are called <strong>clones</strong>.</p></div>
''' + check_block("Think It Over","A mould appears on moist bread after a few days. Where did the mould come from?","Fungal spores already present in the air can settle on moist bread. Warmth and moisture allow the spores to germinate and reproduce, producing visible mould.")),
("5","fa-shuffle","Sexual Reproduction, Meiosis and Variation",r'''
<p><strong>Sexual reproduction</strong> involves genetic contributions from two individuals. A key problem is preventing the chromosome number from doubling in every generation. <strong>Meiosis</strong> solves this problem by reducing the chromosome number to half in cells that become gametes.</p>
<table class="sj-table"><thead><tr><th>Term</th><th>Meaning</th></tr></thead><tbody>
<tr><td>Diploid</td><td>Cell containing the full chromosome number.</td></tr>
<tr><td>Haploid</td><td>Cell containing half the chromosome number.</td></tr>
<tr><td>Gamete</td><td>Reproductive cell such as sperm or egg.</td></tr>
<tr><td>Human gamete</td><td>23 chromosomes; the human zygote has 46 after fusion.</td></tr>
</tbody></table>
<p>During meiosis, chromosomes of each pair separate so that each gamete receives one chromosome from each pair. Random combinations generate many possible combinations of characters and therefore variation among offspring.</p>
''' + check_block("Pause and Ponder","How many combinations of characters can gametes carry if three pairs of contrasting characters are considered, with one choice from each pair?","There are 2 choices for each of the three pairs: 2 × 2 × 2 = <strong>8</strong> combinations.")),
("6","fa-flower","Sexual Reproduction in Flowering Plants",r'''
<p>Flowers are the reproductive organs of flowering plants. A complete flower has four main parts: <strong>sepals, petals, stamens and pistil</strong>.</p>
<div class="sj-grid">
<div class="sj-grid-card"><h4>Sepal</h4><p>The outer green whorl that helps protect the flower in the bud stage.</p></div>
<div class="sj-grid-card"><h4>Petal</h4><p>Often coloured and/or fragrant; these features can help attract pollinators.</p></div>
<div class="sj-grid-card"><h4>Stamen</h4><p>Male reproductive part consisting of filament and anther. The anther produces pollen grains.</p></div>
<div class="sj-grid-card"><h4>Pistil</h4><p>Female reproductive part consisting of stigma, style and ovary. The ovary contains ovules.</p></div>
</div>
<div class="sj-detail"><h4>Structure to remember</h4><p><strong>Stamen → filament + anther.</strong> <strong>Pistil → stigma + style + ovary.</strong> Pollen grains contain male gametes, while an ovule contains the egg cell.</p></div>
'''),
("7","fa-wind","Pollination: Self and Cross",r'''
<p><strong>Pollination</strong> is the transfer of pollen grains from the anther to the stigma of a flower.</p>
<table class="sj-table"><thead><tr><th>Type</th><th>Definition</th></tr></thead><tbody>
<tr><td>Self-pollination</td><td>Pollen reaches the stigma of the same flower or another flower of the same plant.</td></tr>
<tr><td>Cross-pollination</td><td>Pollen moves from a flower of one plant to a flower of another plant of the same type.</td></tr>
</tbody></table>
<p>Pollination can involve <strong>wind, water, insects and birds</strong>. Wind-pollinated plants often produce very large numbers of light pollen grains. Insect-pollinated flowers may be brightly coloured, fragrant and nectar-producing, with pollen that can attach to insects.</p>
''' + check_block("Pause and Ponder","A farmer plants two varieties of maize side by side and seeds form only when pollen from one variety reaches the stigma of the other. What type of pollination is this?","This is <strong>cross-pollination</strong> because pollen is transferred from one plant to another plant of the same type.")),
("8","fa-seedling","Fertilisation and Seed Formation",r'''
<p>After compatible pollen reaches the stigma, the pollen grain germinates and forms a <strong>pollen tube</strong>. The tube grows through the style towards the ovary. The male gamete travels through the tube to the ovule and fuses with the egg cell.</p>
<div class="sj-detail"><h4>Sequence</h4><p><strong>Pollination → pollen germination → pollen tube growth → male gamete reaches ovule → fertilisation → zygote → embryo → seed; ovary → fruit.</strong></p></div>
<p>After fertilisation, the fertilised egg is called a <strong>zygote</strong>. It develops into an embryo. The ovules develop into seeds and the ovary enlarges into a fruit. Seeds may be dispersed by wind, water or animals and germinate when suitable conditions are available.</p>
''' + check_block("Pause and Ponder","In a china-rose plant, a pollen tube continues through the style after pollen lands on the stigma. Which process is about to happen next?","The male gamete is about to reach the ovule and fuse with the egg cell. Thus, <strong>fertilisation</strong> is the next major process.")),
("9","fa-frog","Sexual Reproduction in Animals",r'''
<p>In many aquatic animals such as frogs and most fish, fertilisation occurs outside the body and is called <strong>external fertilisation</strong>. In reptiles, birds and mammals, fertilisation generally occurs inside the female body and is called <strong>internal fertilisation</strong>.</p>
<table class="sj-table"><thead><tr><th>Feature</th><th>External</th><th>Internal</th></tr></thead><tbody>
<tr><td>Place</td><td>Outside the body, commonly in water</td><td>Inside the female body</td></tr>
<tr><td>Examples</td><td>Frog, most fish</td><td>Reptiles, birds, mammals</td></tr>
<tr><td>Protection</td><td>Lower; many eggs may be destroyed or eaten</td><td>Greater protection of fertilised egg/embryo</td></tr>
</tbody></table>
<p>Species with external fertilisation often produce many eggs because survival of each egg is less certain. The chapter also describes larval stages and metamorphosis in organisms such as butterflies and frogs.</p>
''' + check_block("Pause and Ponder","Why do animals with external fertilisation generally produce more eggs than animals with internal fertilisation?","Many eggs and embryos exposed outside the body can be destroyed by environmental conditions or eaten. Producing many eggs increases the chance that some offspring survive.") +
check_block("Pause and Ponder","In animals, which fertilisation method gives greater protection to the gametes and developing embryo?","<strong>Internal fertilisation</strong> generally provides greater protection because fertilisation and early development occur inside the female body.")),
("10","fa-person","Human Reproductive System",r'''
<p>Human reproduction involves specialised reproductive organs that produce gametes and enable fertilisation and development of a new individual.</p>
<div class="sj-grid">
<div class="sj-grid-card"><h4>Male system</h4><p>Testes produce sperm and hormones. Sperm travel through the vas deferens to the urethra. Seminal vesicles and prostate add fluids that nourish and support sperm.</p></div>
<div class="sj-grid-card"><h4>Female system</h4><p>Ovaries produce eggs and hormones. Oviducts connect the ovaries to the uterus. The uterus supports development of the foetus and opens into the vagina through the cervix.</p></div>
</div>
<p>The testes are located in the scrotum, which keeps them slightly cooler than normal body temperature, a condition needed for sperm formation. A sperm has genetic material in its head and a tail that helps it move.</p>
'''),
("11","fa-dna","Gametogenesis, Fertilisation and Menstrual Cycle",r'''
<p><strong>Gametogenesis</strong> is the formation of gametes. In humans, meiosis reduces the chromosome number from 46 in body cells to 23 in sperm and eggs. When sperm and egg fuse, the resulting zygote has 46 chromosomes.</p>
<table class="sj-table"><thead><tr><th>Feature</th><th>Sperm</th><th>Egg</th></tr></thead><tbody>
<tr><td>Size</td><td>Very small</td><td>Large</td></tr><tr><td>Number produced</td><td>Millions</td><td>Few</td></tr>
<tr><td>Stored nutrients</td><td>Absent</td><td>Present</td></tr><tr><td>Motility</td><td>Actively motile</td><td>Non-motile</td></tr>
</tbody></table>
<p>Usually one mature egg is released around the middle of a typical menstrual cycle. This is called <strong>ovulation</strong>. If sperm fuses with the egg in the oviduct, a zygote forms. The zygote divides by mitosis and implants in the uterine lining.</p>
<div class="sj-detail"><h4>Typical 28-day pattern</h4><p>Days 1–5: menstruation. Days 6–14: uterine lining rebuilds and the egg matures. Around day 14: ovulation. Days 15–28: the lining becomes thicker; if fertilisation does not occur, it breaks down and the cycle repeats. The chapter also notes that actual cycles can vary, commonly about 21–35 days.</p></div>
''' + check_block("Pause and Ponder","Ravi suddenly notices rapid height growth, broader shoulders and a cracking voice. What stage of life is he entering?","He is entering <strong>adolescence/puberty</strong>, during which reproductive organs mature and characteristic physical changes occur.") +
check_block("Pause and Ponder","Rina's period occurs every 28 days. Her last period was on 5 March. On which day is she most likely to get her next period?","Counting a 28-day cycle from 5 March gives approximately <strong>2 April</strong> as the expected next start, assuming the cycle remains regular.") +
check_block("Pause and Ponder","A human zygote has just formed. How many chromosomes does it have?","A human zygote normally has <strong>46 chromosomes</strong>, receiving 23 from the sperm and 23 from the egg.")),
("12","fa-baby","Pregnancy, Childbirth and Maternal Health",r'''
<p>After implantation, the developing embryo/foetus grows in the uterus. Human pregnancy lasts about <strong>nine months</strong> and is broadly divided into three trimesters.</p>
<div class="sj-grid">
<div class="sj-grid-card"><h4>First trimester</h4><p>The fertilised egg develops into an embryo and major organs begin forming.</p></div>
<div class="sj-grid-card"><h4>Second trimester</h4><p>The foetus grows larger and stronger; movements are commonly felt by the mother.</p></div>
<div class="sj-grid-card"><h4>Third trimester</h4><p>The baby grows rapidly and prepares for life outside the womb.</p></div>
<div class="sj-grid-card"><h4>After birth</h4><p>Newborn care includes warmth, timely vaccination and appropriate feeding. The mother's nutrition, rest and well-being are also important.</p></div>
</div>
<p>The chapter emphasises balanced nutrition, regular medical check-ups, adequate rest and following medical advice during pregnancy.</p>
'''),
("13","fa-shield-heart","Sexual Maturity, Menstrual Health and Pregnancy Prevention",r'''
<p>Sexual maturity means that the body becomes capable of reproduction. It occurs gradually during adolescence, while emotional and social maturity develop over a longer period. Responsible decision-making is therefore important.</p>
<p><strong>Sexually Transmitted Infections (STIs)</strong> can spread through sexual contact. The chapter names infections including gonorrhoea, herpes, syphilis, genital warts and HIV. Condoms can help reduce STI transmission and also help prevent pregnancy.</p>
<table class="sj-table"><thead><tr><th>Method</th><th>Basic action</th></tr></thead><tbody>
<tr><td>Condoms / barrier methods</td><td>Help prevent sperm from reaching the egg and reduce transmission of STIs.</td></tr>
<tr><td>Oral contraceptive pills</td><td>Use hormones to alter the release of eggs; the chapter notes possible side effects.</td></tr>
<tr><td>IUD such as Copper-T</td><td>Placed in the uterus to prevent pregnancy.</td></tr>
<tr><td>Surgical methods</td><td>Block the vas deferens or fallopian tubes so sperm and egg cannot meet.</td></tr>
</tbody></table>
<div class="sj-detail"><h4>Menstrual hygiene</h4><p>The chapter recommends clean menstrual products, regular changing, hand washing before and after changing products, proper disposal, and correct cleaning and drying of reusable products.</p></div>
''' + check_block("Pause and Ponder","What protective devices can be used during sexual activity to reduce the spread of STIs?","<strong>Condoms</strong> are protective barrier devices that can reduce the spread of many STIs and also help prevent pregnancy.") +
check_block("Pause and Ponder","If a couple uses oral contraceptive pills but not condoms, which risks remain and why?","Oral contraceptive pills can help prevent pregnancy but do <strong>not</strong> provide protection against STIs. Therefore, STI transmission remains a risk.") +
check_block("Pause and Ponder","In many animals, the young ones can walk or find food soon after birth but human babies are completely dependent on adults for a long time. What might be some advantages and disadvantages of this for humans as a species?","A long period of care allows the human brain and body to develop with extensive learning, socialisation and skill-building. The disadvantage is prolonged parental time, food, protection and social support before independence."))
]
CONCEPTS.extend([
("14","fa-wind","Pollination Agents and Their Adaptations",r'''
<p>Pollination depends on external agents and on structural features that improve pollen transfer.</p>
<table class="sj-table"><thead><tr><th>Agent</th><th>Examples</th><th>Adaptations described in the chapter</th></tr></thead><tbody>
<tr><td>Wind</td><td>Wheat, maize, rice</td><td>Light and small pollen, produced in large numbers; stigma is long and feathery.</td></tr>
<tr><td>Water</td><td>Vallisneria, Hydrilla</td><td>Water currents carry pollen from one flower to another.</td></tr>
<tr><td>Insects</td><td>Sunflower, hibiscus, marigold</td><td>Bright colour, nectar and fragrance; pollen may be large, sticky or spiny; stigma may be sticky.</td></tr>
<tr><td>Birds</td><td>Coral tree, hibiscus</td><td>Flowers can attract bird pollinators such as sunbirds.</td></tr>
</tbody></table>
<div class="sj-detail"><h4>Exam reasoning</h4><p><strong>Light + abundant pollen + feathery stigma</strong> points to wind. <strong>Colour + nectar + fragrance + sticky pollen</strong> points to insects. <strong>Water currents</strong> point to water pollination.</p></div>
'''),
("15","fa-chart-bar","Pollination Data and Experimental Thinking",r'''
<p>The chapter compares wind-pollinated grasses with insect-pollinated sunflower using approximate pollen-production and seed-formation data.</p>
<table class="sj-table"><thead><tr><th>Strategy</th><th>Pollen grains / flower</th><th>Estimated seeds formed</th></tr></thead><tbody>
<tr><td>Wind-pollinated grasses</td><td>5,00,000–10,00,000</td><td>50–200</td></tr>
<tr><td>Insect-pollinated plants</td><td>20,000–40,000</td><td>800–1,000</td></tr>
</tbody></table>
<p>Producing huge quantities of pollen can compensate for the low probability that an individual pollen grain reaches a compatible stigma. Insect pollination can use fewer pollen grains because pollinators transport pollen more directly.</p>
<div class="sj-detail"><h4>Experiment vocabulary</h4><p><strong>Independent variable:</strong> the factor deliberately changed, such as sugar concentration. <strong>Dependent variable:</strong> the response measured, such as pollen germination. <strong>Controlled variables:</strong> factors kept the same, such as pollen source/amount, temperature, volume and observation time.</p></div>
'''),
("16","fa-seedling","Plant Breeding and Applied Reproduction",r'''
<p>Sexual reproduction has practical importance in <strong>plant breeding</strong>. The chapter mentions selective breeding, artificial hybridisation and genetically engineered crops.</p>
<div class="sj-detail"><h4>Selective breeding</h4><p>Plants with desirable characters are selected for reproduction so that useful characteristics can be developed or combined in future generations.</p></div>
<div class="sj-detail"><h4>Artificial hybridisation</h4><p>The chapter describes removing stamens, covering the flower to prevent unwanted self-pollination, and manually transferring pollen with desired characters.</p></div>
<div class="sj-detail"><h4>Genetic engineering</h4><p>Desired genetic material can be introduced into selected varieties to develop traits such as high yield or disease resistance.</p></div>
<p>Vegetative propagation is especially useful when the goal is to multiply a desirable plant while retaining its existing genetic combination.</p>
'''),
("17","fa-fish","Animal Reproductive Strategies and Development",r'''
<p>Animals differ in egg number, fertilisation method and protection of developing young.</p>
<table class="sj-table"><thead><tr><th>Animal</th><th>Habitat</th><th>Fertilisation</th><th>Eggs</th><th>Young survival</th></tr></thead><tbody>
<tr><td>Fish</td><td>Water</td><td>External</td><td>100s–1000s</td><td>Low</td></tr>
<tr><td>Frog</td><td>Water/land</td><td>External</td><td>5,000–50,000</td><td>Low</td></tr>
<tr><td>Lizard</td><td>Land</td><td>Internal</td><td>2–20</td><td>Moderate</td></tr>
<tr><td>Bird</td><td>Water/land</td><td>Internal</td><td>1–15</td><td>Moderate to High</td></tr>
</tbody></table>
<p>Fish, amphibians and insects can produce many eggs and may have a larval stage. The larva feeds and grows before transformation into the adult form. Butterfly: <strong>egg → larva → pupa → adult</strong>. Reptiles and birds produce eggs with enough yolk to nourish the embryo until hatching, while mammals develop the zygote inside the female body.</p>
'''),
("18","fa-user-shield","Human Reproductive Health: Key Connections",r'''
<div class="sj-detail"><h4>From gamete to pregnancy</h4><p><strong>Meiosis → sperm/egg (23 chromosomes) → fertilisation → zygote (46 chromosomes) → mitotic divisions → implantation → embryo → foetus.</strong></p></div>
<div class="sj-detail"><h4>Why implantation matters</h4><p>The chapter states that the zygote divides while travelling to the uterus and then implants into the uterine lining, where it receives nourishment for development.</p></div>
<div class="sj-detail"><h4>Sex chromosomes</h4><p>The chapter explains XX for females and XY for males; the mother contributes X while the father contributes X or Y.</p></div>
<div class="sj-detail"><h4>Menstrual hygiene</h4><p>Use clean products, change them regularly, wash hands before and after changing products, dispose of used products responsibly, and clean and dry reusable products correctly.</p></div>
<div class="sj-detail"><h4>Physical versus emotional maturity</h4><p>Physical sexual maturity develops gradually, while emotional and social maturity take longer. Responsible choices require thoughtful decisions and communication.</p></div>
''')
])

_engine.CONCEPTS = CONCEPTS

# ---------------------------------------------------------------------------
# Official end-of-chapter questions Q1–Q13 ONLY
# ---------------------------------------------------------------------------
_engine.NCERT = [
nq(1,"A flower's anthers are removed before it matures. Later, pollen from another plant of the same species is dusted onto its stigma and seeds are produced. Which process has been ensured here?",
"<p><strong>Answer: (ii) Cross-pollination.</strong> The anthers were removed to prevent self-pollination, and pollen from another plant of the same species was transferred to the stigma.</p>","1",
["(i) Self-pollination","(ii) Cross-pollination","(iii) Fertilisation","(iv) Tissue culture"]),
nq(2,"Arrange the following stages of sexual reproduction in plants in the correct order: (i) Pollen germination on stigma (ii) Fertilisation (iii) Pollination (iv) Formation of zygote",
"<p><strong>Answer: (iii) → (i) → (ii) → (iv).</strong> First pollen is transferred to the stigma, then it germinates, fertilisation occurs, and a zygote is formed.</p>","1"),
nq(3,"Assertion (A): The zygote formed after fertilisation immediately attaches to the uterus wall.<br>Reason (R): The uterus wall is always prepared to receive the zygote.",
"<p><strong>Answer: (iv) A is false, but R is true.</strong> The zygote first undergoes mitotic divisions while travelling towards the uterus and then implants. The uterine lining prepares for possible implantation during the cycle.</p>","2",
["(i) Both A and R are true, and R is the correct explanation of A.","(ii) Both A and R are true, but R is not the correct explanation of A.","(iii) A is true, but R is false.","(iv) A is false, but R is true."]),
nq(4,"Why does asexual reproduction produce offsprings that are genetically identical to the parent?",
"<p>Asexual reproduction involves one parent and no fusion of gametes from two parents. Offspring arise through cell division such as mitosis and generally receive the same genetic information and chromosome number. They are therefore called <strong>clones</strong>.</p>","2"),
nq(5,"Explain why the menstrual cycle stops during pregnancy.",
"<p>During pregnancy the embryo/foetus is developing in the uterus and the uterine lining is maintained to support it. The normal shedding of the lining therefore does not occur as menstruation.</p>","2"),
nq(6,"Why are flowers that bloom at night white or light in colour as compared to flowers that bloom during the day?",
"<p>Light-coloured flowers are easier to see in low light. This can help attract nocturnal pollinators and support pollen transfer.</p>","2"),
nq(7,"Why do vegetatively propagated plants tend to be more vulnerable to diseases than sexually reproduced plants?",
"<p>Vegetative propagation produces genetically very similar or identical plants. If a disease can infect one plant effectively, many genetically similar plants may also be susceptible. Sexual reproduction produces variation, so some offspring may have greater resistance.</p>","3"),
nq(8,"If all flowers in a type of plant were only capable of self-pollination, how would it affect the genetic diversity over several generations? Explain.",
"<p>Exclusive self-pollination would reduce mixing of genetic material between different plants. Over generations, genetic diversity would generally be lower than with cross-pollination. Reduced variation can limit the range of responses available when environmental conditions change.</p>","3"),
nq(9,"A farmer wants to produce a large number of genetically identical plants quickly. Suggest suitable reproduction methods and explain why they are effective.",
"<p><strong>Suitable methods:</strong> cutting, layering, grafting where appropriate, and especially <strong>tissue culture</strong> for rapid large-scale multiplication. They use vegetative material from a desirable parent and do not require seed formation, so many genetically similar plants can be produced quickly.</p>","3"),
nq(10,"Suresh prepares slides with pollen grains in different sugar concentrations (0%, 2.5%, 5%, 7.5%, 10%) to study the germination of pollen.<br><br>(i) What are the different hypotheses which can be tested using this set-up?<br>(ii) What parameters should be kept the same in this set-up?",
"<p><strong>(i) Hypotheses:</strong> sugar concentration affects pollen germination; there may be an optimum concentration at which germination is greatest; concentrations that are too low or too high may reduce germination.</p><p><strong>(ii) Controlled parameters:</strong> type/source and amount of pollen, volume of solution, temperature, time allowed for germination, slide conditions and observation conditions. Only sugar concentration should be deliberately varied.</p>","3"),
nq(11,"Look at the picture given below and think in line with the given prompts and find out which type(s) of pollination might have been followed in these flowers — Tomato, Wheat, Papaya.",
"<p><strong>Tomato:</strong> the arrangement described suggests self-pollination is likely. <strong>Wheat:</strong> wind pollination is indicated by its adaptations. <strong>Papaya:</strong> male and female flowers are often borne on different plants, so pollen transfer between plants is cross-pollination.</p>","3"),
nq(12,"In the lower Himalayan region of northern India, apple yield is declining along with a decline in natural pollinators. Two orchards, A and B, were compared; A used natural pollinators and B used beekeeping. Answer: (i) What hypotheses were considered? (ii) What are the different parameters? (iii) Compare the two orchards in terms of high apple yield. (iv) What do you infer from the data?",
"<p><strong>(i)</strong> A hypothesis is that increasing pollinator availability through beekeeping may increase fruit setting and/or reduce fruit drop, increasing apple yield.</p><p><strong>(ii)</strong> Parameters include pollination treatment, fruit setting, fruit drop and resulting apple yield.</p><p><strong>(iii)–(iv)</strong> The supplied text refers to Fig. 11.24 for the numerical comparison, but the plotted values are not present in the supplied text extract. Exact values should therefore be read from the figure. The intended experimental inference is that better pollination should be associated with higher fruit setting, lower fruit drop and higher yield.</p>","4"),
nq(13,"A student claims, “In humans, ovulation always happens on day 14 of the menstrual cycle”. Critically examine this claim and state whether the claim is correct or not. Give at least two reasons for your answer.",
"<p>The claim is <strong>not universally correct</strong>. (1) Day 14 is an approximate point in a typical 28-day cycle, not a fixed rule for every person. (2) The chapter gives a common cycle range of about 21–35 days. Therefore ovulation timing can vary between people and cycles.</p>","3")
]

# ---------------------------------------------------------------------------
# Chapter 11 quiz and tests
# ---------------------------------------------------------------------------
def q(question, options, answer, explanations, hint="Use the chapter concept and the exact sequence or definition involved."):
    return {"question":question,"options":options,"correctIdx":answer,"hint":hint,"explanations":explanations}
_engine.QUIZ = [
q("Asexual reproduction usually involves:",["one parent","two parents","three parents","no parent"],0,
["Correct: asexual reproduction usually involves one parent.","Two-parent genetic contribution is sexual reproduction.","Three parents are not involved.","The offspring arise from a living parent."]),
q("Vegetative propagation is reproduction using:",["vegetative parts of plants","only seeds","only pollen","only flowers"],0,
["Correct: stems, leaves and other vegetative parts can produce new plants.","Seed formation is not required.","Pollen is involved in sexual reproduction.","Flowers are reproductive organs but are not required for vegetative propagation."]),
q("Genetically identical asexual offspring are called:",["hybrids","clones","gametes","zygotes"],1,
["Hybrids arise from crossing genetically different parents.","Correct: genetically identical offspring are clones.","Gametes are reproductive cells.","A zygote forms after fertilisation."]),
q("Meiosis reduces chromosome number to:",["double","half","zero","four times"],1,
["Meiosis does not double the chromosome number.","Correct: meiosis produces haploid cells with half the chromosome number.","Chromosomes are not eliminated.","Fourfold increase is incorrect."]),
q("Human sperm normally contains:",["23 chromosomes","46 chromosomes","92 chromosomes","12 chromosomes"],0,
["Correct: human sperm is haploid and has 23 chromosomes.","46 is the usual number in human body cells and the zygote.","92 is incorrect.","12 is incorrect."]),
q("The male reproductive part of a flower is the:",["pistil","stamen","ovary","stigma"],1,
["Pistil is the female reproductive part.","Correct: stamen is the male reproductive part.","Ovary is part of the pistil.","Stigma is the receptive tip of the pistil."]),
q("The anther produces:",["ovules","pollen grains","seeds","fruits"],1,
["Ovules are in the ovary.","Correct: anther produces pollen grains.","Seeds form after fertilisation.","Ovary develops into fruit."]),
q("Pollination is transfer from:",["anther to stigma","ovary to ovule","stigma to anther","root to stem"],0,
["Correct: pollination is transfer of pollen from anther to stigma.","The ovary does not transfer pollen.","The direction is not stigma to anther.","Roots and stems are not involved in pollination."]),
q("Cross-pollination means pollen transfer:",["within one flower only","between two plants of the same type","from root to flower","from ovary to seed"],1,
["That is not the definition.","Correct: pollen moves from a flower of one plant to another plant of the same type.","Roots do not transfer pollen.","Ovary to seed is not pollination."]),
q("After fertilisation, an ovule develops into a:",["fruit","seed","petal","stigma"],1,
["The ovary develops into fruit.","Correct: the ovule develops into a seed.","Petals do not develop into seeds.","Stigma is part of the pistil."]),
q("External fertilisation is common in:",["frogs and most fish","birds only","mammals only","reptiles only"],0,
["Correct: the chapter gives frogs and most fish as examples.","Birds generally use internal fertilisation.","Mammals generally use internal fertilisation.","Reptiles generally use internal fertilisation."]),
q("The organ producing sperm is the:",["ovary","testis","uterus","oviduct"],1,
["Ovaries produce eggs.","Correct: testes produce sperm.","The uterus supports foetal development.","The oviduct carries the egg."]),
q("Ovulation means:",["release of a mature egg","shedding of uterine lining","formation of sperm","implantation"],0,
["Correct: ovulation is release of a mature egg from an ovary.","Shedding is menstruation.","Sperm formation is gametogenesis in testes.","Implantation is attachment in the uterine lining."]),
q("Menstruation involves shedding of the:",["uterine lining","ovary","testis","pollen tube"],0,
["Correct: the uterine lining is shed.","The ovary is not shed.","The testis is a male organ.","Pollen tubes are plant structures."]),
q("A human zygote normally has:",["23 chromosomes","46 chromosomes","92 chromosomes","12 chromosomes"],1,
["23 is the chromosome number of a human gamete.","Correct: 23 + 23 = 46 in the zygote.","92 is incorrect.","12 is incorrect."]),
q("The uterus is the organ in which:",["a foetus develops","sperm are produced","pollen is formed","spores are made"],0,
["Correct: the foetus develops in the uterus.","Sperm are produced in testes.","Pollen is produced in anthers.","Spores are reproductive structures of organisms such as fungi."]),
q("A pollen tube grows through the:",["style","sepal","filament","petal"],0,
["Correct: pollen tube grows through the style toward the ovary.","Sepals protect the bud.","Filament supports the anther.","Petals often attract pollinators."]),
q("Fertilisation is:",["fusion of male and female gametes","transfer of pollen","formation of a bud","shedding of the uterine lining"],0,
["Correct: fertilisation is fusion of male and female gametes.","Pollen transfer is pollination.","Bud formation is budding.","Shedding is menstruation."]),
q("A major advantage of sexual reproduction is:",["genetic variation","genetic identity of all offspring","absence of gametes","no meiosis"],0,
["Correct: sexual reproduction creates genetic variation.","Genetic identity is more characteristic of asexual reproduction.","Sexual reproduction requires gametes.","Meiosis is important in gamete formation."]),
q("A farmer wanting many genetically identical plants should favour:",["vegetative propagation","cross-pollination only","meiosis only","seed dispersal"],0,
["Correct: vegetative propagation can rapidly multiply desirable plants.","Cross-pollination increases genetic mixing.","Meiosis forms gametes.","Seed dispersal spreads seeds but does not guarantee genetic identity."]),
q("The female reproductive organs that produce eggs are:",["testes","ovaries","prostate glands","seminal vesicles"],1,
["Testes produce sperm.","Correct: ovaries produce eggs.","Prostate adds fluid to semen.","Seminal vesicles add nourishing fluid."]),
q("Condoms can help:",["prevent pregnancy and reduce STI transmission","cause ovulation","produce eggs","form pollen tubes"],0,
["Correct: condoms are barrier methods that help prevent pregnancy and reduce transmission of many STIs.","Condoms do not cause ovulation.","Eggs are produced by ovaries.","Pollen tubes belong to plant reproduction."]),
q("Oral contraceptive pills are described as methods that:",["alter hormonal control of egg release","produce sperm","produce pollen","double chromosomes"],0,
["Correct: the chapter describes hormonal alteration of egg release.","Sperm are produced in testes.","Pollen is produced in anthers.","Contraceptive pills do not double chromosomes."]),
q("A typical 28-day cycle is used in the chapter to illustrate ovulation around:",["day 1","day 7","day 14","day 28"],2,
["Day 1 is the start of menstruation in the typical pattern.","Day 7 is within the rebuilding phase.","Correct: the chapter places ovulation around day 14 in a typical 28-day cycle.","Day 28 is near the end of the illustrated cycle."]),
q("Which process restores the diploid chromosome number?",["fertilisation","pollination","budding","spore formation"],0,
["Correct: fusion of two haploid gametes restores the diploid number.","Pollination is pollen transfer.","Budding is asexual reproduction.","Spore formation is asexual reproduction in fungi."]),
q("Tissue culture is useful because it can:",["produce many healthy plantlets","produce human sperm","cause menstruation","prevent meiosis"],0,
["Correct: tissue culture is used for mass propagation of healthy plantlets.","It is not a method for producing human sperm.","It does not cause menstruation.","It does not prevent meiosis."]),
q("A population of vegetatively propagated plants has low variation. A new disease appears. A likely risk is:",["many plants may be susceptible","all plants must be resistant","variation immediately becomes high","pollination becomes impossible"],0,
["Correct: genetic similarity can make many plants susceptible to the same disease.","Resistance is not guaranteed.","Asexual reproduction does not suddenly create high variation.","Pollination is not necessarily impossible."]),
q("The stigma, style and ovary together form the:",["stamen","pistil","anther","filament"],1,
["Stamen is the male part.","Correct: stigma, style and ovary form the pistil.","Anther is part of the stamen.","Filament supports the anther."]),
q("The long period of dependence of human babies allows:",["extended development and learning","immediate independence","absence of parental care","no social development"],0,
["Correct: prolonged care allows extensive physical, cognitive and social development.","Human babies do not become immediately independent.","Parental care is important.","Social development is strongly supported by prolonged care."]),
q("Which statement is correct?",["Pollination and fertilisation are the same","Pollination is pollen transfer; fertilisation is gamete fusion","Ovulation is menstruation","A zygote has 23 chromosomes"],1,
["They are different processes.","Correct: pollination is pollen transfer, while fertilisation is fusion of gametes.","Ovulation and menstruation are different processes.","A normal human zygote has 46 chromosomes."])
]

def mcq(question, options, answer, marks=1):
    return {"type":"mcq","marks":marks,"question":question,"options":options,"correctIdx":answer}
def ar(question, options, answer):
    return {"type":"ar","marks":1,"question":question,"options":options,"correctIdx":answer}
def sub(question, answer, marks=2):
    return {"type":"subjective","marks":marks,"question":question,"sampleAnswer":answer}

_engine.TESTS = {
"basic":[
mcq("Reproduction ensures:",["continuity of life","loss of cells","absence of variation","death of offspring"],0),
mcq("Asexual reproduction generally involves:",["one parent","two parents","three parents","no organism"],0),
mcq("The male part of a flower is:",["pistil","stamen","ovary","stigma"],1),
ar("Assertion (A): Asexual offspring are generally genetically identical to the parent.\n\nReason (R): Asexual reproduction does not involve fusion of gametes from two parents.",["(A) Both A and R are true and R is the correct explanation of A.","(B) Both A and R are true but R is not the correct explanation of A.","(C) A is true but R is false.","(D) A is false but R is true."],0),
sub("What is vegetative propagation?","It is asexual reproduction in plants in which new plants arise from vegetative parts such as stems or leaves.",2),
sub("Why are asexual offspring called clones?","They are generally genetically identical to the parent because there is no mixing of genetic material from two parents.",2),
sub("What is pollination?","Pollination is the transfer of pollen grains from the anther to the stigma of a flower.",3),
sub("Differentiate stamen and pistil.","The stamen is the male reproductive part and consists of filament and anther. The pistil is the female reproductive part and consists of stigma, style and ovary.",3),
sub("Explain the role of meiosis in sexual reproduction.","Meiosis reduces the chromosome number to half in gamete-forming cells, so fusion of two haploid gametes restores the diploid number instead of doubling it each generation.",5),
sub("Case: A student sees a small outgrowth on a yeast cell and later sees a new cell separate from it. Identify the process and explain it.","The process is budding. Repeated cell division at a particular site forms a bud; the bud grows and may separate from the parent to live independently.",5)
],
"standard":[
mcq("A farmer wants many genetically identical plants quickly. The best approach is:",["vegetative propagation/tissue culture","cross-pollination only","meiosis only","seed dispersal"],0),
mcq("A human zygote normally contains:",["23","46","69","92"],1),
mcq("Correct sequence in flowering plants:",["pollination → pollen germination → fertilisation → zygote","fertilisation → pollination → zygote","zygote → pollination → fertilisation","pollen germination → menstruation"],0),
ar("Assertion (A): Cross-pollination can increase genetic variation between offspring.\n\nReason (R): It transfers pollen from one plant to another plant of the same type.",["(A) Both A and R are true and R is the correct explanation of A.","(B) Both A and R are true but R is not the correct explanation of A.","(C) A is true but R is false.","(D) A is false but R is true."],0),
sub("Differentiate self-pollination and cross-pollination.","Self-pollination is transfer to the same flower or another flower of the same plant. Cross-pollination is transfer from one plant to another plant of the same type.",2),
sub("Why do animals with external fertilisation generally produce many eggs?","Many eggs can be destroyed by water currents or eaten by other animals. Producing many increases the chance that some offspring survive.",2),
sub("Explain how a pollen tube leads to fertilisation.","After pollen reaches a compatible stigma it germinates and forms a pollen tube through the style. The male gamete travels through the tube to the ovule and fuses with the egg cell.",3),
sub("Explain the formation of seed and fruit after fertilisation.","The fertilised egg forms a zygote and develops into an embryo. The ovules develop into seeds, while the ovary enlarges and develops into a fruit.",3),
sub("Explain why meiosis is essential for maintaining chromosome number across generations.","Meiosis forms haploid gametes with half the chromosome number. In humans, sperm and eggs have 23 chromosomes; their fusion forms a zygote with 46, preventing chromosome number from doubling every generation.",5),
sub("Case: A flower has bright petals, fragrance, nectar and sticky pollen. Predict the likely pollination agent and justify your answer.","Insect pollination is likely. The chapter associates bright colour, nectar and fragrance with attraction of insects; sticky or spiny pollen can attach to an insect’s body and a sticky stigma can receive it.",5)
],
"advanced":[
mcq("Why can a genetically uniform crop be vulnerable when a disease appears?",["many plants may share susceptibility","all plants become resistant","variation becomes maximum","pollination stops"],0),
mcq("Why is day 14 not a universal ovulation day?",["cycle length and timing vary","ovulation never occurs","all cycles last exactly 14 days","gametes contain 46 chromosomes"],0),
mcq("In a pollen-germination experiment, which should be kept constant?",["temperature","sugar concentration","the independent variable","the treatment being tested"],0),
ar("Assertion (A): Internal fertilisation generally gives greater protection to the developing embryo.\n\nReason (R): Fertilisation and early development occur inside the female body.",["(A) Both A and R are true and R is the correct explanation of A.","(B) Both A and R are true but R is not the correct explanation of A.","(C) A is true but R is false.","(D) A is false but R is true."],0),
sub("Why does exclusive self-pollination tend to reduce genetic diversity compared with cross-pollination?","It reduces mixing of genetic material between different plants. Over generations, the population generally has less genetic variation than a population in which pollen is exchanged between plants.",2),
sub("Explain why vegetatively propagated plants can be more vulnerable to the same disease.","Vegetative propagation produces genetically similar or identical plants. If one plant is susceptible to a disease, many genetically similar plants may also be susceptible, whereas sexual reproduction introduces more variation.",2),
sub("A pollen experiment uses 0%, 2.5%, 5%, 7.5% and 10% sugar. State the independent variable and two controlled variables.","The independent variable is sugar concentration. Controlled variables can include pollen source/amount, temperature, volume of solution, time allowed and observation conditions.",3),
sub("Explain the difference between external and internal fertilisation with examples.","External fertilisation occurs outside the body, commonly in water, as in frogs and most fish. Internal fertilisation occurs inside the female body, as in reptiles, birds and mammals.",3),
sub("Explain the complete chain from ovulation to implantation in humans.","A mature egg is released during ovulation and enters the oviduct. If sperm fuses with the egg, a zygote forms. It undergoes mitotic divisions while travelling to the uterus and then implants in the uterine lining, where it receives nourishment.",5),
sub("Case: An orchard introduces beekeeping and records fruit setting and fruit drop. Design the reasoning for the investigation: state a hypothesis, identify variables, and give the expected interpretation if fruit setting rises and fruit drop falls.","A suitable hypothesis is that increasing pollinator availability improves pollination and therefore increases fruit setting and reduces fruit drop. The treatment is pollinator availability; fruit setting and fruit drop are measured responses. If fruit setting rises while fruit drop falls, the data support the idea that better pollination improves reproductive success and can increase yield.",5)
]
}

# ---------------------------------------------------------------------------
# Revision page
# ---------------------------------------------------------------------------
_engine.REVISION = r'''
<section class="sj-card"><div class="sj-cheader"><div class="sj-cicon"><i class="fas fa-bolt"></i></div><div><h2>Chapter 11 — Master Revision</h2><p class="sj-section-subtitle">Definitions • sequences • comparisons • mnemonics • exam traps</p></div></div>
<div class="sj-detail"><h4>One-page concept map</h4><p><strong>Reproduction → Asexual / Sexual.</strong> Asexual → one parent → mitosis → clones → rapid multiplication. Sexual → gametes → meiosis → fertilisation → zygote → variation. Plants → flower → pollination → pollen tube → fertilisation → seed + fruit. Humans → gametogenesis → ovulation → possible fertilisation → implantation → pregnancy.</p></div></section>
<section class="sj-card"><h2>Must-Know Definitions</h2><div class="sj-grid">
<div class="sj-grid-card"><h4>Reproduction</h4><p>Biological process by which living organisms produce new individuals of their own kind.</p></div>
<div class="sj-grid-card"><h4>Asexual reproduction</h4><p>Reproduction involving a single parent, generally producing genetically identical offspring.</p></div>
<div class="sj-grid-card"><h4>Vegetative propagation</h4><p>Formation of new plants from vegetative parts such as stems or leaves.</p></div>
<div class="sj-grid-card"><h4>Budding</h4><p>Formation of a new individual as an outgrowth from the parent.</p></div>
<div class="sj-grid-card"><h4>Spore formation</h4><p>Production of numerous lightweight spores that can disperse and germinate under suitable conditions.</p></div>
<div class="sj-grid-card"><h4>Meiosis</h4><p>Cell division that reduces chromosome number to half in gamete-forming cells.</p></div>
<div class="sj-grid-card"><h4>Pollination</h4><p>Transfer of pollen from anther to stigma.</p></div>
<div class="sj-grid-card"><h4>Fertilisation</h4><p>Fusion of male and female gametes to form a zygote.</p></div>
<div class="sj-grid-card"><h4>Ovulation</h4><p>Release of a mature egg from an ovary.</p></div>
<div class="sj-grid-card"><h4>Menstruation</h4><p>Shedding of the uterine lining when pregnancy has not occurred.</p></div>
<div class="sj-grid-card"><h4>Gametogenesis</h4><p>Formation of reproductive cells.</p></div>
<div class="sj-grid-card"><h4>Implantation</h4><p>Attachment of the developing conceptus to the uterine lining after travel to the uterus.</p></div>
</div></section>
<section class="sj-card"><h2>Asexual Reproduction — Methods at a Glance</h2><table class="sj-table"><thead><tr><th>Method</th><th>Key idea</th><th>Examples / use</th></tr></thead><tbody>
<tr><td>Vegetative propagation</td><td>New plant from vegetative part</td><td>Potato, ginger, sugarcane, money plant, Bryophyllum</td></tr><tr><td>Cutting</td><td>Stem cutting develops into plant</td><td>Horticultural propagation</td></tr><tr><td>Grafting</td><td>Stem piece fitted into rooted plant</td><td>Desirable varieties</td></tr><tr><td>Layering</td><td>Buried twig develops roots before separation</td><td>Flexible twigs such as lemon</td></tr><tr><td>Tissue culture</td><td>Plant material produces many plantlets</td><td>Mass multiplication, including banana</td></tr><tr><td>Budding</td><td>Outgrowth develops on parent</td><td>Yeast, hydra</td></tr><tr><td>Spore formation</td><td>Many lightweight spores disperse</td><td>Fungi/moulds</td></tr>
</tbody></table><p><strong>Memory aid:</strong> <strong>CGLT</strong> = Cutting, Grafting, Layering, Tissue culture.</p></section>
<section class="sj-card"><h2>Sexual Reproduction and Meiosis</h2><div class="sj-detail"><h4>Chromosome logic</h4><p><strong>Diploid 46 → meiosis → haploid 23 + haploid 23 → fertilisation → zygote 46.</strong></p></div><p>Meiosis prevents chromosome number from doubling each generation and creates different combinations of chromosomes in gametes. Sexual reproduction combines genetic material from two individuals, producing variation.</p><p><strong>Exam trap:</strong> meiosis reduces chromosome number; fertilisation restores it.</p></section>
<section class="sj-card"><h2>Flower — Structure to Memorise</h2><table class="sj-table"><thead><tr><th>Part</th><th>Subparts / feature</th><th>Key fact</th></tr></thead><tbody>
<tr><td>Sepal</td><td>Outer whorl</td><td>Protects flower in bud</td></tr><tr><td>Petal</td><td>Often coloured/fragrant</td><td>Can attract pollinators</td></tr><tr><td>Stamen</td><td>Filament + anther</td><td>Male part; anther produces pollen</td></tr><tr><td>Pistil</td><td>Stigma + style + ovary</td><td>Female part; ovary contains ovules</td></tr>
</tbody></table><p><strong>Mnemonic: S-P-S-P</strong> = Sepal, Petal, Stamen, Pistil. <strong>Pistil: S-S-O</strong> = Stigma → Style → Ovary. <strong>Stamen: F-A</strong> = Filament + Anther.</p></section>
<section class="sj-card"><h2>Pollination — Never Confuse These</h2><table class="sj-table"><thead><tr><th>Type</th><th>Pollen movement</th></tr></thead><tbody><tr><td>Self-pollination</td><td>Same flower or another flower of the same plant</td></tr><tr><td>Cross-pollination</td><td>One plant → another plant of the same type</td></tr></tbody></table><p><strong>Agents:</strong> Wind (wheat, maize, rice), Water (Vallisneria, Hydrilla), Insects (sunflower, hibiscus, marigold), Birds (coral tree, hibiscus).</p><p><strong>Mnemonic: W-W-I-B</strong> = Wind, Water, Insects, Birds.</p></section>
<section class="sj-card"><h2>Fertilisation → Seed → Fruit</h2><p><strong>Pollination → pollen germination → pollen tube → male gamete → ovule → fertilisation → zygote → embryo.</strong></p><div class="sj-grid"><div class="sj-grid-card"><h4>Ovule</h4><p>After fertilisation → <strong>seed</strong>.</p></div><div class="sj-grid-card"><h4>Ovary</h4><p>After fertilisation → <strong>fruit</strong>.</p></div></div><p><strong>High-frequency distinction:</strong> Pollination = transfer; fertilisation = fusion.</p></section>
<section class="sj-card"><h2>Animal Reproductive Strategies</h2><table class="sj-table"><thead><tr><th>External</th><th>Internal</th></tr></thead><tbody><tr><td>Outside female body</td><td>Inside female body</td></tr><tr><td>Frog, most fish</td><td>Reptiles, birds, mammals</td></tr><tr><td>More eggs because losses can be high</td><td>Greater protection</td></tr></tbody></table><p><strong>Butterfly:</strong> Egg → Larva → Pupa → Adult. Memory aid: <strong>ELPA</strong>.</p></section>
<section class="sj-card"><h2>Human Reproductive System</h2><div class="sj-grid"><div class="sj-grid-card"><h4>Male</h4><p>Testes → sperm + hormones. Vas deferens → sperm transport. Urethra → common passage. Seminal vesicles and prostate → supporting fluids. Scrotum → cooler environment for sperm formation.</p></div><div class="sj-grid-card"><h4>Female</h4><p>Ovaries → eggs + hormones. Oviducts → connect ovaries to uterus. Uterus → foetal development. Cervix → passage between uterus and vagina.</p></div></div><p><strong>Routes:</strong> Testis → Vas deferens → Urethra. Ovary → Oviduct → Uterus → Cervix → Vagina.</p></section>
<section class="sj-card"><h2>Sperm vs Egg</h2><table class="sj-table"><thead><tr><th>Feature</th><th>Sperm</th><th>Egg</th></tr></thead><tbody><tr><td>Size</td><td>Very small</td><td>Large</td></tr><tr><td>Number</td><td>Millions</td><td>Few</td></tr><tr><td>Stored nutrients</td><td>Absent</td><td>Present</td></tr><tr><td>Motility</td><td>Actively motile</td><td>Non-motile</td></tr></tbody></table></section>
<section class="sj-card"><h2>Ovulation, Fertilisation and Implantation</h2><p><strong>Ovulation:</strong> mature egg released from ovary. <strong>Fertilisation:</strong> sperm fuses with egg in the oviduct, forming zygote. <strong>Implantation:</strong> developing zygote/embryonic stage attaches to uterine lining after mitotic divisions during travel.</p><p><strong>Chromosome checkpoint:</strong> sperm 23 + egg 23 = zygote 46.</p></section>
<section class="sj-card"><h2>Menstrual Cycle</h2><table class="sj-table"><thead><tr><th>Typical stage</th><th>Main event</th></tr></thead><tbody><tr><td>Days 1–5</td><td>Menstruation — lining shed</td></tr><tr><td>Days 6–14</td><td>Lining rebuilds; egg matures</td></tr><tr><td>Around day 14</td><td>Ovulation in a typical 28-day cycle</td></tr><tr><td>Days 15–28</td><td>Lining becomes thicker; without fertilisation it breaks down</td></tr></tbody></table><p><strong>Important:</strong> the chapter gives a common cycle range of 21–35 days, so day 14 is not a universal fixed day.</p><p><strong>Memory sequence:</strong> Shedding → Building → Releasing → Thickening → Repeat.</p></section>
<section class="sj-card"><h2>Pregnancy and Maternal Health</h2><p>Pregnancy lasts about nine months and is described in three trimesters. First: embryo development and major organ formation. Second: substantial foetal growth and commonly felt movements. Third: rapid growth and preparation for life outside the womb.</p><p>Balanced nutrition, regular medical check-ups, adequate rest, medical advice and emotional support are emphasised for maternal and foetal well-being.</p></section>
<section class="sj-card"><h2>Sexual Maturity, STIs and Pregnancy Prevention</h2><p>Sexual maturity develops gradually, while emotional and social maturity take longer. Responsible choices help prevent unplanned pregnancy and reduce STI risk.</p><table class="sj-table"><thead><tr><th>Method</th><th>Core idea</th></tr></thead><tbody><tr><td>Condom/barrier</td><td>Helps prevent sperm from reaching egg and reduces transmission of many STIs.</td></tr><tr><td>Oral pills</td><td>Hormonal method affecting egg release; possible side effects are noted.</td></tr><tr><td>IUD/Copper-T</td><td>Placed in uterus to prevent pregnancy.</td></tr><tr><td>Surgical methods</td><td>Block vas deferens or fallopian tubes so sperm and egg cannot meet.</td></tr></tbody></table><p><strong>Exam trap:</strong> oral contraceptive pills help prevent pregnancy but do not provide STI protection; condoms provide barrier protection.</p></section>
<section class="sj-card"><h2>Master Mnemonics & Quick Tricks</h2><div class="sj-detail"><h4>Flower parts</h4><p><strong>S-P-S-P</strong> = Sepal, Petal, Stamen, Pistil.</p></div><div class="sj-detail"><h4>Stamen</h4><p><strong>F-A</strong> = Filament + Anther.</p></div><div class="sj-detail"><h4>Pistil</h4><p><strong>S-S-O</strong> = Stigma → Style → Ovary.</p></div><div class="sj-detail"><h4>Pollination agents</h4><p><strong>W-W-I-B</strong> = Wind, Water, Insects, Birds.</p></div><div class="sj-detail"><h4>Butterfly</h4><p><strong>ELPA</strong> = Egg → Larva → Pupa → Adult.</p></div><div class="sj-detail"><h4>Chromosomes</h4><p><strong>23 + 23 = 46</strong>. Gametes are haploid; zygote is diploid.</p></div><div class="sj-detail"><h4>Plant after fertilisation</h4><p><strong>O-O</strong>: Ovule → seed; Ovary → fruit.</p></div><div class="sj-detail"><h4>Do not mix up</h4><p><strong>Pollination = transfer.</strong> <strong>Fertilisation = fusion.</strong> <strong>Ovulation = egg release.</strong> <strong>Menstruation = lining shedding.</strong> <strong>Implantation = attachment in uterine lining.</strong></p></div></section>
<section class="sj-card"><h2>High-Frequency Exam Traps</h2><ul><li>Pollination does not itself form the zygote; fertilisation forms the zygote.</li><li>Anther produces pollen; stigma receives pollen.</li><li>Ovule becomes seed; ovary becomes fruit.</li><li>Human gametes have 23 chromosomes; the zygote normally has 46.</li><li>Day 14 is typical for a 28-day cycle, not a universal fixed date.</li><li>Asexual offspring are generally genetically identical, which is why they are described as clones.</li><li>External fertilisation is exemplified by frogs and most fish; internal fertilisation by reptiles, birds and mammals in this chapter.</li><li>Oral contraceptive pills do not protect against STIs; barrier protection such as condoms reduces STI transmission risk.</li><li>In experiments, identify the independent variable, dependent variable and controlled variables separately.</li></ul></section>
<section class="sj-card"><h2>60-Second Recall</h2><p><strong>One parent → asexual → mitosis → clone.</strong></p><p><strong>Sexual → meiosis → gametes → fertilisation → zygote → variation.</strong></p><p><strong>Flower: sepal, petal, stamen, pistil.</strong></p><p><strong>Anther → pollen; stigma → receives pollen; ovary → ovules.</strong></p><p><strong>Pollination → pollen tube → fertilisation → zygote → embryo → seed; ovary → fruit.</strong></p><p><strong>Human: testes → sperm; ovaries → egg; 23 + 23 = 46; ovulation → fertilisation → implantation.</strong></p></section>
'''


# ---------------------------------------------------------------------------
# Content renderers
# ---------------------------------------------------------------------------
def concepts_html():
    return "\n".join(
        f'''<section class="sj-card">
<div class="sj-cheader"><div class="sj-cicon"><i class="fas {icon}"></i></div><div><h2>{num}. {title}</h2></div></div>
{body}
</section>'''
        for num,icon,title,body in _engine.CONCEPTS
    )

def ncert_html():
    blocks=[]
    for qno,question,options,answer,marks in _engine.NCERT:
        option_html=""
        if options:
            option_html='<div class="sj-ncert-options"><strong>Options:</strong><ol>' + "".join(
                f"<li>{html.escape(str(o))}</li>" for o in options) + "</ol></div>"
        blocks.append(f'''<div class="sj-ncert-question">
<div class="sj-ncert-qtop"><div class="sj-ncert-qnumber">Q{qno}</div><span class="marks-badge">{marks} Marks</span></div>
<div class="sj-ncert-qtext">{question}</div>{option_html}
<details class="sj-ncert-answer"><summary>View Solution &amp; Marking Scheme</summary>
<div class="sj-answer-content">{answer}</div></details></div>''')
    return f'''<section class="sj-card sj-ncert-card">
<div class="sj-cheader"><div class="sj-cicon" style="color:#e74c3c;"><i class="fas fa-pencil-ruler"></i></div>
<div><h2>Revise, Reflect, Refine</h2><p class="sj-section-subtitle">Questions 1–13</p></div></div>
{"".join(blocks)}</section>'''

_engine.concepts_html = concepts_html
_engine.ncert_html = ncert_html

# Explicitly inject the final UI into each generated page.
def build_content_page(page_type, content):
    template=_engine.TEMPLATES[page_type]
    doc=template.read_text(encoding="utf-8")
    doc=_engine.update_metadata(doc,page_type)
    doc=_engine.replace_tbar(doc,page_type)
    doc=_engine.replace_page_content(doc,content,page_type)
    doc=inject_css(doc)
    doc=doc.replace("<body>","<body>\n<!-- SJMaths Class 9 Science | Chapter 11 | Page: "+page_type+" -->",1)
    output_dir=_engine.CH8/page_type
    output_dir.mkdir(parents=True,exist_ok=True)
    output=output_dir/"index.html"
    output.write_text(doc,encoding="utf-8")
    print(f"✓ {output}")

_engine.build_content_page=build_content_page
_engine.DESCRIPTIONS={
"concepts":"Detailed Class 9 Science Chapter 11 concepts: asexual and sexual reproduction, vegetative propagation, meiosis, flowers, pollination, fertilisation, animal reproduction, human reproduction, menstrual cycle, pregnancy and reproductive health.",
"ncert-exercises":"Official Class 9 Science Chapter 11 Revise, Reflect, Refine end-of-chapter questions Q1–Q13 with model solutions and marking guidance. Embedded textbook checks remain on Concepts.",
"quiz":"Chapter 11 interactive quiz covering reproduction, meiosis, pollination, fertilisation, human reproduction and reproductive health.",
"tests":"Chapter 11 Basic, Standard and Advanced tests.",
"revision-notes":"Chapter 11 revision notes with sequences, comparisons, chromosome numbers and exam traps."
}

def main():
    original_print = builtins.print

    def chapter11_print(*args, **kwargs):
        converted = []
        for value in args:
            if isinstance(value, str):
                replacements = {
                    "SJMaths — Class 9 Science Chapter 9": "SJMaths — Class 9 Science Chapter 11",
                    "Atomic Foundations of Matter": "Reproduction: How Life Continues",
                    "CONTENT:     Chapter 9": "CONTENT:     Chapter 11",
                    "Chapter 9 folder not found": "Chapter 11 folder not found",
                    "chapter-9-atomic-foundations-of-matter/": "chapter-11-reproduction-how-life-continues/",
                    "✓ CHAPTER 9 COMPLETE": "✓ CHAPTER 11 COMPLETE",
                }
                for old, new in replacements.items():
                    value = value.replace(old, new)
                converted.append(value)
            else:
                converted.append(value)
        original_print(*converted, **kwargs)

    builtins.print = chapter11_print
    try:
        _engine.main()
    finally:
        builtins.print = original_print

if __name__=="__main__":
    main()