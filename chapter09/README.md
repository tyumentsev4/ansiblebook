For the scripts in this directory, we use Vagrant's Ansible support to do all of
the provisioning, so you just need to do:

    cd playbooks
    vagrant up

The Makefile has scenarios, checks and a test. `make all` will do a full test-cycle. Type `make help` for help.

Then point your browser to: <http://192.168.56.10.nip.io> or
<https://www.192.168.56.10.nip.io>. You'll get a security warning if you use the
https site since it's a self-signed certificate, this is normal.
