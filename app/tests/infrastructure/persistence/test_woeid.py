import pytest

from domain.model.woeid import WoeIdModel
from infrastructure.database import db
from infrastructure.persistence.woeid import WoeIdPersistence


# フィクスチャ
@pytest.fixture
def wip() -> WoeIdPersistence:
    return WoeIdPersistence(db=db) 


class TestWoeIdPersistence(object):
    """WoeIdPersistenceのテスト"""

    def test_find_all(self, wip: WoeIdPersistence):
        result = wip.find_all()
        assert len(result) > 0
    
    def test_no_result_find_all(self, mocker, wip: WoeIdPersistence):
        # メソッドチェーンのモックを作る
        get_mock = mocker.MagicMock()
        get_mock.get = mocker.Mock(return_value=[])
        table_mock = mocker.MagicMock()
        table_mock.table = mocker.Mock(return_value=get_mock)
        mocker.patch.object(wip, "_db", table_mock)
        result = wip.find_all()
        assert len(result) == 0

    def test_exception_find_all(self, mocker, wip: WoeIdPersistence):
        mock = mocker.MagicMock()
        mock.table = mocker.Mock(side_effect=Exception)
        mocker.patch.object(wip, "_db", mock)
        with pytest.raises(Exception):
            wip.find_all()

    @pytest.mark.parametrize('id, expected', [
        (23424856, WoeIdModel(id=23424856, name='Japan')),
    ])
    def test_success_find_by_id(self, id, expected, wip: WoeIdPersistence):
        result = wip.find_by_id(woeid=id)
        assert result.id == expected.id
        assert result.name == expected.name

    @pytest.mark.parametrize('id, expected', [
        (99999999, None),
        (98765432, None),
        (87898798, None),
    ])
    def test_failed_find_by_id(self, id, expected, wip: WoeIdPersistence):
        result = wip.find_by_id(woeid=id)
        assert result == expected

    @pytest.mark.parametrize('id, ex, expected', [
        (99999999, 'test', AttributeError),
        (99999999, 1234, AttributeError),
    ])
    def test_exception_find_by_id(self, mocker, id, ex, expected, wip: WoeIdPersistence):
        mocker.patch.object(wip, '_db', ex)
        with pytest.raises(expected):
            wip.find_by_id(woeid=id)
