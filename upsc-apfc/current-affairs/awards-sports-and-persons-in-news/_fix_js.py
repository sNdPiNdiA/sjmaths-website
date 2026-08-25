fpath = r'C:\Users\sande\Documents\GitHub\sjmaths-website\upsc-apfc\current-affairs\awards-sports-and-persons-in-news\index.html'
with open(fpath, 'r', encoding='utf-8') as f:
    c = f.read()

# --- 1. Replace the render function ---
# The current render function (after my earlier edits)
old_render = '''    function render() {
      renderTabs();
      renderStats();
      const md = monthData();
      let any = false, idx = 0;

      let html = "";
      for (const [k, c] of Object.entries(catCfg)) {
        const items = filt(md[k] || []);
        if (!items.length) continue;
        any = true;
        html += `<section class=\"cat-card ${c.cls} reveal\">
          <header class=\"cat-head\">
            <div class=\"cat-id\"><span class=\"cat-icon\" aria-hidden=\"true\">${c.icon}</span>
              <div><h2 class=\"cat-title\">${c.label}</h2><p class=\"cat-desc\">${c.desc} · ${activeMonth} 2026</p></div>
            </div>
            <span class=\"count-pill\">${items.length} ${items.length === 1 ? "entry" : "entries"}</span>
          </header>
          <ol class=\"item-list\">` +
          items.map((it, i) =>
            `<li class=\"item\"><span class=\"idx\">${String(i + 1).padStart(2, "0")}</span><div>
              <p class=\"item-title\">${esc(it.who || it.event)}</p>
              <p class=\"item-desc\">${esc(it.what || it.detail)}</p>
            </div></li>`).join(\"\") +
          `</ol></section>`;
      }

      if (!any) html += `<div class=\"empty-state reveal in\"><strong>No matches for \\u201C${esc(search)}\\u201D</strong> in ${activeMonth}.<br>Try another keyword or pick a different month.</div>`;

      html += `<aside class=\"ui-callout success reveal\"><strong>\\u{1F4CC} APFC Exam Focus — </strong>prioritise <strong>National Sports Awards</strong> (Khel Ratna, Arjuna, Dronacharya), <strong>Padma Awards 2026</strong>, <strong>Gallantry Awards</strong> (Ashoka Chakra), <strong>Jnanpith / Sahitya Akademi / Grammy / Oscar winners</strong>, <strong>CWG 2026 India medal highlights</strong>, the <strong>FIFA World Cup 2026 winner</strong>, and <strong>first-time achievements</strong> by Indian athletes.</aside>`;

      html += quizSectionHtml();
      $wrap.innerHTML = html;
      observeReveals();
      animateLastAnswer();
      movePill();
    }'''

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
          html += `<div class="empty-state reveal in"><strong>No matches for \\u201C${esc(search)}\\u201D</strong> in ${activeMonth} ${catLabels[activeCat]}.<br>Try another keyword or pick a different month.</div>`;
        } else {
          html += `<section class="cat-card ${cfg.cls} reveal">
            <header class="cat-head">
              <div class="cat-id"><span class="cat-icon" aria-hidden="true">${cfg.icon}</span>
                <div><h2 class="cat-title">${cfg.label}</h2><p class="cat-desc">${cfg.desc} · ${activeMonth} 2026</p></div>
              </div>
              <span class="count-pill">${items.length} ${items.length === 1 ? "entry" : "entries"}</span>
            </header>
            <ol class="item-list">` +
            items.map((it, i) =>
              `<li class="item"><span class="idx">${String(i + 1).padStart(2, "0")}</span><div>
                <p class="item-title">${esc(it.who || it.event)}</p>
                <p class="item-desc">${esc(it.what || it.detail)}</p>
              </div></li>`).join("") +
            `</ol></section>`;
        }
      }

      html += `<aside class="ui-callout success reveal"><strong>\\u{1F4CC} APFC Exam Focus — </strong>prioritise <strong>National Sports Awards</strong> (Khel Ratna, Arjuna, Dronacharya), <strong>Padma Awards 2026</strong>, <strong>Gallantry Awards</strong> (Ashoka Chakra), <strong>Jnanpith / Sahitya Akademi / Grammy / Oscar winners</strong>, <strong>CWG 2026 India medal highlights</strong>, the <strong>FIFA World Cup 2026 winner</strong>, and <strong>first-time achievements</strong> by Indian athletes.</aside>`;

      $wrap.innerHTML = html;
      observeReveals();
      animateLastAnswer();
      moveCatPill();
    }'''

if old_render in c:
    c = c.replace(old_render, new_render, 1)
    print('1. Render function replaced')
else:
    print('1. ERROR: render function not found (already replaced?)')
    # Check if render function still exists with different content
    idx = c.find('function render()')
    if idx >= 0:
        print('   render() found at index', idx)
        print('   snippet:', c[idx:idx+100])

# --- 2. Add category tab click handler ---
events_marker = '    /* ---- events ---- */\n    $tabs.addEventListener'
cat_click = '''    /* ---- category tab click ---- */
    $catTabs.addEventListener("click", e => {
      const btn = e.target.closest(".cat-tab");
      if (!btn || btn.classList.contains("active")) return;
      activeCat = btn.dataset.cat;
      render();
      moveCatPill();
    });

    /* ---- events ---- */
    $tabs.addEventListener'''

if events_marker in c:
    c = c.replace(events_marker, cat_click, 1)
    print('2. Category tab click handler added')
else:
    print('2. ERROR: events marker not found')

# --- 3. Add activeCat reset when month changes ---
month_reset_old = 'activeMonth = btn.dataset.month;\n      search = "";\n      $search.value = "";'
month_reset_new = 'activeMonth = btn.dataset.month;\n      activeCat = "awards";\n      search = "";\n      $search.value = "";'
if month_reset_old in c:
    c = c.replace(month_reset_old, month_reset_new, 1)
    print('3. Month reset (activeCat = awards) added')
else:
    print('3. ERROR: month reset marker not found')

# --- 4. Update resize listener ---
resize_old = 'addEventListener("resize", movePill, { passive:true });\n    addEventListener("load", () => setTimeout(movePill, 60));'
resize_new = 'addEventListener("resize", () => { movePill(); moveCatPill(); }, { passive:true });\n    addEventListener("load", () => { setTimeout(movePill, 60); setTimeout(moveCatPill, 60); });'
if resize_old in c:
    c = c.replace(resize_old, resize_new, 1)
    print('4. Resize listener updated')
else:
    print('4. ERROR: resize marker not found')

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(c)
print('All JS fixes applied. File length:', len(c))
