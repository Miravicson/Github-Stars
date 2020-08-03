import requests
from pprint import pprint as pp
from repos.exceptions import GitHubApiException
from repos.models import GitHubRepo


GITHUB_API_URL = "https://api.github.com/search/repositories"



def create_query(languages, min_stars):

    """
    Create the query string for the GitHub search API,
    based on the minimum amount of stars for a project, and
    the provided programming languages.
    """

    query = " ".join([f"language:{language.strip()}" for language in languages])
    query = f"stars:>{min_stars} " + query
    return query

def repos_with_most_stars(languages, min_stars=40000, sort="stars", order="desc"):
    query = create_query(languages, min_stars)
    parameters = {"q": query, "sort": sort, "order": order}
    print(parameters)
    response = requests.get(GITHUB_API_URL, params=parameters)

    status_code = response.status_code

    if status_code != 200:
        raise GitHubApiException(status_code)

    response_json = response.json()
    items = response_json["items"]
    pp(items[0])
    return [GitHubRepo(repo["name"], repo["language"], repo["stargazers_count"], repo["clone_url"]) for repo in items]