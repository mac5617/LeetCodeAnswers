class Codec:
    def __init__(self):
        self.lookup = {}
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.lookup[hash(longUrl)] = longUrl
        return f'http://tinyurl.com/{hash(longUrl)}'

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        clean = shortUrl.replace("http://tinyurl.com/",'')
        return self.lookup[int(clean)]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))