
from json import loads

class AppConfig:
    def __init__(self, config_file: str | None=None):
        self._config_file = config_file
        #self.reload() -- лучше наверное не грузить инит логикой и сделать отдельной функцией
    
    def reload(self):
        self.params = loads(self._config_file)
        
        