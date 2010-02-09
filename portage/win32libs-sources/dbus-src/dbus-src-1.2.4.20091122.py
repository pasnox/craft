# -*- coding: utf-8 -*-
import utils
import os
import info

class subinfo(info.infoclass):
    def setTargets( self ):
        svnurl = "https://windbus.svn.sourceforge.net/svnroot/windbus/"
        self.svnTargets['1.2.1'] = svnurl + 'tags/1.2.1'
        self.svnTargets['1.2.3'] = svnurl + 'tags/1.2.3'
        self.svnTargets['1.2.4'] = svnurl + 'tags/1.2.4'
        self.svnTargets['svnHEAD'] = svnurl + 'trunk'
        self.defaultTarget = '1.2.4'
        self.targetInstSrc['1.2.4'] = 'tags/1.2.4'
        self.targetConfigurePath['1.2.4'] = 'cmake'
        self.svnTargets['gitHEAD'] = 'git://anongit.freedesktop.org/git/dbus/dbus'
        self.targetConfigurePath['gitHEAD'] = 'cmake'
        self.targetConfigurePath['svnHEAD'] = 'cmake'
    
    def setDependencies( self ):
        self.hardDependencies['win32libs-bin/libxml2'] = 'default'
        self.hardDependencies['win32libs-bin/expat'] = 'default'
        self.hardDependencies['virtual/base'] = 'default'

from Package.CMakePackageBase import *
                
class Package(CMakePackageBase):
    def __init__( self, **args ):
        self.subinfo = subinfo()
        CMakePackageBase.__init__( self )
        self.subinfo.options.package.packageName = 'dbus'
        self.subinfo.options.configure.defines = "-DDBUS_USE_EXPAT=ON -DDBUS_DISABLE_EXECUTABLE_DEBUG_POSTFIX=ON"
        self.subinfo.options.make.slnBaseName = 'dbus'
        
    def unpack(self):
        if not CMakePackageBase.unpack(self):
            return False
        if self.buildTarget in ['1.2.1', '1.2.3', '1.2.4', 'svnHEAD']:
            utils.copyFile( os.path.join(self.packageDir(), "wspiapi.h"), os.path.join(self.buildDir(), "wspiapi.h") )
        return True

    
if __name__ == '__main__':
    Package().execute()
