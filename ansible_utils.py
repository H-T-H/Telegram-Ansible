import ansible_runner
import yaml

def run_ansible_task(private_data_dir='.', playbook='./playbook.yaml', inventory='./hosts.ini'):
    # 设置 Ansible Runner 配置
    r = ansible_runner.run(private_data_dir=private_data_dir, playbook=playbook, inventory=inventory)
    return r.status
    

# 测试函数
if __name__ == "__main__":
    result = run_ansible_task()
    print(result)
