fpath = r'C:\Users\sande\Documents\GitHub\sjmaths-website\upsc-apfc\current-affairs\awards-sports-and-persons-in-news\index.html'
with open(fpath, 'r', encoding='utf-8') as f:
    c = f.read()

start_marker = '    function render() {\n      renderTabs();\n      renderStats();'
end_marker = '      movePill();\n    }\n\n    /* ---- quiz ---- */'

s = c.find(start_marker)
e = c.find(end_marker, s) + len('      movePill();\n    }')

new_render = '''    function render() {
      renderTabs();
      renderCatTabs();
      renderStats();
      const md = monthData();

      let html = "";

      if (activeCat === "quiz") {
        html += quizSectionHtml();
      } else {
        const items = filt(md[activeCat] || []);
        const cfg = catCfg[activeCat];
        if (items.length === 0) {
          html += '<div class="empty-state reveal in"><strong>No matches for \\u201c' + esc(search) + '\\u201d</strong> in ' + activeMonth + ' ' + catLabels[activeCat] + '.<br>Try another keyword or pick a different month.</div>';
        } else {
          html += '<section class="cat-card ' + cfg.cls + ' reveal">';
          html += '<header class="cat-head"><div class="cat-id"><span class="cat-icon" aria-hidden="true">' + cfg.icon + '</span>';
          html += '<div><h2 class="cat-title">' + cfg.label + '</h2><p class="cat-desc">' + cfg.desc + ' \\u00b7 ' + activeMonth + ' 2026</p></div></div>';
          html += '<span class="count-pill">' + items.length + ' ' + (items.length === 1 ? 'entry' : 'entries') + '</span></header>';
          html += '<ol class="item-list">';
          html += items.map((it, i) =>
            '<li class="item"><span class="idx">' + String(i + 1).padStart(2, '0') + '</span><div><p class="item-title">' + esc(it.who || it.event) + '</p><p class="item-desc">' + esc(it.what || it.desc || it.detail) + '</p></div></li>'
          ).join('');
          html += '</ol></section>';
        }
      }

      html += '<aside class="ui-callout success reveal"><strong>\\u{1F4CC} APFC Exam Focus \\u2014 </strong>prioritise <strong>National Sports Awards</strong> (Khel Ratna, Arjuna, Dronacharya), <strong>Padma Awards 2026</strong>, <strong>Gallantry Awards</strong> (Ashoka Chakra), <strong>Jnanpith / Sahitya Akademi / Grammy / Oscar winners</strong>, <strong>CWG 2026 India medal highlights</strong>, the <strong>FIFA World Cup 2026 winner</strong>, and <strong>first-time achievements</strong> by Indian athletes.</aside>';

      $wrap.innerHTML = html;
      observeReveals();
      animateLastAnswer();
      moveCatPill();
    }'''

c = c[:s] + new_render + c[e:]

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(c)
print('Render function replaced successfully')
print('New file length:', len(c))
