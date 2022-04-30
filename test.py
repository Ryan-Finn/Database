import cmd

commands = [
    "foo",
    "foo bar blah",
    "bar",
    "bar baz blah",
    "baz",
    "baz foo blah"]


class Console(cmd.Cmd):
    intro = "Test console for" + \
            "http://stackoverflow.com/questions/4001708/\n" + \
            "Type \"cmd<space><tab><tab>\" to test " + \
            "auto-completion with spaces in commands\nwith " + \
            "similar beginings."

    def do_cmd(self, line):
        print(line)

    def complete_cmd(self, text, line, start_index, end_index):
        if text:
            return [command for command in commands
                    if command.startswith(text)]
        else:
            return commands


if __name__ == "__main__":
    command = Console()
    command.cmdloop()
