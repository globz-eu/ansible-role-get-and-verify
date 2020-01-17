import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_dependencies(host):
    if host.system_info.codename in ['xenial', 'buster']:
        gpg = host.package('gnupg')
    else:
        gpg = host.package('gpg')

    assert gpg.is_installed


def test_gpg_key_present(host):
    assert host.run_expect([0], 'gpg --list-keys 51852D87348FFC4C')


def test_vagrant_checksum_file(host):
    vagrant_checksum = host.file('/tmp/vagrant_2.2.6_SHA256SUMS')

    assert vagrant_checksum.exists
    assert vagrant_checksum.user == 'root'
    assert vagrant_checksum.group == 'root'


def test_vagrant_sig_file(host):
    vagrant_sig = host.file('/tmp/vagrant_2.2.6_SHA256SUMS.sig')

    assert vagrant_sig.exists
    assert vagrant_sig.user == 'root'
    assert vagrant_sig.group == 'root'


def test_vagrant_deb_file(host):
    vagrant_deb = host.file('/tmp/vagrant_2.2.6_x86_64.deb')

    assert vagrant_deb.exists
    assert vagrant_deb.user == 'root'
    assert vagrant_deb.group == 'root'
