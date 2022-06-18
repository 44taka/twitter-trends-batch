from orator.migrations import Migration


class CreateWoeid(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('woeid') as table:
            table.increments('id')
            table.string('name', 100)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop_if_exists('woeid')
