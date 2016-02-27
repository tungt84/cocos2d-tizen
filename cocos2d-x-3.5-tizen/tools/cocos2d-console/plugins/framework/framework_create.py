
import cocos

from package.helper import ProjectHelper


class FrameworkCreate(cocos.CCPlugin):
    @staticmethod
    def plugin_name():
        return "create-framework"

    @staticmethod
    def brief_description():
        return "Creates a framework in an existing project"

    # parse arguments
    def parse_args(self, argv):
        from argparse import ArgumentParser

        parser = ArgumentParser(prog="cocos %s" % self.__class__.plugin_name(),
                                description=self.__class__.brief_description())
        parser.add_argument("name", metavar="NAME", help="Specifies the package name")
        return parser.parse_args(argv)

    def run(self, argv):
        args = self.parse_args(argv)
        name = args.name

        project = ProjectHelper.get_current_project()
        ProjectHelper.create_framework(project, name)
