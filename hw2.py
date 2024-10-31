import data
from typing import Optional
from typing import List

# Write your functions for each part in the space below.

# Part 1
def create_rectangle(p1: data.Point, p2: data.Point) -> data.Rectangle:
    """
    Create a rectangle from two points, determining the top-left and bottom-right corners.

    Parameters:
        p1 (Point): First point.
        p2 (Point): Second point.

    Returns:
        Rectangle: Rectangle object defined by the two points.
    """
    top_left = data.Point(min(p1.x, p2.x), max(p1.y, p2.y))
    bottom_right = data.Point(max(p1.x, p2.x), min(p1.y, p2.y))
    return data.Rectangle(top_left, bottom_right)

# Part 2
def shorter_duration_than(d1: data.Duration, d2: data.Duration) -> bool:
    """
    Check if the first duration is shorter than the second duration.

    Parameters:
        d1 (Duration): First duration.
        d2 (Duration): Second duration.

    Returns:
        bool: True if d1 is shorter than d2, False otherwise.
    """
    d1_total_seconds = d1.minutes * 60 + d1.seconds
    d2_total_seconds = d2.minutes * 60 + d2.seconds
    return d1_total_seconds < d2_total_seconds

# Part 3
def songs_shorter_than(songs: List[data.Song], max_duration: data.Duration) -> List[data.Song]:
    """
    Return a list of songs with durations shorter than a given duration.

    Parameters:
        songs (list[Song]): List of Song objects.
        max_duration (Duration): Upper bound on song length.

    Returns:
        list[Song]: List of songs with duration less than max_duration.
    """
    return [song for song in songs if shorter_duration_than(song.duration, max_duration)]

# Part 4
def running_time(songs: List[data.Song], playlist_indices: List[int]) -> data.Duration:
    """
    Calculate the total running time of a playlist of songs.

    Parameters:
        songs (list[Song]): List of Song objects.
        playlist_indices (list[int]): List of indices specifying the playlist.

    Returns:
        Duration: Total duration of the playlist as a Duration object.
    """
    total_seconds = sum(
        songs[i].duration.minutes * 60 + songs[i].duration.seconds
        for i in playlist_indices if 0 <= i < len(songs)
    )

    minutes, seconds = divmod(total_seconds, 60)
    return data.Duration(minutes, seconds)

# Part 5
def validate_route(city_links: List[List[str]], route: List[str]) -> bool:
    """
    Validate a route based on city connections.

    Parameters:
        city_links (list[list[str]]): List of pairs representing city connections.
        route (list[str]): List of city names representing the route.

    Returns:
        bool: True if the route is valid, False otherwise.
    """
    city_connections = {frozenset(link) for link in city_links}

    for i in range(len(route) - 1):
        if frozenset([route[i], route[i + 1]]) not in city_connections:
            return False
    return True

# Part 6
def longest_repetition(numbers: List[int]) -> Optional[int]:
    """
    Find the starting index of the longest contiguous repetition of a number in the list.

    Parameters:
        numbers (list[int]): List of integers.

    Returns:
        Optional[int]: Index of the longest contiguous repetition, or None if the list is empty.
    """
    if not numbers:
        return None

    max_start = 0
    max_length = 1
    current_start = 0
    current_length = 1

    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                max_start = current_start
            current_start = i
            current_length = 1

    if current_length > max_length:
        max_start = current_start

    return max_start
