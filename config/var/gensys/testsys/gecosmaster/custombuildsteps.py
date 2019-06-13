# -*- coding: utf-8 -*-

from buildbot.steps.shell import ShellCommand, WithProperties
from buildbot.steps.transfer import FileUpload
from buildbot.status.builder import SUCCESS, FAILURE, WARNINGS
import subprocess
import distroconf
from distroconf import halt_on_lintian_error
from distroconf import livebuild_gecos, livebuild_gecos_lite, pdebuild, codename_gecos

class RemoveGIT(ShellCommand):
    """ Removes the .svn directories recursively"""

    name = "RemoveGIT"
    command = ["rm", "-rf", "$(find -name .git)"]
    description = [name]

    def __init__(self, **kwargs):
        ShellCommand.__init__(self, **kwargs)


class PBuildPkg(ShellCommand):
    """Perfoms the building of a package with pdebuild
    It counts and logs lintian error and lintian warnings.
    On lintian errors can return FAILURE if distroconf.halt_on_lintian_error 
    it's True.
    """

    name = "PBuildPkg"
    command = pdebuild
    description = [name]

    def __init__(self, **kwargs):
        ShellCommand.__init__(self, **kwargs)

    def createSummary(self, log):
        warning_log = []
        error_log = []
        self.descriptionDone = [self.name]

        for line in log.readlines():
            if line.strip().startswith("W:"):
                warning_log.append(line)
            if line.strip().startswith("E:"):
                error_log.append(line)

        self.warnings = len(warning_log)
        self.errors = len(error_log)

        if self.warnings:
            self.addCompleteLog('Warnings', "".join(warning_log))
            self.descriptionDone.append("warn=%d" % self.warnings)

        if self.errors:
            self.addCompleteLog('Errors', "".join(error_log))
            self.descriptionDone.append("err=%d" % self.errors)
    def evaluateCommand(self, cmd):
        """
        Evaluates the result of pdebuild command.

        If lintian errors are founded it can return
        FAILURE or WARNINGS depending on distroconf.halt_on_lintian_errors
        """
        if cmd.rc != 0:
            return FAILURE
        if self.errors:
            if halt_on_lintian_error:
                return FAILURE
            else:
                return WARNINGS
        if self.warnings:
            return WARNINGS
        return SUCCESS


class PBuildPkg(ShellCommand):
    """Perfoms the building of a package with pdebuild
    It counts and logs lintian error and lintian warnings.
    On lintian errors can return FAILURE if distroconf.halt_on_lintian_error 
    it's True.
    """

    name = "PBuildPkg"
    command = pdebuild
    description = [name]

    def __init__(self, **kwargs):
        ShellCommand.__init__(self, **kwargs)

    def createSummary(self, log):
        warning_log = []
        error_log = []
        self.descriptionDone = [self.name]

        for line in log.readlines():
            if line.strip().startswith("W:"):
                warning_log.append(line)
            if line.strip().startswith("E:"):
                error_log.append(line)

        self.warnings = len(warning_log)
        self.errors = len(error_log)

        if self.warnings:
            self.addCompleteLog('Warnings', "".join(warning_log))
            self.descriptionDone.append("warn=%d" % self.warnings)

        if self.errors:
            self.addCompleteLog('Errors', "".join(error_log))
            self.descriptionDone.append("err=%d" % self.errors)
    def evaluateCommand(self, cmd):
        """
        Evaluates the result of pdebuild command.

        If lintian errors are founded it can return
        FAILURE or WARNINGS depending on distroconf.halt_on_lintian_errors
        """
        if cmd.rc != 0:
            return FAILURE
        if self.errors:
            if halt_on_lintian_error:
                return FAILURE
            else:
                return WARNINGS
        if self.warnings:
            return WARNINGS
        return SUCCESS


class GCSBuild(PBuildPkg):
    """It performs the building of a gcs package."""
    name = "GCSBuild"
    command = ["gcs_build"]
    description = [name]

    def __init__(self, **kwargs):
        PBuildPkg.__init__(self, **kwargs)


class FreightAddGecos(ShellCommand):
    name = "FreightAddGecos"
    description = [name]
    command = ["sh", "-c",\
        "freight add -c /etc/freight-gecos.conf %(package)s apt/%(codename)s;"  \
            %  {'codename': codename_gecos,\
                'package': '../*.deb'}]

    def __init__(self, **kwargs):
        ShellCommand.__init__(self, **kwargs)


class RemoveDebs(ShellCommand):
    name = "RemoveDebs"
    description = [name]
    command = ["sh", "-c","rm -f ../*.deb ../*.dsc ../*.tar.gz ../*.changes ../*.build"]

    def __init__(self, **kwargs):
        ShellCommand.__init__(self, **kwargs)	


class FreightCacheGecos(ShellCommand):
    name = "FreightCacheGecos"
    description = [name]
    command = ["sh", "-c","rm -f /var/gensys/deb-repositories/gecos/dists/%(codename)s; freight cache -c /etc/freight-gecos.conf -p /var/gensys/repo.key" \
            % {'codename': codename_gecos}]


    def __init__(self, **kwargs):
        ShellCommand.__init__(self, **kwargs)



class LiveBuildGecos(ShellCommand):
    name = "livebuild"
    command = livebuild_gecos
    description = [name]

    def __init__(self, **kwargs):
        ShellCommand.__init__(self, **kwargs)

    def createSummary(self, log):
        for line in log.readlines():
            if line.strip().startswith("Error:"):
                self.error_log = line

    def evaluateCommand(self, cmd):
        self.descriptionDone = [self.name]

        if cmd.rc == 255:
                self.descriptionDone.append(self.error_log)
                return FAILURE

        if cmd.rc != 0:
                return FAILURE

        return SUCCESS


class LiveBuildGecosLite(ShellCommand):
    name = "livebuild"
    command = livebuild_gecos_lite
    description = [name]

    def __init__(self, **kwargs):
        ShellCommand.__init__(self, **kwargs)

    def createSummary(self, log):
        for line in log.readlines():
            if line.strip().startswith("Error:"):
                self.error_log = line

    def evaluateCommand(self, cmd):
        self.descriptionDone = [self.name]

        if cmd.rc == 255:
                self.descriptionDone.append(self.error_log)
                return FAILURE

        if cmd.rc != 0:
                return FAILURE

        return SUCCESS


class SetGitRevGecos(ShellCommand):
    """
    In gcs packages, it sets the svn-revision as package version/revision.
    """
    name = "SetGitRev"
    command = ["git-revision-gecos"]
    description = [name]

    def __init__(self, **kwargs):
        ShellCommand.__init__(self, **kwargs)


class SetRepoPermsGecos(ShellCommand):
    name = "set-repository-perms"
    description = [name]
    command = ["sh", "-c", "sudo chmod -R 755 "+distroconf.repo_dir_gecos]

    def __init__(self, **kwargs):
        ShellCommand.__init__(self, **kwargs)



class SetBinaryPermsGecos(ShellCommand):
    name = "set-binary-perms-gecos"
    description = [name]
    command = ["sh", "-c", "sudo chmod -R 755 "+distroconf.rawimage_gecos]

    def __init__(self, **kwargs):
        ShellCommand.__init__(self, **kwargs)


class SetBinaryPermsGecosLite(ShellCommand):
    name = "set-binary-perms-gecos-lite"
    description = [name]
    command = ["sh", "-c", "sudo chmod -R 755 "+distroconf.rawimage_gecos_lite]

    def __init__(self, **kwargs):
        ShellCommand.__init__(self, **kwargs)

