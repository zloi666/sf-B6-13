from bottle import route
from bottle import run
from bottle import request
from bottle import HTTPError
import albums


@route("/albums/<artist>")
def get_artist_albums(artist):
    all_albums = albums.find_albums(artist)
    names = []
    for album in all_albums:
        names.append(album.album)
    message = "artist <strong>{}</strong> create total {} albums<br>".format(artist, len(all_albums))
    message += "<h3>albums:</h3>"
    for name in names:
        message += "{}<br>".format(name)
    return message


@route("/albums", method="POST")
def write_data():
    artist = request.forms.get("artist")
    genre = request.forms.get("genre")
    album = request.forms.get("album")
    year = request.forms.get("year")

    alb_list = albums.find_albums(artist)
    alb_names = [alb.album for alb in alb_list]

    if album not in alb_names:
        albums.write_album(artist, genre, album, year)
        message = "alldata is : {} {} {} {}".format(artist, genre, album, year)
        return message
    else:
        message = HTTPError(409, "Альбом есть в базе")
        return message


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
