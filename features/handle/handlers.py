from aiohttp import web
import json
import pandas as pd

from features.handle.mergeDict.mergeDict import mergeDict

data = pd.read_csv('data/result.csv')

DICT = data.to_dict()    

dict1 = DICT['Produto']

dict2 = mergeDict(DICT['Cartão'], DICT['Espécie'])

dict3 = mergeDict(DICT['Produto'], DICT['Compra'])

dict4 = mergeDict(DICT['Produto'], DICT['Periodo'])

async def handle(request):
    response_obj = { 'status' : 'success'}
    return web.Response(text=json.dumps(response_obj))

async def graf1(request):
    response_obj = dict1
    return web.Response(text=json.dumps(response_obj))

async def graf2(request):
    response_obj = dict2
    return web.Response(text=json.dumps(response_obj))

async def graf3(request):
    response_obj = dict3
    return web.Response(text=json.dumps(response_obj))

async def graf4(request):
    response_obj = dict4
    return web.Response(text=json.dumps(response_obj))