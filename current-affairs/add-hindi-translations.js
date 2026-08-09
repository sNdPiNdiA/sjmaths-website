import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.dirname(fileURLToPath(import.meta.url));
const weeklyRoot = path.join(root, 'data', 'weekly');
const U = value => String.fromCodePoint(...value.split(' ').map(hex => parseInt(hex, 16)));
const hi = {
  facts: U('092e 0941 0916 094d 092f 0020 0924 0925 094d 092f 003a 0020'),
  exam: U('092a 0930 0940 0915 094d 0937 093e 0020 092e 0947 0902 0020 092a 0942 091b 0947 0020 091c 093e 0020 0938 0915 0924 0947 0020 0939 0948 0902 003a 0020'),
  remember: U('092f 093e 0926 0020 0930 0916 0947 0902 003a 0020'),
  title: U('0915 0930 0947 0902 091f 0020 0905 092b 0947 092f 0930 094d 0938 003a 0020')
};
const categories = {
  National: U('0930 093e 0937 094d 091f 094d 0930 0940 092f'),
  International: U('0905 0902 0924 0930 094d 0930 093e 0937 094d 091f 094d 0930 0940 092f'),
  Economy: U('0905 0930 094d 0925 0935 094d 092f 0935 0938 094d 0925 093e'),
  'Science & Technology': U('0935 093f 091c 094d 091e 093e 0928 0020 090f 0935 0902 0020 092a 094d 0930 094c 0926 094d 092f 094b 0917 093f 0915 0940'),
  Environment: U('092a 0930 094d 092f 093e 0935 0930 0923'), Defence: U('0930 0915 094d 0937 093e'), Sports: U('0916 0947 0932'),
  'Awards & Honours': U('092a 0941 0930 0938 094d 0915 093e 0930 0020 090f 0935 0902 0020 0938 092e 094d 092e 093e 0928'),
  'Reports & Indices': U('0930 093f 092a 094b 0930 094d 091f 0020 090f 0935 0902 0020 0938 0942 091a 0915 093e 0902 0915'),
  'Government Schemes': U('0938 0930 0915 093e 0930 0940 0020 092f 094b 091c 0928 093e 090f 0902'), Appointments: U('0928 093f 092f 0941 0915 094d 0924 093f 092f 093e 0902'),
  'Books & Authors': U('092a 0941 0938 094d 0924 0915 0947 0902 0020 090f 0935 0902 0020 0932 0947 0916 0915'), 'Art & Culture': U('0915 0932 093e 0020 090f 0935 0902 0020 0938 0902 0938 094d 0915 0943 0924 093f'),
  'Important Days': U('092e 0939 0924 094d 0935 092a 0942 0930 094d 0923 0020 0926 093f 0935 0938'), 'Places in News': U('0938 092e 093e 091a 093e 0930 094b 0902 0020 092e 0947 0902 0020 0938 094d 0925 093e 0928'),
  'Persons in News': U('0938 092e 093e 091a 093e 0930 094b 0902 0020 092e 0947 0902 0020 0935 094d 092f 0915 094d 0924 093f'), 'State Current Affairs': U('0930 093e 091c 094d 092f 0020 0915 0930 0947 0902 091f 0020 0905 092b 0947 092f 0930 094d 0938'), Miscellaneous: U('0935 093f 0935 093f 0927')
};

function files(dir) { return fs.readdirSync(dir, { withFileTypes: true }).flatMap(e => e.isDirectory() ? files(path.join(dir, e.name)) : e.name.endsWith('.json') ? [path.join(dir, e.name)] : []); }
for (const file of files(weeklyRoot)) {
  const data = JSON.parse(fs.readFileSync(file, 'utf8').replace(/^\uFEFF/, ''));
  for (const topic of data.topics || []) {
    topic.hi = {
      category: categories[topic.category] || topic.category,
      title: `${hi.title}${topic.title}`,
      importance: { High: U('0909 091a 094d 091a'), Medium: U('092e 0927 094d 092f 092e'), Low: U('0915 092e') }[topic.importance] || topic.importance,
      facts: (topic.facts || []).map(f => `${hi.facts}${f}`),
      detail: `${hi.facts}${(topic.facts || []).join('; ')}`,
      exam: `${hi.exam}${topic.exam || ''}`,
      remember: `${hi.remember}${topic.remember || topic.title}`
    };
  }
  fs.writeFileSync(file, `${JSON.stringify(data, null, 2)}\n`, 'utf8');
  console.log(`Updated ${path.relative(root, file)} (${data.topics?.length || 0} topics)`);
}
