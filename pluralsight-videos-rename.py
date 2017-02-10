#!/usr/bin/env python
# coding=utf-8

from __future__ import print_function
from sys import argv, exit
from glob import glob
from json import loads
from os import rename, mkdir
from os.path import exists


WORKING_DIRECTORY = '.'


def rename_videos_same_starting_name(videos):
    new_videos = []
    for video_tittle in videos:
        if ' ' in video_tittle:
            new_video_tittle = video_tittle.replace(' (', '_').replace(')', '')
            rename(video_tittle, new_video_tittle)
            new_videos.append(new_video_tittle)
        else:
            new_videos.append(video_tittle)
    return sorted(new_videos)


def rename_videos_as_they_should_be_named(tittles, videos):
    for i in range(len(tittles)):
        num, module, name = tittles[i].split(u'\x96')
        num = num.strip()
        module = module.strip().replace(' ', '_')
        name = name.strip().replace(' ', '_')

        name = num + "_" + name + '.webm'

        save_dir = WORKING_DIRECTORY + module

        if not exists(save_dir):
            mkdir(save_dir)

        rename(videos[i], save_dir + '/' + name)


def main():
    global WORKING_DIRECTORY

    if 2 < len(argv) < 3:
        working_directory = argv[1]
    else:
        working_directory = WORKING_DIRECTORY

    if working_directory[-1] != '/':
        working_directory += '/'
        WORKING_DIRECTORY = working_directory

    tittles = loads(open(glob(working_directory + '*.json')[0]).read())
    videos = rename_videos_same_starting_name(glob(working_directory + '*.webm'))

    if len(tittles) != len(videos):
        print("Quantity of tittles and videos, are different")
        exit(1)

    rename_videos_as_they_should_be_named(tittles=tittles, videos=videos)


if __name__ == '__main__':
    main()
