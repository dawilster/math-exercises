// GET /api/state — read completion state from Vercel Blob
import { list } from '@vercel/blob';

export default async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');
  try {
    const { blobs } = await list({ prefix: 'dashboard-state.json' });
    if (!blobs.length) return res.status(200).json({ completed: {} });
    const data = await fetch(blobs[0].url, { cache: 'no-store' }).then(r => r.json());
    return res.status(200).json(data);
  } catch (e) {
    return res.status(500).json({ error: String(e) });
  }
}
