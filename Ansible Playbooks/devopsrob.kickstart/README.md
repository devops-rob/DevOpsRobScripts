devopsrob.kickstart
=========

This role installs and configures the required components for a Kickstart server.  At present, this role is for use with CentOS and Redhat linux distributions only.  PLEASE NOTE THAT THIS ROLE IS STILL UNDER DEVELOPMENT.

Requirements
------------
Requires CentOS or Redhat Linux distribution

Role Variables
--------------

Most of the Variables in this role utilise the vars_prompt ansible feature to prompt for users input at the beginning of the playbook, allowing users to customise the installation of their kickstart instance to their needs

Dependencies
------------
There are no external dependencies for this role

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

This role is written and maintained by Robert Barnes aka DevOpsRob
