import os
class Config:
    '''
    configuration parent class
    '''
    NEWS_API_BASE_URL='https://newsapi.org/v2/everything?q={}&apiKey={}'
    SOURCE_API_BASE_URL='https://newsapi.org/v2/sources?category={}&language=en&apiKey={}'
    ARTICLE_API_BASE_URL='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    SEARCH_URL = 'https://newsapi.org/v2/everything?q={}apiKey={}'
    
    NEWS_API_KEY= os.environ.get('NEWS_API_KEY')
    SECRET_KEY= os.environ.get('SECRET_KEY')
    pass



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

config_options = {
'development':DevConfig,
'production':ProdConfig
}