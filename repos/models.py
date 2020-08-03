class GitHubRepo:
    """
    A class used to represent a single GithHub Repository.
    """

    def __init__(self, name, language, num_stars, url):
        self.name = name
        self.language = language
        self.num_stars = num_stars
        self.url = url


    def __str__(self):
        return f"-> {self.name} is a {self.language} repo with {self.num_stars} stars"

    def __repr__(self):
        return f"GitHubRepo('{repr(self.name)}', '{repr(self.language)}', '{repr(self.num_stars)}')"