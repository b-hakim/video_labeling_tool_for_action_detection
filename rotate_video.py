import glob

import numpy

import cv2
import os


def rotate_video(list_video_path):
    with open(list_video_path) as fw:
        c=0
        for vid_path in fw:
            vid_path = vid_path.strip()
            try:
                cap = cv2.VideoCapture(vid_path)
                fourcc = cv2.VideoWriter_fourcc(*'XVID')
                vid_path2 = "/home/bassel/data/office-actions/office_actions_19/side_view/s_{:03}.mp4".format(c)
                c+=1
                out = None

                while True:
                    has_frame, frame = cap.read()

                    if not has_frame:
                        break

                    frame = numpy.rot90(frame, 2)

                    if out is None:
                        h, w = frame.shape[:2]
                        out = cv2.VideoWriter(vid_path2, fourcc, 30.0, (w, h))

                    out.write(frame)
                    # cv2.imshow("", frame)

                    # cv2.waitKey(1)
                out.release()
                cap.release()
                print(vid_path + " deleted")
                os.remove(vid_path)
                # os.rename(vid_path2, vid_path)
            except:
                print("error occurred at path " + vid_path)


def rem_audio_video(list_video_path, out_dir, front_side, initialize_counter=0):
    with open(list_video_path) as fw:
        c = initialize_counter

        for vid_path in fw:
            vid_path = vid_path.strip()

            try:
                cap = cv2.VideoCapture(vid_path)
                fourcc = cv2.VideoWriter_fourcc(*'XVID')
                vid_path2 = out_dir + front_side +"_{:03}.mp4".format(c)

                out = None

                while True:
                    has_frame, frame = cap.read()

                    if not has_frame:
                        break

                    if out is None:
                        h, w = frame.shape[:2]
                        out = cv2.VideoWriter(vid_path2.strip(), fourcc, 30.0, (w, h))

                    out.write(frame)
                    # cv2.imshow("", frame)

                    # cv2.waitKey(1)
                out.release()
                cap.release()
                print(vid_path + " deleted")
                os.remove(vid_path)
                c += 1
            except:
                print("error occurred at path " + vid_path)
            # os.rename(vid_path2, vid_path)


def rename_files(dir, start, end, new_start):
    new_name_start = new_start

    for i in range(start, end+1):
        file_name = os.path.join(dir, "s_{:03}.mp4".format(i))
        file_new_name = os.path.join(dir, "s_{:03}.mp4".format(new_name_start))
        new_name_start += 1

        os.rename(file_name, file_new_name)


def order_files(dir, char):
    files = glob.glob(dir+"*.mp4")

    for file_name in files:
        file_new_name = file_name.replace(".", "_2.")
        os.rename(file_name, file_new_name)

    files = glob.glob(dir+"*.mp4")
    files.sort()
    counter = 0

    for file_name in files:
        file_new_name = dir+char+"_{:03}".format(counter)
        counter += 1
        os.rename(file_name, file_new_name)


def add_mp4_extension(dir):
    files = glob.glob(dir+"/*")

    for file_name in files:
        file_new_name = file_name+".mp4"
        os.rename(file_name, file_new_name)



if __name__ == '__main__':
    # rotate_video("/home/bassel/data/office-actions/to_rotate")
    # rotate_video("/home/bassel/data/office-actions/tt")
    # rem_audio_video("/home/bassel/data/office-actions/rem_audio", "/home/bassel/data/office-actions/office_actions_19/side_view/", 's', 42)
    # rem_audio_video("/home/bassel/data/office-actions/rem_audio2", "/home/bassel/data/office-actions/office_actions_19/front_view/vds/", 'f')
    # rename_files("/home/bassel/data/office-actions/office_actions_19/side_view/",
    #              24, 41, 80)
    # order_files("/home/bassel/data/office-actions/office_actions_19/front_view/", "f")
    # order_files("/home/bassel/data/office-actions/office_actions_19/side_view/", "s")
    # add_mp4_extension("/home/bassel/data/office-actions/office_actions_19/side_view/")
    pass
