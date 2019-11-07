from multiprocessing.pool import Pool

import socketio
import time

sio = socketio.Client()


def stream_data(id):

    @sio.event
    def connect():
        print('connected to the server for client = ', id)
        sio.emit('authentication')

    @sio.event
    def disconnect():
        print('coneection closed for client = ', id)

    @sio.event
    def my_message():
        print('signal received')

    @sio.on('authenticated')
    def authorized(data):
        print('authorized')
        time.sleep(3)
        while True:
            print('sending logs for client ', id)
            sio.emit('my_log', {'id': id, 'name': 'lorem'})
            time.sleep(0.25)
    sio.connect('http://localhost:8000')
    sio.wait()


if __name__ == '__main__':
    print('start of client id')
    start_client_id = input()
    num = int(start_client_id)
    pool = Pool(num+9)
    pool.map(stream_data, range(num, num+9))
    # pool.map(stream_data, range(1, 3))
