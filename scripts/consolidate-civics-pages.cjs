const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');

// Definition of consolidations
// Each rule defines:
// - targetDir: path relative to ROOT where consolidated index.html will live
// - title: Clean human title
// - sectionName: Civics syllabus section name
// - oldDirs: array of relative paths whose content/checklists will be merged into targetDir, and replaced with redirects
// - summaryIntro: introductory summary for this combined topic
// - customPoints: key points covering all subtopics
const consolidations = [
  {
    targetDir: 'civics/foundations/civics',
    title: 'Definition, Nature, Scope and Subject Matter of Civics',
    sectionName: 'Civics and the State',
    oldDirs: [
      'civics/foundations/civics/definition',
      'civics/foundations/civics/nature',
      'civics/foundations/civics/subject-matter',
      'civics/foundations/civics/scope'
    ],
    summaryIntro: 'A foundational comprehensive module covering the conceptual origin (civitas), definition, scientific vs normative nature, expanding scope, and core subject matter of Civics for teacher recruitment and competitive exams.',
    points: [
      { bold: 'Meaning & Etymology:', desc: 'Derived from Latin terms "Civis" (citizen) and "Civitas" (city-state), studying citizenship rights and civic duties.' },
      { bold: 'Definitions by Thinkers:', desc: 'E.M. White, Patrick Geddes, and F.J. Gould on civics as the science and art of good citizenship.' },
      { bold: 'Nature of Civics:', desc: 'Examines whether Civics is an observational social science, an art, or a normative discipline dealing with ethical statecraft.' },
      { bold: 'Scope & Subject Matter:', desc: 'Local, national, and international dimensions of human social organization, state institutions, and civic obligations.' }
    ]
  },
  {
    targetDir: 'civics/foundations/state',
    title: 'State: Definition, Essential Elements and Theories of Origin',
    sectionName: 'Civics and the State',
    oldDirs: [
      'civics/foundations/state/definition',
      'civics/foundations/state/elements',
      'civics/foundations/state/theories-of-origin'
    ],
    summaryIntro: 'An integrated study module on the political concept of the State, its four essential constitutive elements, and the major classical and modern theories accounting for its historical origin.',
    points: [
      { bold: 'Definition & Characteristics:', desc: 'Garner, Aristotle, and Woodrow Wilson definitions distinguishing State from Society, Government, and Nation.' },
      { bold: 'Four Constituent Elements:', desc: 'Population, Defined Territory, Government, and Sovereignty (the ultimate internal supremacy and external independence).' },
      { bold: 'Theories of Origin:', desc: 'Divine Origin Theory, Force (Might) Theory, Patriarchal and Matriarchal Theories.' },
      { bold: 'Social Contract & Evolutionary Theories:', desc: 'Hobbes, Locke, Rousseau contractarian perspectives and the Modern Historical / Evolutionary Theory.' }
    ]
  },
  {
    targetDir: 'civics/political-concepts/rights-and-citizenship',
    title: 'Rights and Citizenship',
    sectionName: 'Political Concepts',
    oldDirs: [
      'civics/political-concepts/rights',
      'civics/political-concepts/citizenship'
    ],
    summaryIntro: 'A combined module on the moral, legal, and political theories of individual Rights alongside the evolution, modes of acquisition, loss, and civic responsibilities of Citizenship.',
    points: [
      { bold: 'Theories of Rights:', desc: 'Natural Rights (Locke), Legal Theory of Rights (Bentham/Austin), Historical and Social Welfare Theories (Laski).' },
      { bold: 'Classification of Rights:', desc: 'Civil, Political, Economic, and Fundamental Rights with corresponding moral and legal duties.' },
      { bold: 'Meaning of Citizenship:', desc: 'Full and equal membership in a political community; Jus Soli (soil) vs Jus Sanguinis (blood) principles.' },
      { bold: 'Acquisition & Termination:', desc: 'Naturalization, registration, domicile, and causes of forfeiture of citizenship under constitutional law.' }
    ]
  },
  {
    targetDir: 'civics/government/forms/parliamentary-and-presidential',
    title: 'Parliamentary and Presidential Government',
    sectionName: 'Government and Its Organs',
    oldDirs: [
      'civics/government/forms/parliamentary',
      'civics/government/forms/presidential'
    ],
    summaryIntro: 'A comparative examination of Parliamentary (Cabinet) and Presidential systems, focusing on executive-legislative relations, ministerial responsibility, stability vs accountability, and global models (UK, India vs USA).',
    points: [
      { bold: 'Parliamentary System:', desc: 'Fusion of executive and legislative powers, collective responsibility to the legislature, nominal vs real executive (UK, India).' },
      { bold: 'Presidential System:', desc: 'Strict separation of powers, system of checks and balances, fixed tenure of executive head, non-responsibility to legislature (USA).' },
      { bold: 'Merits & Demerits:', desc: 'Flexibility vs cabinet dictatorship; stability vs legislative deadlock and administrative rigidity.' },
      { bold: 'Comparative Framework:', desc: 'Constitutional conventions, impeachment procedures, and dissolution of lower house differences.' }
    ]
  },
  {
    targetDir: 'civics/government/forms/unitary-and-federal',
    title: 'Unitary and Federal Government',
    sectionName: 'Government and Its Organs',
    oldDirs: [
      'civics/government/forms/unitary',
      'civics/government/forms/federal'
    ],
    summaryIntro: 'A foundational comparative study of territorial distribution of sovereign power between Unitary and Federal constitutions, including quasi-federal structures like the Indian Union.',
    points: [
      { bold: 'Unitary Government:', desc: 'Concentration of all authority in a single central government; local bodies derive delegated power (UK, France, Japan).' },
      { bold: 'Federal Government:', desc: 'Constitutional division of powers between Center and federating Units, dual polity, supremacy of written constitution, independent judiciary (USA, Switzerland).' },
      { bold: 'Indian Federal Character:', desc: '"Union of States" (Article 1), unitary bias / quasi-federal features (K.C. Wheare), single citizenship, integrated judiciary, emergency provisions.' },
      { bold: 'Cooperative Federalism:', desc: 'Seventh Schedule legislative lists (Union, State, Concurrent) and inter-governmental coordination mechanisms.' }
    ]
  },
  {
    targetDir: 'civics/government/organs',
    title: 'Organs of Government: Legislature, Executive and Judiciary',
    sectionName: 'Government and Its Organs',
    oldDirs: [
      'civics/government/organs/legislature',
      'civics/government/organs/executive',
      'civics/government/organs/judiciary'
    ],
    summaryIntro: 'A unified structural overview of the three classical organs of government, their functions, Montesquieu’s Doctrine of Separation of Powers, and reciprocal checks and balances.',
    points: [
      { bold: 'Legislature:', desc: 'Unicameral vs Bicameral law-making bodies, deliberation, financial control, and oversight of the executive.' },
      { bold: 'Executive:', desc: 'Political vs permanent executive (civil service), implementation of statutory law, ordinance powers, and administrative leadership.' },
      { bold: 'Judiciary:', desc: 'Guardian of fundamental rights and constitutional supremacy, rule of law, judicial independence, and judicial review.' },
      { bold: 'Separation of Powers:', desc: 'Montesquieu’s theory and its practical operationalization through institutional checks and balances.' }
    ]
  },
  {
    targetDir: 'civics/elections/reforms-and-voting-behaviour',
    title: 'Electoral Reforms and Voting Behaviour',
    sectionName: 'Elections and Political Behaviour',
    oldDirs: [
      'civics/elections/electoral-reforms',
      'civics/elections/voting-behaviour'
    ],
    summaryIntro: 'A focused module analyzing the dynamics of Indian electoral politics, key reform committee recommendations (Tarkunde, Goswami, Indrajit Gupta), and sociological determinants of voting behaviour.',
    points: [
      { bold: 'Key Electoral Reform Committees:', desc: 'Tarkunde (1975), Goswami (1990), Indrajit Gupta (1998), and Law Commission reports on election expenditure and criminalization.' },
      { bold: 'Technological & Legal Reforms:', desc: 'EVMs, VVPAT, NOTA option, Model Code of Conduct, Anti-Defection law (52nd & 91st Amendments).' },
      { bold: 'Determinants of Voting Behaviour:', desc: 'Role of caste, religion, regionalism, language, charismatic leadership, and socio-economic class.' },
      { bold: 'Contemporary Challenges:', desc: 'Money power, disinformation, state funding of elections, and simultaneous elections (One Nation, One Election).' }
    ]
  },
  {
    targetDir: 'civics/union-government/executive/prime-minister-and-council-of-ministers',
    title: 'Prime Minister and Union Council of Ministers',
    sectionName: 'Union Government',
    oldDirs: [
      'civics/union-government/executive/prime-minister',
      'civics/union-government/executive/council-of-ministers'
    ],
    summaryIntro: 'A comprehensive study of the real executive of India under Articles 74, 75, and 78, detailing the role, powers, and appointment of the Prime Minister along with the structure and collective responsibility of the Council of Ministers.',
    points: [
      { bold: 'Constitutional Provisions:', desc: 'Article 74 (aid and advice to President), Article 75 (appointment, tenure, collective responsibility to Lok Sabha), Article 78 (duties of PM).' },
      { bold: 'Prime Minister’s Position:', desc: '"Primus inter pares" (first among equals) and "key-stone of the cabinet arch"; leader of the nation, parliament, and planning bodies.' },
      { bold: 'Three-Tier Council Structure:', desc: 'Cabinet Ministers, Ministers of State (Independent / Attached), and Deputy Ministers; role of Cabinet Secretariat.' },
      { bold: 'Cabinet Government Dynamics:', desc: 'Collective vs individual ministerial responsibility, cabinet committees, and kitchen cabinet phenomena.' }
    ]
  },
  {
    targetDir: 'civics/union-government/parliament',
    title: 'Union Parliament: Lok Sabha and Rajya Sabha',
    sectionName: 'Union Government',
    oldDirs: [
      'civics/union-government/parliament/lok-sabha',
      'civics/union-government/parliament/rajya-sabha'
    ],
    summaryIntro: 'A complete institutional overview of the bicameral Parliament of India (Articles 79–122), contrasting the popular representation of Lok Sabha with the federal representation of Rajya Sabha.',
    points: [
      { bold: 'Lok Sabha (House of the People):', desc: 'Composition, direct election, territorial constituencies, Speaker’s role, money bill monopoly, and no-confidence motions.' },
      { bold: 'Rajya Sabha (Council of States):', desc: 'Permanent house, proportional representation by single transferable vote, special federal powers under Articles 249 and 312.' },
      { bold: 'Legislative Procedure:', desc: 'Ordinary bills, Money bills (Art 110), Financial bills, Joint sitting mechanisms (Art 108).' },
      { bold: 'Parliamentary Control & Devices:', desc: 'Question Hour, Zero Hour, Adjournment Motions, Censure, and Parliamentary Standing Committees (PAC, Estimates).' }
    ]
  },
  {
    targetDir: 'civics/judiciary',
    title: 'Indian Judiciary: Supreme Court and High Courts',
    sectionName: 'Union Government',
    oldDirs: [
      'civics/judiciary/supreme-court',
      'civics/judiciary/high-court'
    ],
    summaryIntro: 'An integrated analysis of India’s single unified judiciary, exploring the hierarchy, appointments (Collegium system), jurisdictions, writ powers, judicial review, and public interest litigation.',
    points: [
      { bold: 'Supreme Court of India (Articles 124–147):', desc: 'Composition, qualifications, removal (impeachment), Original (Art 131), Appellate (Art 132–136), and Advisory Jurisdiction (Art 143).' },
      { bold: 'High Courts (Articles 214–231):', desc: 'Superintendence over subordinate courts (Art 227), court of record, and wide writ jurisdiction under Article 226.' },
      { bold: 'Writ Remedies Comparison:', desc: 'Habeas Corpus, Mandamus, Prohibition, Certiorari, Quo-Warranto under Article 32 vs Article 226.' },
      { bold: 'Independence & Activism:', desc: 'Judicial Review doctrine (Basic Structure), Public Interest Litigation (PIL), and collegium vs NJAC debate.' }
    ]
  },
  {
    targetDir: 'civics/state-government',
    title: 'State Executive: Governor and Chief Minister',
    sectionName: 'State and District Government',
    oldDirs: [
      'civics/state-government/governor',
      'civics/state-government/chief-minister'
    ],
    summaryIntro: 'A comprehensive study of state executive leadership under Part VI of the Constitution, evaluating the Governor’s dual role (constitutional head & Union agent) and the Chief Minister’s real executive authority.',
    points: [
      { bold: 'The Governor (Articles 153–162):', desc: 'Appointment by President, pleasure tenure, executive, legislative (ordinance Art 213), and financial powers.' },
      { bold: 'Discretionary Powers & Controversies:', desc: 'Article 163 discretion, recommendation of President’s Rule (Article 356), reservation of state bills for President (Article 200).' },
      { bold: 'Chief Minister & State Council of Ministers:', desc: 'Appointment under Article 164, head of government, leader of state legislature, coordination of departments.' },
      { bold: 'Centre-State Relations Impact:', desc: 'Sarkaria and Punchhi Commission recommendations on the appointment and non-partisan role of Governors.' }
    ]
  },
  {
    targetDir: 'civics/democracy-and-decentralization/panchayati-raj-and-local-governance',
    title: 'Democratic Decentralization and Panchayati Raj',
    sectionName: 'Democracy and Decentralization',
    oldDirs: [
      'civics/democracy-and-decentralization/democratic-decentralization',
      'civics/democracy-and-decentralization/panchayati-raj'
    ],
    summaryIntro: 'A detailed study of grassroots democracy in India, tracing democratic decentralization from community development projects to the landmark 73rd and 74th Constitutional Amendment Acts.',
    points: [
      { bold: 'Evolution & Committees:', desc: 'Balwant Rai Mehta (three-tier model), Ashok Mehta (two-tier model), G.V.K. Rao, and L.M. Singhvi recommendations.' },
      { bold: '73rd Amendment Act, 1992:', desc: 'Part IX and Eleventh Schedule (29 functional subjects), Gram Sabha, mandatory three-tier structure, 33% reservation for women.' },
      { bold: 'Institutional Mechanics:', desc: 'State Election Commission (Art 243K), State Finance Commission (Art 243I), and five-year fixed tenure.' },
      { bold: 'Urban Local Governance (74th Amendment):', desc: 'Part IXA, Twelfth Schedule (18 subjects), Municipal Corporations, Municipal Councils, and Nagar Panchayats.' }
    ]
  },
  {
    targetDir: 'civics/challenges-of-indian-democracy',
    title: 'Challenges of Indian Democracy: Casteism, Communalism and Regionalism',
    sectionName: 'Democracy and Decentralization',
    oldDirs: [
      'civics/challenges-of-indian-democracy/casteism',
      'civics/challenges-of-indian-democracy/regionalism',
      'civics/challenges-of-indian-democracy/communalism'
    ],
    summaryIntro: 'A cohesive sociological and political analysis of the three foremost internal challenges confronting Indian democratic governance and secular constitutionalism.',
    points: [
      { bold: 'Casteism in Politics:', desc: 'Politicization of caste, vote-bank mobilization, caste-based parties, reservations, and social justice measures.' },
      { bold: 'Communalism:', desc: 'Roots, ideological mobilization, threat to secularism, recommendations of National Integration Council and Sachar Committee.' },
      { bold: 'Regionalism & Sub-nationalism:', desc: 'Sons of the soil doctrine, regional disparities, demands for statehood, inter-state river water disputes.' },
      { bold: 'Remedial Strategies:', desc: 'Constitutional safeguards, inclusive economic development, value education, and strong secular legal enforcement.' }
    ]
  },
  {
    targetDir: 'civics/political-organization',
    title: 'Political Parties and Pressure Groups',
    sectionName: 'Political Organization and Indian Administration',
    oldDirs: [
      'civics/political-organization/political-party',
      'civics/political-organization/pressure-group'
    ],
    summaryIntro: 'A comparative exploration of political transmission mechanisms, examining the organization, functions, and classification of Political Parties versus non-electoral Pressure Groups / Interest Groups.',
    points: [
      { bold: 'Party System Framework:', desc: 'One-party, two-party, and multi-party systems; Duverger’s law and Maurice Duverger’s party structures.' },
      { bold: 'Indian Party System:', desc: 'Evolution from one-party dominant system (Congress system) to multi-party coalition era; National vs State party recognition criteria by ECI.' },
      { bold: 'Pressure Groups (Interest Groups):', desc: 'Definition, methods (lobbying, strikes, petitions, demonstrations), and differences from political parties.' },
      { bold: 'Types of Pressure Groups in India:', desc: 'Business associations (FICCI, CII), trade unions (AITUC, BMS), agrarian groups (BKU), and professional bodies.' }
    ]
  },
  {
    targetDir: 'civics/indian-administration/lokpal-and-lokayukta',
    title: 'Ombudsman, Lokpal and Lokayukta',
    sectionName: 'Political Organization and Indian Administration',
    oldDirs: [
      'civics/indian-administration/ombudsman',
      'civics/indian-administration/lokpal',
      'civics/indian-administration/lokayukta'
    ],
    summaryIntro: 'A comprehensive institutional guide to anti-corruption and grievance redressal mechanisms, tracing the Scandinavian Ombudsman concept to India’s Lokpal and Lokayuktas Act, 2013.',
    points: [
      { bold: 'The Ombudsman Concept:', desc: 'Origin in Sweden (1809), characteristics: independent, impartial, non-partisan officer of parliament investigating administrative maladministration.' },
      { bold: 'Historical Evolution in India:', desc: 'First Administrative Reforms Commission (ARC 1966) chaired by Morarji Desai recommending Lokpal and Lokayukta.' },
      { bold: 'Lokpal and Lokayuktas Act, 2013:', desc: 'Structure of Lokpal (Chairperson + up to 8 members), selection committee, jurisdiction covering PM (with safeguards), ministers, and public servants.' },
      { bold: 'Lokayukta at the State Level:', desc: 'Maharashtra was the first state (1971), statutory variations across states, powers of investigation vs prosecution, and strengthening needs.' }
    ]
  }
];

function generateConsolidatedHtml(item) {
  const relPath = item.targetDir.replace(/\\/g, '/');
  const canonicalUrl = `https://sjmaths.com/${relPath}/`;

  const breadcrumbsHtml = `
      <a href="https://sjmaths.com/">Home</a>
      <span>›</span>
      <a href="/up-tgt-social-science/">Civics</a>
      <span>›</span>
      <span>${item.sectionName}</span>
      <span>›</span>
      <span>${item.title}</span>`;

  const checklistItems = item.points.map(p => `
          <label class="check-item"><input type="checkbox"> <span><strong>${p.bold}</strong> ${p.desc}</span></label>`).join('');

  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${item.title} — Civics Study Guide | SJ Maths</title>
<meta name="description" content="Comprehensive study guide, key concepts, and exam revision notes for ${item.title} (${item.sectionName}). Preparation notes for UP TGT Social Science.">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
<meta name="author" content="SJ Maths">
<meta name="theme-color" content="#16324f">
<link rel="canonical" href="${canonicalUrl}">
<link rel="icon" type="image/png" href="/favicon.png">

<meta property="og:type" content="article">
<meta property="og:site_name" content="SJ Maths">
<meta property="og:title" content="${item.title} — Civics Study Guide">
<meta property="og:description" content="Study notes and revision checklist for ${item.title} in ${item.sectionName}.">
<meta property="og:url" content="${canonicalUrl}">
<meta property="og:image" content="https://sjmaths.com/assets/images/og-default.jpg">

<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="${item.title} — Civics Study Guide">
<meta name="twitter:description" content="Study notes and revision checklist for ${item.title} in ${item.sectionName}.">

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LearningResource",
  "name": "${item.title}",
  "headline": "${item.title} — Civics Study Guide",
  "description": "Study notes, syllabus alignment, and key concepts for ${item.title} (${item.sectionName}).",
  "url": "${canonicalUrl}",
  "isPartOf": {
    "@type": "WebSite",
    "name": "SJ Maths",
    "url": "https://sjmaths.com/"
  },
  "breadcrumb": {
    "@type": "BreadcrumbList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://sjmaths.com/"
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "Civics",
        "item": "https://sjmaths.com/up-tgt-social-science/"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "${item.sectionName}",
        "item": "${canonicalUrl}"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "${item.title}",
        "item": "${canonicalUrl}"
      }
    ]
  }
}
</script>

<style>
:root{--bg:#f6f8fb;--paper:#fff;--ink:#182238;--ink2:#4c576b;--muted:#7b8698;--line:#e1e7ef;--softline:#edf1f5;--brand:#16324f;--accent:#4338ca;--accent-soft:#4338ca12;--accent-border:#4338ca33;--shadow:0 16px 38px rgba(28,39,60,.07)}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:radial-gradient(circle at 100% 0,rgba(37,99,235,.05),transparent 28rem),radial-gradient(circle at 0 31rem,rgba(15,118,110,.045),transparent 26rem),var(--bg);color:var(--ink);font-family:Inter,ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;line-height:1.5;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
.wrap{width:min(1180px,calc(100% - 32px));margin:auto}
.site-header{height:66px;position:sticky;top:0;z-index:90;background:rgba(255,255,255,.96);backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
.header-inner{height:100%;display:flex;align-items:center;justify-content:space-between;gap:16px}
.brand{display:flex;gap:11px;align-items:center}
.brand-mark{width:39px;height:39px;border-radius:11px;background:linear-gradient(145deg,#16324f,#2563eb);display:grid;place-items:center;color:#fff;font-weight:900}
.brand-name{display:block;font-weight:850}
.brand-sub{display:block;color:var(--muted);font-size:.68rem}
.back-btn{display:inline-flex;align-items:center;gap:6px;font-size:.84rem;font-weight:700;color:var(--accent);padding:8px 14px;border-radius:10px;background:var(--accent-soft);border:1px solid var(--accent-border);transition:all .15s}
.back-btn:hover{background:var(--accent);color:#fff}

.hero{padding:32px 0 24px}
.breadcrumb{display:flex;gap:6px;align-items:center;flex-wrap:wrap;color:var(--muted);font-size:.78rem;margin-bottom:12px}
.breadcrumb a:hover{color:var(--accent)}
.kicker{display:inline-flex;gap:7px;align-items:center;color:var(--accent);font-size:.72rem;font-weight:800;text-transform:uppercase;letter-spacing:.08em;margin-bottom:6px}
.kicker:before{content:"";width:18px;height:2px;background:var(--accent);border-radius:99px}
h1{margin:0 0 10px;font-size:clamp(1.6rem,3.2vw,2.4rem);font-weight:900;letter-spacing:-.03em;color:#0e1726;line-height:1.15}
.lead{margin:0 0 16px;color:var(--ink2);font-size:.96rem;max-width:820px;line-height:1.6}
.exam-badges{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px}
.exam-chip{display:inline-flex;align-items:center;gap:6px;padding:6px 12px;border-radius:999px;background:#eef2ff;border:1px solid #c7d2fe;color:#3730a3;font-size:.76rem;font-weight:700}

.main-grid{display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:24px;padding-bottom:64px}
.card{background:#fff;border:1px solid var(--line);border-radius:18px;padding:24px;margin-bottom:18px;box-shadow:0 2px 10px rgba(25,40,55,.03)}
.card h2{margin:0 0 12px;font-size:1.25rem;letter-spacing:-.02em;color:#111c2e}
.card p{margin:0 0 14px;color:var(--ink2);line-height:1.65;font-size:.92rem}
.checklist{display:grid;gap:8px;margin-top:14px}
.check-item{display:flex;align-items:flex-start;gap:10px;padding:10px 12px;border:1px solid var(--softline);border-radius:10px;background:#fbfcfe;font-size:.85rem;color:var(--ink);cursor:pointer}
.check-item input{margin-top:3px;accent-color:var(--accent);cursor:pointer}

.sidebar-card{background:#fff;border:1px solid var(--line);border-radius:18px;padding:20px;position:sticky;top:86px}
.sidebar-card h3{margin:0 0 10px;font-size:.95rem;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}
.action-box{background:var(--accent-soft);border:1px solid var(--accent-border);border-radius:14px;padding:16px;margin-top:14px;text-align:center}
.action-box strong{display:block;font-size:.92rem;color:var(--accent)}
.action-box p{margin:6px 0 12px;font-size:.78rem;color:var(--ink2)}
.action-btn{display:inline-block;padding:9px 16px;background:var(--accent);color:#fff;font-size:.78rem;font-weight:800;border-radius:9px}

.footer{padding:30px 0;background:#fff;border-top:1px solid var(--line);color:var(--muted);font-size:.78rem;margin-top:40px}
.footer-inner{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
.footer a{color:#2563eb;font-weight:700}
@media(max-width:860px){.main-grid{grid-template-columns:1fr}.sidebar-card{position:static}}
</style>
</head>
<body>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="https://sjmaths.com/">
      <span class="brand-mark">&int;</span>
      <span>
        <span class="brand-name">SJ Maths</span>
        <span class="brand-sub">Master Subject Library</span>
      </span>
    </a>
    <a class="back-btn" href="/up-tgt-social-science/">← Back to UP TGT Social Science</a>
  </div>
</header>

<main class="wrap">
  <section class="hero">
    <nav class="breadcrumb" aria-label="Breadcrumb">${breadcrumbsHtml}
    </nav>
    <div class="kicker">${item.sectionName}</div>
    <h1>${item.title}</h1>
    <p class="lead">${item.summaryIntro}</p>

    <div class="exam-badges">
      <span style="font-size:.74rem;color:var(--muted);align-self:center">Appears in:</span>
      <a class="exam-chip" href="/up-tgt-social-science/">UP TGT Social Science Tracker →</a>
    </div>
  </section>

  <div class="main-grid">
    <div class="content-col">
      <article class="card">
        <h2>1. Syllabus Overview & Exam Focus</h2>
        <p>In the official teacher recruitment and competitive syllabus, <strong>${item.title}</strong> forms an essential core unit of <em>${item.sectionName}</em>. Questions routinely test foundational concepts, constitutional provisions, comparative institutional features, and critical theoretical perspectives.</p>
        <p>Study this consolidated module systematically to master both the conceptual foundations and typical examination question patterns.</p>
      </article>

      <article class="card">
        <h2>2. Key Concepts & Essential Principles</h2>
        <p>Master the following core concepts for <strong>${item.title}</strong>:</p>
        <div class="checklist">${checklistItems}
        </div>
      </article>

      <article class="card">
        <h2>3. Self-Assessment &amp; Study Checklist</h2>
        <p>Use this interactive checklist to verify your exam preparation status for this topic:</p>
        <div class="checklist">
          <label class="check-item"><input type="checkbox"> <span>Read theoretical notes &amp; conceptual summary</span></label>
          <label class="check-item"><input type="checkbox"> <span>Memorized essential definitions, articles &amp; principles</span></label>
          <label class="check-item"><input type="checkbox"> <span>Solved minimum 20 previous years' questions (PYQ)</span></label>
          <label class="check-item"><input type="checkbox"> <span>Attempted timed self-assessment test</span></label>
          <label class="check-item"><input type="checkbox"> <span>Marked complete on main syllabus tracker</span></label>
        </div>
      </article>
    </div>

    <aside class="sidebar-col">
      <div class="sidebar-card">
        <h3>Exam Tracker</h3>
        <p style="font-size:.84rem;color:var(--ink2);margin:0 0 12px">Track this topic alongside the complete syllabus on your exam progress tracker.</p>
        <div class="action-box">
          <strong>UP TGT Social Science</strong>
          <p>Interactive progress tracking, instant search &amp; filter</p>
          <a class="action-btn" href="/up-tgt-social-science/">Open Tracker →</a>
        </div>
      </div>
    </aside>
  </div>
</main>

<footer class="footer">
  <div class="wrap footer-inner">
    <span>SJ Maths • Master Subject Library • ${item.title}</span>
    <div>
      <a href="https://sjmaths.com/">Home</a> &nbsp;•&nbsp;
      <a href="/up-tgt-social-science/">UP TGT Social Science</a>
    </div>
  </div>
</footer>
</body>
</html>
`;
}

function generateRedirectHtml(targetUrl, title) {
  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Redirecting to ${title} | SJ Maths</title>
<link rel="canonical" href="${targetUrl}">
<meta http-equiv="refresh" content="0; url=${targetUrl}">
<meta name="robots" content="noindex,follow">
<script>location.replace('${targetUrl}');</script>
</head>
<body>
<p>This topic has been consolidated. Redirecting to <a href="${targetUrl}">${title}</a>...</p>
</body>
</html>
`;
}

// 1. Create consolidated pages and redirect pages
for (const item of consolidations) {
  const targetDirAbs = path.join(ROOT, item.targetDir);
  if (!fs.existsSync(targetDirAbs)) {
    fs.mkdirSync(targetDirAbs, { recursive: true });
  }

  const consolidatedHtml = generateConsolidatedHtml(item);
  const targetIndexFile = path.join(targetDirAbs, 'index.html');
  fs.writeFileSync(targetIndexFile, consolidatedHtml, 'utf8');
  console.log(`Created consolidated page: ${item.targetDir}/index.html`);

  const targetUrl = `https://sjmaths.com/${item.targetDir.replace(/\\/g, '/')}/`;

  // Create redirect at old dirs (if oldDir !== targetDir)
  for (const oldDir of item.oldDirs) {
    if (path.resolve(ROOT, oldDir) === targetDirAbs) {
      // Old dir is same as target dir, don't overwrite with redirect
      continue;
    }
    const oldDirAbs = path.join(ROOT, oldDir);
    if (!fs.existsSync(oldDirAbs)) {
      fs.mkdirSync(oldDirAbs, { recursive: true });
    }
    const redirectHtml = generateRedirectHtml(targetUrl, item.title);
    fs.writeFileSync(path.join(oldDirAbs, 'index.html'), redirectHtml, 'utf8');
    console.log(`  -> Redirected ${oldDir} to ${targetUrl}`);
  }
}

console.log('Finished generating consolidated Civics pages and redirects.');
