# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 22:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ansible_CallBack_Model_Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True, verbose_name='输出内容')),
            ],
        ),
        migrations.CreateModel(
            name='Ansible_CallBack_PlayBook_Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True, verbose_name='输出内容')),
            ],
        ),
        migrations.CreateModel(
            name='Ansible_Playbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playbook_name', models.CharField(max_length=50, unique=True, verbose_name='剧本名称')),
                ('playbook_desc', models.CharField(blank=True, max_length=200, null=True, verbose_name='功能描述')),
                ('playbook_vars', models.TextField(blank=True, null=True, verbose_name='模块参数')),
                ('playbook_uuid', models.CharField(max_length=50, verbose_name='唯一id')),
                ('playbook_server_model', models.CharField(blank=True, choices=[('service', 'service'), ('group', 'group'), ('custom', 'custom')], max_length=10, null=True, verbose_name='服务器选择类型')),
                ('playbook_server_value', models.SmallIntegerField(blank=True, null=True, verbose_name='服务器选择类型值')),
                ('playbook_file', models.FileField(upload_to='./upload/playbook/', verbose_name='剧本路径')),
                ('playbook_auth_group', models.SmallIntegerField(blank=True, null=True, verbose_name='授权组')),
                ('playbook_auth_user', models.SmallIntegerField(blank=True, null=True, verbose_name='授权用户')),
            ],
            options={
                'db_table': 'opsmanage_ansible_playbook',
                'verbose_name_plural': 'Ansible剧本配置表',
                'permissions': (('can_read_ansible_playbook', '读取Ansible剧本权限'), ('can_change_ansible_playbook', '更改Ansible剧本权限'), ('can_add_ansible_playbook', '添加Ansible剧本权限'), ('can_delete_ansible_playbook', '删除Ansible剧本权限')),
                'verbose_name': 'Ansible剧本配置表',
            },
        ),
        migrations.CreateModel(
            name='Ansible_Playbook_Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playbook_server', models.CharField(blank=True, max_length=100, null=True, verbose_name='目标服务器')),
                ('playbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='server_number', to='ops.Ansible_Playbook')),
            ],
            options={
                'db_table': 'opsmanage_ansible_playbook_number',
                'verbose_name_plural': 'Ansible剧本成员表',
                'permissions': (('can_read_ansible_playbook_number', '读取Ansible剧本成员权限'), ('can_change_ansible_playbook_number', '更改Ansible剧本成员权限'), ('can_add_ansible_playbook_number', '添加Ansible剧本成员权限'), ('can_delete_ansible_playbook_number', '删除Ansible剧本成员权限')),
                'verbose_name': 'Ansible剧本成员表',
            },
        ),
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assets_type', models.CharField(choices=[('server', '服务器'), ('switch', '交换机'), ('route', '路由器'), ('printer', '打印机'), ('scanner', '扫描仪'), ('firewall', '防火墙'), ('storage', '存储设备'), ('wifi', '无线设备')], default='server', max_length=100, verbose_name='资产类型')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='资产编号')),
                ('sn', models.CharField(max_length=100, verbose_name='设备序列号')),
                ('buy_time', models.DateField(blank=True, null=True, verbose_name='购买时间')),
                ('expire_date', models.DateField(blank=True, null=True, verbose_name='过保修期')),
                ('buy_user', models.CharField(blank=True, max_length=100, null=True, verbose_name='购买人')),
                ('management_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='管理IP')),
                ('manufacturer', models.CharField(blank=True, max_length=100, null=True, verbose_name='制造商')),
                ('provider', models.CharField(blank=True, max_length=100, null=True, verbose_name='供货商')),
                ('model', models.CharField(blank=True, max_length=100, null=True, verbose_name='资产型号')),
                ('status', models.SmallIntegerField(blank=True, null=True, verbose_name='状态')),
                ('put_zone', models.SmallIntegerField(blank=True, null=True, verbose_name='放置区域')),
                ('group', models.SmallIntegerField(blank=True, null=True, verbose_name='使用组')),
                ('business', models.SmallIntegerField(blank=True, null=True, verbose_name='业务类型')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'opsmanage_assets',
                'verbose_name_plural': '总资产表',
                'permissions': (('can_read_assets', '读取资产权限'), ('can_change_assets', '更改资产权限'), ('can_add_assets', '添加资产权限'), ('can_delete_assets', '删除资产权限')),
                'verbose_name': '总资产表',
            },
        ),
        migrations.CreateModel(
            name='Cron_Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cron_minute', models.CharField(default=None, max_length=10, verbose_name='分')),
                ('cron_hour', models.CharField(default=None, max_length=10, verbose_name='时')),
                ('cron_day', models.CharField(default=None, max_length=10, verbose_name='天')),
                ('cron_week', models.CharField(default=None, max_length=10, verbose_name='周')),
                ('cron_month', models.CharField(default=None, max_length=10, verbose_name='月')),
                ('cron_user', models.CharField(default=None, max_length=50, verbose_name='任务用户')),
                ('cron_name', models.CharField(default=None, max_length=100, verbose_name='任务名称')),
                ('cron_desc', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='任务描述')),
                ('cron_command', models.CharField(default=None, max_length=200, verbose_name='任务参数')),
                ('cron_script', models.FileField(blank=True, default=None, null=True, upload_to='./upload/cron/', verbose_name='脚本路径')),
                ('cron_script_path', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='脚本路径')),
                ('cron_status', models.SmallIntegerField(default=None, verbose_name='任务状态')),
            ],
            options={
                'db_table': 'opsmanage_cron_config',
                'verbose_name_plural': '任务配置表',
                'permissions': (('can_read_cron_config', '读取任务配置权限'), ('can_change_cron_config', '更改任务配置权限'), ('can_add_cron_config', '添加任务配置权限'), ('can_delete_cron_config', '删除任务配置权限')),
                'verbose_name': '任务配置表',
            },
        ),
        migrations.CreateModel(
            name='Disk_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_volume', models.CharField(blank=True, max_length=100, null=True, verbose_name='硬盘容量')),
                ('device_status', models.CharField(blank=True, max_length=100, null=True, verbose_name='硬盘状态')),
                ('device_model', models.CharField(blank=True, max_length=100, null=True, verbose_name='硬盘型号')),
                ('device_brand', models.CharField(blank=True, max_length=100, null=True, verbose_name='硬盘生产商')),
                ('device_serial', models.CharField(blank=True, max_length=100, null=True, verbose_name='硬盘序列号')),
                ('device_slot', models.SmallIntegerField(blank=True, null=True, verbose_name='硬盘插槽')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('assets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ops.Assets')),
            ],
            options={
                'db_table': 'opsmanage_disk_assets',
                'verbose_name_plural': '磁盘资产表',
                'permissions': (('can_read_disk_assets', '读取磁盘资产权限'), ('can_change_disk_assets', '更改磁盘资产权限'), ('can_add_disk_assets', '添加磁盘资产权限'), ('can_delete_disk_assets', '删除磁盘资产权限')),
                'verbose_name': '磁盘资产表',
            },
        ),
        migrations.CreateModel(
            name='Email_Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=100, verbose_name='部署站点')),
                ('host', models.CharField(max_length=100, verbose_name='邮件发送服务器')),
                ('port', models.SmallIntegerField(verbose_name='邮件发送服务器端口')),
                ('user', models.CharField(max_length=100, verbose_name='发送用户账户')),
                ('passwd', models.CharField(max_length=100, verbose_name='发送用户密码')),
                ('subject', models.CharField(default='[OPS]', max_length=100, verbose_name='发送邮件主题标识')),
                ('cc_user', models.TextField(blank=True, null=True, verbose_name='抄送用户列表')),
            ],
            options={
                'db_table': 'opsmanage_email_config',
            },
        ),
        migrations.CreateModel(
            name='Global_Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ansible_model', models.SmallIntegerField(blank=True, null=True, verbose_name='是否开启ansible模块操作记录')),
                ('ansible_playbook', models.SmallIntegerField(blank=True, null=True, verbose_name='是否开启ansible剧本操作记录')),
                ('cron', models.SmallIntegerField(blank=True, null=True, verbose_name='是否开启计划任务操作记录')),
                ('project', models.SmallIntegerField(blank=True, null=True, verbose_name='是否开启项目操作记录')),
                ('assets', models.SmallIntegerField(blank=True, null=True, verbose_name='是否开启资产操作记录')),
                ('server', models.SmallIntegerField(blank=True, null=True, verbose_name='是否开启服务器命令记录')),
                ('email', models.SmallIntegerField(blank=True, null=True, verbose_name='是否开启邮件通知')),
            ],
            options={
                'db_table': 'opsmanage_global_config',
            },
        ),
        migrations.CreateModel(
            name='Line_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'opsmanage_line_assets',
                'verbose_name_plural': '出口线路资产表',
                'permissions': (('can_read_line_assets', '读取出口线路资产权限'), ('can_change_line_assetss', '更改出口线路资产权限'), ('can_add_line_assets', '添加出口线路资产权限'), ('can_delete_line_assets', '删除出口线路资产权限')),
                'verbose_name': '出口线路资产表',
            },
        ),
        migrations.CreateModel(
            name='Log_Ansible_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans_user', models.CharField(default=None, max_length=50, verbose_name='使用用户')),
                ('ans_model', models.CharField(default=None, max_length=100, verbose_name='模块名称')),
                ('ans_args', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='模块参数')),
                ('ans_server', models.TextField(default=None, verbose_name='服务器')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='执行时间')),
            ],
            options={
                'db_table': 'opsmanage_log_ansible_model',
                'verbose_name_plural': 'Ansible模块执行记录表',
                'permissions': (('can_read_log_ansible_model', '读取Ansible模块执行记录权限'), ('can_change_log_ansible_model', '更改Ansible模块执行记录权限'), ('can_add_log_ansible_model', '添加Ansible模块执行记录权限'), ('can_delete_log_ansible_model', '删除Ansible模块执行记录权限')),
                'verbose_name': 'Ansible模块执行记录表',
            },
        ),
        migrations.CreateModel(
            name='Log_Ansible_Playbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans_id', models.IntegerField(blank=True, default=None, null=True, verbose_name='id')),
                ('ans_user', models.CharField(default=None, max_length=50, verbose_name='使用用户')),
                ('ans_name', models.CharField(default=None, max_length=100, verbose_name='模块名称')),
                ('ans_content', models.CharField(default=None, max_length=100)),
                ('ans_server', models.TextField(default=None, verbose_name='服务器')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='执行时间')),
            ],
            options={
                'db_table': 'opsmanage_log_ansible_playbook',
                'verbose_name_plural': 'Ansible剧本操作记录表',
                'verbose_name': 'Ansible剧本操作记录表',
            },
        ),
        migrations.CreateModel(
            name='Log_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assets_id', models.IntegerField(blank=True, default=None, null=True, verbose_name='资产类型id')),
                ('assets_user', models.CharField(default=None, max_length=50, verbose_name='操作用户')),
                ('assets_content', models.CharField(default=None, max_length=100, verbose_name='名称')),
                ('assets_type', models.CharField(default=None, max_length=50)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='执行时间')),
            ],
            options={
                'db_table': 'opsmanage_log_assets',
                'verbose_name_plural': '项目配置操作记录表',
                'verbose_name': '项目配置操作记录表',
            },
        ),
        migrations.CreateModel(
            name='Log_Cron_Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cron_id', models.IntegerField(blank=True, default=None, null=True, verbose_name='id')),
                ('cron_user', models.CharField(default=None, max_length=50, verbose_name='操作用户')),
                ('cron_name', models.CharField(default=None, max_length=100, verbose_name='名称')),
                ('cron_content', models.CharField(default=None, max_length=100)),
                ('cron_server', models.CharField(default=None, max_length=100)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='执行时间')),
            ],
            options={
                'db_table': 'opsmanage_log_cron_config',
                'verbose_name_plural': '任务配置操作记录表',
                'verbose_name': '任务配置操作记录表',
            },
        ),
        migrations.CreateModel(
            name='Log_Project_Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.IntegerField(blank=True, default=None, null=True, verbose_name='资产类型id')),
                ('project_user', models.CharField(default=None, max_length=50, verbose_name='操作用户')),
                ('project_name', models.CharField(default=None, max_length=100, verbose_name='名称')),
                ('project_content', models.CharField(default=None, max_length=100)),
                ('project_branch', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='执行时间')),
            ],
            options={
                'db_table': 'opsmanage_log_project_config',
                'verbose_name_plural': '项目配置操作记录表',
                'verbose_name': '项目配置操作记录表',
            },
        ),
        migrations.CreateModel(
            name='Network_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bandwidth', models.CharField(blank=True, max_length=100, null=True, verbose_name='背板带宽')),
                ('ip', models.CharField(blank=True, max_length=100, null=True, verbose_name='管理ip')),
                ('port_number', models.SmallIntegerField(blank=True, null=True, verbose_name='端口个数')),
                ('firmware', models.CharField(blank=True, max_length=100, null=True, verbose_name='固件版本')),
                ('cpu', models.CharField(blank=True, max_length=100, null=True, verbose_name='cpu型号')),
                ('stone', models.CharField(blank=True, max_length=100, null=True, verbose_name='内存大小')),
                ('configure_detail', models.TextField(blank=True, max_length=100, null=True, verbose_name='配置说明')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('assets', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ops.Assets')),
            ],
            options={
                'db_table': 'opsmanage_network_assets',
                'verbose_name_plural': '网络资产表',
                'permissions': (('can_read_network_assets', '读取网络资产权限'), ('can_change_network_assets', '更改网络资产权限'), ('can_add_network_assets', '添加网络资产权限'), ('can_delete_network_assets', '删除网络资产权限')),
                'verbose_name': '网络资产表',
            },
        ),
        migrations.CreateModel(
            name='NetworkCard_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('macaddress', models.CharField(max_length=64, unique=True, verbose_name='MAC')),
                ('ipaddress', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP')),
                ('device_model', models.CharField(blank=True, max_length=100, null=True, verbose_name='网卡型号')),
                ('device_brand', models.CharField(blank=True, max_length=100, null=True, verbose_name='网卡生产商')),
                ('device_status', models.CharField(blank=True, max_length=100, null=True, verbose_name='网卡状态')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('assets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ops.Assets')),
            ],
            options={
                'db_table': 'opsmanage_networkcard_assets',
                'verbose_name_plural': '网卡资产表',
                'permissions': (('can_read_networkcard_assets', '读取网卡资产权限'), ('can_change_networkcard_assets', '更改网卡资产权限'), ('can_add_networkcard_assets', '添加网卡资产权限'), ('can_delete_networkcard_assets', '删除网卡资产权限')),
                'verbose_name': '网卡资产表',
            },
        ),
        migrations.CreateModel(
            name='Project_Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_env', models.CharField(default=None, max_length=50, verbose_name='项目环境')),
                ('project_name', models.CharField(default=None, max_length=100, verbose_name='项目名称')),
                ('project_local_command', models.TextField(blank=True, default=None, null=True, verbose_name='部署服务器要执行的命令')),
                ('project_repo_dir', models.CharField(default=None, max_length=100, verbose_name='本地仓库目录')),
                ('project_dir', models.CharField(default=None, max_length=100, verbose_name='代码目录')),
                ('project_exclude', models.TextField(blank=True, default=None, null=True, verbose_name='排除文件')),
                ('project_address', models.CharField(default=None, max_length=100, verbose_name='版本仓库地址')),
                ('project_uuid', models.CharField(max_length=50, verbose_name='唯一id')),
                ('project_repo_user', models.CharField(blank=True, max_length=50, null=True, verbose_name='仓库用户名')),
                ('project_repo_passwd', models.CharField(blank=True, max_length=50, null=True, verbose_name='仓库密码')),
                ('project_repertory', models.CharField(choices=[('git', 'git'), ('svn', 'svn')], default=None, max_length=10, verbose_name='仓库类型')),
                ('project_status', models.SmallIntegerField(blank=True, default=None, null=True, verbose_name='是否激活')),
                ('project_remote_command', models.TextField(blank=True, default=None, null=True, verbose_name='部署之后执行的命令')),
                ('project_user', models.CharField(default=None, max_length=50, verbose_name='项目文件宿主')),
                ('project_model', models.CharField(choices=[('branch', 'branch'), ('tag', 'tag')], default=None, max_length=10, verbose_name='上线类型')),
                ('project_audit_group', models.SmallIntegerField(blank=True, default=None, null=True, verbose_name='项目授权组')),
            ],
            options={
                'db_table': 'opsmanage_project_config',
                'verbose_name_plural': '项目管理表',
                'permissions': (('can_read_project_config', '读取项目权限'), ('can_change_project_config', '更改项目权限'), ('can_add_project_config', '添加项目权限'), ('can_delete_project_config', '删除项目权限')),
                'verbose_name': '项目管理表',
            },
        ),
        migrations.CreateModel(
            name='Project_Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server', models.CharField(default=None, max_length=100, verbose_name='服务器IP')),
                ('dir', models.CharField(default=None, max_length=100, verbose_name='项目目录')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_number', to='ops.Project_Config')),
            ],
            options={
                'db_table': 'opsmanage_project_number',
                'verbose_name_plural': '项目成员表',
                'permissions': (('can_read_project_number', '读取项目成员权限'), ('can_change_project_number', '更改项目成员权限'), ('can_add_project_number', '添加项目成员权限'), ('can_delete_project_number', '删除项目成员权限')),
                'verbose_name': '项目成员表',
            },
        ),
        migrations.CreateModel(
            name='Project_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_user', models.CharField(max_length=30, verbose_name='工单申请人')),
                ('order_subject', models.CharField(max_length=200, verbose_name='工单申请主题')),
                ('order_content', models.TextField(verbose_name='工单申请内容')),
                ('order_branch', models.CharField(blank=True, max_length=50, null=True, verbose_name='分支版本')),
                ('order_comid', models.CharField(blank=True, max_length=100, null=True, verbose_name='版本id')),
                ('order_tag', models.CharField(blank=True, max_length=50, null=True, verbose_name='标签')),
                ('order_audit', models.CharField(max_length=30, verbose_name='部署指派人')),
                ('order_status', models.IntegerField(choices=[(0, '已通过'), (1, '已拒绝'), (2, '审核中'), (3, '已部署')], default='审核中', verbose_name='工单状态')),
                ('order_level', models.IntegerField(choices=[(0, '非紧急'), (1, '紧急')], default='非紧急', verbose_name='工单紧急程度')),
                ('order_cancel', models.TextField(blank=True, null=True, verbose_name='取消原因')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='工单发布时间')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='工单最后修改时间')),
                ('order_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ops.Project_Config', verbose_name='项目id')),
            ],
            options={
                'db_table': 'opsmanage_project_order',
                'verbose_name_plural': '项目部署工单表',
                'permissions': (('can_read_project_order', '读取项目部署权限'), ('can_change_project_order', '更改项目部署权限'), ('can_add_project_order', '添加项目部署权限'), ('can_delete_project_order', '删除项目部署权限')),
                'verbose_name': '项目部署工单表',
            },
        ),
        migrations.CreateModel(
            name='Raid_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raid_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'opsmanage_raid_assets',
                'verbose_name_plural': 'Raid资产表',
                'permissions': (('can_read_raid_assets', '读取Raid资产权限'), ('can_change_raid_assets', '更改Raid资产权限'), ('can_add_raid_assets', '添加Raid资产权限'), ('can_delete_raid_assets', '删除Raid资产权限')),
                'verbose_name': 'Raid资产表',
            },
        ),
        migrations.CreateModel(
            name='Ram_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_model', models.CharField(blank=True, max_length=100, null=True, verbose_name='内存型号')),
                ('device_volume', models.CharField(blank=True, max_length=100, null=True, verbose_name='内存容量')),
                ('device_brand', models.CharField(blank=True, max_length=100, null=True, verbose_name='内存生产商')),
                ('device_slot', models.SmallIntegerField(blank=True, null=True, verbose_name='内存插槽')),
                ('device_status', models.CharField(blank=True, max_length=100, null=True, verbose_name='内存状态')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('assets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ops.Assets')),
            ],
            options={
                'db_table': 'opsmanage_ram_assets',
                'verbose_name_plural': '内存资产表',
                'permissions': (('can_read_ram_assets', '读取内存资产权限'), ('can_change_ram_assets', '更改内存资产权限'), ('can_add_ram_assets', '添加内存资产权限'), ('can_delete_ram_assets', '删除内存资产权限')),
                'verbose_name': '内存资产表',
            },
        ),
        migrations.CreateModel(
            name='Server_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('hostname', models.CharField(blank=True, max_length=100, null=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('passwd', models.CharField(blank=True, max_length=100, null=True)),
                ('keyfile', models.SmallIntegerField(blank=True, null=True)),
                ('port', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True)),
                ('line', models.SmallIntegerField(blank=True, null=True)),
                ('cpu', models.CharField(blank=True, max_length=100, null=True)),
                ('cpu_number', models.SmallIntegerField(blank=True, null=True)),
                ('vcpu_number', models.SmallIntegerField(blank=True, null=True)),
                ('cpu_core', models.SmallIntegerField(blank=True, null=True)),
                ('disk_total', models.CharField(blank=True, max_length=100, null=True)),
                ('ram_total', models.IntegerField(blank=True, null=True)),
                ('kernel', models.CharField(blank=True, max_length=100, null=True)),
                ('selinux', models.CharField(blank=True, max_length=100, null=True)),
                ('swap', models.CharField(blank=True, max_length=100, null=True)),
                ('raid', models.SmallIntegerField(blank=True, null=True)),
                ('system', models.CharField(blank=True, max_length=100, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('assets', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ops.Assets')),
            ],
            options={
                'db_table': 'opsmanage_server_assets',
                'verbose_name_plural': '服务器资产表',
                'permissions': (('can_read_server_assets', '读取服务器资产权限'), ('can_change_server_assets', '更改服务器资产权限'), ('can_add_server_assets', '添加服务器资产权限'), ('can_delete_server_assets', '删除服务器资产权限')),
                'verbose_name': '服务器资产表',
            },
        ),
        migrations.CreateModel(
            name='Server_Command_Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, verbose_name='远程用户')),
                ('server', models.CharField(max_length=50, verbose_name='服务器IP')),
                ('client', models.CharField(blank=True, max_length=50, null=True, verbose_name='客户机IP')),
                ('command', models.TextField(blank=True, null=True, verbose_name='历史命令')),
                ('etime', models.CharField(max_length=50, unique=True, verbose_name='命令执行时间')),
            ],
            options={
                'db_table': 'opsmanage_server_command_record',
                'verbose_name_plural': '服务器操作日志表',
                'permissions': (('can_read_server_command_record', '读取服务器操作日志权限'), ('can_change_server_command_record', '更改服务器操作日志权限'), ('can_add_server_command_record', '添加服务器操作日志权限'), ('can_delete_server_command_record', '删除服务器操作日志权限')),
                'verbose_name': '服务器操作日志表',
            },
        ),
        migrations.CreateModel(
            name='Service_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'opsmanage_service_assets',
                'verbose_name_plural': '业务分组表',
                'permissions': (('can_read_service_assets', '读取业务资产权限'), ('can_change_service_assets', '更改业务资产权限'), ('can_add_service_assets', '添加业务资产权限'), ('can_delete_service_assets', '删除业务资产权限')),
                'verbose_name': '业务分组表',
            },
        ),
        migrations.CreateModel(
            name='Zone_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'opsmanage_zone_assets',
                'verbose_name_plural': '机房资产表',
                'permissions': (('can_read_zone_assets', '读取机房资产权限'), ('can_change_zone_assets', '更改机房资产权限'), ('can_add_zone_assets', '添加机房资产权限'), ('can_delete_zone_assets', '删除机房资产权限')),
                'verbose_name': '机房资产表',
            },
        ),
        migrations.AlterUniqueTogether(
            name='project_config',
            unique_together=set([('project_env', 'project_name')]),
        ),
        migrations.AddField(
            model_name='cron_config',
            name='cron_server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ops.Server_Assets'),
        ),
        migrations.AddField(
            model_name='ansible_callback_playbook_result',
            name='logId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ops.Log_Ansible_Playbook'),
        ),
        migrations.AddField(
            model_name='ansible_callback_model_result',
            name='logId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ops.Log_Ansible_Model'),
        ),
        migrations.AlterUniqueTogether(
            name='ram_assets',
            unique_together=set([('assets', 'device_slot')]),
        ),
        migrations.AlterUniqueTogether(
            name='project_order',
            unique_together=set([('order_project', 'order_subject', 'order_user')]),
        ),
        migrations.AlterUniqueTogether(
            name='project_number',
            unique_together=set([('project', 'server')]),
        ),
        migrations.AlterUniqueTogether(
            name='disk_assets',
            unique_together=set([('assets', 'device_slot')]),
        ),
        migrations.AlterUniqueTogether(
            name='cron_config',
            unique_together=set([('cron_name', 'cron_server', 'cron_user')]),
        ),
    ]
