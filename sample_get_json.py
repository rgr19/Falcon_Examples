# sample.py
import falcon


class QuoteResource:

    def on_get(self, req, resp):

        quote = {
            'quote': ("I've always been more interested in "
                      "the future than in the past."),
            'author': 'Grace Hopper'
        }
        resp.media = quote


api = falcon.API()
api.add_route('/quote', QuoteResource())
