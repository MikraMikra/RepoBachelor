#req: moviepy

from moviepy.editor import VideoFileClip
import os
import argparse

def convert_video_to_images(input_video, output_folder):
    # Create the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # load the video
    video_clip = VideoFileClip(input_video)

    # Iterate over every second of the video and save an image
    for i, frame in enumerate(video_clip.iter_frames(fps=1, dtype='uint8')):
        image_file = os.path.join(output_folder, f'frame_{i + 1}.jpg')
        video_clip.save_frame(image_file, t=i)

    # close the video
    video_clip.close()


def main():
    parser = argparse.ArgumentParser(description='Convert a video to images.')
    parser.add_argument('--source', required=True, help='Path to the input video file.')
    parser.add_argument('--output', required=True, help='Path to the output folder for images.')

    args = parser.parse_args()

    convert_video_to_images(args.source, args.output)

main()
