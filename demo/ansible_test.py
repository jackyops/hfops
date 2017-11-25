from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.executor.playbook_executor import PlaybookExecutor

loader = DataLoader()

variable_manager = VariableManager()

#inventory = Inventory(loader=loader,variable_manager=variable_manager,host_list=['192.168.5.10','192.168.5.32'])
inventory = Inventory(loader=loader,variable_manager=variable_manager,host_list=['all'])
variable_manager.set_inventory(inventory)

passwords=dict(conn_pass='123')

Options = namedtuple('Options',
                     ['connection',
                      'remote_user',
                      'ask_sudo_pass',
                      'verbosity',
                      'ack_pass',
                      'module_path',
                      'forks',
                      'become',
                      'become_method',
                      'become_user',
                      'check',
                      'listhosts',
                      'listtasks',
                      'listtags',
                      'syntax',
                      'sudo_user',
                      'sudo'])
# 初始化需要的对象
options = Options(connection='smart',
                       remote_user='root',
                       ack_pass=None,
                       sudo_user='root',
                       forks=5,
                       sudo='yes',
                       ask_sudo_pass=False,
                       verbosity=5,
                       module_path=None,
                       become=True,
                       become_method='sudo',
                       become_user='root',
                       check=None,
                       listhosts=None,
                       listtasks=None,
                       listtags=None,
                       syntax=None)

playbook = PlaybookExecutor(playbooks=['test.yml'],inventory=inventory,variable_manager=variable_manager,loader=loader,options=options,passwords=passwords)

playbook.run()