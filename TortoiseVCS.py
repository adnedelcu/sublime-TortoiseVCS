import sublime
import sublime_plugin
import os
import os.path
import subprocess

class TortoiseVcsCommand(sublime_plugin.WindowCommand):
    def run(self, cmd, paths=None, isHung=False):
        dir = self.getPath(paths)

        if not dir:
            return

        settings = sublime.load_settings('TortoiseVCS.sublime-settings')
        git_tortoiseproc_path = settings.get('git_tortoiseproc_path')
        svn_tortoiseproc_path = settings.get('svn_tortoiseproc_path')

        if not os.path.isfile(git_tortoiseproc_path):

