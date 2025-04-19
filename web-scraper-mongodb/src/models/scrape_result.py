class ScrapeResult:
    def __init__(self, url, content):
        self.url = url
        self.content = content

    def to_dict(self):
        return {
            "url": self.url,
            "content": self.content
        }