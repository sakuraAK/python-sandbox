from typing import List

from sqlalchemy import String, create_engine, select, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from sqlalchemy.sql import func
import json
from dataclasses import dataclass
import os
from abc import abstractmethod, ABC



class Base(DeclarativeBase):
    def to_dict(self):
        """Return a dictionary representation of this model."""
        ret_data = {}
        columns = self.__table__.columns.keys()
        for c in columns:
            ret_data[c] = getattr(self, c)
        return ret_data



class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    tweets: Mapped[List["Tweet"]] = relationship(back_populates="user")

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

class Follower(Base):
    __tablename__ = "follower"
    id: Mapped[int] = mapped_column(primary_key=True)
    followee_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    follower_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    followed_on: Mapped[str] = mapped_column(DateTime(timezone=True), server_default=func.now())
    UniqueConstraint("followee_id", "follower_id", name="uix_1")

class Like(Base):
    __tablename__ = "like"
    id: Mapped[int] = mapped_column(primary_key=True)
    tweet_id: Mapped[int] = mapped_column(ForeignKey("tweet.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    liked_on: Mapped[str] = mapped_column(DateTime(timezone=True), server_default=func.now())
    UniqueConstraint("tweet_id", "user_id", name="uix_1")

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
        self._session.execute('pragma foreign_keys=on')
        return self._session

    def add_user(self, name: str) -> User:
        user = User(name=name)
        self.session.add(user)
        self.session.commit()
        return user

    def get_users(self, filter: str) -> List[User]:
        stmt = select(User)
        if not filter is None:
            stmt = select(User).filter(User.name.like(f"%{filter}%"))
        result = self.session.execute(stmt).scalars().all()
        return result

    def get_user(self, id) -> User:
        user = self.session.get(User, id)
        if user is None:
            return User()
        else:
            return user

    def add_tweet(self, message: str, user_id: int) -> Tweet:
        """
        To implement
        :param message: Tweet message
        :param user_id: Id of posting user (should be an id from user table)
        :return: Json string with newly created tweet
        """
        new_tweet = Tweet()
        new_tweet.message = message
        new_tweet.posted_by = user_id
        self.session.add(new_tweet)
        self.session.commit()
        return new_tweet

    def get_tweets(self, filter: str) -> List[Tweet]:
        """
        To implement. Return list of tweets
        :param filter: optional parameter to filter the messages
        :return: List of Json string
        """
        stmt = select(Tweet)
        if not filter is None:
            stmt = select(Tweet).filter(Tweet.message.like(f"%{filter}%"))
        result = self.session.execute(stmt).scalars().all()
        return result

    def follow(self, followee_id, follower_id):
        pass

    def unfollow(self, followee_id, follower_id):
        pass
    def add_like(self, tweet_id, user_id):
        pass

    def remove_like(self, tweet_id, user_id):
        pass

    def get_feed(self, user_id):
        """
        Get user feed. Tweets posted by the followed users.
        The most liked and the most recent on top
        :param user_id:
        :return:
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
