import info

class subinfo(info.infoclass):
    def setDependencies( self ):
        self.dependencies['virtual/base'] = 'default'
        self.dependencies['libs/qtbase'] = 'default'
        self.dependencies['win32libs/openssl'] = 'default'
        self.dependencies['win32libs/cyrus-sasl'] = 'default'

    def setTargets( self ):
        self.svnTargets['master'] = 'kde:qca.git|qt5'
        self.shortDescription = "Qt Cryptographic Architecture (QCA)"
        self.defaultTarget = 'master'

from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__( self, **args ):
        CMakePackageBase.__init__(self)



