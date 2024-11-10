class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        def do_list(items):
            if not items:
                return "-"
            li = []
            for item in items:
                li.append(f"- {item}")
            return "\n".join(li)

        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            f"\n \nAuthors:\n{do_list(self.authors)}"
            f"\n \nDependencies:\n{do_list(self.dependencies)}"
            f"\n \nDevelopment dependencies:\n{do_list(self.dev_dependencies)}" #{self._stringify_dependencies(self.dev_dependencies)}"
        )
