from aiohttp import web

# request handlers imports

from features.handle.handlers import handle, graf1, graf2, graf3, graf4


def create_app():
    app = web.Application()
    app.router.add_get('/', handle)
    app.router.add_get('/graf1', graf1)
    app.router.add_get('/graf2', graf2)
    app.router.add_get('/graf3', graf3)
    app.router.add_get('/graf4', graf4)
    return app


def app_run(port):
    app = create_app()
    web.run_app(app, port=port)

    
if __name__ == "__main__":
    port = 5858
    app_run(port)