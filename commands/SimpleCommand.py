from wpilib.command import Command

class SimpleCommand(Command):

    def __init__(self):
        super().__init__('Simple Command')
	# set instance vars, and require them        


    def initialize(self):
        pass
	# put subsystem(s) in a known state

    def execute(self):
        pass
	# do something using the subsystems

    def isFinished(self):
        pass
	# determine if the command is done
	
    def end(self):
        pass
	# put the subsystems back in a known state
