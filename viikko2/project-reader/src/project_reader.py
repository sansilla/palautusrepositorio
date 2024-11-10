from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print("Raw content:", content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        #return Project("Test name", "Test description", [], [])

        raw = tomli.loads(content)
        #print("Parsed data:", raw)

        data = raw.get("tool", {}).get("poetry", {})

        name = data.get("name", "")
        description = data.get("description", "")
        dependencies = data.get("dependencies", [])
        dev_dependencies = data.get("group", {}).get("dev", {}).get("dependencies", {}).keys()

        license = data.get("license", "")
        authors = data.get("authors", [])


        #print("Project name:", name)
        #print("Description:", description)
        #print("Dependencies:", dependencies)
        #print("Dev dependencies:", dev_dependencies)

        return Project(name, description, license, authors, dependencies, dev_dependencies)
