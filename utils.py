from os import path


def check_file_exists(file):
    if path.isfile(file):
        return True
    else:
        return False


def check_path_validity(candidate_path):
    if path.isdir(candidate_path):
        return True
    else:
        return False


def check_path_validity_traversable(*paths):
    """ Check that all paths are correct """
    are_valid = list(map(check_path_validity, paths))
    for x in are_valid:
        if not x:
            return False
    return True