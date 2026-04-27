from app.utils.url_utils import url_hash


class Deduplicator:
    def __init__(self):
        self._seen: set[str] = set()

    def is_duplicate(self, url: str) -> bool:
        h = url_hash(url)
        if h in self._seen:
            return True
        self._seen.add(h)
        return False

    def reset(self):
        self._seen.clear()
