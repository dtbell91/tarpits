#!/usr/bin/env python3

import asyncio
import random
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s : %(levelname)s : %(message)s')

async def handler(_reader, writer):
    logging.info('status="new connection" client_ip="%s:%s"' % (writer.get_extra_info('peername')))
    writer.write(b'HTTP/1.1 200 OK\r\n')
    try:
        while True:
            await asyncio.sleep(5)
            header = random.randint(0, 2**32)
            value = random.randint(0, 2**32)
            logging.info('status="sending random data" client_ip="%s:%s"' % (writer.get_extra_info('peername')))
            writer.write(b'X-%x: %x\r\n' % (header, value))
            await writer.drain()
    except ConnectionResetError:
        logging.info('status="connection reset" client_ip="%s:%s"' % (writer.get_extra_info('peername')))
        pass

async def main():
    logging.info('status="starting"')
    server = await asyncio.start_server(handler, '0.0.0.0', 8080)
    async with server:
        logging.info(server)
        await server.serve_forever()

asyncio.run(main())
