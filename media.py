import webbrowser
class Movie():
    """This class stores information about movies"""
    """Functions here play trailers, does something"""
    VALID_RATINGS = ["G", "PG", "PG13", "R", "NR"]
    
    def __init__(self, mov_title, mov_storyline, mov_poster, mov_trailer):       
        #variabes_inside_this_class = variables_defined_in_the_instance_variable
        self.title = mov_title
        self.storyline = mov_storyline
        self.poster_image_url= mov_poster
        self.trailer_youtube_url  = mov_trailer

    def play_trailer(self):
        webbrowser.open(self.trailer)
