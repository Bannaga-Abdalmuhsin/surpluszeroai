const $ = id => document.getElementById(id);
const fmt = value => Math.round(value).toLocaleString('en-US');
const baseline = {
  generation: 68400, demand: 66500, transfer: 350,
  redispatch: 450, storage: 300, flex: 650
};
const resources = [
  ['Interregional transfer', 'Move excess to a connected deficit zone'],
  ['Generator redispatch', 'Reduce controllable output safely'],
  ['Storage', 'Charge batteries, thermal or pumped storage'],
  ['Productive flexible demand', 'Cooling, water, EVs, industry and hydrogen']
];

function use(remaining, available) {
  const amount = Math.min(Math.max(remaining, 0), Math.max(available, 0));
  return [amount, remaining - amount];
}

function scenario() {
  const generation = baseline.generation * +$('generationScale').value / 100;
  const demand = baseline.demand * +$('demandScale').value / 100;
  const action = +$('actionScale').value / 100;
  const flexScale = +$('flexScale').value / 100;
  const initial = Math.max(0, generation - demand);
  let remaining = initial;
  let transfer, redispatch, storage, flex;
  [transfer, remaining] = use(remaining, baseline.transfer * action);
  [redispatch, remaining] = use(remaining, baseline.redispatch * action);
  [storage, remaining] = use(remaining, baseline.storage * action);
  [flex, remaining] = use(remaining, baseline.flex * flexScale);

  $('generation').firstChild.textContent = `${fmt(generation)} `;
  $('demand').firstChild.textContent = `${fmt(demand)} `;
  $('excess').firstChild.textContent = `${fmt(initial)} `;
  $('residual').firstChild.textContent = `${fmt(remaining)} `;
  $('gv').textContent = `${fmt(generation)} MW`;
  $('dv').textContent = `${fmt(demand)} MW`;
  $('av').textContent = `${Math.round(action * 100)}%`;
  $('fv').textContent = `${fmt(baseline.flex * flexScale)} MW`;
  $('transfer').textContent = fmt(transfer);
  $('redispatch').textContent = fmt(redispatch);
  $('storage').textContent = fmt(storage);
  $('flex').textContent = fmt(flex);

  const stages = [
    ['Initial excess', initial], ['Transfer', transfer], ['Redispatch', redispatch],
    ['Storage', storage], ['Flexible loads', flex], ['Residual', remaining]
  ];
  const max = Math.max(1, initial);
  $('waterfall').innerHTML = stages.map(([name, value], index) =>
    `<div class="asset"><label>${name}</label><div class="track"><i style="width:${100 * value / max}%"></i></div><b>${fmt(value)} MW</b></div>`
  ).join('');
  draw(generation, demand);
}

function draw(generation, demand) {
  const svg = $('chart'), width = 900, height = 285, pad = 18;
  const rows = Array.from({length: 49}, (_, index) => {
    const hour = index / 2;
    const solarShape = Math.max(0, Math.sin((hour - 6) / 12 * Math.PI));
    const demandShape = .91 + .07 * Math.sin((hour - 8) / 24 * Math.PI * 2) + .08 * Math.exp(-((hour - 20) ** 2) / 10);
    return {g: generation * (.91 + .09 * solarShape), d: demand * demandShape};
  });
  const maximum = Math.max(...rows.flatMap(row => [row.g, row.d]));
  const path = key => rows.map((row, index) => `${index ? 'L' : 'M'} ${pad + index * (width - 2 * pad) / (rows.length - 1)} ${height - row[key] / maximum * (height - 30)}`).join(' ');
  svg.innerHTML = Array.from({length: 6}, (_, index) => {
    const y = height - index / 5 * (height - 30);
    return `<line x1="${pad}" y1="${y}" x2="${width-pad}" y2="${y}" stroke="#173247"/>`;
  }).join('') + `<path d="${path('g')}" fill="none" stroke="#ffc75a" stroke-width="3"/><path d="${path('d')}" fill="none" stroke="#55a7ff" stroke-width="3"/>`;
}

$('assets').innerHTML = resources.map(([name, detail]) => `<div class="asset"><label>${name}</label><div class="track"><i style="width:100%"></i></div><b title="${detail}">Eligible</b></div>`).join('');
['generationScale', 'demandScale', 'actionScale', 'flexScale'].forEach(id => $(id).addEventListener('input', scenario));
$('reset').addEventListener('click', () => {
  $('generationScale').value = $('demandScale').value = $('actionScale').value = $('flexScale').value = 100;
  scenario();
});
scenario();
