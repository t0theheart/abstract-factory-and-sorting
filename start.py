from program import Sorting, Writer, get_program


def main():
    """
        Example of using

        Sorting-writing program started!
        Writer types: "line", "column"
        Enter writer type: column
        Sort types: "bubble", "selection", "insertion"
        Enter type sort: insertion
        Enter read from: array.txt
        Enter write to: result.txt
        Sorting-writing end.
    """

    print('Sorting-writing program started!')
    print(f'Writer types: "{Writer.line.value}", "{Writer.column.value}"')
    writer_type = input('Enter writer type: ')
    print(f'Sort types: "{Sorting.bubble.value}", "{Sorting.selection.value}", "{Sorting.insertion.value}"')
    sort_type = input('Enter type sort: ')
    read_from = input('Enter read from: ')
    write_to = input('Enter write to: ')

    program_class = get_program(writer_type, sort_type)
    if program_class:
        program = program_class(read_from, write_to)

        program.read()
        program.do_action()
        program.write()
    else:
        print('Wrong "writer type" or "type sort", please try again!')
    print('Sorting-writing end.')


if __name__ == '__main__':
    main()
