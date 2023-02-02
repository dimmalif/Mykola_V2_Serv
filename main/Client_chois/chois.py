class ChooseInterface:
    """Цей клас повинен приймати у скриптів з директорії Apps
    вибір відносно моделі та типу розпізнавання"""

    __slots__ = ('__model', '__platform')

    PLATFORMS = ('Desktop', 'Server')
    MODELS = ('Mykola', 'Dmytro')

    def __init__(self, model, platforms=PLATFORMS[1]):
        self.__model = model
        self.__platform = platforms

        self.__validator(self.__model, self.__platform)

    def get_param(self):
        return {'Model': self.__model,
                'Platform': self.__platform}

    def __repr__(self):
        return f'Model: {self.__model}, Platform: {self.__platform}'

    @classmethod
    def __validator(cls, model, platform):
        if platform not in cls.PLATFORMS or model not in cls.MODELS:
            raise AttributeError(f'Mast by: \n Platforms: {cls.PLATFORMS} \n Models: {cls.MODELS}')


c = ChooseInterface('Mykola', 'Server')
print(c.get_param())


