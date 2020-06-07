from program import Sorting, Writer, get_program


def main():
    print(f'Writer types: "{Writer.line.value}", "{Writer.column.value}"')
    writer_type = input('Enter writer type: ')
    print(f'Sort types: "{Sorting.bubble.value}", "{Sorting.selection.value}", "{Sorting.insertion.value}"')
    sort_type = input('Enter type sort: ')
    read_from = input('Enter read from: ')
    write_to = input('Enter write to: ')

    program_class = get_program(writer_type, sort_type)

    program = program_class(read_from, write_to)

    program.read()
    program.do_action()
    program.write()


if __name__ == '__main__':
    main()
