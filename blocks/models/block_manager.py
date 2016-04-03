from django.db import models

class BlockManager(models.Manager):

    def all_ordered(self):
        """Return all blocks in order defined by their difficulty level
        """
        return self.order_by('level')
