/* Score converter. Every table below is transcribed from the IRCC test-equivalency
   charts. Where a chart is not published for a test, the test is not offered here
   rather than filled with a plausible number. */
(function () {
  var T = {
    ielts: { label: 'IELTS General Training', system: 'CLB', step: 0.5, min: 0, max: 9,
      rows: [
        [10, 8.5, 8.0, 7.5, 7.5], [9, 8.0, 7.0, 7.0, 7.0], [8, 7.5, 6.5, 6.5, 6.5],
        [7, 6.0, 6.0, 6.0, 6.0], [6, 5.5, 5.0, 5.5, 5.5], [5, 5.0, 4.0, 5.0, 5.0],
        [4, 4.5, 3.5, 4.0, 4.0]
      ], kind: 'min' },
    celpip: { label: 'CELPIP-General', system: 'CLB', step: 1, min: 0, max: 12,
      rows: [[10,10,10,10,10],[9,9,9,9,9],[8,8,8,8,8],[7,7,7,7,7],[6,6,6,6,6],[5,5,5,5,5],[4,4,4,4,4]],
      kind: 'min' },
    tef: { label: 'TEF Canada', system: 'NCLC', step: 1, min: 0, max: 699,
      bands: [
        [10,[546,699],[546,699],[558,699],[556,699]], [9,[503,545],[503,545],[512,557],[518,555]],
        [8,[462,502],[462,502],[472,511],[494,517]],  [7,[434,461],[434,461],[428,471],[456,493]],
        [6,[393,433],[393,433],[379,427],[422,455]],  [5,[352,392],[352,392],[330,378],[387,421]],
        [4,[306,351],[306,351],[268,329],[328,386]]
      ], kind: 'band' },
    tcf: { label: 'TCF Canada', system: 'NCLC', step: 1, min: 0, max: 699, only7: true,
      bands: [[7,[458,502],[453,498],[10,11],[10,11]]], kind: 'band' }
  };
  var ORDER = ['listening','reading','writing','speaking'];

  function levelFor(t, i, v) {
    if (v === '' || isNaN(v)) return null;
    v = Number(v);
    if (t.kind === 'min') {
      for (var r = 0; r < t.rows.length; r++) if (v >= t.rows[r][i + 1]) return t.rows[r][0];
      return 'below';
    }
    for (var b = 0; b < t.bands.length; b++) {
      var band = t.bands[b][i + 1];
      if (v >= band[0] && v <= band[1]) return t.bands[b][0];
      if (t.only7 && v > band[1]) return 'above';
    }
    return t.only7 ? 'below' : 'below';
  }

  window.SELMCalc = function (L) {
    var form = document.getElementById('calcForm'),
        sel = document.getElementById('calcTest'),
        out = document.getElementById('calcOut');
    Object.keys(T).forEach(function (k) {
      var o = document.createElement('option'); o.value = k; o.textContent = T[k].label; sel.appendChild(o);
    });
    function refresh() {
      var t = T[sel.value];
      ORDER.forEach(function (s) {
        var el = document.getElementById('f_' + s);
        el.step = t.step; el.min = t.min; el.max = t.max; el.placeholder = t.system === 'CLB' && t.step === 0.5 ? '0.0' : '0';
      });
      document.getElementById('calcNote').textContent = t.only7 ? L.only7 : '';
    }
    sel.addEventListener('change', function () { refresh(); out.innerHTML = ''; out.className = 'res empty'; });
    refresh();

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var t = T[sel.value], levels = [], html = '<div class="tbl-scroll"><table><thead><tr><th>' +
        L.skill + '</th><th>' + L.score + '</th><th>' + t.system + '</th></tr></thead><tbody>';
      var any = false;
      ORDER.forEach(function (s, i) {
        var raw = document.getElementById('f_' + s).value;
        var lv = levelFor(t, i, raw);
        if (lv !== null) any = true;
        levels.push(lv);
        var shown = lv === null ? '—' : (lv === 'below' ? L.below : (lv === 'above' ? L.above : t.system + ' ' + lv));
        html += '<tr><td>' + L.skills[i] + '</td><td>' + (raw === '' ? '—' : raw) + '</td><td><strong>' + shown + '</strong></td></tr>';
      });
      html += '</tbody></table></div>';
      if (!any) { out.className = 'res empty'; out.textContent = L.enter; return; }
      var nums = levels.filter(function (x) { return typeof x === 'number'; });
      if (nums.length === ORDER.length) {
        var governing = Math.min.apply(null, nums);
        html = '<div class="res-lvl">' + t.system + ' ' + governing + '</div><p class="muted">' + L.governing + '</p>' + html;
        if (t.system === 'NCLC') {
          html += '<div class="callout"><p style="margin-bottom:0">' + (governing >= 7 ? L.bonusYes : L.bonusNo) + '</p></div>';
        }
      } else {
        html += '<p class="muted">' + L.partial + '</p>';
      }
      html += '<p class="muted">' + L.disclaimer + '</p>';
      out.className = 'res'; out.innerHTML = html;
    });
  };
})();
