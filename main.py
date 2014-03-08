import webapp2

from google.appengine.api import users

class LoginPage(webapp2.RequestHandler):
    def get(self):
        self.redirect(users.create_login_url(self.request.uri))

class LogoutPage(webapp2.RequestHandler):
    def get(self):
        self.redirect(users.create_login_url('/main'))

urls = [
    ('/login', LoginPage),
    ('/logout', LogoutPage),
]
app = webapp2.WSGIApplication(urls, debug=True)
