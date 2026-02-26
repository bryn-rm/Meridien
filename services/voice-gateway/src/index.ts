import express from 'express';
import { createServer } from 'http';
import { WebSocketServer } from 'ws';

const app = express();
const server = createServer(app);
const wss = new WebSocketServer({ server });

app.get('/healthz', (_req, res) => res.json({ status: 'ok', service: 'voice-gateway' }));

wss.on('connection', (socket) => {
  socket.send(JSON.stringify({ type: 'status', text: 'voice gateway connected' }));
  socket.on('message', (msg) => {
    const transcript = msg.toString();
    socket.send(JSON.stringify({ type: 'transcript', text: transcript }));
    socket.send(JSON.stringify({ type: 'assistant', text: `Meridian heard: ${transcript}` }));
  });
});

const port = Number(process.env.PORT ?? 8080);
server.listen(port, () => console.log(`Voice gateway listening on :${port}`));
