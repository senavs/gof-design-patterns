from typing import Set, Any

from patterns.observer.observ import ABCObservable


class YouTubeChanel(ABCObservable):
    _posted_videos: Set[str] = set()
    _new_video: bool = False

    def __init__(self, name):
        self.name = name

    def post_video(self, title: str):
        self._posted_videos.add(title)
        self._new_video = True

    def notify(self):
        super().notify()
        self._new_video = False

    def state(self) -> Any:
        return self._new_video
