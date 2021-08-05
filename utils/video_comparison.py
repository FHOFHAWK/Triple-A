import moviepy.editor as mp
import hashlib
import os
from core.models import Lesson
from video_photo_loader.models import LessonVideo


def file_unique(media_folder, file_name, lesson_id):
    video = mp.VideoFileClip(media_folder + file_name)
    video.audio.write_audiofile(media_folder + file_name + ".wav", bitrate='50k')
    with open(media_folder + file_name + ".wav", "rb") as f:
        new_hashed_b64 = (hashlib.md5(f.read())).hexdigest()
        os.remove(media_folder + file_name + ".wav")
        os.remove(media_folder + file_name)

        hashes = []
        videos = LessonVideo.objects.all()
        for video in videos:
            hashes.append(video.video_hash)

        if new_hashed_b64 in hashes:
            return False
        else:
            LessonVideo.objects.create(video_hash=new_hashed_b64)
            lesson = Lesson.objects.get(id=lesson_id)
            lesson.video_uploaded = True
            lesson.save()
            return True
