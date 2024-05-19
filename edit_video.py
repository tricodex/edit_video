import os
from datetime import datetime
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip
from moviepy.video.fx.all import speedx, crop

def get_video_files(directory):
    """
    Returns a list of video file paths from the specified directory.
    """
    supported_formats = ('.mp4', '.avi', '.mov', '.mkv', '.flv')
    return [os.path.join(directory, file) for file in os.listdir(directory) if file.lower().endswith(supported_formats)]

def scale_video(video, target_size):
    """
    Scales the video to match the target size while maintaining the aspect ratio.
    """
    return video.resize(newsize=target_size)

def apply_slow_motion(video, factor):
    """
    Applies slow motion to the video by the given factor.
    """
    return speedx(video, factor=factor)

def crop_video(video, x1, y1, x2, y2):
    """
    Crops the video to the specified region.
    """
    return crop(video, x1=x1, y1=y1, x2=x2, y2=y2)

def trim_video(video, start_time, end_time):
    """
    Trims the video to the specified start and end times.
    """
    return video.subclip(start_time, end_time)

def concatenate_videos(video_infos, output_path, audio_path=None):
    """
    Concatenates videos from the list of video paths and saves the output video.
    Optionally adds an audio track and applies slow motion or cropping.
    """
    if not video_infos:
        raise ValueError("No video information provided")

    # Load and process each video
    clips = []
    for info in video_infos:
        video = VideoFileClip(info['path'])
        if 'start_time' in info and 'end_time' in info:
            video = trim_video(video, info['start_time'], info['end_time'])
        if 'crop' in info:
            video = crop_video(video, *info['crop'])
        if 'slow_motion_factor' in info:
            video = apply_slow_motion(video, info['slow_motion_factor'])
        if clips:
            video = scale_video(video, clips[0].size)
        clips.append(video)

    # Concatenate the video clips
    final_clip = concatenate_videoclips(clips)

    # Add audio if provided
    if audio_path:
        audio_clip = AudioFileClip(audio_path)
        final_clip = final_clip.set_audio(audio_clip)

    # Write the output video to the specified path
    final_clip.write_videofile(output_path, codec="libx264")

def generate_output_path(base_dir, prefix="final_video"):
    """
    Generates a unique output file path using the current date and time.
    """
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{prefix}_{current_time}.mp4"
    return os.path.join(base_dir, filename)

def main():
    # Define the input video information (path, start_time, end_time, crop, slow_motion_factor)
    video_infos = [
        {'path': 'path/to/video1.mp4', 'start_time': 0, 'end_time': 10, 'crop': (0, 0, 320, 240), 'slow_motion_factor': 0.5},
        {'path': 'path/to/video2.mp4', 'start_time': 5, 'end_time': 15}
    ]

    # Define the output base directory and optional audio path
    output_base_dir = "output"
    audio_path = "path/to/audio.mp3"  # Set to None if no audio is to be added

    # Ensure the output directory exists
    os.makedirs(output_base_dir, exist_ok=True)

    # Generate a unique output file path
    output_path = generate_output_path(output_base_dir)

    # Concatenate videos and optionally add audio
    concatenate_videos(video_infos, output_path, audio_path)

if __name__ == "__main__":
    main()
