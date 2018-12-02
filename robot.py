#!/usr/bin/env python3

import wpilib
from wpilib.command import Command, Scheduler
from commandbased import CommandBasedRobot

from subsystems.SimpleSubsystem import SimpleSubsystem 
import oi
from commands.GroupCommand import GroupCommand
from commands.SimpleCommand import SimpleCommand

class PyBot(CommandBasedRobot):
    '''
    The CommandBasedRobot base class implements almost everything you need for
    a working robot program. All you need to do is set up the subsystems and
    commands. You do not need to override the "periodic" functions, as they
    will automatically call the scheduler. You may override the "init" functions
    if you want to do anything special when the mode changes.
    '''

    def robotInit(self):
        '''
        Since OI instantiates commands and commands need access to subsystems,
        OI must be initialized after subsystems.
	So - instantiate in this order
	1) Subsystems
	2) Commands
	3) OI (operator interface)
        '''

        Command.getRobot = lambda x=0: self

        #Instantiate a subsystem

        #self.autonomousProgram = somecommand(self.logger)
        #self.teleopProgram = somecommand(self.logger)
        
        self.joystick = oi.getJoystick()

    def autonomousInit(self):
        self.autonomousProgram.start()
        
    #def autonomousPeriodic(self):
        #Scheduler.getInstance().run()
        

    def teleopInit(self):
        if self.autonomousProgram is not None:
            self.autonomousProgram.cancel()            
        self.teleopProgram.start()
        
    def teleopPeriodic(self):
        #Scheduler.getInstance().run()
        #if self.teleopProgram.isFinished():
            #self.logger.info('finished')
	    # If we want to restart the command again,
	    # create a new instance of the teleop command and start it
            
if __name__ == '__main__':
    wpilib.run(PyBot)
