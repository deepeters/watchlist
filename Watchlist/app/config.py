class Config:
    '''
    General configuration parent class
    '''
    pass
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/550?api_key=15b64426a487c5223111e93c3f2fa32f'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True