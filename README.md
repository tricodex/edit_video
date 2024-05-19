# Simple Video Stick with Audio

This Python script concatenates multiple video files, scales them to a uniform size, optionally applies a slow-motion effect, and adds an audio track. The script uses MoviePy for video manipulation and requires FFmpeg for video processing.

## Features

- Concatenates multiple video files from a directory or a predefined list.
- Scales all videos to match the resolution of the first video.
- Optionally applies a slow-motion effect to specific videos.
- Optionally trims and crops specific parts of each video.
- Optionally adds an audio track to the final video.
- Generates a uniquely named output file using the current date and time to avoid conflicts.

## Requirements

- Python 3.6 or higher
- MoviePy
- FFmpeg

## Installation

1. Install MoviePy using pip:

   ```sh
   pip install moviepy
   ```

2. Install FFmpeg and ensure it is added to your system's PATH. Follow the installation instructions from the [FFmpeg website](https://ffmpeg.org/download.html).

## Usage

1. Clone or download the repository.

2. Modify the `main()` function in the script to set the correct input directory, output directory, audio path, and slow motion factor.

3. Run the script:

   ```sh
   python simple_video_stick_with_audio.py
   ```

### Example Configuration

```python
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
```

## Functions

- `get_video_files(directory)`: Returns a list of video file paths from the specified directory.
- `scale_video(video, target_size)`: Scales the video to match the target size while maintaining the aspect ratio.
- `apply_slow_motion(video, factor)`: Applies slow motion to the video by the given factor.
- `crop_video(video, x1, y1, x2, y2)`: Crops the video to the specified region.
- `trim_video(video, start_time, end_time)`: Trims the video to the specified start and end times.
- `concatenate_videos(video_infos, output_path, audio_path=None)`: Concatenates videos from the list of video paths and saves the output video. Optionally adds an audio track and applies slow motion or cropping.
- `generate_output_path(base_dir, prefix="final_video")`: Generates a unique output file path using the current date and time.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### Notes

- Ensure FFmpeg is installed and accessible via the system's PATH.
- Adjust the `video_infos`, `output_base_dir`, `audio_path`, and `slow_motion_factor` variables as necessary.
- The script generates a uniquely named output file based on the current date and time to avoid file name conflicts.