#
# copyright (c) 2011 Hannah von Reth <vonreth@kde.org>
#
from .CollectionPackagerBase import *
from .SevenZipPackager import *
from .NullsoftInstallerPackager import *

class PortablePackager(CollectionPackagerBase, SevenZipPackager):
    """
Packager for portal 7zip archives
"""

    @InitGuard.init_once
    def __init__(self, whitelists=None, blacklists=None):
        SevenZipPackager.__init__(self)
        CollectionPackagerBase.__init__(self, whitelists, blacklists)

    def createPortablePackage(self):
        """create portable 7z package with digest files located in the manifest subdir"""
        if not "setupname" in self.defines or not self.defines["setupname"]:
            self.defines["setupname"] = os.path.join(self.packageDestinationDir(), self.binaryArchiveName(includeRevision=True))
        if not "srcdir" in self.defines or not self.defines["srcdir"]:
            self.defines["srcdir"] = self.archiveDir()

        self._compress(self.defines["setupname"], self.defines["srcdir"], self.packageDestinationDir())

    def createPackage(self):
        """ create a package """
        print("packaging using the PortablePackager")

        self.internalCreatePackage()
        self.createPortablePackage()

        absSetupPath = self.defines["setupname"]
        if not os.path.isabs(absSetupPath):
            absSetupPath = os.path.join(self.packageDestinationDir(), absSetupPath)

        CraftHash.createDigestFiles(absSetupPath)

        return True
