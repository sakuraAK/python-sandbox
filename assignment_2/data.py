from typing import List

from sqlalchemy import String, create_engine, select, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship, sessionmaker
from sqlalchemy.sql import func
from json import JSONEncoder
import os
from abc import abstractmethod, ABC


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    tweets: Mapped[List["Tweet"]] = relationship(back_populates="user")

    def to_json(self):
        return "{}'id': {}, 'name' : '{}'{}".format('{', self.id, self.name, '}')

    def __repr__(self):
        return f"<User name: {self.name}>"


class Tweet(Base):
    __tablename__ = "tweet"
    id: Mapped[int] = mapped_column(primary_key=True)
    message: Mapped[str] = mapped_column(String(280))
    posted_on: Mapped[str] = mapped_column(DateTime(timezone=True), server_default=func.now())
    posted_by: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="tweets")

    def __repr__(self):
        return f"<Tweet: {self.message}, Posted by: {self.user.name}, Posted on: {self.posted_on}>"

    def to_json(self):
        """
        To implement (similar to User.to_json)
        :return:  Json representation of object
        """
        pass


class DbWrapper(ABC):
    def __init__(self):
        self.set_engine()
        self._session = None
        self.setup()

    @abstractmethod
    def set_engine(self):
        pass

    @abstractmethod
    def setup(self):
        pass

    @property
    def session(self):
        if self._session == None:
            self._session = Session(self._engine)
        return self._session

    def add_user(self, name: str):
        user = User(name=name)
        self.session.add(user)
        self.session.commit()

    def get_users(self, filter: str):
        stmt = select(User)
        if not filter is None:
            stmt = select(User).filter(User.name.like(f"%{filter}%"))
            print(stmt)
        result = self.session.execute(stmt).scalars().all()
        json_result = []
        for r in result:
            json_result.append(r.to_json())
        return json_result

    def get_user(self, id):
        result = self.session.get(User, id)
        if result is None:
            return "{}"
        else:
            return result.to_json()

    def add_tweet(self, message: str, user_id: int) -> str:
        """
        To implement
        :param message: Tweet message
        :param user_id: Id of posting user (should be an id from user table)
        :return: Json string with newly created tweet
        """
        pass

    def get_tweets(self, filter: str):
        """
        To implement. Return list of tweets
        :param filter: optional parameter to filter the messages
        :return: List of Json string
        """
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._session.close()


class SqlLiteDbWrapper(DbWrapper):

    def __init__(self, db_file_path):
        self._path = db_file_path
        super().__init__()

    def set_engine(self):
        self._engine = create_engine("sqlite:///" + self._path)

    def setup(self):
        if os.path.exists(self._path):
            return
        Base.metadata.create_all(self._engine)
