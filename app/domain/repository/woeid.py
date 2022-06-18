from abc import ABC, abstractmethod
from typing import List, Optional

from domain.model.woeid import WoeIdModel


class WoeIdRepository(ABC):

    @abstractmethod
    def find_all(self) -> List[WoeIdModel]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, woeid: int) -> Optional[WoeIdModel]:
        raise NotImplementedError
