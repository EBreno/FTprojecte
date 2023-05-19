import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller

video = cv2.VideoCapture(0)

video.set(3, 1280)
video.set(4, 720)

kb = Controller()

detector = HandDetector(detectionCon=0.8)
estado1 = [0, 0, 0, 0, 0]

while True:
    _, img = video.read()
    hands, img = detector.findHands(img)

    if hands:
        for hand in hands:
            if hand['type'] == 'Left':
                estado2 = detector.fingersUp(hand)

                if estado2 != estado1 and estado2 == [0, 1, 0, 0, 0]:
                    print('passar slide')
                    kb.press(Key.right)
                    kb.release(Key.right)

                if estado2 != estado1 and estado2 == [0, 0, 0, 0, 1]:
                    print('voltar slide')
                    kb.press(Key.left)
                    kb.release(Key.left)

                estado1 = estado2

    cv2.imshow('img', cv2.resize(img, (640, 420)))
    if cv2.waitKey(1) == ord('e'):
        break