import os
import glob
import time
import datetime
import threading
from rearender.utils import traverse_dir, render_media
from rearender.autogui import close_project
import beyond.Reaper


# start
program_start_time = time.time()

# config
tolerance_sec = 20

# IO folders
# [!] full path recommended
# path_indir = '/Users/username/.../data/signle_media/midi'
# path_outdir = '/Users/username/.../data/signle_media/audio'

path_indir = '/Users/Alex/Desktop/Uni/6. Semester/Bachelorarbeit/code/remi/inp/'
path_outdir = '/result_synthesized/' # this is /Users/Alex/AppData/Roaming/REAPER/ProjectTemplates/path_outdir/
# C:\Users\Alex\AppData\Roaming\REAPER\ProjectTemplates\result_synthesized


# list files
filelist = traverse_dir(
    path_indir, 
    is_pure=True, 
    is_sort=True)
num_files = len(filelist)
print('num files:', num_files)

# initialize with False, so that project does not get reopened every time
already_open = False

# list files
for fidx in range(num_files):
    time.sleep(0.5)
    song_start_time = time.time()

    # set file
    filename = filelist[fidx]
    ext = filename.split('.')[-1]
    path_midi = os.path.join(path_indir, filename)
    path_audio = os.path.join(path_outdir, filename[:-len(ext)-1])

    # print
    print('({}/{}) - {}'.format(fidx, num_files, filename))
    print(' > audio:', path_audio)

    # synthesis
    render_media(path_midi, path_audio, bpm=120, already_open=already_open)
    already_open = True

    # runtime
    runtime = time.time() - song_start_time
    print(' > runtime', runtime)

    # should not be necessary anymore: see comment in utils.py
    # if runtime > tolerance_sec:
    #     # reopen project
    #     close_project(reopen=True)

# finished
print('\n===== Finished =====')
runtime = time.time() - program_start_time
print('Elapsed time:', str(datetime.timedelta(seconds=runtime)))
