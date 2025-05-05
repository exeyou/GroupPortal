import re

def extract_youtube_video_id(text):
    """
    Extracts a YouTube video ID from the given text.
    Supports both long and short YouTube URL formats.
    Returns the video ID or None if not found.
    """
    # Full link formats
    youtube_regex = (
        r'(?:youtube\.com/watch\?v=|youtu\.be/)([^\s&]+)'
    )
    match = re.search(youtube_regex, text)
    if match:
        return match.group(1)
    return None
