/* Native answer disclosures work without this optional print/share enhancement. */
(function () {
  'use strict';
  const answers = [...document.querySelectorAll('.worksheet-solution')];
  const toggle = document.getElementById('toggle-sheet-answers');
  if (!toggle) return;
  const sync = () => {
    const allOpen = answers.every(answer => answer.open);
    toggle.textContent = allOpen ? 'Hide all answers' : 'Show all answers';
    toggle.setAttribute('aria-pressed', String(allOpen));
  };
  toggle.addEventListener('click', () => {
    const open = !answers.every(answer => answer.open);
    answers.forEach(answer => { answer.open = open; });
    sync();
  });
  answers.forEach(answer => answer.addEventListener('toggle', sync));
  let beforePrint = null;
  const restore = () => {
    if (!beforePrint) return;
    answers.forEach((answer, i) => { answer.open = beforePrint[i]; });
    beforePrint = null;
    document.body.classList.remove('print-answers');
    sync();
  };
  document.getElementById('print-sheet').addEventListener('click', () => {
    beforePrint = answers.map(answer => answer.open);
    const withAnswers = document.getElementById('print-sheet-answers').checked;
    document.body.classList.toggle('print-answers', withAnswers);
    answers.forEach(answer => { answer.open = withAnswers; });
    window.print();
  });
  window.addEventListener('afterprint', restore);
  document.getElementById('share-sheet').addEventListener('click', async () => {
    const status = document.getElementById('sheet-share-status');
    try {
      if (navigator.share) await navigator.share({ title: document.title, url: location.href });
      else if (navigator.clipboard && window.isSecureContext) {
        await navigator.clipboard.writeText(location.href);
        status.textContent = 'Worksheet link copied.';
      } else status.textContent = 'Copy this worksheet’s address from the browser address bar.';
    } catch (error) {
      status.textContent = error.name === 'AbortError' ? 'Sharing cancelled.' : 'Sharing unavailable. Copy the address from the browser address bar.';
    }
  });
  sync();
}());
