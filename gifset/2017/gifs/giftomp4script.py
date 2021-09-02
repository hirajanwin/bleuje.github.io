import os
import cv2
import glob
import moviepy.editor as mp

filenames = glob.glob('*.gif');
'''
for f in filenames:
    string = 'ffmpeg -i '
    file_path = f
    print(f)
    print(f)
    
    string += file_path + ' -y' # the -y just doesn't ask for confirmation on overwriting existing files

    if not os.path.exists(file_path):
        continue

        
    # this section basically caps the gif's height or width to a maximum of 1080px, you can change this
    # also feel free to mess around with brightness, saturation and contrast, default values are 1.0
    vid = cv2.VideoCapture(file_path)
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    scale = max(height, width)

    if scale > 1080:
        if width > height:
            string += r' -y -vcodec libx264 -crf 4 -pix_fmt yuv420p -vf eq=gamma=1.05:saturation=1.1:contrast=1.1:scale=1080:-1 '
        else:
            string += r' -y -vcodec libx264 -crf 4 -pix_fmt yuv420p -vf eq=gamma=1.05:saturation=1.1:contrast=1.1:scale=-1:1080 '
    else:
        string += r' -y -vcodec libx264 -crf 4 -pix_fmt yuv420p -vf eq=gamma=1.05:saturation=1.1:contrast=1.1 '

    # string += r'C:\outputfolder\video'+num+r'.mp4'
    string += f[:-4] + '.mp4'

    os.system(string)
    
    print(string)
    
    break;
    '''
for f in filenames:
	clip = mp.VideoFileClip(f)
	clip.write_videofile(f[:-4] + '.mp4')
	print(f)
