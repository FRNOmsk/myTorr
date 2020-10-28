import asyncio
import torrent
import signal
import logging
from client import TorrentClient

from concurrent.futures import CancelledError

def main():
    loop = asyncio.get_event_loop()
    client = TorrentClient(torrent.Torrent('hunt.torrent'))
    task = loop.create_task(client.start())
    # print(client)

    def signal_handler(*_):
        logging.info('Exiting, please wait until everything is shutdown...')
        client.stop()
        task.cancel()

    signal.signal(signal.SIGINT, signal_handler)

    try:
        loop.run_until_complete(task)
    except CancelledError:
        logging.warning('Event loop was canceled')
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
