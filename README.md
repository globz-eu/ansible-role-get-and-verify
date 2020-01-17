Get and Verify
=========

Download and verify a target file. Download the target file's checksum and signature files. Verify the signature of the checksum file. Verify the checksum of the target file.

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see defaults/main.yml):

```yaml
get_download_directory: /tmp
get_base_download_url: ""
get_target_file: ""
get_verify: false
get_gpg_key: ""
get_key_server: ""
get_sig_file: ""
get_checksum_file: ""
```

## Dependencies

None.

## Example Playbook

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

```yaml
- hosts: all
  vars:
    get_download_directory: /home/user
    get_base_download_url: https://releases.hashicorp.com/vagrant/2.2.6
    get_target_file: vagrant_2.2.6_x86_64.deb
    get_verify: true
    get_gpg_key: 51852D87348FFC4C
    get_key_server: keyserver.ubuntu.com
    get_sig_file: vagrant_2.2.6_SHA256SUMS.sig
    get_checksum_file: vagrant_2.2.6_SHA256SUMS
  roles:
    - role: get-and-verify
```

## License

MIT
