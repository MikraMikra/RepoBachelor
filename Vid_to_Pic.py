from moviepy.editor import VideoFileClip
from moviepy.video.VideoClip import ImageClip
import os
import argparse
from PIL import Image


def convert_video_to_images(input_video, output_folder, image_size):
    # Create the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # load the video
    video_clip = VideoFileClip(input_video)

    # Iterate over every second of the video and save an image
    for i, frame in enumerate(video_clip.iter_frames(fps=1, dtype='uint8')):
        image_file = os.path.join(output_folder, f'frame_{i + 1}.jpg')
        img_clip = ImageClip(frame)

        if image_size:
            img_clip = img_clip.resize((image_size[0], image_size[1]))

        img_clip.save_frame(image_file, withmask=False)

    # close the video
    video_clip.close()


def main():
    parser = argparse.ArgumentParser(description='Convert a video to images.')
    parser.add_argument('--source', required=True, help='Path to the input video file.')
    parser.add_argument('--output', required=True, help='Path to the output folder for images.')
    parser.add_argument('--size', default=None, type=str,
                        help='Size of the output images (widthxheight). Example: 640x480')

    args = parser.parse_args()

    image_size = None
    if args.size:
        image_size = tuple(map(int, args.size.split('x')))

    convert_video_to_images(args.source, args.output, image_size)


if __name__ == "__main__":
    main()