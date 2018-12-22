# Batch-Py-Remux
Convert mkv video to hevc (h.265)

I scripted this a long time ago and uploading here now. I don't fully remember its functionalities.
Here is simple algorithm:
- Use MKV
- Extract Video Tracks, Audio Tracks, Subtitle Tracks
- Convert Video to H.265
- Convert All Audio Tracks to ACC
- Convert All Subtitles To SRT without markup (no style)
- Copy all track names and language etc
- Mux Them back to one MKV file

One more thing:
It uses ffmpeg, mkvextract and mkvmerge. ffmpeg can use nvidia gpu but not all architectures are supported. See this page for more information:
https://developer.nvidia.com/ffmpeg

To decode using cpu, use tracksDeMux.py and to decode using nvidia gpu, use tracksDeMux.hevc_nvenc.py. Just change the name in import statement (line #5) in run.py to use other script.
