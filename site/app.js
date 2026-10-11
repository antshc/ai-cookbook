/* Progressive enhancement: canonical pages and all materials remain usable without JS. */
'use strict';
const cfg = window.COOKBOOK;
const fields = ['search', 'problem', 'artifact', 'task', 'kind'];
const keys = ['q', 'problem', 'artifact', 'task', 'kind'];
const kinds = {recipe:'Recipe', reference:'Reference', template:'Template', 'source-only':'Recipe needed'};
function matches(m, state) {
  const terms = state.q.toLocaleLowerCase().trim().split(/\s+/).filter(Boolean);
  const haystack = [m.title, m.use_when, ...m.keywords, m.content || ''].join(' ').toLocaleLowerCase();
  return (!state.problem || m.problems.includes(state.problem)) &&
    (!state.artifact || m.applies_to.includes(state.artifact)) &&
    (!state.task || m.task_types.includes(state.task)) &&
    (!state.kind || m.kind === state.kind) && terms.every(t => haystack.includes(t));
}
function stateFromURL(params) {
  return {q:params.get('q') || '', problem:params.get('problem') ?? cfg.problem,
    artifact:params.get('artifact') || '', task:params.get('task') || '', kind:params.get('kind') || ''};
}
function createCard(m) {
  const a = document.createElement('a'); a.className = 'card';
  a.href = m.kind === 'source-only' ? m.url : cfg.prefix + m.url;
  const badge = document.createElement('span'); badge.className = 'badge ' + m.kind; badge.textContent = kinds[m.kind];
  const title = document.createElement('h3'); title.textContent = m.title;
  const intro = document.createElement('p'); intro.textContent = m.use_when;
  const end = document.createElement('span'); end.className = 'card-end'; end.textContent = (m.kind === 'source-only' ? 'Read source' : 'Open material') + ' ↗';
  a.append(badge,title,intro,end); return a;
}
document.querySelectorAll('aside nav a').forEach(a => { if (a.href.split('?')[0] === location.href.split('?')[0]) a.setAttribute('aria-current','page'); });
const form = document.getElementById('filters');
if (form) {
  form.addEventListener('submit',e => e.preventDefault());
  fetch(cfg.prefix + 'search-index.json').then(r => { if (!r.ok) throw new Error('Search unavailable'); return r.json(); }).then(data => {
    const controls = fields.map(id => document.getElementById(id));
    let limit = 24;
    function state() { return Object.fromEntries(keys.map((k,i) => [k,controls[i].value])); }
    function restore() {
      const s = stateFromURL(new URLSearchParams(location.search));
      controls.forEach((c,i) => { c.value = s[keys[i]]; });
    }
    function render(updateURL = false) {
      const s = state();
      if (updateURL) {
        const params = new URLSearchParams();
        for (const [k,v] of Object.entries(s)) if (v || (k === 'problem' && cfg.problem)) params.set(k,v);
        const query = params.toString(); history.replaceState(null,'',location.pathname + (query ? '?' + query : '') + location.hash);
      }
      const filtered = data.materials.filter(m => matches(m,s)).sort((a,b) => Object.keys(kinds).indexOf(a.kind)-Object.keys(kinds).indexOf(b.kind));
      const results = document.getElementById('results'); results.replaceChildren(...filtered.slice(0,limit).map(createCard));
      const recipes = filtered.filter(m => m.kind === 'recipe').length;
      document.getElementById('count').textContent = `${filtered.length} materials · ${recipes} recipes · ${filtered.filter(m => m.kind === 'source-only').length} awaiting recipes`;
      document.getElementById('empty').hidden = filtered.length !== 0;
      document.getElementById('more').hidden = limit >= filtered.length;
    }
    controls.forEach(c => c.addEventListener(c.id === 'search' ? 'input':'change',() => { limit=24; render(true); }));
    document.getElementById('reset').addEventListener('click',() => { controls.forEach(c => c.value=''); limit=24; render(true); });
    document.getElementById('more').addEventListener('click',() => { limit+=24; render(); });
    window.addEventListener('popstate',() => { restore(); limit=24; render(); });
    restore(); render();
  }).catch(() => { document.getElementById('count').textContent='Search could not load. All chapter materials remain available below.'; form.hidden=true; });
}
const copy = document.getElementById('copy-instructions');
if (copy) {
  const blocks = [...document.querySelectorAll('.prose blockquote')];
  if (!blocks.length) copy.hidden=true;
  copy.addEventListener('click',async () => {
    const status=document.getElementById('copy-status');
    try { await navigator.clipboard.writeText(blocks.map(b => b.innerText.trim()).join('\n\n')); status.textContent='Instructions copied.'; }
    catch { status.textContent='Select the instruction text to copy manually.'; }
  });
}
