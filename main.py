#!python

import os
import logging

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app


class JSSpecHandler(webapp.RequestHandler):
  def get(self, module):
    base = self.request.get('base')
    scripts = self.request.get('script', allow_multiple=True)
    title = self.request.get('title') or scripts and os.path.basename(scripts[0]) or 'JSSpec'

    path = os.path.join(os.path.dirname(__file__), 'templates/jsspec.html')
    t = {
      'title'  : title,
      'base'   : base,
      'scripts': scripts,
      'modules': module and module.split('/')[1:] or None,
    }
    self.response.out.write(template.render(path, t))


class QUnitHandler(webapp.RequestHandler):
  def get(self, module):
    base = self.request.get('base')
    scripts = self.request.get('script', allow_multiple=True)
    title = self.request.get('title') or scripts and os.path.basename(scripts[0]) or 'QUnit'

    path = os.path.join(os.path.dirname(__file__), 'templates/qunit.html')
    t = {
      'title'  : title,
      'base'   : base,
      'scripts': scripts,
      'modules': module and module.split('/')[1:] or None,
    }
    self.response.out.write(template.render(path, t))


def main():
  application = webapp.WSGIApplication(
    [
      (r'/jsspec(/.*)?', JSSpecHandler),
      (r'/qunit(/.*)?', QUnitHandler)],
    debug=True)
  run_wsgi_app(application)


if __name__ == '__main__':
  main()
