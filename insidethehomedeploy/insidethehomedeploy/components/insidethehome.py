from fabric.api import sudo
from elmer.packages import packages, InstallOptions

packagedefs = packages(("artifactory:insidethehome,{{ INSIDETHEHOME_VERSION|default('1.0') }}",
                        InstallOptions(force=True, clean_cache=True)))


def postconfigure():
    """
    Enable nginx site.
    """
    sudo("ln -sf ../sites-available/insidethehome /etc/nginx/sites-enabled/")
    sudo("rm -f /etc/nginx/sites-enabled/default")
