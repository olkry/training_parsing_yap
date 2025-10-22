import requests_cache

MAIN_DOC_URL = 'https://docs.python.org/3/'

if __name__ == '__main__':

    session = requests_cache.CachedSession()
    # session.cache.clear()
    response = session.get(MAIN_DOC_URL)

    print(session.cache.urls())
