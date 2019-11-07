import eventlet
import socketio


sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('connection from client = ', sid)

@sio.event
def my_message(data):
    print('data rcvd =', data)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


@sio.on('authentication')
def authenticated(data):
    # do stuff for authentication
    sio.emit('authenticated')


@sio.on('my_log')
def custom_event(sid, data):
    print('recieving logs = ', data)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)
