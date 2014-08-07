from os.path import dirname
from getpass import getuser

from fabric.api import env, local

from fabware.manage import *  # noqa
from confab.api import *  # noqa
from elmer.bootstrap import *  # noqa
from elmer.api import *  # noqa

env.use_ssh_config = True

generate_tasks(dirname(__file__))


@task
def setup_artifacts(version="1.0"):
    dest = "/var/tmp/{username}/build/insidethehome/{version}/insidethehome/deb-build-dir/".format(username=getuser(), version=version)  # noqa
    local("mkdir -p {}".format(dest))
    local("cp ../build/insidethehome_{}_amd64.deb {}".format(version, dest))
