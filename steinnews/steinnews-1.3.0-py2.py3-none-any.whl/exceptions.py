class NoChanges(Exception):
    def __init__(self, message="No changes found in latest section"):
        self.message = message
        super().__init__(self.message)