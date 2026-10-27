
from json import loads

class AppConfig:
    def __init__(self, config: str | None=None):
        self._config = config
        #self.reload() -- лучше наверное не грузить инит логикой и сделать отдельной функцией
    
    def reload(self):
        self.params = loads(self._config)
        
        