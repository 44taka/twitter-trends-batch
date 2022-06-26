from abc import ABC, abstractmethod
from typing import List, Optional

from domain.model.twitter.trends import TwitterTrendsApiModel
from domain.model.woeid import WoeIdModel

from infrastructure.persistence.woeid import WoeIdPersistence
from infrastructure.persistence.twitter.trends import TwitterTrendsPersistence


class TwitterTrendsUseCase(ABC):
    
    @abstractmethod
    def woeid_find_all(self) -> List[WoeIdModel]:
        raise NotImplementedError

    @abstractmethod
    def woeid_find_by_id(self, woeid: int) -> Optional[WoeIdModel]:
        raise NotImplementedError

    @abstractmethod
    def get(self, woeid: int) -> List[TwitterTrendsApiModel]:
        raise NotImplementedError

    @abstractmethod
    def register(self, trends: List[TwitterTrendsApiModel]) -> None:
        raise NotImplementedError



# TODO:エラーハンドリングが足りない気がする。
class TwitterTrendsUseCaseImpl(TwitterTrendsUseCase):
    
    def __init__(self, wip: WoeIdPersistence, ttp: TwitterTrendsPersistence):
        self._wip = wip
        self._ttp = ttp

    def woeid_find_all(self) -> List[WoeIdModel]:
        return self._wip.find_all()

    def woeid_find_by_id(self, woeid: int) -> Optional[WoeIdModel]:
        result = self._wip.find_by_id(woeid=woeid)
        if result is None:
            raise Exception('Woeid not found')
        return result

    def get(self, woeid: int) -> List[TwitterTrendsApiModel]:
        return self._ttp.find(woeid=woeid)

    def register(self, trends: List[TwitterTrendsApiModel]) -> None:
        self._ttp.insert(trends=trends)
