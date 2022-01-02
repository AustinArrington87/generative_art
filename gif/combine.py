# Copyright Austin Arrington, 2022
# This script is for combining multiple GIFs, using numpy to stack thme 

import imageio
import numpy as np    

#Create reader object for the gif
gif1 = imageio.get_reader('/Users/Austin.Arrington/Desktop/ML/generated/slow.gif')
gif2 = imageio.get_reader('/Users/Austin.Arrington/Desktop/ML/generated/medium.gif')
gif3 = imageio.get_reader('/Users/Austin.Arrington/Desktop/ML/generated/fast.gif')

#If they don't have the same number of frame take the shorter
number_of_frame = min(gif1.get_length(), gif2.get_length(), gif3.get_length()) 

#Create writer object
new_gif = imageio.get_writer('output.gif')

for frame_number in range(number_of_frame):
    img1 = gif1.get_next_data()
    img2 = gif2.get_next_data()
    img3 = gif3.get_next_data()
    #here is the magic
    new_image1 = np.hstack((img1, img2, img3))
    new_image2 = np.hstack((img3, img2, img1))
    new_image3 = np.hstack((img1, img2, img3))
    new_image4 = np.vstack((new_image1, new_image2, new_image3))
    new_gif.append_data(new_image4)

gif1.close()
gif2.close()    
new_gif.close()
