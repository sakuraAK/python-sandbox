from typing import List

from sqlalchemy import String, create_engine, select, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from sqlalchemy.sql import func
from json import JSONEncoder





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
    message:  Mapped[str] = mapped_column(String(280))
    posted_on: Mapped[str] = mapped_column(DateTime(timezone=True), server_default=func.now())
    posted_by: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="tweets")

    def __repr__(self):
        return f"<Tweet: {self.message}, Posted by: {self.user.name}, Posted on: {self.posted_on}>"


# engine = create_engine("sqlite:///demo.db")
# Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)

class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class DbWrapper:
    def __init__(self):
        self._engine = create_engine("sqlite:///e2e_demo//demo.db")
        self._session = None

    @property
    def session(self):
        if self._session == None:
            self._session = Session(self._engine)
        return self._session
    def add_user(self, name: str):
        user = User(name=name)
        self.session.add(user)
        self.session.commit()

    def get_users(self):
        stmt = select(User)
        result = self.session.execute(stmt).scalars().all()
        json_result = []
        for r  in result:
            json_result.append(r.to_json())
        print(json_result)
        return json_result

    def get_user(self, id):
        return self.session.get(User, id).to_json()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._session.close()


# CRUD
# user = User(name="Bill Shakespear")
# tweet = Tweet(message="Check out my new play.#books #goat")
# tweet.user = user
# user_1 = User(name="John Wayne")
# tweet_1 = Tweet(message="Just finished the new play by W. Shakespear. Wow!#newbooks")
# tweet_1.user = user_1
# # tweet.user = user
# with Session(engine) as session:
#     subq = select(Tweet).filter(Tweet.message.like("%book%")).subquery()
#     stmt = select(User).join(subq, User.id == subq.c.posted_by)
#     # print(stmt)c
#     result = session.execute(stmt).scalars().all()
#     for r in result:
#         print(r)
#     #     print(r.user.name)
#     # user = session.get(User, 1)
#     # print(user)
#     # for tweet in user.tweets:
#     #     print(tweet)
#     # session.add_all([tweet_1, tweet])
#     # session.commit()
#     # session.add(tweet)
#     # session.commit()

# with Session(engine) as session:
#     # session.add(user)
#     # session.commit()
#     # stmt = select(User).filter(User.name.like("%Do%"))
#     #print(stmt)
#     # result = session.execute(stmt).scalars().all()
#
#     # for r in result:
#     #     print(r)
#     user = session.get(User, 1)
#     # user.name = "Jack Rabbit"
#     session.delete(user)
#     print(session.deleted)
#     session.commit()

