from __future__ import with_statement
from fabric.api import *
# from fabric.contrib.console import confirm

env.hosts = ['warrior@127.0.0.1']
# env['password'] = ''

# def test():
#     with settings(warn_only=True):
#         result = local('./manage.py test my_app', capture=True)
#     if result.failed and not confirm("Tests failed. Continue anyway?"):
#         abort("Aborting at user request.")


def commit():
    local('hg add && hg commit -m " "')
    # local("hg add && hg commit")


def push():
    local("hg push")


def prepare_deploy():
    # test()
    commit()
    push()


def deploy():
    code_dir = '/home/warrior/DjangoProjects/tempsurge'
        # with settings(warn_only=True):
        #     if run("test -d %s" % code_dir).failed:
        #         run("git clone user@vcshost:/path/to/repo/.git %s" % code_dir)
    with cd(code_dir):
        run("hg pull && hg update")
        # run("touch app.wsgi")

    collect()
    reboot()


def collect():
    sudo("source .env/bin/activate && cd tempsurge && python manage.py collectstatic")


def reboot():
    "Reboot App Server"
    sudo("sudo supervisorctl restart tempsurge")


# from fabric.api import sudo, run, local, require
#
# def production():
#     env.host = ['162.243.88.59']
#
# def reboot():
#     "Reboot Apache2 server."
#     sudo("apache2ctl graceful")

# def production():
#     """ Set the target to production. """
#     config.fab_hosts = ['162.243.88.59']
# #     set(fab_hosts=['162.243.88.59'])
# #     set(fab_key_filename='~/.ssh/id_rsa.pub')
#     set(remote_proj_dir='/home/ts/tempsurge')
#
# def deploy():
#     """ Deploy the site. """
#     require('fab_hosts', provided_by = [production,])
#     local("hg push")
#     run("cd $(remote_proj_dir); hg pull; hg update")
#     run("cd $(remote_proj_dir); python manage.py syncdb")
#     run("service httpd restart")

# def debugon():
#     """Turn debug mode on for the production server."""
#     require('fab_hosts', provided_by = [production,])
#     run("cd $(remote_proj_dir); sed -i -e 's/DEBUG = .*/DEBUG = True/' deploy.py")
#     run("service httpd restart")
#
# def debugoff():
#     """Turn debug mode off for the production server."""
#     require('fab_hosts', provided_by = [production,])
#     run("cd $(remote_proj_dir); sed -i -e 's/DEBUG = .*/DEBUG = False/' deploy.py")
#     run("service httpd restart")