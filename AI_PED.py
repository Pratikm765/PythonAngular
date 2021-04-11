import cv2

def function1():
    img_file = 'sample.png'
    cascade_file = 'cars_detector.xml'

    img = cv2.imread(img_file)
    img = cv2.resize(img, (960, 540))
    bw_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    car_tracker = cv2.CascadeClassifier(cascade_file)

    cars = car_tracker.detectMultiScale(bw_img,
                                        minSize=(150, 150))

    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    print(cars)

    cv2.imshow('Cars Detection', img)

    cv2.waitKey()

def function2():
    import cv2

    # Opening image
    img = cv2.imread("image.jpg")

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    stop_data = cv2.CascadeClassifier('stop_data.xml')

    found = stop_data.detectMultiScale(img_gray,
                                       minSize=(20, 20))

    for (x, y, width, height) in found:
        cv2.rectangle(img_rgb, (x, y),
                      (x + height, y + width),
                      (0, 255, 0), 5)

    cv2.imshow('Signal Detection', img_rgb)

    cv2.waitKey()

def function3():
    video=cv2.VideoCapture("testVideo.mp4")
    car_tracker = cv2.CascadeClassifier('cars_detector.xml')

    while True:
        (read_successful,frame)=video.read()
        if(read_successful):
            bw_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        else:
            break

        cars = car_tracker.detectMultiScale(bw_frame, minSize=(150, 150))
        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow('Cars Tracking',frame)
        key=cv2.waitKey(1)

        if key==81 or key==113:
            break


function3()
