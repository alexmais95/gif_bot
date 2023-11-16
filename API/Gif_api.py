import giphy_client
from giphy_client.rest import ApiException
from settings.settings import API_GIF



class Gif:
    def __init__(self):
        self.api_instance = giphy_client.DefaultApi()
        self.url = "http://api.giphy.com/v1/gifs/search"
        self.api_key = API_GIF
        self.rating = 'g'
        self.fmt = 'json'

    def get_gif(self, search):
        try:
            api_response = self.api_instance.gifs_search_get(self.api_key, search, rating=self.rating, limit=5)
            data_api = list(api_response.data)

        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

        return data_api