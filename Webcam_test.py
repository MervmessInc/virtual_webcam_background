import cv2
import PySimpleGUI as sg

window = sg.Window('Demo Application - OpenCV Integration',
                   [[sg.Image(filename='', key='image')], ], location=(100, 100))


# Setup the camera as a capture device
cap = cv2.VideoCapture(0)
# USB Microsoft Lifecam
#cap = cv2.VideoCapture(1 + cv2.CAP_DSHOW)

# The PSG "Event Loop"
while True:
    # get events for the window with 20ms max wait
    event, values = window.Read(timeout=20, timeout_key='timeout')

    if event is None:
        # if user closed window, quit
        break

    # Update image in window
    success, frame = cap.read()
    success, img = cv2.imencode('.png', frame)
    window.FindElement('image').Update(data=img.tobytes())
