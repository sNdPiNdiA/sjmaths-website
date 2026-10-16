/**
 * Civics Topic and Hub Interactive Utilities
 * SJ Maths - Zero-dependency client-side checklist persistence
 */
(function() {
  'use strict';

  function initChecklists() {
    try {
      var key = 'sjmaths_civics_chk_' + window.location.pathname;
      var boxes = document.querySelectorAll('.checklist input[type="checkbox"]');
      if (!boxes || !boxes.length) return;

      var saved = [];
      try {
        var raw = localStorage.getItem(key);
        if (raw) saved = JSON.parse(raw);
        if (!Array.isArray(saved)) saved = [];
      } catch (err) {
        saved = [];
      }

      boxes.forEach(function(box, index) {
        if (saved.indexOf(index) !== -1) {
          box.checked = true;
        }

        box.addEventListener('change', function() {
          var state = [];
          boxes.forEach(function(b, i) {
            if (b.checked) state.push(i);
          });
          try {
            localStorage.setItem(key, JSON.stringify(state));
          } catch (storageErr) {}
        });
      });
    } catch (e) {}
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initChecklists);
  } else {
    initChecklists();
  }
})();
