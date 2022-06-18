from abc import ABC, abstractmethod
from typing import List

from domain.model.twitter.trends import TwitterTrendsModel


class TwitterTrendsRepository(ABC):

    @abstractmethod
    # TODO:ここで加工する？
    def find(self, woeid: int) -> List[TwitterTrendsModel]:
        raise NotImplementedError
    
    @abstractmethod
    def insert(self, trends: List[TwitterTrendsModel]) -> None:
        raise NotImplementedError
    