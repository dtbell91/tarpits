#!/usr/bin/env python3

import asyncio
import random
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s : %(levelname)s : %(message)s')

async def handler(_reader, writer):
    client = '%s:%s' % writer.get_extra_info('peername')
    connections = len(asyncio.all_tasks())
    if connections > 500:
        logging.info('status="too many connections" client="%s" connections=%d' % (client, connections))
        await writer.drain()
        writer.close()
        return

    start = datetime.now()
    logging.info('status="new connection" client="%s" connections=%d' % (client, connections))
    try:
        while True:
            wait = 10
            await asyncio.sleep(wait)
            header = random.getrandbits(32)
            value = random.getrandbits(32)
            #writer.write(b'X-%x: %x\r\n' % (header, value))
            #writer.write(b'X-%x: %x' % (header, value))
            writer.write(b'250-%x\r\n' % (header,))
            await writer.drain()
    except ConnectionResetError:
        end = datetime.now()
        duration = end - start
        logging.info('status="connection reset" client="%s" duration="%s" connections=%d' % (client, duration, connections))
        pass

async def main():
    logging.info('status="starting"')
    server = await asyncio.start_server(handler, '0.0.0.0', 25)
    async with server:
        logging.info(server)
        await server.serve_forever()

asyncio.run(main())
