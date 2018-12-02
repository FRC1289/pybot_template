import wpilib
from wpilib.command.subsystem import Subsystem
from ctre import WPI_TalonSRX
import robotmap

class SimpleSubsystem(Subsystem):


    def __init__(self):

        super().__init__('SimpleSubsystem')
	# create a WPI TalonSRX based on the CAN bus assignment

# other control methods as needed that operate on instance variables
