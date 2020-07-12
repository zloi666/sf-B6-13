import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE = "sqlite:///albums.sqlite3"
Base = declarative_base()


class Album(Base):
    # модель таблицы album
    __tablename__ = "album"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    year = sqlalchemy.Column(sqlalchemy.Integer)
    artist = sqlalchemy.Column(sqlalchemy.Text)
    genre = sqlalchemy.Column(sqlalchemy.Text)
    album = sqlalchemy.Column(sqlalchemy.Text)


def connect_db():
    # коннектор к базе
    engine = sqlalchemy.create_engine(DATABASE)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    return session


def find_albums(artist):
    # поиск альбомов по исполнителю.
    session = connect_db()
    albums = session.query(Album).filter(Album.artist == artist).all()
    return albums


def get_all_albums():
    # запрос на все альбомы
    session = connect_db()
    albums = session.query(Album).all()
    return albums


def validate_year(year):
    # валидация года
    if year.isdigit() and len(year) == 4:
        year = int(year)
        return year
    else:
        return "wrong year"


def write_album(artist, genre, album, year):
    # производит запись в базу
    session = connect_db()

    if artist and genre and album and year:
        year = validate_year(year)
        if year != "wrong year":
            al = Album(
                year=year,
                artist=artist,
                genre=genre,
                album=album
            )
            session.add(al)
            session.commit()
        else:
            print(year)
    else:
        print("non complete data")
