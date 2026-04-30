document.addEventListener('DOMContentLoaded', async () => {
  const yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();
  try {
    const res = await fetch('data/updates.json', {cache:'no-cache'});
    if (res.ok) {
      const data = await res.json();
      renderRoadmap(data);
      renderChangelog(data);
      const overall = document.getElementById('overall-progress');
      if (overall) overall.textContent = (data.overall_progress ?? 0) + '%';
    }
  } catch(e) { console.warn('updates.json not found', e); }
});
function renderRoadmap(data){
  const wrap = document.getElementById('timeline');
  if (!wrap || !data?.phases) return;
  wrap.innerHTML = '';
  data.phases.forEach(p => {
    const el = document.createElement('div');
    const badgeCls = p.status === 'complete' ? 'complete' : (p.status === 'in-progress' ? 'in-progress' : 'planned');
    el.className = 'phase';
    el.innerHTML = `<div class="badge ${badgeCls}">${p.status}</div>
      <div><div class="phase-title">Phase ${p.id} — ${p.title}</div>
      <div class="phase-meta">${p.date || ''} • ${p.percent}%</div>
      ${Array.isArray(p.highlights)?`<ul style="margin:8px 0 0 0; padding-left:20px;">${p.highlights.map(h=>`<li>${h}</li>`).join('')}</ul>`:''}</div>`;
    wrap.appendChild(el);
  });
}
function renderChangelog(data){
  const wrap = document.getElementById('changelog');
  if (!wrap || !data?.changelog) return;
  wrap.innerHTML = '';
  data.changelog.forEach(item => {
    const card = document.createElement('div');
    card.className = 'card';
    card.innerHTML = `<div style="display:flex;justify-content:space-between;align-items:center;gap:8px;">
        <strong>Version ${item.version}</strong>
        <span style="color:#9fb2c3">${item.date}</span></div>
      <div style="margin-top:6px">${item.title}</div>
      ${Array.isArray(item.items)?`<ul style="margin:8px 0 0 0; padding-left:20px;">${item.items.map(h=>`<li>${h}</li>`).join('')}</ul>`:''}`;
    wrap.appendChild(card);
  });
}