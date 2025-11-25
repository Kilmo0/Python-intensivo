import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
rr = requests.get(url)
print("Status code:", rr.status_code)

response = rr.json()
print(response.keys())

repo_dict = response['items']

print(f"O total de repositórios retornados: {len(repo_dict)}\n")

names, stars = [], []
for i in repo_dict:
    names.append(i['name'])
    stars.append(i['stargazers_count'])

my_syle = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_syle, x_label_rotation = 45,
                  show_legend = False)
chart.title = "most starret python projects"
chart.x_labels = names

chart.add('', stars)
chart.render_to_file("Python rep.svg")