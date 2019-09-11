import os.path


def basedir() -> str:
    """
    assume this file is a submodule of a main application
    so we'll get dirname of dirname of full pathe of this file
    :return:
    """
    return  os.path.normpath(
        os.path.dirname(
            os.path.dirname(
                os.path.realpath(__file__)
            )
        )
    )


def assetsdir() -> str:
    return os.path.join(basedir(), 'assets')


def fullname(name: str) -> str:
    if name.startswith('/'):  # absolute name: return as is
        return name
    return os.path.join(assetsdir(), name)


def load(name: str) -> str:
    return open(fullname(name), 'r').read()
