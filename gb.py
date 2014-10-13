import webapp2
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
	def get(self):
		html = template.render('template/index.html', {})
		self.response.out.write(html)

app = webapp2.WSGIApplication([('/', MainPage)],
							  debug=True)