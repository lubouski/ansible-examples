from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.action import ActionBase
import socket

class ActionModule(ActionBase):

    def run(self, tmp=None, task_vars=None):

        if task_vars is None:
            task_vars = dict()

        result = super(ActionModule, self).run(tmp, task_vars)

        image_name = self._task.args.get('image_name', None)
        
        new_module_args = dict()
	new_module_args.update(
            dict(
                image_name=image_name,
            ),
        )

        result.update(
            self._execute_module(
                module_name='docker_module',
                module_args=new_module_args,
            )
        )

        return result

