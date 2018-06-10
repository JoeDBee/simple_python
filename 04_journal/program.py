import journal

def print_header():
    print('-------------------------')
    print('     Journal App         ')
    print('-------------------------')


def run_event_loop():

    journal_name = input('Enter journal name:\n')
    if not journal_name:
        journal_name = 'default'

    journal_data = journal.load(journal_name)

    cmd = 'Empty!'
    print('Enter journal command:\n')
    while cmd != 'x' and cmd:
        cmd = input(
            '[L]ist entries, [A]dd an entry, [S]ave journal, E[x]it: \n'
        )
        cmd = cmd.lower().strip()

        if cmd == 'l' or cmd == 'list':
            list_entries(journal_data)
        elif cmd == 'a' or cmd == 'add':
            add_entry(journal_data)
        elif cmd == 's' or cmd == 'save':
            journal_name = input(
                "Please enter journal name: \n"
            )
            journal.save(journal_name, journal_data)
            cmd = 'x'
        elif cmd != 'x' and cmd:
            print('Sorry, the input {} is not valid\n'.format(cmd))

    print('Done. Exiting...')


def list_entries(data):
    print('Journal entries (first in, last out):')
    print('-------------------------------------')
    entries = reversed(data)
    # for entry in entries:
    #     print(entry)
    for (ix, entry) in enumerate(entries):
        print('* [{}] {}'.format(ix+1, entry))

    print('-------------------------------------')


def add_entry(data):
    text = input('Type your entry, <enter> to exit: \n')
    journal.add_entry(text, data)
    # data.append(text)


def main():
    print_header()
    run_event_loop()


if __name__ == '__main__':
    main()