# Credit - Adil Deokar
# adildeokar.com

import time
import serial

import adafruit_fingerprint


# import board
# uart = busio.UART(board.TX, board.RX, baudrate=57600)

# If using with a computer such as Linux/RaspberryPi, Mac, Windows with USB/serial converter:
#uart = serial.Serial("/dev/ttyUSB0", baudrate=57600, timeout=1)

# If using with Linux/Raspberry Pi and hardware UART:
uart = serial.Serial("/dev/ttyS0", baudrate=57600, timeout=1)

# If using with Linux/Raspberry Pi 3 with pi3-disable-bt
# uart = serial.Serial("/dev/ttyAMA0", baudrate=57600, timeout=1)

finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)

##################################################


def get_fingerprint():
    """Get a finger print image, template it, and see if it matches!"""
    print("Waiting for image...")
    while finger.get_image() != adafruit_fingerprint.OK:
        pass
    print("Templating...")
    if finger.image_2_tz(1) != adafruit_fingerprint.OK:
        return False
    print("Searching...")
    if finger.finger_search() != adafruit_fingerprint.OK:
        return False
    return True


# pylint: disable=too-many-branches
def get_fingerprint_detail():
    """Get a finger print image, template it, and see if it matches!
    This time, print out each error instead of just returning on failure"""
    print("Getting image...", end="")
    i = finger.get_image()
    if i == adafruit_fingerprint.OK:
        print("Image taken")
    else:
        if i == adafruit_fingerprint.NOFINGER:
            print("No finger detected")
        elif i == adafruit_fingerprint.IMAGEFAIL:
            print("Imaging error")
        else:
            print("Other error")
        return False

    print("Templating...", end="")
    i = finger.image_2_tz(1)
    if i == adafruit_fingerprint.OK:
        print("Templated")
    else:
        if i == adafruit_fingerprint.IMAGEMESS:
            print("Image too messy")
        elif i == adafruit_fingerprint.FEATUREFAIL:
            print("Could not identify features")
        elif i == adafruit_fingerprint.INVALIDIMAGE:
            print("Image invalid")
        else:
            print("Other error")
        return False

    print("Searching...", end="")
    i = finger.finger_fast_search()
    # pylint: disable=no-else-return
    # This block needs to be refactored when it can be tested.
    if i == adafruit_fingerprint.OK:
        print("Found fingerprint!")
        return True
    else:
        if i == adafruit_fingerprint.NOTFOUND:
            print("No match found")
        else:
            print("Other error")
        return False


# pylint: disable=too-many-statements
def enroll_finger(location):
    """Take a 2 finger images and template it, then store in 'location'"""
    for fingerimg in range(1, 3):
        if fingerimg == 1:
            print("Place finger on sensor...", end="")
        else:
            print("Place same finger again...", end="")

        while True:
            i = finger.get_image()
            if i == adafruit_fingerprint.OK:
                print("Image taken")
                break
            if i == adafruit_fingerprint.NOFINGER:
                print(".", end="")
            elif i == adafruit_fingerprint.IMAGEFAIL:
                print("Imaging error")
                return False
            else:
                print("Other error")
                return False

        print("Templating...", end="")
        i = finger.image_2_tz(fingerimg)
        if i == adafruit_fingerprint.OK:
            print("Templated")
        else:
            if i == adafruit_fingerprint.IMAGEMESS:
                print("Image too messy")
            elif i == adafruit_fingerprint.FEATUREFAIL:
                print("Could not identify features")
            elif i == adafruit_fingerprint.INVALIDIMAGE:
                print("Image invalid")
            else:
                print("Other error")
            return False

        if fingerimg == 1:
            print("Remove finger")
            time.sleep(1)
            while i != adafruit_fingerprint.NOFINGER:
                i = finger.get_image()

    print("Creating model...", end="")
    i = finger.create_model()
    if i == adafruit_fingerprint.OK:
        print("Created")
    else:
        if i == adafruit_fingerprint.ENROLLMISMATCH:
            print("Prints did not match")
        else:
            print("Other error")
        return False

    print("Storing model #%d..." % location, end="")
    i = finger.store_model(location)
    if i == adafruit_fingerprint.OK:
        print("Stored")
    else:
        if i == adafruit_fingerprint.BADLOCATION:
            print("Bad storage location")
        elif i == adafruit_fingerprint.FLASHERR:
            print("Flash storage error")
        else:
            print("Other error")
        return False

    return True


def save_fingerprint_image(filename):
    """Scan fingerprint then save image to filename."""
    while finger.get_image():
        pass

    # let PIL take care of the image headers and file structure
    from PIL import Image  # pylint: disable=import-outside-toplevel

    img = Image.new("L", (256, 288), "white")
    pixeldata = img.load()
    mask = 0b00001111
    result = finger.get_fpdata(sensorbuffer="image")
    # this block "unpacks" the data received from the fingerprint
    #   module then copies the image data to the image placeholder "img"
    #   pixel by pixel.  please refer to section 4.2.1 of the manual for
    #   more details.  thanks to Bastian Raschke and Danylo Esterman.
    # pylint: disable=invalid-name
    x = 0
    # pylint: disable=invalid-name
    y = 0
    # pylint: disable=consider-using-enumerate
    for i in range(len(result)):
        pixeldata[x, y] = (int(result[i]) >> 4) * 17
        x += 1
        pixeldata[x, y] = (int(result[i]) & mask) * 17
        if x == 255:
            x = 0
            y += 1
        else:
            x += 1

    if not img.save(filename):
        return True
    return False


##################################################
def gg():
    session=1
    r = [0] * 11
    while session==1:
        if get_fingerprint():
            print("Detected #", finger.finger_id, "with confidence", finger.confidence)

            if finger.finger_id == 1:
                print("Name     : Zoya Pathan")
                print("Roll no  : 1")
                print("Enroll no: ADT23SOCB1374")
                r[1]+=1
           
            elif finger.finger_id == 2:
                print("Name     : Adil Deokar")
                print("Roll no  : 2")
                print("Enroll no: ADT23SOCB0049")
                r[2]+=1
            elif finger.finger_id == 3:
                print("Name     : Prem Maradiya")
                print("Roll no  : 3")
                print("Enroll no: ADT23SOCB0799")
                r[3]+=1
            elif finger.finger_id == 4:
                print("Name     : Dhruv Shah")
                print("Roll no  : 4")
                print("Enroll no: ADT23SOCB0359")
                r[4]+=1
            elif finger.finger_id == 5:
                print("Name     : Mohit Pokale")
                print("Roll no  : 5")
                print("Enroll no: ADT23SOCB0049")
                r[5]+=1
            elif finger.finger_id == 6:
                print("Name     : Aman Khan")
                print("Roll no  : 6")
                print("Enroll no: ADT23SOCB0114")
                r[6]+=1
            elif finger.finger_id == 7:
                print("Name     : Anurag Dube")
                print("Roll no  : 7")
                print("Enroll no: ADT23SOCB1508")
                r[7]+=1
            elif finger.finger_id == 8:
                print("Name     : Pranav Bulbule")
                print("Roll no  : 8")
                print("Enroll no: ADT23SOCB0748")
                r[8]+=1
            elif finger.finger_id == 9:
                print("Name     : Baijunath Karvir")
                print("Roll no  : 9")
                print("Enroll no: ADT23SOCB0298")
                r[9]+=1
            elif finger.finger_id == 10:
                print("Name     : Sarthak Chakurkar")
                print("Roll no  : 10")
                print("Enroll no: ADT23SOCB0987")
                r[10]+=1
            else:
                print("Finger not found")
        print("1: continue");
        print("2: stop");
        session=int(input())
    print("--------------------")
    print("Present roll nos")
    for z in range(1,11,1):
        if(r[z]>=1):
            print(z)
    print("--------------------")
    print("Absent roll nos")
    for z in range(1,11,1):
        if(r[z]==0):
            print(z)

def get_num(max_number):
    """Use input() to get a valid number from 0 to the maximum size
    of the library. Retry till success!"""
    i = -1
    while (i > max_number - 1) or (i < 0):
        try:
            i = int(input("Enter ID # from 0-{}: ".format(max_number - 1)))
        except ValueError:
            pass
    return i

print("----------------")
print("ANTI PROXY ATTENDANCE SYSTEM")
print("----------------")

   
while True:
    print("----------------")
    if finger.read_templates() != adafruit_fingerprint.OK:
        raise RuntimeError("Failed to read templates")
    if finger.count_templates() != adafruit_fingerprint.OK:
        raise RuntimeError("Failed to read templates")
    if finger.read_sysparam() != adafruit_fingerprint.OK:
        raise RuntimeError("Failed to get system parameters")
    print("e) enroll student")
    print("f) Mark Attendance")
    print("d) delete print")
    print("s) save fingerprint image")
    print("r) reset library")
    print("q) quit")
    print("----------------")
    c = input("> ")

    if c == "e":
        enroll_finger(get_num(finger.library_size))
    if c == "f":
        print("---------------")
        print("Choose Subject")
        print("1- CEW")
        print("2- DT")
        sub= int(input())
        if sub == 1 :
            print("Place finger Mr Pranav Chippalkatti......")
            get_fingerprint()
            if finger.finger_id == 21:
                print("---------------")
                print("Success - Starting CEW attendance  ")
                print("---------------")
                gg()
            else:
                print ("enter CEW Teacher Fingerprint")
        if sub == 2 :
            print("Place finger Mr Charanjeet Barmi......")
            get_fingerprint()
            if finger.finger_id == 22:
                print("---------------")
                print("Success - Starting DT attendance  ")
                print("---------------")
                gg()
            else:
                print ("enter DT Teacher Fingerprint")

    if c == "d":
        if finger.delete_model(get_num(finger.library_size)) == adafruit_fingerprint.OK:
            print("Deleted!")
        else:
            print("Failed to delete")
    if c == "s":
        if save_fingerprint_image("fingerprint.png"):
            print("Fingerprint image saved")
        else:
            print("Failed to save fingerprint image")
    if c == "r":
        if finger.empty_library() == adafruit_fingerprint.OK:
            print("Library empty!")
        else:
            print("Failed to empty library")
    if c == "q":
        print("Ending class attendance ")
        endpin = int(input("End Attendance pin : "))
        if endpin == 4321:
            print("Success - ending class attendance  ")
            raise SystemExit
        else:
            print("Incorrect pin  ")
