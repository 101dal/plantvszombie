from utils.Spawnable import Spawnable


class Sun(Spawnable):
    def __init__(self, value: int) -> None:
        super().__init__()
        
        self.value = value