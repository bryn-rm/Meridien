import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { z } from 'zod';

const server = new McpServer({ name: 'google-calendar', version: '0.1.0' });

server.tool(
  'list_events',
  { start: z.string(), end: z.string() },
  async ({ start, end }) => ({
    content: [
      {
        type: 'text',
        text: JSON.stringify([
          { title: 'Standup', start, end },
          { title: 'Product sync', start, end }
        ])
      }
    ]
  })
);

export default server;
