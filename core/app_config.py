from json import loads
from pathlib import Path

class AppConfig:
    def __init__(self, path: Path):
        self.path = path
        self.params = {}


    def reload(self):
        with open(self.path, encoding="utf-8") as f:
            self.params = loads(f.read())
    

    def save(self):
        tmp = self.path.with_suffix(".tmp")
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(self.params, f, ensure_ascii=False, indent=4)
        os.replace(tmp, self.path)   # атомарно: при падении не останется полузаписанного файла