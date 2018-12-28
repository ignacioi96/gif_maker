#!/usr/bin/env python
# coding: utf-8

# In[8]:


from cv2 import VideoCapture, waitKey, imshow
import numpy as np
from imageio import mimsave
from datetime import datetime, date


# In[2]:


file_path = input("File: ")


# In[10]:


start_time = int(input("Enter start time (in seconds): "))*1000
end_time = int(input("Enter end time (in seconds): "))*1000


# In[12]:


cap = VideoCapture(file_path)

output_gif = []


i = start_time

size_percentage = 0.2
width = 50
height = 500

# video capture set start time
cap.set(0, start_time)

# set the width of the gif
cap.set(3, width)

# set the height of the gif
cap.set(4, height)

while(cap.isOpened() and cap.get(0) <= end_time):
    print(i)
    ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2GRAY)
    output_gif.append(frame)
    imshow('frame', frame)
    if(waitKey(1) & 0xFF == ord('q')):
        break
    i +=1

output_file = 'title-' + (str(datetime.today()).split(' ')[0]) + '.gif'
mimsave(output_file, output_gif)
# cv2.destroyAllWindows()
cap.release()


# In[ ]:




