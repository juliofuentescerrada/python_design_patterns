import unittest
from unittest.mock import MagicMock, call

from facade.components.amplifier import Amplifier
from facade.components.cd_player import CdPlayer
from facade.components.dvd_player import DvdPlayer
from facade.components.popcorn_popper import PopcornPopper
from facade.components.projector import Projector
from facade.components.screen import Screen
from facade.components.theather_lights import TheaterLights
from facade.components.tuner import Tuner
from facade.home_theater_facade import HomeTheaterFacade


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.output = MagicMock()

    def test_home_theater(self):
        amp = Amplifier(self.output)
        tuner = Tuner(self.output)
        cd = CdPlayer(self.output)
        dvd = DvdPlayer(self.output)
        projector = Projector(self.output)
        screen = Screen(self.output)
        lights = TheaterLights(self.output)
        popper = PopcornPopper(self.output)

        home_theater = HomeTheaterFacade(
            amp,
            tuner,
            cd,
            dvd,
            projector,
            screen,
            lights,
            popper
        )

        home_theater.watch_movie('foo')

        calls = [
            call('PopcornPopper: ON'),
            call('PopcornPopper: POP'),
            call('TheaterLights: DIM LIGHTS TO 10'),
            call('Screen: DOWN'),
            call('Projector: ON'),
            call('Projector: SET WIDE MODE'),
            call('Amplifier: ON'),
            call('Amplifier: SET DVD'),
            call('Amplifier: SET SURROUND SOUND'),
            call('Amplifier: SET VOLUME TO 5'),
            call('DvdPlayer: ON'),
            call('DvdPlayer: PLAY foo')

        ]

        self.output.write.assert_has_calls(calls)


if __name__ == '__main__':
    unittest.main()
