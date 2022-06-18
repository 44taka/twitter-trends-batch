from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TwitterTrendsApiModel(BaseModel):
    name: str
    url: str
    tweet_volume: Optional[int]


class TwitterTrendsModel(TwitterTrendsApiModel):
    # id: Optional[int]
    rank: int
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    
    class Config:
        allow_mutation = False
        table_name = 'twitter_trends'
