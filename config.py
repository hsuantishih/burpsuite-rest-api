config = {
    'SERVER_URL' : 'http://127.0.0.1:1337/v0.1/'
}

class Config(object):
    def __init__(self):
        self._config = config

    def get_property(self, property_name):
        if property_name not in self._config.keys():
            return None
        return self._config[property_name]