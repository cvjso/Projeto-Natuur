from aiohttp import web

# request handlers imports

from features.handle.handlers import handle, saida, preco, produto, chegada, cartao, especie, quantidade, compra, periodo


def create_app():
    app = web.Application()
    app.router.add_get('/', handle)
    app.router.add_get('/saida', saida)
    app.router.add_get('/preco', preco)
    app.router.add_get('/produto', produto)
    app.router.add_get('/chegada', chegada)
    app.router.add_get('/cartao', cartao)
    app.router.add_get('/especie', especie)
    app.router.add_get('/quantidade', quantidade)
    app.router.add_get('/compra', compra)
    app.router.add_get('/periodo', periodo)
    return app


def app_run(port):
    app = create_app()
    web.run_app(app, port=port)

    
if __name__ == "__main__":
    port = 5858
    app_run(port)