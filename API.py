import giphy_client
from giphy_client.rest import ApiException
import random
from setting import API


class Gif:
    def __init__(self):
        self.api_instance = giphy_client.DefaultApi()
        self.url = "http://api.giphy.com/v1/gifs/search"
        self.api_key = API
        self.rating = 'g'
        self.fmt = 'json'

    def get_gif(self, search):
        try:
            api_response = self.api_instance.gifs_search_get(self.api_key, search, rating=self.rating, limit=5)
            lst_ = list(api_response.data)
            giff = random.choice(lst_)

        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)
        return giff.embed_url


