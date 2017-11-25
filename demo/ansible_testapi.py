from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.plugins.callback import CallbackBase
import json


# 用来加载解析yaml文件或JSON内容,并且支持vault的解密
loader = DataLoader()

# 管理变量的类,包括主机,组,扩展等变量,之前版本是在 inventory 中的
variable_manager = VariableManager()

inventory = Inventory(loader=loader,variable_manager=variable_manager)
# 根据 inventory 加载对应变量
variable_manager.set_inventory(inventory)

class Options(object):
    '''
    这是一个公共的类,因为ad-hoc和playbook都需要一个options参数
    并且所需要拥有不同的属性,但是大部分属性都可以返回None或False
    因此用这样的一个类来省去初始化大一堆的空值的属性
    '''

    def __init__(self):
        self.connection = 'localhost'
        self.forks = 1
        self.check = False

    def __getattr__(self, name):
        return None


options = Options()

def run_adhoc():
    # 增加外部变量
    variable_manager.extra_vars={"ansible_ssh_user":"root" , "ansible_ssh_pass":"123"}
    # 构建pb, 这里很有意思, 新版本运行ad-hoc或playbook都需要构建这样的pb, 只是最后调用play的类不一样
    # :param name: 任务名,类似playbook中tasks中的name
    # :param hosts: playbook中的hosts
    # :param tasks: playbook中的tasks, 其实这就是playbook的语法, 因为tasks的值是个列表,因此可以写入多个task
    play_source = {"name":"Ansible Ad-Hoc","hosts":"192.168.5.32","gather_facts":"no","tasks":[{"action":{"module":"shell","args":"w"}}]}
    play = Play().load(play_source,variable_manager=variable_manager,loader=loader)
    tqm = None
    try:
        tqm = TaskQueueManager(
            inventory=inventory,
            variable_manager=variable_manager,
            loader=loader,
            options=options,
            passwords=None,
           # stdout_callback='results_callback',
            run_tree=False,
        )
        result = tqm.run(play)
        print(result)
    finally:
        if tqm is not None:
            tqm.cleanup()

def run_playbook():
     playbooks=['task.yaml'] # 这里是一个列表, 因此可以运行多个playbook
     variable_manager.extra_vars={"ansible_ssh_user":"root" , "ansible_ssh_pass":"123"} # 增加外部变量
     pb = PlaybookExecutor(playbooks=playbooks, inventory=inventory, variable_manager=variable_manager, loader=loader, options=options, passwords=None)
     result = pb.run()
     print(result)


if __name__ == '__main__':
    run_adhoc()
    #run_playbook()

