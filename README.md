# ansible-role-secure-openssh-server
[![Build Status](https://travis-ci.org/elnappo/ansible-role-secure-openssh-server.svg?branch=master)](https://travis-ci.org/elnappo/ansible-role-secure-openssh-server) [![Ansible Galaxy](https://img.shields.io/badge/galaxy-elnappo.secure--openssh--server-blue.svg?style=flat)](https://galaxy.ansible.com/elnappo/secure-openssh-server/)

Set up a secure config for OpenSSH Server >= 6.5. This playbook extends your sshd config file instead of replacing it.

* Disable SSH version 1
* Disable RSAAuthentication (only available in version 1)
* Don't allow empty passwords
* Allow root login only without password
* Use StrictModes
* Allow only KexAlgorithms, Ciphers and MACs which where recommended by [Secure Secure Shell](https://stribika.github.io/2015/01/04/secure-secure-shell.html)
* Removes DSA and ECDSA host keys by default. Change `ssh_remove_deprecated_server_keys` if this is not what you want
* Regenerates RSA host key if shorter than 4096 bits (default)
* Disable password login by default which also sets `MaxAuthTries 1` and `LoginGraceTime 30`
shields.io
#### Recommended `~/.ssh/config`, `/etc/ssh/ssh_config`
```
Host *
    HashKnownHosts yes
    PasswordAuthentication no
    PubkeyAuthentication yes
    ChallengeResponseAuthentication no
    HostKeyAlgorithms ssh-ed25519-cert-v01@openssh.com,ssh-rsa-cert-v01@openssh.com,ssh-ed25519,ssh-rsa,ecdsa-sha2-nistp521-cert-v01@openssh.com,ecdsa-sha2-nistp384-cert-v01@openssh.com,ecdsa-sha2-nistp256-cert-v01@openssh.com,ecdsa-sha2-nistp521,ecdsa-sha2-nistp384,ecdsa-sha2-nistp256
    KexAlgorithms curve25519-sha256@libssh.org,diffie-hellman-group-exchange-sha256
    Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr
    MACs hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com,hmac-ripemd160-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-512,hmac-sha2-256,hmac-ripemd160,umac-128@openssh.com
```

alias for legacy connections: `alias ssh_ignore="ssh -F /dev/null"`

## Inspired by
* [Secure Secure Shell](https://stribika.github.io/2015/01/04/secure-secure-shell.html)
* [Mozilla Wiki - Security/Guidelines/OpenSSH](https://wiki.mozilla.org/Security/Guidelines/OpenSSH)
* [BetterCrypto](https://github.com/BetterCrypto/Applied-Crypto-Hardening)
* [Manpage sshd_config](http://www.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man5/sshd_config.5)

## Requirements
* Ubuntu or Debian
* OpenSSH Server >= 6.5 (which is in Ubuntu >= 14.04 and Debian >= 8)

## Role Variables
* `ssh_sshd_config_dir: /etc/ssh/`
* `ssh_sshd_config_path: "{{ ssh_sshd_config_dir }}sshd_config"`
* `ssh_permit_root_login: "without-password"` quotes are mandatory!
* `ssh_disable_password_login: true`
* `ssh_remove_deprecated_server_keys: true` disables DSA, ECDSA and regenerate RSA key if <`ssh_host_rsa_key_length`
* `ssh_host_rsa_key_length: 4096`
* `ssh_setup_ufw: true`
* `ssh_port: 22`

## Dependencies
None.

## Example Playbook

```yaml
- hosts: server
  remote_user: root
  vars:
    - ssh_remove_deprecated_server_keys: false
    - ssh_port: 1813
  roles:
    - { role: elnappo.secure_openssh_server }
```

## License
MIT

## Author Information
elnappo <elnappo@nerdpol.io>
