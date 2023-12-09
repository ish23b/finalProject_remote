from PyQt6.QtWidgets import *
from gui import *
from television import *

class Logic(QMainWindow, Ui_MainWindow):

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        Method to initialize an object in the class
        """
        super().__init__()
        self.setupUi(self)

        self.__status = False
        self.__muted = False
        self.__volume = Logic.MIN_VOLUME
        self.__channel = Logic.MIN_CHANNEL

        self.button_power.clicked.connect(lambda: self.power())
        self.button_chUp.clicked.connect(lambda: self.channel_up())

    def power(self) -> None:
        """
        Method to turn on and off the power. And changes the background
        color of the channel display (white when power is on, black when off).
        """
        if self.__status == False:
            self.__status = True
            self.label_channelDisplay.setStyleSheet("background-color: rgb(221, 221, 221)")
        else:
            self.__status = False
            self.label_channelDisplay.setStyleSheet("background-color: rgb(98, 98, 98)")

    def mute(self) -> None:
        """
        Method to mute the volume
        """
        if self.__status:
            if self.__muted == False:
                self.__muted = True
            else:
                self.__muted = False

    def channel_text(self) -> str:
        """
        Determines what channel text should be displayed
        :return: a string with the channel text
        """
        if self.__channel == 0:
            return "PBS"
        elif self.__channel == 1:
            return "NBC"
        elif self.__channel == 2:
            return "ABC"
        else:
            return "CBS"

    def channel_up(self) -> None:
        """
        Method to increase the tv channel.
        """
        test = "test"
        if self.__status:
            if self.__channel < Power.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Power.MIN_CHANNEL
            self.label_channelDisplay.setText(channel_text())

    def channel_down(self) -> None:
        """
        Method to decrease the tv channel.
        """
        if self.__status:
            if self.__channel > Logic.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Logic.MAX_CHANNEL
            self.label_channelDisplay.setText(self.channel_text())

    def volume_up(self) -> None:
        """
        Method to turn up the volume a single level and,
        if muted, to unmute and then turn up volume a single level
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to turn down the volume a single level and,
        if muted, to unmute and then turn down volume a single level
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1