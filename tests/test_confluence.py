import logging
import os
import pytest
import haip.config as config
import haip.confluence as confluence

logging.basicConfig()
logger = logging.getLogger('haip')
logger.setLevel(logging.DEBUG)

TESTPAGEPARENT = 256931421
TESTPAGEID = 256924966

basedir = os.path.dirname(__file__)

@pytest.fixture
def setup():
    config.load(basedir + os.sep + 'etc', 'dev')

@pytest.mark.skip(reason="you need a running confluence server for this test")
@pytest.mark.asyncio
async def test_getBody(setup):
    response = await confluence.getBody(TESTPAGEID)
    assert 'version' in response


@pytest.mark.skip(reason="you need a running confluence server for this test")
@pytest.mark.asyncio
async def test_setBody(setup):
    response = await confluence.setBody(TESTPAGEID, 'hello world')
    assert 'version' in response  

@pytest.mark.skip(reason="you need a running confluence server for this test")
@pytest.mark.asyncio
async def test_getChildren(setup):
    children = await confluence.getChildren(TESTPAGEPARENT)
    assert children 

# @pytest.mark.skip(reason="you need a running confluence server for this test")
@pytest.mark.asyncio
async def test_upload(setup):
    response = await confluence.upload(256931828, 'attachment.txt', f'{basedir}/data/attachment.txt')
    assert 'status' in response 