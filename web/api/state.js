// GET /api/state — read completion state from Vercel Blob (private store)
import { list } from '@vercel/blob';

export default async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');
  try {
    const { blobs } = await list({ prefix: 'dashboard-state.json' });
    if (!blobs.length) return res.status(200).json({ completed: {} });
    const url = blobs[0].downloadUrl || blobs[0].url;
    // Private-store blobs require the token as a bearer header even to read —
    // the URL itself isn't a pre-signed public link.
    const data = await fetch(url, {
      cache: 'no-store',
      headers: { Authorization: `Bearer ${process.env.BLOB_READ_WRITE_TOKEN}` },
    }).then(r => r.json());
    return res.status(200).json(data);
  } catch (e) {
    return res.status(500).json({ error: String(e) });
  }
}
