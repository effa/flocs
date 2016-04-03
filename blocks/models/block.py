"""Definition of block model
"""

from django.db import models
import json

from .block_manager import BlockManager

class BlockModel(models.Model):
    """Representation of a code block
    """
    objects = BlockManager()

    name = models.TextField(
        help_text="name of a block")

    identifiers = models.TextField(
        help_text="unique identifier(s) of all variants of a block(s) used internally")

    identifiers_condensed = models.TextField(
        verbose_name="unique identifier(s) of a block(s) used internally")

    level = models.SmallIntegerField(
        help_text="level required to use this block",
        default=1)

    def get_identifiers_list(self):
        return json.loads(self.identifiers)

    def get_identifiers_condensed_list(self):
        return json.loads(self.identifiers_condensed)

    def __str__(self):
        return '[{pk}] {name}'.format(pk=self.pk, name=self.name)

    def to_json(self):
        """Returns JSON (dictionary) representation of the block.
        """
        block_dict = {
            'block-id': self.pk,
            'name': self.name,
            'identifiers': json.loads(self.identifiers),
            'identifiers-condensed': json.loads(self.identifiers_condensed),
        }
        return block_dict
