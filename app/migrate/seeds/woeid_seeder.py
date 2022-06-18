from orator.seeds import Seeder


class WoeidSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('woeid').insert({
            'id': 23424856,
            'name': 'Japan'
        })
