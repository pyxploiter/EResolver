import web, json
from eresolver import resolver

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:        
    def GET(self, query):
        return json.dumps(resolver(query), indent=2, sort_keys=True)

if __name__ == "__main__":
    app.run()
