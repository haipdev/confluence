import logging
import aiohttp 
import haip.config as config

_logger = logging.getLogger(__name__)

def getSession():
    cfg = config.get('confluence', username=None, password=None, timeout=10)
    params = {'timeout': aiohttp.ClientTimeout(total=cfg.timeout)}
    if cfg.username is not None:
        params['auth'] = aiohttp.BasicAuth(cfg.username, cfg.password)
    return aiohttp.ClientSession(**params)

async def getBody(id, expand="version,body.storage"):
    cfg = config.get('confluence', url=config.MANDATORY)
    url = f'{cfg.url}content/{id}?expand={expand}'
    async with getSession() as session:
        async with session.get(url, headers={'Content-Type': 'application/json'}) as response:
            data = await response.json()
            return { 'version': data['version']['number'], 
                     'title': data['title'],
                     'body': data['body']['storage']['value'] }

async def setBody(id, body):
    current = await getBody(id)
    cfg = config.get('confluence', url=config.MANDATORY)
    url = f'{cfg.url}content/{id}?expand=version'
    payload = {
        'version': {
            'number': current['version'] + 1
        }, 
        'title': current['title'],
        'type': 'page',
        'body': {
            'storage': {
                'value': body,
                'representation': 'storage'
            }
        }
    }
    async with getSession() as session:
        async with session.put(url, json=payload) as response:
            data = await response.json()
            _logger.info("update confluence page %d (old_version=%d, new_version=%d)", 
                         id, current['version'], data['version']['number'])
            return data
