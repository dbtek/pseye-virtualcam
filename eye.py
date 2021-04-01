from pseyepy import Camera
# This script is the sample from the README.
import pyvirtualcam

with pyvirtualcam.Camera(width=640, height=480, fps=60, print_fps=True) as vcam:
    print(f'Using virtual camera: { vcam.device }')
    
    # initialize all connected cameras
    c = Camera(fps=60, resolution=Camera.RES_LARGE)

    while True:
        frame, timestamp = c.read()
        vcam.send(frame)
        vcam.sleep_until_next_frame()

    print(f'Closing camera...')
    c.end()