# ansible-role-secure-openssh-server [![Build Status](https://travis-ci.org/elnappo/ansible-role-secure-openssh-server.svg?branch=master)](https://travis-ci.org/elnappo/ansible-role-secure-openssh-server)
Set up a secure config for OpenSSH Server >= 6.5. This playbook extends your sshd config file instead of replacing it. 

* Disable SSH version 1
* Disable RSAAuthentication (only available in version 1)
* Don't allow empty passwords
* Allow root login only without password
* Use StrictModes
* Allow only KexAlgorithms, Ciphers and MACs which where recommended by [Secure Secure Shell](https://stribika.github.io/2015/01/04/secure-secure-shell.html)
* Removes DSA and ECDSA host keys by default. Change  `ssh_remove_deprecated_server_keys` if this is not what you want.
* Disable password login by default which also sets `MaxAuthTries 1` and `LoginGraceTime 30`

#### Recommended `~/.ssh/config`, `/etc/ssh/ssh_config`
```
Host github.com
    KexAlgorithms curve25519-sha256@libssh.org,diffie-hellman-group-exchange-sha256,diffie-hellman-group-exchange-sha1,diffie-hellman-group14-sha1
    
Host *
	PasswordAuthentication no
	PubkeyAuthentication yes
	ChallengeResponseAuthentication no
	KexAlgorithms curve25519-sha256@libssh.org,diffie-hellman-group-exchange-sha256
	Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr
	MACs hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com,hmac-ripemd160-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-512,hmac-sha2-256,hmac-ripemd160,umac-128@openssh.com
```

## Inspired by
* [Secure Secure Shell](https://stribika.github.io/2015/01/04/secure-secure-shell.html)
* [BetterCrypto](https://github.com/BetterCrypto/Applied-Crypto-Hardening)
* [Manpage sshd_config](http://www.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man5/sshd_config.5)

## Requirements
* Ubuntu or Debian
* OpenSSH Server >= 6.5 (which is in Ubuntu >= 14.04 and Debian >=8)

## Role Variables
* `ssh_sshd_config_dir: /etc/ssh/`
* `ssh_sshd_config_path: "{{ ssh_sshd_config_dir }}sshd_config"`
* `ssh_permit_root_login: without-password`
* `ssh_disable_password_login: true`
* `ssh_remove_deprecated_server_keys: true` disables DSA and ECDSA
* `ssh_setup_ufw: true`
* `ssh_port: 22`

## Dependencies
None.

## Example Playbook
    - hosts: server
	  remote_user: root
	  vars:
	    - ssh_remove_deprecated_server_keys: false
	    - ssh_port: 1813
	  roles:
	    - { role: elnappoo.secure-openssh-server }

## License
MIT

## Author Information
elnappo <elnappo@nerdpol.io>
