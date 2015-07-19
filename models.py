from database import db
from pony.orm import Required
from datetime import datetime


class Subscription(db.Entity):

    _table_ = "subscriptions"
    email = Required(str, unique=True, index=True)
    created_at = Required(datetime, default=lambda: datetime.now())
