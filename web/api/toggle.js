// POST /api/toggle {id} — flip a unit's completion in Vercel Blob state
import { list, put } from '@vercel/blob';

export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).end();
  try {
    const { id } = req.body || {};
    if (!id) return res.status(400).json({ error: 'missing id' });

    let state = { completed: {} };
    const { blobs } = await list({ prefix: 'dashboard-state.json' });
    if (blobs.length) {
      state = await fetch(blobs[0].url, { cache: 'no-store' }).then(r => r.json());
    }
    if (state.completed[id]) delete state.completed[id];
    else state.completed[id] = new Date().toISOString().slice(0, 10);

    await put('dashboard-state.json', JSON.stringify(state, null, 2), {
      access: 'public', addRandomSuffix: false, allowOverwrite: true,
      contentType: 'application/json',
    });
    res.setHeader('Cache-Control', 'no-store');
    return res.status(200).json(state);
  } catch (e) {
    return res.status(500).json({ error: String(e) });
  }
}
