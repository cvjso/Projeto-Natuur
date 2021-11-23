from aiohttp import web
import json
import pandas as pd

data = pd.read_csv('data/result.csv')

DICT = data.to_dict()    

async def handle(request):
    response_obj = { 'status' : 'success'}
    return web.Response(text=json.dumps(response_obj))

async def saida(request):
    response_obj = DICT['Hora de saida']
    return web.Response(text=json.dumps(response_obj))

async def preco(request):
    response_obj = DICT['Preço']
    return web.Response(text=json.dumps(response_obj))

async def produto(request):
    response_obj = DICT['Produto']
    return web.Response(text=json.dumps(response_obj))

async def chegada(request):
    response_obj = DICT['Hora de chegada']
    return web.Response(text=json.dumps(response_obj))

async def cartao(request):
    response_obj = DICT['Cartão']
    return web.Response(text=json.dumps(response_obj))

async def especie(request):
    response_obj = DICT['Espécie']
    return web.Response(text=json.dumps(response_obj))

async def quantidade(request):
    response_obj = DICT['Quantidade']
    return web.Response(text=json.dumps(response_obj))

async def compra(request):
    response_obj = DICT['Compra']
    return web.Response(text=json.dumps(response_obj))

async def periodo(request):
    response_obj = DICT['Periodo']
    return web.Response(text=json.dumps(response_obj))