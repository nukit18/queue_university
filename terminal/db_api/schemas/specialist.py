from db_api.db_gino import TimedBaseModel
from sqlalchemy import Column, BigInteger, String, sql, Date, Boolean, Integer
from sqlalchemy.dialects import postgresql


class Specialist(TimedBaseModel):
    __tablename__ = 'specialists'
    id = Column(BigInteger, primary_key=True)
    queue = Column(postgresql.ARRAY(Integer))
    new_queue = Column(BigInteger)
    last_queue = Column(BigInteger)
    on_reception = Column(String(10))
    num_window = Column(BigInteger)
    start_talon = Column(String(10))
    name_spec = Column(String(100))
    ip_address = Column(String(100))
    description = Column(String(200))
    bakalavr = Column(BigInteger)
    specialist = Column(BigInteger)

    query: sql.Select