import time

from datetime import datetime

import cv2 as cv

import numpy as np

import smtplib

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

from email.mime.base import MIMEBase

from email import encoders

import winsound

import os
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import cv2
from twilio.rest import Client 
# camera_port = 0
# ramp_frames = 30
# camera = cv2.VideoCapture(camera_port)
# def get_image():

#     ret, im = camera.read()
#     return im

# for i in range(ramp_frames):
#     temp = get_image()
# print("Taking image...")

# camera_capture = get_image()
# file = "ravi.png"

# cv2.imwrite(file, camera_capture)
# del (camera)
def mail():
	subject = "An email with attachment from Python"
	body = "This is an email with attachment sent from Python"
	sender_email = " "
	receiver_email = " "
	password = ""

	# Create a multipart message and set headers
	message = MIMEMultipart()
	message["From"] = sender_email
	message["To"] = receiver_email
	message["Subject"] = subject

	# message["Bcc"] = receiver_email  # Recommended for mass emails
	# Add body to email
	message.attach(MIMEText(body, "plain"))

	filename = "ravi.png"  # In same directory as script

	# Open PDF file in binary mode
	with open(filename, "rb") as attachment:
	    part = MIMEBase("application", "octet-stream")
	    part.set_payload(attachment.read())    
	encoders.encode_base64(part)
	part.add_header(
	    "Content-Disposition",
	    f"attachment; filename= {filename}",
	)
	message.attach(part)
	text = message.as_string()
	# Log in to server using secure context and send email
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
	    server.login(sender_email, password)
	    server.sendmail(sender_email, receiver_email, text)
mail()
class MotionDetectorInstantaneous():

    def onChange(self, val):  # callback when the user change the detection threshold

        self.threshold = val

 

    def __init__(self, threshold=8, doRecord=True, showWindows=True):

        self.writer = None

        self.font = None

        self.doRecord = doRecord  # Either or not record the moving object

        self.show = showWindows  # Either or not show the 2 windows

        self.frame = None

 

        self.capture = cv.VideoCapture(0)

        _, self.frame = self.capture.read()

    

        self.height, self.width = self.frame.shape[:2]

 

        if doRecord:

            self.initRecorder()

        self.frame1gray = cv.cvtColor(self.frame, cv.COLOR_BGR2GRAY)

 

        # Will hold the thresholded result

        self.res = np.zeros((self.height, self.width), dtype=np.uint8)

 

        self.frame2gray = np.zeros((self.height, self.width), dtype=np.uint8)  # Gray frame at t

 

        self.nb_pixels = self.width * self.height

        self.threshold = threshold

        self.isRecording = False

        self.trigger_time = 0  # Hold timestamp of the last detection

 

        if showWindows:

            cv.namedWindow("Image")

            cv.createTrackbar("Detection treshold: ", "Image", self.threshold, 100, self.onChange)

 

    def initRecorder(self):  # Create the recorder

        codec = cv.VideoWriter_fourcc('M', 'J', 'P', 'G')  # ('W', 'M', 'V', '2')

        self.writer = cv.VideoWriter(filename=datetime.now().strftime("%b-%d_%H_%M_%S") + ".avi", fourcc=codec, fps=5,

                                     frameSize=(self.width, self.height), isColor=True)

        #cv.VideoWriter(os.path.join(path, self.writer), self.frame)

        # FPS set to 5 because it seems to be the fps of my cam but should be ajusted to your needs

        self.font = cv.FONT_HERSHEY_SIMPLEX  # Creates a font

 

    def run(self):

        started = time.time()

        while True:

           

            _, curframe = self.capture.read() 

            instant = time.time()  # Get timestamp of the frame

            self.processImage(curframe)  # Process the image

            if not self.isRecording:

                if self.somethingHasMoved():

                    self.trigger_time = instant  # Update the trigger_time

                    if instant > started + 5:  # Wait 5 second after the webcam start for luminosity adjusting etc..

                        print(datetime.now().strftime("%b %d, %H:%M:%S"), "Something is moving !")

                        if self.doRecord:  # set isRecording=True only if we record a video

                            self.isRecording = True          #65

                            
                            for i in range(3):
                                return_value,image=self.capture.read()   
                            freq = 1000
                            duration = 1000 
                            winsound.Beep(freq, duration)

            else:

                if instant >= self.trigger_time + 20:  # Record during 10 seconds

                    print(datetime.now().strftime("%b %d, %H:%M:%S"), "Stop recording")

                    self.isRecording = False

 

                else:

                    cv.putText(curframe, datetime.now().strftime("%b %d, %H:%M:%S"), (25, 30), self.font, 1, 1, 2, 8,

                               0)  # Put date on the frame

                    self.writer.write(curframe)  # Write the frame

 

            if self.show:

                cv.imshow("Image", curframe)

               

                cv.imshow("Res", self.res)

            self.frame1gray = self.frame2gray

            c = cv.waitKey(1) % 0x100

            if c == 27 or c == 10:  # Break if user enters 'Esc'.

                break

 

    def processImage(self, frame):

        self.frame2gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)

# Remove the noise and do the threshold
        self.res = cv.blur(self.res, (5, 5))
        self.res = cv.morphologyEx(self.res, cv.MORPH_OPEN, (5, 5))
        self.res = cv.morphologyEx(self.res, cv.MORPH_CLOSE, (5, 5))
        _, self.res = cv.threshold(self.res, 10, 255, cv.THRESH_BINARY_INV)
           

         

    def somethingHasMoved(self):
        nb = 0  # Will hold the number of black pixels
        for x in range(self.height):  # Iterate the hole image
            for y in range(self.width):
                if self.res[x, y] == 0.0:  # If the pixel is black keep it
                    nb += 1
        avg = (nb * 100.0) / self.nb_pixels  # Calculate the average of black pixel in the image
        if avg > self.threshold:  # If over the ceiling trigger the alarm
            return True
        else:
            return False

  
# Your Account Sid and Auth Token from twilio.com / console 
    account_sid = 'AC3a846e5983cc3d62b4c303813b605241'
    auth_token = 'd66ca53f3f3ada42adf222a420a70fda'
      
    # client = Client(account_sid, auth_token) 
      
    ''' Change the value of 'from' with the number  
    received from Twilio and the value of 'to' 
    with the number in which you want to send message.'''
    message = client.messages.create( 
                                  from_='+12056276621', 
                                  body ='hello ur motion is captured', 
                                  to ='+919533558978')
    print(message.sid) 

 

if __name__ == "__main__":

    detect = MotionDetectorInstantaneous(doRecord=True)

detect.run()




