def card_reader2(self):
    from picamera import PiCamera
    import cv2
    from scipy import ndimage
    import numpy as np
    import pytesseract
    from datetime import datetime, date
    def age(birthdate):
        today = date.today()
        age = today.year - birthdate.year - ((today.month, today.day) <
                                             (birthdate.month, birthdate.day))
        return age
    camera = PiCamera()

    camera.resolution = (1280, 720)
    c = camera.capture('testimage.png')

    # Read the main image
    img_rgb = cv2.imread('testimage.png')
    img_rgb = ndimage.rotate(img_rgb, 270)
    cv2.imwrite('final.png', img_rgb)

    # Convert it to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    # Read the template
    template = cv2.imread('template.png', 0)

    # Store width and height of template in w and h
    w, h = template.shape[::-1]

    # Perform match operations.
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

    # Specify a threshold
    threshold = 0.9

    # Store the coordinates of matched area in a numpy array
    loc = np.where(res >= threshold)
    a = []
    b = []
    # Draw a rectangle around the matched region.
    for pt in zip(*loc[::-1]):
        print(pt)
        print(pt[0] + w, pt[1] + h)
        a.append(pt[0])
        b.append(pt[1])
    averageA = sum(a) / len(a)
    averageB = sum(b) / len(b)
    ptA = int(averageA) + 70
    ptB = int(averageB) - 10

    cv2.rectangle(img_rgb, (ptA, ptB), (ptA + 250, ptB + 70), (0, 255, 255), 2)
    test = img_rgb[ptB + 2:ptB + 68, ptA + 2:ptA + 248]
    cv2.imshow('test', test)
    stri = pytesseract.image_to_string(test, lang='eng', config="-psm 7")
    im2 = stri.replace('\n', '')
    im2 = im2.replace(' ', '')
    im2 = im2.strip(".,;><?abcdefghijklmnopqrstuvwxyz=+-_*&^%$#@!»©|")
    print(im2)
    format_date = datetime.strptime(im2, '%m/%d/%Y')
    print("The date is", format_date.date())
    a = age(format_date.date())
    print(age(format_date.date()))
    age_customer = a

    if (age_customer > 21):
        print("Eligible to drink at our awesome bar")
    else:
        print("Ineligible to drink at our bad bar")
    return a

    cv2.waitKey(0)
