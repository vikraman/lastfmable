import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.redirect("/static/wip.html")

app = webapp2.WSGIApplication([('/',MainPage)], debug=True)
