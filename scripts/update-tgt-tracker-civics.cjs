const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const trackerFile = path.join(ROOT, 'up-tgt-social-science/index.html');
let html = fs.readFileSync(trackerFile, 'utf8');

// The new consolidated list of topics per section (sections 32 to 43)
const newCivicsSections = [
  {
    id: 'civics-32-civics-and-the-state',
    title: 'Civics and the State',
    topics: [
      {
        key: 'civics/foundations/civics',
        title: 'Definition, Nature, Scope and Subject Matter of Civics',
        path: '/civics/foundations/civics/',
        search: 'civics civics and the state definition nature scope subject matter of civics /civics/foundations/civics/'
      },
      {
        key: 'civics/foundations/state',
        title: 'State: Definition, Essential Elements and Theories of Origin',
        path: '/civics/foundations/state/',
        search: 'civics civics and the state definition elements theories of origin of state /civics/foundations/state/'
      }
    ]
  },
  {
    id: 'civics-33-political-concepts',
    title: 'Political Concepts',
    topics: [
      {
        key: 'civics/political-concepts/sovereignty',
        title: 'Sovereignty',
        path: '/civics/political-concepts/sovereignty/',
        search: 'civics political concepts sovereignty /civics/political-concepts/sovereignty/'
      },
      {
        key: 'civics/political-concepts/law',
        title: 'Law',
        path: '/civics/political-concepts/law/',
        search: 'civics political concepts law /civics/political-concepts/law/'
      },
      {
        key: 'civics/political-concepts/punishment',
        title: 'Punishment',
        path: '/civics/political-concepts/punishment/',
        search: 'civics political concepts punishment /civics/political-concepts/punishment/'
      },
      {
        key: 'civics/political-concepts/rights-and-citizenship',
        title: 'Rights and Citizenship',
        path: '/civics/political-concepts/rights-and-citizenship/',
        search: 'civics political concepts rights and citizenship /civics/political-concepts/rights-and-citizenship/'
      },
      {
        key: 'civics/political-concepts/liberty',
        title: 'Liberty',
        path: '/civics/political-concepts/liberty/',
        search: 'civics political concepts liberty /civics/political-concepts/liberty/'
      },
      {
        key: 'civics/political-concepts/equality',
        title: 'Equality',
        path: '/civics/political-concepts/equality/',
        search: 'civics political concepts equality /civics/political-concepts/equality/'
      },
      {
        key: 'civics/forms-of-government/democracy',
        title: 'Democracy',
        path: '/civics/forms-of-government/democracy/',
        search: 'civics political concepts democracy /civics/forms-of-government/democracy/'
      },
      {
        key: 'civics/forms-of-government/dictatorship',
        title: 'Dictatorship',
        path: '/civics/forms-of-government/dictatorship/',
        search: 'civics political concepts dictatorship /civics/forms-of-government/dictatorship/'
      }
    ]
  },
  {
    id: 'civics-34-political-ideologies',
    title: 'Political Ideologies',
    topics: [
      {
        key: 'civics/political-ideologies/individualism',
        title: 'Individualism',
        path: '/civics/political-ideologies/individualism/',
        search: 'civics political ideologies individualism /civics/political-ideologies/individualism/'
      },
      {
        key: 'civics/political-ideologies/liberalism',
        title: 'Liberalism',
        path: '/civics/political-ideologies/liberalism/',
        search: 'civics political ideologies liberalism /civics/political-ideologies/liberalism/'
      },
      {
        key: 'civics/political-ideologies/fascism',
        title: 'Fascism',
        path: '/civics/political-ideologies/fascism/',
        search: 'civics political ideologies fascism /civics/political-ideologies/fascism/'
      },
      {
        key: 'civics/political-ideologies/scientific-socialism',
        title: 'Scientific Socialism',
        path: '/civics/political-ideologies/scientific-socialism/',
        search: 'civics political ideologies scientific socialism /civics/political-ideologies/scientific-socialism/'
      }
    ]
  },
  {
    id: 'civics-35-political-philosophers',
    title: 'Political Philosophers',
    topics: [
      {
        key: 'civics/political-philosophers/plato',
        title: 'Plato',
        path: '/civics/political-philosophers/plato/',
        search: 'civics political philosophers plato /civics/political-philosophers/plato/'
      },
      {
        key: 'civics/political-philosophers/aristotle',
        title: 'Aristotle',
        path: '/civics/political-philosophers/aristotle/',
        search: 'civics political philosophers aristotle /civics/political-philosophers/aristotle/'
      },
      {
        key: 'civics/political-philosophers/hobbes',
        title: 'Hobbes',
        path: '/civics/political-philosophers/hobbes/',
        search: 'civics political philosophers hobbes /civics/political-philosophers/hobbes/'
      },
      {
        key: 'civics/political-philosophers/locke',
        title: 'Locke',
        path: '/civics/political-philosophers/locke/',
        search: 'civics political philosophers locke /civics/political-philosophers/locke/'
      },
      {
        key: 'civics/political-philosophers/rousseau',
        title: 'Rousseau',
        path: '/civics/political-philosophers/rousseau/',
        search: 'civics political philosophers rousseau /civics/political-philosophers/rousseau/'
      },
      {
        key: 'civics/political-philosophers/bentham',
        title: 'Bentham',
        path: '/civics/political-philosophers/bentham/',
        search: 'civics political philosophers bentham /civics/political-philosophers/bentham/'
      },
      {
        key: 'civics/political-philosophers/js-mill',
        title: 'J. S. Mill',
        path: '/civics/political-philosophers/js-mill/',
        search: 'civics political philosophers j. s. mill /civics/political-philosophers/js-mill/'
      },
      {
        key: 'civics/political-philosophers/karl-marx',
        title: 'Karl Marx',
        path: '/civics/political-philosophers/karl-marx/',
        search: 'civics political philosophers karl marx /civics/political-philosophers/karl-marx/'
      },
      {
        key: 'civics/political-philosophers/manu',
        title: 'Manu',
        path: '/civics/political-philosophers/manu/',
        search: 'civics political philosophers manu /civics/political-philosophers/manu/'
      },
      {
        key: 'civics/political-philosophers/kautilya',
        title: 'Kautilya',
        path: '/civics/political-philosophers/kautilya/',
        search: 'civics political philosophers kautilya /civics/political-philosophers/kautilya/'
      },
      {
        key: 'civics/political-philosophers/gandhi',
        title: 'Gandhi',
        path: '/civics/political-philosophers/gandhi/',
        search: 'civics political philosophers gandhi /civics/political-philosophers/gandhi/'
      }
    ]
  },
  {
    id: 'civics-36-government-and-its-organs',
    title: 'Government and Its Organs',
    topics: [
      {
        key: 'civics/government/forms/parliamentary-and-presidential',
        title: 'Parliamentary and Presidential Government',
        path: '/civics/government/forms/parliamentary-and-presidential/',
        search: 'civics government and its organs parliamentary and presidential government /civics/government/forms/parliamentary-and-presidential/'
      },
      {
        key: 'civics/government/forms/unitary-and-federal',
        title: 'Unitary and Federal Government',
        path: '/civics/government/forms/unitary-and-federal/',
        search: 'civics government and its organs unitary and federal government /civics/government/forms/unitary-and-federal/'
      },
      {
        key: 'civics/government/organs',
        title: 'Organs of Government: Legislature, Executive and Judiciary',
        path: '/civics/government/organs/',
        search: 'civics government and its organs organs of government legislature executive judiciary /civics/government/organs/'
      }
    ]
  },
  {
    id: 'civics-37-elections-and-political-behaviour',
    title: 'Elections and Political Behaviour',
    topics: [
      {
        key: 'civics/elections/election-commission',
        title: 'Election Commission',
        path: '/civics/elections/election-commission/',
        search: 'civics elections and political behaviour election commission /civics/elections/election-commission/'
      },
      {
        key: 'civics/elections/reforms-and-voting-behaviour',
        title: 'Electoral Reforms and Voting Behaviour',
        path: '/civics/elections/reforms-and-voting-behaviour/',
        search: 'civics elections and political behaviour electoral reforms and voting behaviour /civics/elections/reforms-and-voting-behaviour/'
      }
    ]
  },
  {
    id: 'civics-38-indian-national-movement-contributions',
    title: 'Indian National Movement — Contributions',
    topics: [
      {
        key: 'civics/indian-national-movement/gopal-krishna-gokhale',
        title: 'Contribution of Gopal Krishna Gokhle',
        path: '/civics/indian-national-movement/gopal-krishna-gokhale/',
        search: 'civics indian national movement — contributions contribution of gopal krishna gokhle /civics/indian-national-movement/gopal-krishna-gokhale/'
      },
      {
        key: 'civics/indian-national-movement/bal-gangadhar-tilak',
        title: 'Contribution of Bal Gangadhar Tilak',
        path: '/civics/indian-national-movement/bal-gangadhar-tilak/',
        search: 'civics indian national movement — contributions contribution of bal gangadhar tilak /civics/indian-national-movement/bal-gangadhar-tilak/'
      },
      {
        key: 'civics/indian-national-movement/mohandas-karamchand-gandhi',
        title: 'Contribution of Mohandas Karamchand Gandhi',
        path: '/civics/indian-national-movement/mohandas-karamchand-gandhi/',
        search: 'civics indian national movement — contributions contribution of mohandas karamchand gandhi /civics/indian-national-movement/mohandas-karamchand-gandhi/'
      },
      {
        key: 'civics/indian-national-movement/jawaharlal-nehru',
        title: 'Contribution of Jawaharlal Nehru',
        path: '/civics/indian-national-movement/jawaharlal-nehru/',
        search: 'civics indian national movement — contributions contribution of jawaharlal nehru /civics/indian-national-movement/jawaharlal-nehru/'
      },
      {
        key: 'civics/indian-national-movement/subhash-chandra-bose',
        title: 'Contribution of Subhash Chandra Bose',
        path: '/civics/indian-national-movement/subhash-chandra-bose/',
        search: 'civics indian national movement — contributions contribution of subhash chandra bose /civics/indian-national-movement/subhash-chandra-bose/'
      },
      {
        key: 'civics/indian-national-movement/mohammad-ali-jinnah',
        title: 'Contribution of Mohammad Ali Jinnah',
        path: '/civics/indian-national-movement/mohammad-ali-jinnah/',
        search: 'civics indian national movement — contributions contribution of mohammad ali jinnah /civics/indian-national-movement/mohammad-ali-jinnah/'
      },
      {
        key: 'civics/indian-national-movement/br-ambedkar',
        title: 'Contribution of Dr. Babasaheb Bhimrao Ramji Ambedkar',
        path: '/civics/indian-national-movement/br-ambedkar/',
        search: 'civics indian national movement — contributions contribution of dr. babasaheb bhimrao ramji ambedkar /civics/indian-national-movement/br-ambedkar/'
      }
    ]
  },
  {
    id: 'civics-39-indian-constitution',
    title: 'Indian Constitution',
    topics: [
      {
        key: 'civics/indian-constitution/salient-features',
        title: 'Salient Features of Indian Constitution',
        path: '/civics/indian-constitution/salient-features/',
        search: 'civics indian constitution salient features of indian constitution /civics/indian-constitution/salient-features/'
      },
      {
        key: 'civics/indian-constitution/fundamental-rights',
        title: 'Fundamental Rights',
        path: '/civics/indian-constitution/fundamental-rights/',
        search: 'civics indian constitution fundamental rights /civics/indian-constitution/fundamental-rights/'
      },
      {
        key: 'civics/indian-constitution/directive-principles-of-state-policy',
        title: 'Directive Principles of State Policy',
        path: '/civics/indian-constitution/directive-principles-of-state-policy/',
        search: 'civics indian constitution directive principles of state policy /civics/indian-constitution/directive-principles-of-state-policy/'
      }
    ]
  },
  {
    id: 'civics-40-union-government',
    title: 'Union Government',
    topics: [
      {
        key: 'civics/union-government/executive/president',
        title: 'President of India',
        path: '/civics/union-government/executive/president/',
        search: 'civics union government president of india /civics/union-government/executive/president/'
      },
      {
        key: 'civics/union-government/executive/prime-minister-and-council-of-ministers',
        title: 'Prime Minister and Union Council of Ministers',
        path: '/civics/union-government/executive/prime-minister-and-council-of-ministers/',
        search: 'civics union government prime minister and union council of ministers /civics/union-government/executive/prime-minister-and-council-of-ministers/'
      },
      {
        key: 'civics/union-government/parliament',
        title: 'Union Parliament: Lok Sabha and Rajya Sabha',
        path: '/civics/union-government/parliament/',
        search: 'civics union government union parliament lok sabha and rajya sabha /civics/union-government/parliament/'
      },
      {
        key: 'civics/judiciary',
        title: 'Indian Judiciary: Supreme Court and High Courts',
        path: '/civics/judiciary/',
        search: 'civics union government indian judiciary supreme court and high courts /civics/judiciary/'
      }
    ]
  },
  {
    id: 'civics-41-state-and-district-government',
    title: 'State and District Government',
    topics: [
      {
        key: 'civics/state-government',
        title: 'State Executive: Governor and Chief Minister',
        path: '/civics/state-government/',
        search: 'civics state and district government governor and chief minister /civics/state-government/'
      },
      {
        key: 'civics/district-administration/district-magistrate',
        title: 'District Magistrate',
        path: '/civics/district-administration/district-magistrate/',
        search: 'civics state and district government district magistrate /civics/district-administration/district-magistrate/'
      }
    ]
  },
  {
    id: 'civics-42-democracy-and-decentralization',
    title: 'Democracy and Decentralization',
    topics: [
      {
        key: 'civics/democracy-and-decentralization/panchayati-raj-and-local-governance',
        title: 'Democratic Decentralization and Panchayati Raj',
        path: '/civics/democracy-and-decentralization/panchayati-raj-and-local-governance/',
        search: 'civics democracy and decentralization democratic decentralization and panchayati raj /civics/democracy-and-decentralization/panchayati-raj-and-local-governance/'
      },
      {
        key: 'civics/challenges-of-indian-democracy',
        title: 'Challenges of Indian Democracy: Casteism, Communalism and Regionalism',
        path: '/civics/challenges-of-indian-democracy/',
        search: 'civics democracy and decentralization challenges of indian democracy casteism communalism regionalism /civics/challenges-of-indian-democracy/'
      }
    ]
  },
  {
    id: 'civics-43-political-organization-and-indian-administration',
    title: 'Political Organization and Indian Administration',
    topics: [
      {
        key: 'civics/political-organization',
        title: 'Political Parties and Pressure Groups',
        path: '/civics/political-organization/',
        search: 'civics political organization and indian administration political parties and pressure groups /civics/political-organization/'
      },
      {
        key: 'civics/indian-administration/bureaucracy',
        title: 'Bureaucracy',
        path: '/civics/indian-administration/bureaucracy/',
        search: 'civics political organization and indian administration bureaucracy /civics/indian-administration/bureaucracy/'
      },
      {
        key: 'civics/indian-administration/lokpal-and-lokayukta',
        title: 'Ombudsman, Lokpal and Lokayukta',
        path: '/civics/indian-administration/lokpal-and-lokayukta/',
        search: 'civics political organization and indian administration ombudsman lokpal and lokayukta /civics/indian-administration/lokpal-and-lokayukta/'
      }
    ]
  }
];

// Helper to build section card HTML
function renderSectionCard(sec, idx) {
  const count = sec.topics.length;
  const numStr = String(idx).padStart(2, '0');

  const topicsHtml = sec.topics.map(t => {
    return `<div class="topic" data-key="${t.key}" data-subject="D" data-search="${t.search}">
<label class="check"><input class="topic-check" type="checkbox" aria-label="Mark ${t.title} complete"></label>
<div class="topic-copy">
<a class="topic-link" href="${t.path}">${t.title}</a>
<div class="topic-tags"><span class="subject-tag" style="--tag:#be123c;--tagsoft:#fff1f2">Civics</span><span class="library-tag">/civics/</span></div>
<span class="topic-path">${t.path}</span>
</div>
<a class="open-topic" href="${t.path}" aria-label="Open ${t.title}">→</a>
</div>`;
  }).join('');

  return `<article class="section-card" id="${sec.id}" data-subject="D" style="--accent:#be123c;--soft:#fff1f2">
<button class="section-head" type="button" aria-expanded="false">
<span class="section-index">${numStr}</span>
<span><span class="unit-label">D. Civics</span><span class="section-title">${sec.title}</span><span class="section-meta">${count} tracked topics</span></span>
<span class="mini-progress"><span class="mini-track"><span data-bar="${sec.id}"></span></span><small><span data-done="${sec.id}">0</span> / ${count}</small></span>
<span class="chev">⌄</span>
</button>
<div class="section-body"><div class="topic-grid">${topicsHtml}</div></div>
</article>`;
}

// Compute total civics topics
const totalCivicsTopics = newCivicsSections.reduce((sum, s) => sum + s.topics.length, 0);
console.log(`Total consolidated Civics topics: ${totalCivicsTopics}`);

// 179 Geography + 79 History + 117 Economics + totalCivicsTopics
const totalAllTopics = 179 + 79 + 117 + totalCivicsTopics;
console.log(`New overall total topics: ${totalAllTopics}`);

// Build complete civics sections HTML block
const allCivicsCardsHtml = newCivicsSections.map((sec, i) => renderSectionCard(sec, 32 + i)).join('');

// Replace existing civics cards in up-tgt-social-science/index.html
const startMarker = '<article class="section-card" id="civics-32-civics-and-the-state"';
const endMarker = '</article></div><div id="empty" class="empty">';

const startIdx = html.indexOf(startMarker);
const endIdx = html.indexOf(endMarker);

if (startIdx === -1 || endIdx === -1) {
  console.error('Could not find civics cards boundaries in up-tgt-social-science/index.html');
  process.exit(1);
}

// Replace the middle civics cards
html = html.substring(0, startIdx) + allCivicsCardsHtml + html.substring(endIdx + '</article>'.length);

// Update counts in hero, progress card, and summary strip
// 447 -> totalAllTopics
html = html.replace(/447 tracked topics/g, `${totalAllTopics} tracked topics`);
html = html.replace(/topics complete<\/span><\/div><div class="progress-track"><span id="overallBar"><\/span><\/div><div class="progress-stats"><div class="pstat"><strong id="statDone">0<\/strong><span>Completed<\/span><\/div><div class="pstat"><strong id="statPending">447<\/strong>/g, `topics complete</span></div><div class="progress-track"><span id="overallBar"></span></div><div class="progress-stats"><div class="pstat"><strong id="statDone">0</strong><span>Completed</span></div><div class="pstat"><strong id="statPending">${totalAllTopics}</strong>`);
html = html.replace(/<span id="doneCount">0<\/span> \/ 447/g, `<span id="doneCount">0</span> / ${totalAllTopics}`);
html = html.replace(/<div class="metric"><strong>72<\/strong><span>Civics topics<\/span><\/div>/g, `<div class="metric"><strong>${totalCivicsTopics}</strong><span>Civics topics</span></div>`);

fs.writeFileSync(trackerFile, html, 'utf8');
console.log('Successfully updated up-tgt-social-science/index.html');
