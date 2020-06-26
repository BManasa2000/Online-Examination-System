'''
This is the code for video streaming using flask.

Resource used: https://github.com/yushulx/web-camera-recorder

Code developed by:
Manasa Reddy Bollavaram
'''
import cv2
import threading

class RecordingThread (threading.Thread):
    def __init__(self, name, camera):
        threading.Thread.__init__(self)
        self.name = name
        self.isRunning = True

        self.cap = camera
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        self.out = cv2.VideoWriter('/static/video3.avi',fourcc, 20.0, (640,480))

    def run(self):
        while self.isRunning:
            ret, frame = self.cap.read()
            if ret:
                self.out.write(frame)

        self.out.release()

    def stop(self):
        self.isRunning = False

    def __del__(self):
        self.out.release()

class VideoCamera(object):
    def __init__(self):
        # Open a camera
        self.cap = cv2.VideoCapture(0)
      
        # Initialize video recording environment
        self.is_record = False
        self.out = None

        # Thread for recording
        self.recordingThread = None
    
    def __del__(self):
        self.cap.release()
    
    def get_frame(self):
        ret, frame = self.cap.read()

        if ret:
            ret, jpeg = cv2.imencode('.jpg', frame)

            # Record video
            # if self.is_record:
            #     if self.out == None:
            #         fourcc = cv2.VideoWriter_fourcc(*'MJPG')
            #         self.out = cv2.VideoWriter('./static/video.avi',fourcc, 20.0, (640,480))
                
            #     ret, frame = self.cap.read()
            #     if ret:
            #         self.out.write(frame)
            # else:
            #     if self.out != None:
            #         self.out.release()
            #         self.out = None  

            return jpeg.tobytes()
      
        else:
            return None

    def start_record(self):
        self.is_record = True
        self.recordingThread = RecordingThread("Video Recording Thread", self.cap)
        self.recordingThread.start()

    def stop_record(self):
        self.is_record = False

        if self.recordingThread != None:
            self.recordingThread.stop()

#from time import time
#import numpy as numpy
#import os
#import cv2
#from flask import request
#
#class Camera(object):
#	def __init__(self):
#		filename = 'student.mp4'
#		frames_per_second = 24.0
#		res = '720p'
#		def change_res(cap, width, height):
#		    cap.set(3, width)
#		    cap.set(4, height)
#
#		# Standard Video Dimensions Sizes
#		STD_DIMENSIONS =  {
#		    "480p": (640, 480),
#		    "720p": (1280, 720),
#		    "1080p": (1920, 1080),
#		    "4k": (3840, 2160),
#		}
#
#
#		# grab resolution dimensions and set video capture to it.
#		def get_dims(cap, res='1080p'):
#		    width, height = STD_DIMENSIONS["480p"]
#		    if res in STD_DIMENSIONS:
#		        width,height = STD_DIMENSIONS[res]
#		    ## change the current caputre device
#		    ## to the resulting resolution
#		    change_res(cap, width, height)
#		    return width, height
#
#		# Video Encoding, might require additional installs
#		# Types of Codes: http://www.fourcc.org/codecs.php
#		VIDEO_TYPE = {
#		    'avi': cv2.VideoWriter_fourcc(*'XVID'),
#		    #'mp4': cv2.VideoWriter_fourcc(*'H264'),
#		    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
#		}
#
#		def get_video_type(filename):
#		    filename, ext = os.path.splitext(filename)
#		    if ext in VIDEO_TYPE:
#		      return  VIDEO_TYPE[ext]
#		    return VIDEO_TYPE['avi']
#		
#		self.cap=cv2.VideoCapture(0)
#		self.out=cv2.VideoWriter(filename, get_video_type(filename), 25, get_dims(self.cap, res))
#
#	def stop_video(self):	
#		self.cap.release()
#		self.out.release()
#		cv2.destroyAllWindows()
#		
#	
#	def get_frame(self):
#		while True:
#			ret,frame= self.cap.read()
#			if request.path=="/solve" & ret:
#				self.out.write(frame)
#				ret1,jpeg=cv2.imencode('jpg',frame)
#			else:
#				break
#		return jpeg.tobytes()

