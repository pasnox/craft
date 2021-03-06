import info
from Package.VirtualPackageBase import *


class subinfo(info.infoclass):
    def setTargets(self):
        self.targets['0.2'] = ""
        self.defaultTarget = '0.2'

    def setDependencies(self):
        self.buildDependencies["gnuwin32/wget"] = "default"
        self.buildDependencies["dev-util/7zip"] = "default"
        self.buildDependencies["gnuwin32/patch"] = "default"
        self.buildDependencies["gnuwin32/sed"] = "default"
        self.buildDependencies["dev-util/cmake"] = "default"
        self.buildDependencies["dev-util/git"] = "default"

        if CraftCore.compiler.isMacOS:
            self.buildDependencies["dev-util/macdylibbundler"] = "default"


        if CraftCore.compiler.isMinGW():
            self.buildDependencies["dev-util/mingw-w64"] = "default"
        if CraftCore.settings.get("Compile", "MakeProgram", "") == "jom":
            self.buildDependencies["dev-util/jom"] = "default"
        if CraftCore.settings.getboolean("Compile", "UseNinja", False):
            self.buildDependencies["dev-util/ninja"] = "default"
        if CraftCore.settings.getboolean("Compile", "UseCCache", False):
            self.buildDependencies["dev-util/ccache"] = "default"

        self.runtimeDependencies["libs/runtime"] = "default"
        self.buildDependencies["craft/craft-blueprints-kde"] = "default"
        self.buildDependencies["craft/craft-core"] = "default"

        # needed by CollectionPackagerBase
        if (CraftCore.settings.getboolean("QtSDK", "Enabled", False) and
            CraftCore.settings.getboolean("QtSDK","PackageQtSDK",True)):
            self.buildDependencies["dev-util/dependencies"] = "default"


class Package(VirtualPackageBase):
    def __init__(self):
        VirtualPackageBase.__init__(self)
