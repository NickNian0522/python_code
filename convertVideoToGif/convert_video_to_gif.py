from moviepy.editor import *
import os
#https://blog.csdn.net/ucsheep/article/details/84387092
CONST_FILE_NAME = os.getcwd()+os.sep+"demo.mp4";
CONST_FILE_OUTPUT_imageio  = os.getcwd()+os.sep+"demo.gif";
print(CONST_FILE_NAME)
vedioClip = VideoFileClip(CONST_FILE_NAME,audio=False)
final_clip=vedioClip.to_RGB();
final_clip.write_gif(CONST_FILE_OUTPUT_imageio,fps=vedioClip.fps);