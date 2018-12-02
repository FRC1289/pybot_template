from wpilib.command.commandgroup import CommandGroup

from wpilib.command.waitcommand import WaitCommand

class GroupCommand(CommandGroup):

    def __init__(self):
        super().__init__('GroupCommand')

	# add sequential/parallel commands here
	# or - create a self-contained command

