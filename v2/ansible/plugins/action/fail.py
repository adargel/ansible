# (c) 2012-2014, Michael DeHaan <michael.dehaan@gmail.com>
# (c) 2012, Dag Wieers <dag@wieers.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

from ansible.plugins.action import ActionBase

class ActionModule(ActionBase):
    ''' Fail with custom message '''

    TRANSFERS_FILES = False

    def run(self, tmp=None, task_vars=dict()):

        msg = 'Failed as requested from task'
        if self._task.args and 'msg' in self._task.args:
            msg = self._task.args.get('msg')

        return dict(failed=True, msg=msg)

