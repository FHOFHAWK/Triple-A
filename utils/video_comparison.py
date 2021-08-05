import moviepy.editor as mp
import os
from base64 import b64encode


def separator(video_file):
    video = mp.VideoFileClip(video_file)
    return video.audio.write_audiofile("../media/"+video_file+".wav", bitrate='50k')


def file_unique(input_video_file, db_path):
    #for i in db_path:             для перебора hash бд
    # vse 4to nije pod for
    separator(input_video_file)
    f = open("../media/" + input_video_file + ".wav", "rb")
    enc1 = b64encode(f.read())
    f.close()

    f = open("db next hash", "rb")
    enc2 = b64encode(f.read())
    f.close()
    os.remove("../media/" + input_video_file + ".wav")
    if hash(enc1) == hash(enc2):
        return False
    else:
        return True


def add_hash_to_base(input_video_file):
    separator(input_video_file)
    f = open("../media/"+input_video_file+".wav", "rb")
    enc = b64encode(f.read())
    f.close()
    #write enc hash to base

    os.remove("../media/"+input_video_file+".wav")
    return 'Success'


if __name__ == "__main__":
    add_hash_to_base('example1.mp4')
