from facade.components.amplifier import Amplifier
from facade.components.cd_player import CdPlayer
from facade.components.dvd_player import DvdPlayer
from facade.components.popcorn_popper import PopcornPopper
from facade.components.projector import Projector
from facade.components.theather_lights import TheaterLights
from facade.components.screen import Screen
from facade.components.tuner import Tuner


class HomeTheaterFacade:
    amp: Amplifier = None
    tuner: Tuner = None
    cd: CdPlayer = None
    dvd: DvdPlayer = None
    projector: Projector = None
    screen: Screen = None
    lights: TheaterLights = None
    popper: PopcornPopper = None

    def __init__(self,
                 amp: Amplifier,
                 tuner: Tuner,
                 cd: CdPlayer,
                 dvd: DvdPlayer,
                 projector: Projector,
                 screen: Screen,
                 lights: TheaterLights,
                 popper: PopcornPopper):
        self.amp = amp
        self.tuner = tuner
        self.cd = cd
        self.dvd = dvd
        self.projector = projector
        self.screen = screen
        self.lights = lights
        self.popper = popper

    def watch_movie(self, movie: str):
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.set_wide_mode()
        self.amp.on()
        self.amp.set_dvd()
        self.amp.set_surround_sound()
        self.amp.set_volume(5)
        self.dvd.on()
        self.dvd.play(movie)

    def end_movie(self):
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.dvd.stop()
        self.dvd.eject()
        self.dvd.off()
