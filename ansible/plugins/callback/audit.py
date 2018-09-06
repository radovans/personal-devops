from datetime import datetime
import os
from ansible.plugins.callback import CallbackBase
from ansible.config.manager import ConfigManager

class CallbackModule(CallbackBase):
  CALLBACK_VERSION = 1.0
  CALLBACK_TYPE = 'notification'
  CALLBACK_NAME = 'audit'
  CALLBACK_NEEDS_WHITELIST = True

  def __init__(self):
    # make sure the expected objects are present, calling the base's __init__
    super(CallbackModule, self).__init__()

    # start the timer when the plugin is loaded, the first play should start a few milliseconds after.
    self.start_time = datetime.now()
    # self.set_option('log_path', './logs/another.log')
    # os.environ['ANSIBLE_LOG_PATH'] = './logs/another.log'
    # config = ConfigManager()

  # def v2_playbook_on_start(self, playbook):
  # def playbook_on_setup(self):
    # self.set_option('log_path', './logs/another.log')
    # self._dis
    # print os.environ
    # os.environ['ANSIBLE_LOG_PATH'] = './logs/another.log'
