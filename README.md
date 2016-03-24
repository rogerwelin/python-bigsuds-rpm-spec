# python-bigsuds-rpm-spec

## What
A spec file how to build an rpm of F5:s bigsuds library that are used to communicate with F5 Networks iControl API

## Why
Pip includes bigsuds, but if you are behind a corporate firewall or prefer to roll your own rpm:s and/or keep track of your dependencies using this spec file is a good idea. Another reason is that if you are using the Ansible modules __bigip__ to provision F5 bigsuds are a requirement

## Tested on
- CentOS 6
- RHEL 6

Should also work equally well on CentOS/RHEL 7 but it's not tested

## More info/reading
- http://docs.ansible.com/ansible/bigip_node_module.html
- https://devcentral.f5.com/articles/getting-started-with-bigsuds-ndasha-new-python-library-for-icontrol

