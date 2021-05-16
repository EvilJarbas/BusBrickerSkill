from mycroft import MycroftSkill


class BusBrickerSkill(MycroftSkill):
    def __init__(self):
        super().__init__()

    def initialize(self):
        self.log.warning("All skills share a messagebus object, this means "
                         "any skill can call the shutdown method and brick "
                         "your mycroft")
        self.log.warning("DO NOT INSTALL RANDOM CRAP")
        self.log.error("each skill should have it's own bus instance")
        self.bus.emitter.shutdown()


def create_skill():
    return BusBrickerSkill()
