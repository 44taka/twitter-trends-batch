from typing import List

from loguru import logger
from orator import DatabaseManager

from domain.model.woeid import WoeIdModel
from domain.repository.woeid import WoeIdRepository


class WoeIdPersistence(WoeIdRepository):
    
    def __init__(self, db: DatabaseManager):
        self._db = db

    def find_all(self) -> List[WoeIdModel]:
        try:
            result = self._db.table(WoeIdModel.Config.table_name).get()
            if len(result) == 0:
                logger.warning('woeid is not found.')
                return []
            return list(map(WoeIdModel.parse_obj, result))
        except:
            raise

    def find_by_id(self, woeid: int) -> (WoeIdModel | None):
        try:
            query = self._db.table(WoeIdModel.Config.table_name)
            result = query.where('id', woeid).first()
            if result is None:
                logger.warning('woeid is not found.')
                return None
            return WoeIdModel.parse_obj(result)
        except:
            raise
