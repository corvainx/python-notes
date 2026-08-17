# Lesson 13: Nested / Inner Classes
# A class defined inside another class for logical encapsulation.

class Computer:
    class OperatingSystem:
        def __init__(self, name: str, version: str):
            self.name = name
            self.version = version

        def boot(self):
            print(f"Booting {self.name} v{self.version}...")

    def __init__(self, model: str, os_name: str, os_version: str):
        self.model = model
        self.os = self.OperatingSystem(os_name, os_version)

    def power_on(self):
        print(f"Powering on machine: {self.model}")
        self.os.boot()

laptop = Computer("ThinkPad X1", "Ubuntu Linux", "24.04 LTS")
laptop.power_on()
