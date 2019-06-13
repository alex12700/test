import rtsp
with rtsp.Client('rtsp://127.0.0.1:5554/user=user&password=&channel=1&stream=1.sdp?real_stream') as client:
    client.preview()