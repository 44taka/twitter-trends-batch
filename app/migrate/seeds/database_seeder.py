from orator.seeds import Seeder

from .woeid_seeder import WoeidSeeder


class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(WoeidSeeder)
