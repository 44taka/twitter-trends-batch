import pytest

from infrastructure.persistence.twitter.trends import TwitterTrendsPersistence
from infrastructure.database import db
from infrastructure.twitter_api import twitter_api


# フィクスチャ
@pytest.fixture
def ttp() -> TwitterTrendsPersistence:
    return TwitterTrendsPersistence(
        db=db, twitter_api=twitter_api
    )


class TestTwitterTrendsPersistence(object):
    """Twitterトレンド永続化処理クラス"""
    
    def test_find(self, ttp: TwitterTrendsPersistence):
        result = ttp.find(woeid=23424856)
        assert len(result) > 0
    
    def test_exception_find(self, ttp: TwitterTrendsPersistence):
        with pytest.raises(Exception):
            ttp.find(woeid=99)

    def test_insert(self, ttp: TwitterTrendsPersistence):
        trends = ttp.find(woeid=23424856)
        result = ttp.insert(trends=trends)
        assert result == None

    def test_eception_insert(self, mocker, ttp: TwitterTrendsPersistence):
        trends = ttp.find(woeid=23424856)
        mocker.patch.object(ttp, '_db', 'test')
        with pytest.raises(Exception):
            ttp.insert(trends=trends)
