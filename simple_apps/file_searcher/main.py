import os
import collections

SearchResult = collections.namedtuple('SearchResult',
                                      'file, line_number, text')


def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("Sorry we can't search that location.")
        return

    text = get_search_text_from_user()
    if not text:
        print("We can't search for nothing!")
        return

    matches = search_folders(folder, text)
    # at this point, the interpreter knows matches is a generated object
    match_count = 0
    for m in matches:  # the yield operations now take place
        match_count += 1
        print('--------- MATCH -------------')
        print('file: ' + m.file)
        print('line: {}'.format(m.line_number))
        print('match: ' + m.text.strip())
        print()

    print("Found {:,} matches.".format(match_count))


def print_header():
    print('-------------------------------------')
    print('           FILE SEARCH APP')
    print('-------------------------------------')


def get_folder_from_user():
    folder = input('What folder do you want to search? ')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input('What are you searching for [single phrases only]? ')
    return text.lower()


def search_folders(folder, text):
    # all_matches = []
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            # if it's a directory, examine all constituent items
            # yield one file at a time
            yield from search_folders(full_item, text)
            # continue
        else:
            # if it's a file, examine all lines in file
            # yield one match at at a time
            yield from search_file(full_item, text)
    #         matches = search_file(full_item, text)
    #         all_matches.extend(matches)
    #
    # return all_matches


def search_file(filename, search_text):
    with open(filename, 'r', encoding='utf-8') as fin:

        for number, line in enumerate(fin):
            if line.lower().find(search_text) >= 0:
                match = SearchResult(line_number=number, file=filename, text=line)
                yield match


if __name__ == '__main__':
    main()
