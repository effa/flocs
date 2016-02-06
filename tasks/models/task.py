from django.db import models
import json


class TaskModel(models.Model):
    """Model for a task (exercise)
    """
    title = models.TextField()
    maze_settings = models.TextField(verbose_name="Maze settings in JSON")
    workspace_settings = models.TextField(verbose_name="Workspace settings in JSON")

    def __str__(self):
        return '[{pk}] {title}'.format(pk=self.pk, title=self.title)

    def to_json(self):
        """Return JSON (dictionary) representation of the task.
        """
        maze_settings_dict = json.loads(self.maze_settings)
        workspace_settings_dict = json.loads(self.workspace_settings)
        task_dict = {
            'task-id': self.pk,
            'title': self.title,
            'maze-settings': maze_settings_dict,
            'workspace-settings': workspace_settings_dict
        }
        return task_dict

