import webbrowser


class Movie():
    '''Movie() class stores/returns the information
    for each movie passed to media.py'''

    '''the constructor method takes in the movie title, storyline,
    poster image, and trialer url for of movie that is passed in
    and sets it to new variable names'''
    def __init__(self, movie_title, movie_storyline, image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = image
        self.trailer_youtube_url = trailer_youtube

    '''show_trailer() will open the trailer
    of the url that is passed through'''
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
