/* Chapter resource menus for the Class 11 Maths hub. */
(function () {
  'use strict';

  const resources = {"ncert":{"chapter-1-sets":["/class-11-maths/ncert-exercise-practice/chapter-1-sets/exercise-1-1.html","/class-11-maths/ncert-exercise-practice/chapter-1-sets/exercise-1-2.html","/class-11-maths/ncert-exercise-practice/chapter-1-sets/exercise-1-3.html","/class-11-maths/ncert-exercise-practice/chapter-1-sets/exercise-1-4.html","/class-11-maths/ncert-exercise-practice/chapter-1-sets/exercise-1-5.html","/class-11-maths/ncert-exercise-practice/chapter-1-sets/misc-exercise.html"],"chapter-2-relations-and-functions":["/class-11-maths/ncert-exercise-practice/chapter-2-relations-and-functions/exercise-2-1.html","/class-11-maths/ncert-exercise-practice/chapter-2-relations-and-functions/exercise-2-2.html","/class-11-maths/ncert-exercise-practice/chapter-2-relations-and-functions/exercise-2-3.html","/class-11-maths/ncert-exercise-practice/chapter-2-relations-and-functions/misc-exercise.html"],"chapter-3-trigonometric-functions":["/class-11-maths/ncert-exercise-practice/chapter-3-trigonometric-functions/exercise-3-1.html","/class-11-maths/ncert-exercise-practice/chapter-3-trigonometric-functions/exercise-3-2.html","/class-11-maths/ncert-exercise-practice/chapter-3-trigonometric-functions/exercise-3-3.html","/class-11-maths/ncert-exercise-practice/chapter-3-trigonometric-functions/misc-exercise.html"],"chapter-4-complex-numbers-and-quadratic-equations":["/class-11-maths/ncert-exercise-practice/chapter-4-complex-numbers-and-quadratic-equations/exercise-4-1.html","/class-11-maths/ncert-exercise-practice/chapter-4-complex-numbers-and-quadratic-equations/exercise-4-2.html"],"chapter-5-linear-inequalities":["/class-11-maths/ncert-exercise-practice/chapter-5-linear-inequalities/exercise-5-1.html","/class-11-maths/ncert-exercise-practice/chapter-5-linear-inequalities/miscellaneous-exercise.html"],"chapter-6-permutations-and-combinations":["/class-11-maths/ncert-exercise-practice/chapter-6-permutations-and-combinations/exercise-6-1.html","/class-11-maths/ncert-exercise-practice/chapter-6-permutations-and-combinations/exercise-6-2.html","/class-11-maths/ncert-exercise-practice/chapter-6-permutations-and-combinations/exercise-6-3.html","/class-11-maths/ncert-exercise-practice/chapter-6-permutations-and-combinations/exercise-6-4.html","/class-11-maths/ncert-exercise-practice/chapter-6-permutations-and-combinations/miscellaneous-exercise.html"],"chapter-7-binomial-theorem":["/class-11-maths/ncert-exercise-practice/chapter-7-binomial-theorem/exercise-7-1.html","/class-11-maths/ncert-exercise-practice/chapter-7-binomial-theorem/miscellaneous-exercise.html"],"chapter-8-sequences-and-series":["/class-11-maths/ncert-exercise-practice/chapter-8-sequences-and-series/exercise-8-1.html","/class-11-maths/ncert-exercise-practice/chapter-8-sequences-and-series/exercise-8-2.html","/class-11-maths/ncert-exercise-practice/chapter-8-sequences-and-series/miscellaneous-exercise.html"],"chapter-9-straight-lines":["/class-11-maths/ncert-exercise-practice/chapter-9-straight-lines/exercise-9-1.html","/class-11-maths/ncert-exercise-practice/chapter-9-straight-lines/exercise-9-2.html","/class-11-maths/ncert-exercise-practice/chapter-9-straight-lines/exercise-9-3.html","/class-11-maths/ncert-exercise-practice/chapter-9-straight-lines/miscellaneous-exercise.html"],"chapter-10-conic-sections":["/class-11-maths/ncert-exercise-practice/chapter-10-conic-sections/exercise-10-1.html","/class-11-maths/ncert-exercise-practice/chapter-10-conic-sections/exercise-10-2.html","/class-11-maths/ncert-exercise-practice/chapter-10-conic-sections/exercise-10-3.html","/class-11-maths/ncert-exercise-practice/chapter-10-conic-sections/exercise-10-4.html","/class-11-maths/ncert-exercise-practice/chapter-10-conic-sections/miscellaneous-exercise.html"],"chapter-11-introduction-to-three-dimensional-geometry":["/class-11-maths/ncert-exercise-practice/chapter-11-introduction-to-three-dimensional-geometry/exercise-11-1.html","/class-11-maths/ncert-exercise-practice/chapter-11-introduction-to-three-dimensional-geometry/exercise-11-2.html","/class-11-maths/ncert-exercise-practice/chapter-11-introduction-to-three-dimensional-geometry/miscellaneous-exercise.html"],"chapter-12-limits-and-derivatives":["/class-11-maths/ncert-exercise-practice/chapter-12-limits-and-derivatives/exercise-12-1.html","/class-11-maths/ncert-exercise-practice/chapter-12-limits-and-derivatives/exercise-12-2.html"],"chapter-13-statistics":["/class-11-maths/ncert-exercise-practice/chapter-13-statistics/exercise-13-1.html","/class-11-maths/ncert-exercise-practice/chapter-13-statistics/exercise-13-2.html"],"chapter-14-probability":["/class-11-maths/ncert-exercise-practice/chapter-14-probability/exercise-14-1.html","/class-11-maths/ncert-exercise-practice/chapter-14-probability/exercise-14-2.html"]},"worksheet":{"chapter-1-sets":["/class-11-maths/worksheets/chapter-1-sets/basic.html","/class-11-maths/worksheets/chapter-1-sets/hots.html","/class-11-maths/worksheets/chapter-1-sets/standard.html"],"chapter-2-relations-and-functions":["/class-11-maths/worksheets/chapter-2-relations-and-functions/basic.html","/class-11-maths/worksheets/chapter-2-relations-and-functions/hots.html","/class-11-maths/worksheets/chapter-2-relations-and-functions/standard.html"],"chapter-3-trigonometric-functions":["/class-11-maths/worksheets/chapter-3-trigonometric-functions/basic.html","/class-11-maths/worksheets/chapter-3-trigonometric-functions/hots.html","/class-11-maths/worksheets/chapter-3-trigonometric-functions/standard.html"],"chapter-4-complex-numbers-and-quadratic-equations":["/class-11-maths/worksheets/chapter-4-complex-numbers-and-quadratic-equations/basic.html","/class-11-maths/worksheets/chapter-4-complex-numbers-and-quadratic-equations/hots.html","/class-11-maths/worksheets/chapter-4-complex-numbers-and-quadratic-equations/standard.html"],"chapter-5-linear-inequalities":["/class-11-maths/worksheets/chapter-5-linear-inequalities/basic.html","/class-11-maths/worksheets/chapter-5-linear-inequalities/hots.html","/class-11-maths/worksheets/chapter-5-linear-inequalities/standard.html"],"chapter-6-permutations-and-combinations":["/class-11-maths/worksheets/chapter-6-permutations-and-combinations/basic.html","/class-11-maths/worksheets/chapter-6-permutations-and-combinations/hots.html","/class-11-maths/worksheets/chapter-6-permutations-and-combinations/standard.html"],"chapter-7-binomial-theorem":["/class-11-maths/worksheets/chapter-7-binomial-theorem/basic.html","/class-11-maths/worksheets/chapter-7-binomial-theorem/hots.html","/class-11-maths/worksheets/chapter-7-binomial-theorem/standard.html"],"chapter-8-sequences-and-series":["/class-11-maths/worksheets/chapter-8-sequences-and-series/basic.html","/class-11-maths/worksheets/chapter-8-sequences-and-series/hots.html","/class-11-maths/worksheets/chapter-8-sequences-and-series/standard.html"],"chapter-9-straight-lines":["/class-11-maths/worksheets/chapter-9-straight-lines/basic.html","/class-11-maths/worksheets/chapter-9-straight-lines/hots.html","/class-11-maths/worksheets/chapter-9-straight-lines/standard.html"],"chapter-10-conic-sections":["/class-11-maths/worksheets/chapter-10-conic-sections/basic.html","/class-11-maths/worksheets/chapter-10-conic-sections/hots.html","/class-11-maths/worksheets/chapter-10-conic-sections/standard.html"],"chapter-11-introduction-to-three-dimensional-geometry":["/class-11-maths/worksheets/chapter-11-introduction-to-three-dimensional-geometry/basic.html","/class-11-maths/worksheets/chapter-11-introduction-to-three-dimensional-geometry/hots.html","/class-11-maths/worksheets/chapter-11-introduction-to-three-dimensional-geometry/standard.html"],"chapter-12-limits-and-derivatives":["/class-11-maths/worksheets/chapter-12-limits-and-derivatives/basic.html","/class-11-maths/worksheets/chapter-12-limits-and-derivatives/hots.html","/class-11-maths/worksheets/chapter-12-limits-and-derivatives/standard.html"],"chapter-13-statistics":["/class-11-maths/worksheets/chapter-13-statistics/basic.html","/class-11-maths/worksheets/chapter-13-statistics/hots.html","/class-11-maths/worksheets/chapter-13-statistics/standard.html"],"chapter-14-probability":["/class-11-maths/worksheets/chapter-14-probability/basic.html","/class-11-maths/worksheets/chapter-14-probability/hots.html","/class-11-maths/worksheets/chapter-14-probability/standard.html"]},"exemplar":{"chapter-1-sets":["/class-11-maths/ncert-exemplar-practice/chapter-1-sets/exemplar-1-1.html","/class-11-maths/ncert-exemplar-practice/chapter-1-sets/exemplar-1-2.html","/class-11-maths/ncert-exemplar-practice/chapter-1-sets/exemplar-1-3.html"],"chapter-2-relations-and-functions":["/class-11-maths/ncert-exemplar-practice/chapter-2-relations-and-functions/exemplar-2-1.html","/class-11-maths/ncert-exemplar-practice/chapter-2-relations-and-functions/exemplar-2-2.html","/class-11-maths/ncert-exemplar-practice/chapter-2-relations-and-functions/exemplar-2-3.html"],"chapter-3-trigonometric-functions":["/class-11-maths/ncert-exemplar-practice/chapter-3-trigonometric-functions/exemplar-3-1.html","/class-11-maths/ncert-exemplar-practice/chapter-3-trigonometric-functions/exemplar-3-2.html","/class-11-maths/ncert-exemplar-practice/chapter-3-trigonometric-functions/exemplar-3-3.html"],"chapter-4-complex-numbers-and-quadratic-equations":["/class-11-maths/ncert-exemplar-practice/chapter-4-complex-numbers/exemplar-4-1.html","/class-11-maths/ncert-exemplar-practice/chapter-4-complex-numbers/exemplar-4-2.html","/class-11-maths/ncert-exemplar-practice/chapter-4-complex-numbers/exemplar-4-3.html"],"chapter-5-linear-inequalities":["/class-11-maths/ncert-exemplar-practice/chapter-5-linear-inequalities/exemplar-5-1.html","/class-11-maths/ncert-exemplar-practice/chapter-5-linear-inequalities/exemplar-5-2.html","/class-11-maths/ncert-exemplar-practice/chapter-5-linear-inequalities/exemplar-5-3.html"],"chapter-6-permutations-and-combinations":["/class-11-maths/ncert-exemplar-practice/chapter-6-permutations/exemplar-6-1.html","/class-11-maths/ncert-exemplar-practice/chapter-6-permutations/exemplar-6-2.html","/class-11-maths/ncert-exemplar-practice/chapter-6-permutations/exemplar-6-3.html"],"chapter-7-binomial-theorem":["/class-11-maths/ncert-exemplar-practice/chapter-7-binomial-theorem/exemplar-7-1.html","/class-11-maths/ncert-exemplar-practice/chapter-7-binomial-theorem/exemplar-7-2.html","/class-11-maths/ncert-exemplar-practice/chapter-7-binomial-theorem/exemplar-7-3.html"],"chapter-8-sequences-and-series":["/class-11-maths/ncert-exemplar-practice/chapter-8-sequences-and-series/exemplar-8-1.html","/class-11-maths/ncert-exemplar-practice/chapter-8-sequences-and-series/exemplar-8-2.html","/class-11-maths/ncert-exemplar-practice/chapter-8-sequences-and-series/exemplar-8-3.html"],"chapter-9-straight-lines":["/class-11-maths/ncert-exemplar-practice/chapter-8-sequences-and-series/exemplar-9-1.html","/class-11-maths/ncert-exemplar-practice/chapter-8-sequences-and-series/exemplar-9-2.html","/class-11-maths/ncert-exemplar-practice/chapter-8-sequences-and-series/exemplar-9-3.html"],"chapter-10-conic-sections":["/class-11-maths/ncert-exemplar-practice/chapter-10-conic-sections/exemplar-10-1.html","/class-11-maths/ncert-exemplar-practice/chapter-10-conic-sections/exemplar-10-2.html","/class-11-maths/ncert-exemplar-practice/chapter-10-conic-sections/exemplar-10-3.html"],"chapter-11-introduction-to-three-dimensional-geometry":["/class-11-maths/ncert-exemplar-practice/chapter-11-3d-geometry/exemplar-11-1.html","/class-11-maths/ncert-exemplar-practice/chapter-11-3d-geometry/exemplar-11-2.html","/class-11-maths/ncert-exemplar-practice/chapter-11-3d-geometry/exemplar-11-3.html"],"chapter-12-limits-and-derivatives":["/class-11-maths/ncert-exemplar-practice/chapter-12-limits-derivatives/exemplar-12-1.html","/class-11-maths/ncert-exemplar-practice/chapter-12-limits-derivatives/exemplar-12-2.html","/class-11-maths/ncert-exemplar-practice/chapter-12-limits-derivatives/exemplar-12-3.html"],"chapter-13-statistics":["/class-11-maths/ncert-exemplar-practice/chapter-13-statistics/exemplar-13-1.html","/class-11-maths/ncert-exemplar-practice/chapter-13-statistics/exemplar-13-2.html","/class-11-maths/ncert-exemplar-practice/chapter-13-statistics/exemplar-13-3.html"],"chapter-14-probability":["/class-11-maths/ncert-exemplar-practice/chapter-14-probability/exemplar-14-1.html","/class-11-maths/ncert-exemplar-practice/chapter-14-probability/exemplar-14-2.html","/class-11-maths/ncert-exemplar-practice/chapter-14-probability/exemplar-14-3.html"]},"test":{"chapter-1-sets":["/class-11-maths/tests/chapter-wise/chapter-1-sets/basic.html","/class-11-maths/tests/chapter-wise/chapter-1-sets/hard.html","/class-11-maths/tests/chapter-wise/chapter-1-sets/standard.html"],"chapter-2-relations-and-functions":["/class-11-maths/tests/chapter-wise/chapter-2-relations-and-functions/basic.html","/class-11-maths/tests/chapter-wise/chapter-2-relations-and-functions/hard.html","/class-11-maths/tests/chapter-wise/chapter-2-relations-and-functions/standard.html"],"chapter-3-trigonometric-functions":["/class-11-maths/tests/chapter-wise/chapter-3-trigonometric-functions/basic.html","/class-11-maths/tests/chapter-wise/chapter-3-trigonometric-functions/hard.html","/class-11-maths/tests/chapter-wise/chapter-3-trigonometric-functions/standard.html"],"chapter-4-complex-numbers-and-quadratic-equations":["/class-11-maths/tests/chapter-wise/chapter-4-complex-numbers-and-quadratic-equations/basic.html","/class-11-maths/tests/chapter-wise/chapter-4-complex-numbers-and-quadratic-equations/hard.html","/class-11-maths/tests/chapter-wise/chapter-4-complex-numbers-and-quadratic-equations/standard.html"],"chapter-5-linear-inequalities":["/class-11-maths/tests/chapter-wise/chapter-5-linear-inequalities/basic.html","/class-11-maths/tests/chapter-wise/chapter-5-linear-inequalities/hard.html","/class-11-maths/tests/chapter-wise/chapter-5-linear-inequalities/standard.html"],"chapter-6-permutations-and-combinations":["/class-11-maths/tests/chapter-wise/chapter-6-permutations-and-combinations/basic.html","/class-11-maths/tests/chapter-wise/chapter-6-permutations-and-combinations/hard.html","/class-11-maths/tests/chapter-wise/chapter-6-permutations-and-combinations/standard.html"],"chapter-7-binomial-theorem":["/class-11-maths/tests/chapter-wise/chapter-7-binomial-theorem/basic.html","/class-11-maths/tests/chapter-wise/chapter-7-binomial-theorem/hard.html","/class-11-maths/tests/chapter-wise/chapter-7-binomial-theorem/standard.html"],"chapter-8-sequences-and-series":["/class-11-maths/tests/chapter-wise/chapter-8-sequences-and-series/basic.html","/class-11-maths/tests/chapter-wise/chapter-8-sequences-and-series/hard.html","/class-11-maths/tests/chapter-wise/chapter-8-sequences-and-series/standard.html"],"chapter-9-straight-lines":["/class-11-maths/tests/chapter-wise/chapter-9-straight-lines/basic.html","/class-11-maths/tests/chapter-wise/chapter-9-straight-lines/hard.html","/class-11-maths/tests/chapter-wise/chapter-9-straight-lines/standard.html"],"chapter-10-conic-sections":["/class-11-maths/tests/chapter-wise/chapter-10-conic-sections/basic.html","/class-11-maths/tests/chapter-wise/chapter-10-conic-sections/hard.html","/class-11-maths/tests/chapter-wise/chapter-10-conic-sections/standard.html"],"chapter-11-introduction-to-three-dimensional-geometry":["/class-11-maths/tests/chapter-wise/chapter-11-introduction-to-three-dimensional-geometry/basic.html","/class-11-maths/tests/chapter-wise/chapter-11-introduction-to-three-dimensional-geometry/hard.html","/class-11-maths/tests/chapter-wise/chapter-11-introduction-to-three-dimensional-geometry/standard.html"],"chapter-12-limits-and-derivatives":["/class-11-maths/tests/chapter-wise/chapter-12-limits-and-derivatives/basic.html","/class-11-maths/tests/chapter-wise/chapter-12-limits-and-derivatives/hard.html","/class-11-maths/tests/chapter-wise/chapter-12-limits-and-derivatives/standard.html"],"chapter-13-statistics":["/class-11-maths/tests/chapter-wise/chapter-13-statistics/basic.html","/class-11-maths/tests/chapter-wise/chapter-13-statistics/hard.html","/class-11-maths/tests/chapter-wise/chapter-13-statistics/standard.html"],"chapter-14-probability":["/class-11-maths/tests/chapter-wise/chapter-14-probability/basic.html","/class-11-maths/tests/chapter-wise/chapter-14-probability/hard.html","/class-11-maths/tests/chapter-wise/chapter-14-probability/standard.html"]}};

  function chapterSlug(card) {
    const notes = card.querySelector('a.notes-tab[href]');
    const match = notes && notes.getAttribute('href').match(/chapter-wise-notes\/(chapter-[^/]+)\//);
    return match ? match[1] : '';
  }

  function resourceLabel(href, category) {
    const file = href.split('/').pop().replace(/\.html$/, '');
    const numbered = file.match(/^(exercise|exemplar)-(\d+)-(\d+)$/);
    if (numbered) return (numbered[1] === 'exercise' ? 'Exercise ' : 'Exemplar ') + numbered[2] + '.' + numbered[3];
    if (file === 'misc-exercise' || file === 'miscellaneous-exercise') return 'Miscellaneous Exercise';
    if (file === 'hots') return 'HOTS Worksheet';
    if (file === 'basic') return category === 'Test' ? 'Basic Test' : 'Basic Worksheet';
    if (file === 'standard') return category === 'Test' ? 'Standard Test' : 'Standard Worksheet';
    if (file === 'hard') return 'Challenge Test';
    return file.split('-').map(function (word) { return word.charAt(0).toUpperCase() + word.slice(1); }).join(' ');
  }

  function makeDropdown(anchor, links, category) {
    const details = document.createElement('details');
    details.className = 'quick-tab-dropdown ' + anchor.className;

    const summary = document.createElement('summary');
    summary.className = 'quick-tab-summary';
    summary.innerHTML = anchor.innerHTML + '<span class="quick-tab-chevron" aria-hidden="true">&#9662;</span>';
    details.appendChild(summary);

    const menu = document.createElement('div');
    menu.className = 'quick-tab-menu';
    menu.setAttribute('role', 'group');
    menu.setAttribute('aria-label', category + ' resources');
    links.forEach(function (href) {
      const link = document.createElement('a');
      link.href = href;
      link.textContent = resourceLabel(href, category);
      menu.appendChild(link);
    });
    details.appendChild(menu);
    return details;
  }

  function closeOtherDropdowns(current) {
    document.querySelectorAll('.quick-tab-dropdown[open]').forEach(function (dropdown) {
      if (dropdown !== current) dropdown.removeAttribute('open');
    });
  }

  function positionMenu(dropdown) {
    const menu = dropdown.querySelector('.quick-tab-menu');
    if (!menu) return;
    const button = dropdown.getBoundingClientRect();
    const menuWidth = Math.min(260, window.innerWidth - 32);
    const left = Math.max(8, Math.min(button.left, window.innerWidth - menuWidth - 8));
    menu.style.position = 'absolute';
    menu.style.width = menuWidth + 'px';
    menu.style.left = '0px';
    menu.style.right = 'auto';
    menu.style.top = 'calc(100% + .4rem)';
    menu.style.transform = 'none';
    const origin = menu.getBoundingClientRect();
    menu.style.left = (left - origin.left) + 'px';
  }

  function init() {
    document.querySelectorAll('.ch-card-item').forEach(function (card) {
      const slug = chapterSlug(card);
      if (!slug) return;

      [
        ['ncert', 'ncert-tab', 'NCERT'],
        ['worksheet', 'sheet-tab', 'Worksheet'],
        ['exemplar', 'pyq-tab', 'Exemplar'],
        ['test', 'test-tab', 'Test']
      ].forEach(function (entry) {
        const anchor = card.querySelector('a.' + entry[1]);
        const links = resources[entry[0]] && resources[entry[0]][slug];
        if (!anchor || !links || links.length < 2) return;

        const dropdown = makeDropdown(anchor, links, entry[2]);
        dropdown.addEventListener('toggle', function () {
          if (dropdown.open) {
            closeOtherDropdowns(dropdown);
            requestAnimationFrame(function () { positionMenu(dropdown); });
          }
        });
        anchor.replaceWith(dropdown);
      });
    });
  }

  const style = document.createElement('style');
  style.textContent = [
    '.quick-tab-dropdown{position:relative;display:block!important;min-width:0;padding:0!important;border:0!important;background:transparent!important;}',
    '.quick-tab-dropdown[open]{z-index:100;}',
    '.ch-card-item:has(.quick-tab-dropdown[open]){overflow:visible;z-index:20;}',
    '.quick-tab-dropdown summary{list-style:none;cursor:pointer;}',
    '.quick-tab-dropdown summary::-webkit-details-marker{display:none;}',
    '.quick-tab-summary{position:relative;display:flex!important;flex-direction:column;align-items:center;justify-content:center;gap:.12rem;}',
    '.quick-tab-chevron{font-size:1em;line-height:1;transition:transform .2s ease;}',
    '.quick-tab-dropdown[open] .quick-tab-chevron{transform:rotate(180deg);}',
    '.quick-tab-dropdown .quick-tab-summary{width:100%;min-height:52px;box-sizing:border-box;padding:.25rem .15rem .6rem;border:1px solid currentColor;border-radius:8px;background:#fff;font-size:.68rem;line-height:1.15;font-weight:700;}',
    '.quick-tab-summary .quick-tab-chevron{position:absolute;right:3px;bottom:2px;font-size:.58rem;}',
    '.quick-tab-menu{position:absolute;z-index:101;top:calc(100% + .4rem);left:50%;transform:translateX(-50%);display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:.35rem;min-width:13rem;margin:0;padding:.45rem;border:1px solid #c9ddd5;border-radius:.7rem;background:#fffefa;box-shadow:0 10px 24px rgba(13,50,40,.18);}',
    '.quick-tab-menu a{display:flex;align-items:center;min-width:0;min-height:2.6rem;padding:.55rem .7rem;border-radius:.45rem;background:#f2f7f4;color:#12634e;text-decoration:none;font-size:.82rem;line-height:1.2;font-weight:650;overflow-wrap:anywhere;}',
    '.quick-tab-menu a:hover,.quick-tab-menu a:focus-visible{background:#dff2e9;color:#07553f;outline:2px solid #008a68;outline-offset:1px;}',
    'body.dark-mode .quick-tab-dropdown .quick-tab-summary{background:#17312d;}',
    'body.dark-mode .quick-tab-menu{background:#142c27;border-color:#37675b;box-shadow:0 10px 28px rgba(0,0,0,.5);}',
    'body.dark-mode .quick-tab-menu a{background:#1d4039;color:#c9e7dc;}',
    'body.dark-mode .quick-tab-menu a:hover,body.dark-mode .quick-tab-menu a:focus-visible{background:#285647;color:#effaf5;}',
    '@media(max-width:640px){.quick-tab-menu{min-width:0;grid-template-columns:repeat(2,minmax(0,1fr));}.quick-tab-menu a{min-height:2.75rem;font-size:.78rem;}.quick-tab-summary>span:not(.quick-tab-chevron){max-width:100%;overflow-wrap:anywhere;text-align:center;}}'
  ].join('');
  document.head.appendChild(style);

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
}());
