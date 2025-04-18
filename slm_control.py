import numpy as np

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

import wx
import threading
import time
from PIL import Image
from numpy import asarray

EVT_NEW_IMAGE = wx.PyEventBinder(wx.NewEventType(), 0)


class ImageEvent(wx.PyCommandEvent):
    def __init__(self, eventType=EVT_NEW_IMAGE.evtType[0], id=0):
        wx.PyCommandEvent.__init__(self, eventType, id)
        self.img = None
        self.color = False
        self.oldImageLock = None
        self.eventLock = None


class SLMframe(wx.Frame):
    """Frame used to display full screen image."""

    def __init__(self, x0, resX, resY, name, isImageLock=True):
        style = wx.BORDER_NONE | wx.STAY_ON_TOP
        self.isImageLock = isImageLock
        # Set the frame to the position and size of the target monitor
        super().__init__(None, -1, f"{name}", pos=(x0, 0), size=(resX, resY), style=style)
        self.img = wx.Image(2, 2)
        self.bmp = self.img.ConvertToBitmap()
        self.clientSize = self.GetClientSize()
        # Update the image upon receiving an event EVT_NEW_IMAGE
        self.Bind(EVT_NEW_IMAGE, self.UpdateImage)
        # Set full screen
        # self.ShowFullScreen(not self.IsFullScreen(), wx.FULLSCREEN_ALL)
        self.SetFocus()

    def InitBuffer(self):
        self.bmp = self.img.Scale(self.clientSize[0], self.clientSize[1]).ConvertToBitmap()
        dc = wx.ClientDC(self)
        dc.DrawBitmap(self.bmp, 0, 0)

    def UpdateImage(self, event):
        try:
            self.eventLock = event.eventLock
        except AttributeError:
            time.sleep(1)
            self.eventLock = event.eventLock
        self.img = event.img
        self.InitBuffer()
        self.ReleaseEventLock()

    def ReleaseEventLock(self):
        if self.eventLock:
            if self.eventLock.locked():
                self.eventLock.release()


class SLMdisplay:
    """Interface for sending images to the display frame."""

    def __init__(self, x0s, resXs, resYs, names, isImageLock=True):
        self.isImageLock = isImageLock
        self._x0s = x0s
        self._resXs = resXs
        self._resYs = resYs
        self._names = names
        # Create the thread in which the window app will run
        # It needs its thread to continuously refresh the window
        self.vt = videoThread(self)
        self.eventLock = threading.Lock()
        if self.isImageLock:
            self.eventLock = threading.Lock()

    def create_update_event(self, array):
        """
        Update the SLM monitor with the supplied array.
        Note that the array is not the same size as the SLM resolution,
        the image will be deformed to fit the screen.
        """
        # create a wx.Image from the arrays
        h, w = array.shape[0], array.shape[1]
        data = array.tobytes()
        img = wx.ImageFromBuffer(width=w, height=h, dataBuffer=data)

        # Create the event
        event = ImageEvent()
        event.img = img
        event.eventLock = self.eventLock

        # Wait for the lock to be released (if isImageLock = True)
        # to be sure that the previous image has been displayed
        # before displaying the next one - it avoids skipping images
        time.sleep(0.1)
        
        if self.isImageLock:
            event.eventLock.acquire()

        return event

    def generate_img(self, path, x_pos, y_pos):
        """generate a black canvas and paste photo"""
        # print(path)
        img = Image.open(path)
        print(img)
        array = asarray(img)
        print(array)
        bg_img = Image.new('L', (1920, 1152), 0)
        print(bg_img)
        print(x_pos)
        print(y_pos)
        img = Image.fromarray(array, 'L')
        print(img)
        bg_img.paste(img, (x_pos, y_pos))
        return bg_img


    def updateArray(self, slm_name, array):
        #put the array on the SLM

#         #reads an RGB image so need to repeat 3 times
#         aray = np.repeat(array[...,None],3 ,axis = -1)

#         #data type needs to be uint8
#         array = array.astype('uint8')
        array = self.make_right_array(array)
    
        event = self.create_update_event(array)
        self.vt.frames[slm_name].AddPendingEvent(event)
        
    def make_right_array(self, temp):
        #reads an RGB image so need to repeat 3 times
        temp = np.repeat(temp[...,None],3 ,axis = -1)

        #data type needs to be uint8
        temp = temp.astype('uint8')
        # temp.dtype
        
        return temp


class videoThread(threading.Thread):
    """Run the MainLoop as a thread. Access the frame with self.frame."""

    def __init__(self, parent, autoStart=True):
        super().__init__()
        self.parent = parent
        # Set as deamon so that it does not prevent the main program from exiting
        self.setDaemon(True)
        self.start_orig = self.start
        self.start = self.start_local
        self.frames = {}  # to be defined in self.run
        self.lock = threading.Lock()
        self.lock.acquire()  # lock until variables are set
        if autoStart:
            self.start()  # automatically start thread on init

    def run(self):
        self.app = wx.App()
        for i in range(len(self.parent._x0s)):
            frame = SLMframe(self.parent._x0s[i], self.parent._resXs[i], self.parent._resYs[i],
                             self.parent._names[i])
            frame.Show(True)
            self.frames[self.parent._names[i]] = frame
        self.lock.release()
        self.app.MainLoop()

    def start_local(self):
        self.start_orig()
        # Use lock to wait for the functions to get defined
        self.lock.acquire()




# if __name__=='__main__':
#     # meadowlark mode generator
#     slm_w_1 = int(1920) / 2  # 1920
#     slm_h_1 = int(1152) / 2  # 1152
#
#     # initialize the display
#     slm1 = SLMdisplay([2560],
#                       [slm_w_1],
#                       [slm_h_1],
#                       ['SLM1'],
#                       isImageLock=False)
#     path = r'D:\Oxford_Postdoc\Lab_code\SLM_control/output_image_100x100.png'

    # bg_array = slm1.generate_img(path, 10, 20)

    # slm1.updateArray('SLM1', bg_array)