async function fetchGraph() {
  const res = await fetch('/api/graph/');
  if (!res.ok) throw new Error('Failed to fetch graph');
  return res.json();
}

function nodeStyle() {
  return [
    {
      selector: 'node',
      style: {
        'background-color': '#4e79a7',
        'label': 'data(label)',
        'color': '#222',
        'text-outline-color': '#fff',
        'text-outline-width': 2,
        'font-size': 12,
        'width': 30,
        'height': 30,
        'shape': 'ellipse'
      }
    },
    {
      selector: 'node[type = "router"]',
      style: { 'shape': 'hexagon', 'background-color': '#59a14f' }
    },
    {
      selector: 'node[type = "switch"]',
      style: { 'shape': 'round-rectangle', 'background-color': '#f28e2b' }
    },
    {
      selector: 'edge',
      style: {
        'line-color': '#9c9c9c',
        'width': 2,
        'curve-style': 'bezier',
        'target-arrow-color': '#9c9c9c',
        'target-arrow-shape': 'triangle',
        'label': 'data(label)',
        'font-size': 10,
        'text-background-color': '#fff',
        'text-background-opacity': 0.8,
        'text-background-padding': 2
      }
    },
    {
      selector: 'edge[directed = false]',
      style: { 'target-arrow-shape': 'none' }
    }
  ];
}

function layoutOptions() {
  return { name: 'cose', animate: true, fit: true, padding: 30 };
}

async function init() {
  const container = document.getElementById('topology');
  const { elements } = await fetchGraph();

  const cy = cytoscape({
    container,
    elements,
    style: nodeStyle(),
    layout: layoutOptions(),
    wheelSensitivity: 1
  });

  cy.on('tap', 'node', (evt) => {
    const n = evt.target;
    const meta = n.data();
    alert(`Node: ${meta.label}\nType: ${meta.type || 'n/a'}\nData: ${JSON.stringify(meta, null, 2)}`);
  });

  cy.on('tap', 'edge', (evt) => {
    const e = evt.target;
    const d = e.data();
    alert(`Link: ${d.label}\nBandwidth: ${d.bandwidth_mbps || 'n/a'} Mbps\nLatency: ${d.latency_ms || 'n/a'} ms`);
  });

  document.getElementById('fit').addEventListener('click', () => cy.fit());
  document.getElementById('reset-layout').addEventListener('click', () => cy.layout(layoutOptions()).run());
}

init().catch(err => {
  console.error(err);
  const container = document.getElementById('topology');
  container.innerHTML = '<p style="padding:16px;color:#b00020;">Failed to load topology.</p>';
});
