import os  # so we don't have to deal with OS dependant paths


def load(name):
    """
    This method creates and loads a journal.

    :param name: Basename of journal to load:
    :return: A new journal data structure
    """

    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as file:
            for entry in file.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    filename = get_full_pathname(name)
    print("Saving to: {}".format(filename))

    with open(filename, 'a+') as file:

        for entry in journal_data:
            file.write(entry + '\n')


def get_full_pathname(name):
    filename = os.path.abspath(
        os.path.join('.', 'journals', name + '.txt')
    )
    return filename


def add_entry(text, journal_data):
    journal_data.append(text)


