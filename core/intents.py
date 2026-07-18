from lolka import Intents

class IntentsFromConf:
    def __init__(self, intents_conf: dict):
        self.intents_conf = intents_conf

    def build_intents(self):
        intents = Intents.none()
        for name, enabled in self.intents_conf.items():
            if name not in Intents.VALID_FLAGS:
                raise ValueError(f"Неизвестный intent: {name!r}")
            setattr(intents, name, bool(enabled))
        return intents