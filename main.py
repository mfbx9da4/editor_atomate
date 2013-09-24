import webapp2
import os
import jinja2
import logging
from misc.bitly import getShortURLs
from misc.fb_editor import postUnpublishedPosts

template_dir = os.path.dirname(__file__) + '/templates'
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)
def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)
class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))



class Home(BaseHandler):
    def get(self):
        self.render('home.html')

class Bitly(BaseHandler):
    def get(self):
        self.render('bitly.html')

    def post(self):
        urls = self.request.get('URLs').split('\n')
        self.render('bitly_post.html', urls=getShortURLs(urls))


class CreateUnpublishedPosts(BaseHandler):
    def get(self):
        self.render('create_unpublished_posts.html')

    def post(self):
        data = self.request.get('data')
        access_token = self.request.get('access_token')
        self.render('unpublished_post_ids.html', ids=postUnpublishedPosts(access_token, data))

application = webapp2.WSGIApplication([
    ('/?', Home),
    ('/bitly', Bitly),
    ('/unpublished_posts', CreateUnpublishedPosts)
], debug=True)




