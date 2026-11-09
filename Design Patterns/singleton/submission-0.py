class Singleton:

    # In python consider this method as the 'getInstance'
    _uniq=None
    def __new__(cls):
        if cls._uniq is None:
            cls._uniq=super(Singleton,cls).__new__(cls)
        return cls._uniq

    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str):
        self.value=value

