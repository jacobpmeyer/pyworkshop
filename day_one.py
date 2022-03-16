import requests
import json

class GithubResponseError(Exception):
  def __init__(self, value):
    message = f"The response code was: {value}"
    super().__init__(message)

def main(languages):
  stars = 50000
  repos = repos_with_most_stars(stars, languages)
  langs_str = ""
  if len(languages) != 0:
    langs_str = f"for {', '.join(languages[:-1])}, and {languages[-1]} "
  print(f"The top GitHub repos {langs_str}are..")
  for i, name in enumerate(repos):
    print(f"{i + 1}: {name}")

def repos_with_most_stars(stars, languages):
  api_response = requests.get(
    "https://api.github.com/search/repositories",
    params=create_query(stars, languages)
  )
  if api_response.status_code != 200:
    raise GithubResponseError(api_response.status_code)
  json_response = api_response.json()
  items = json_response["items"]
  names = [item["name"] for item in items]
  return names

def create_query(stars, languages):
  stars = f"stars:>{stars}+"
  formatted_langs = [f"language:{lang}+" for lang in languages]
  langs_str = "".join(formatted_langs)
  sort = "&sort=stars"
  order = "&order=desc"
  return f"q={stars}+{langs_str}{sort}{order}"

if __name__ == "__main__":
  main(["javascript", "python", "ruby"])
