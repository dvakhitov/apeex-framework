from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from apeex.orm import EntityManagerInterface, UnitOfWorkInterface
from typing import Any, Type

# ----------------------------
# UnitOfWork
# ----------------------------
class UnitOfWorkAdapter(UnitOfWorkInterface):
    def __init__(self, session: Session):
        self.session = session

    def register_new(self, entity: Any) -> None:
        self.session.add(entity)

    def register_dirty(self, entity: Any) -> None:
        self.session.add(entity)

    def register_removed(self, entity: Any) -> None:
        self.session.delete(entity)

    def commit(self) -> None:
        self.session.commit()


# ----------------------------
# Базовый EntityManagerAdapter
# ----------------------------
class BaseEntityManagerAdapter(EntityManagerInterface):
    """
    Base adapter EntityManager.
    OCP: changeable for different DBMS.
    """
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url, echo=True)
        self.Session = sessionmaker(bind=self.engine)
        self._session = self.Session()
        self.unit_of_work = UnitOfWorkAdapter(self._session)

    def persist(self, entity: Any) -> None:
        self.unit_of_work.register_new(entity)

    def remove(self, entity: Any) -> None:
        self.unit_of_work.register_removed(entity)

    def find(self, entity_class: Type, id: Any) -> Any:
        return self._session.get(entity_class, id)

    def flush(self) -> None:
        self.unit_of_work.commit()

    def clear(self) -> None:
        self._session.expunge_all()


# ----------------------------
# Specific adapters for DBMS
# ----------------------------
class SQLiteEntityManagerAdapter(BaseEntityManagerAdapter):
    def __init__(self, settings: Optional[Mapping[str, str]] = None):
        db_url = settings.get("db_url") if settings and "db_url" in settings else "sqlite:///:memory:"
        super().__init__(db_url)


class PostgresEntityManagerAdapter(BaseEntityManagerAdapter):
    def __init__(self, settings: Optional[Mapping[str, str]] = None):
        db_url = settings.get("db_url") if settings and "db_url" in settings else "postgresql+psycopg2://user:pass@localhost/db"
        super().__init__(db_url)
        # можно добавить специфические настройки Postgres здес