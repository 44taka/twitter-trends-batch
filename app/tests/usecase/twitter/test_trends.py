import pytest

from infrastructure.database import db
from infrastructure.twitter_api import twitter_api

from domain.model.woeid import WoeIdModel
from infrastructure.persistence.woeid import WoeIdPersistence
from infrastructure.persistence.twitter.trends import TwitterTrendsPersistence
from usecase.twitter.trends import TwitterTrendsUseCaseImpl


# フィクスチャ
@pytest.fixture
def ttu():
    wip = WoeIdPersistence(db=db)
    ttp = TwitterTrendsPersistence(
        db=db, twitter_api=twitter_api
    )
    return TwitterTrendsUseCaseImpl(wip=wip, ttp=ttp)


class TestTwitterTrendsUseCaseImpl(object):
    
    def test_woeid_find_all(self, ttu: TwitterTrendsUseCaseImpl):
        result = ttu.woeid_find_all()
        assert len(result) > 0

    @pytest.mark.parametrize('id, expected', [
        (23424856, WoeIdModel(id=23424856, name='Japan')),
    ])
    def test_woeid_find_by_id(self, ttu: TwitterTrendsUseCaseImpl, id, expected):
        result = ttu.woeid_find_by_id(woeid=id)
        assert result.id == expected.id
        assert result.name == expected.name

    @pytest.mark.parametrize('id, expected', [
        (99999999, None),
        (98765432, None),
        (87898798, None),
    ])
    def test_failed_woeid_find_by_id(self, ttu: TwitterTrendsUseCaseImpl, id, expected):
        result = ttu.woeid_find_by_id(woeid=id)
        assert result == expected

    def test_get(self, ttu: TwitterTrendsUseCaseImpl):
        result = ttu.get(woeid=23424856)
        assert len(result) > 0

    def test_insert(self, ttu: TwitterTrendsUseCaseImpl):
        trends = ttu.get(woeid=23424856)
        result = ttu.register(trends=trends)
        assert result == None
