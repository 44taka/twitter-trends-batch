from orator.migrations import Migration


class CreateTwitterTrends(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('twitter_trends') as table:
            table.increments('id')
            table.small_integer('rank')
            table.string('name', 100)
            table.string('url', 255)
            table.integer('tweet_volume').nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop_if_exists('twitter_trends')
