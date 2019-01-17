import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ssh_server_is_installed(host):
    ssh = host.package('openssh-server')

    assert ssh.is_installed


def test_ssh_is_running(host):
    ssh = host.service('ssh')

    assert ssh.is_running
    assert ssh.is_enabled


def test_ssh_is_listening(host):
    assert host.socket("tcp://0.0.0.0:22").is_listening
