from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella 
        testi = toml.loads(content)
        nimi = testi['tool']['poetry']['name']
        des = testi['tool']['poetry']['description']
        lisenssi = testi['tool']['poetry']['license']
        aut = testi['tool']['poetry']['authors']
        dep = list(testi['tool']['poetry']['dependencies'].keys())
        devdep = list(testi['tool']['poetry']['group']['dev']['dependencies'].keys())

        return Project(nimi, des, lisenssi, aut, dep, devdep)
