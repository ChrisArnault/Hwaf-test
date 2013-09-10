# -*- python -*-

# stdlib imports
import os
import os.path as osp
import sys

# waf imports ---
import waflib.Utils
import waflib.Logs as msg
import waflib.Configure
import waflib.Build
import waflib.Task
import waflib.Tools.ccroot
from waflib.Configure import conf
from waflib.TaskGen import feature, before_method, after_method, extension, after


@after_method('apply_link')
@feature('hwaf_export_lib')
def hwaf_export_lib(self):
    """
A task to properly export a library definition.
"""
    # extract package name
    pkgdir = self.path.abspath()
    pkgname = self.bld.hwaf_pkg_name(pkgdir)
    b_pkgname = osp.basename(pkgname)
    if not hasattr(self, 'link_task'):
        msg.debug('hwaf: task [%s] has no link_task' % self.name)
        return

    uses = [self.name] + waflib.Utils.to_list(getattr(self, 'use', []))
    self.bld.env.append_unique('LIB_%s' % self.name, uses)
    #self.env.append_unique('LIB_%s' % self.name, uses)
    #msg.debug('hwaf: export-lib: %s => %r' % (self.name, uses))
    return

