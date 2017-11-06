"""
This module is named source instead of import because import is a Python
keyword.
"""
from flask import Blueprint
from zou.app.utils.api import configure_api_from_blueprint

from .shotgun.project import (
    ImportShotgunProjectsResource,
    ImportRemoveShotgunProjectResource
)
from .shotgun.person import (
    ImportShotgunPersonsResource,
    ImportRemoveShotgunPersonResource
)
from .shotgun.shot import (
    ImportShotgunShotsResource,
    ImportRemoveShotgunShotResource
)
from .shotgun.sequence import (
    ImportShotgunSequencesResource,
    ImportRemoveShotgunSequenceResource
)
from .shotgun.episode import (
    ImportShotgunEpisodesResource,
    ImportRemoveShotgunEpisodeResource
)
from .shotgun.assets import (
    ImportShotgunAssetsResource,
    ImportRemoveShotgunAssetResource
)
from .shotgun.steps import (
    ImportShotgunStepsResource,
    ImportRemoveShotgunStepResource
)
from .shotgun.status import (
    ImportShotgunStatusResource,
    ImportRemoveShotgunStatusResource
)
from .shotgun.tasks import (
    ImportShotgunTasksResource,
    ImportRemoveShotgunTaskResource
)
from .shotgun.versions import (
    ImportShotgunVersionsResource,
    ImportRemoveShotgunVersionResource
)
from .shotgun.import_errors import (
    ShotgunImportErrorsResource,
    ShotgunImportErrorResource
)
from .shotgun.notes import (
    ImportShotgunNotesResource,
    ImportRemoveShotgunNoteResource
)

from .csv.projects import ProjectsCsvImportResource
from .csv.persons import PersonsCsvImportResource
from .csv.assets import AssetsCsvImportResource
from .csv.shots import ShotsCsvImportResource
from .csv.tasks import TasksCsvImportResource

routes = [
    ("/import/shotgun/persons", ImportShotgunPersonsResource),
    ("/import/shotgun/projects", ImportShotgunProjectsResource),
    ("/import/shotgun/shots", ImportShotgunShotsResource),
    ("/import/shotgun/episodes", ImportShotgunEpisodesResource),
    ("/import/shotgun/sequences", ImportShotgunSequencesResource),
    ("/import/shotgun/assets", ImportShotgunAssetsResource),
    ("/import/shotgun/steps", ImportShotgunStepsResource),
    ("/import/shotgun/status", ImportShotgunStatusResource),
    ("/import/shotgun/tasks", ImportShotgunTasksResource),
    ("/import/shotgun/versions", ImportShotgunVersionsResource),
    ("/import/shotgun/notes", ImportShotgunNotesResource),
    ("/import/shotgun/errors", ShotgunImportErrorsResource),
    ("/import/shotgun/errors/<error_id>", ShotgunImportErrorResource),
    ("/import/shotgun/remove/project", ImportRemoveShotgunProjectResource),
    ("/import/shotgun/remove/person", ImportRemoveShotgunPersonResource),
    ("/import/shotgun/remove/shot", ImportRemoveShotgunShotResource),
    ("/import/shotgun/remove/episode", ImportRemoveShotgunEpisodeResource),
    ("/import/shotgun/remove/sequence", ImportRemoveShotgunSequenceResource),
    ("/import/shotgun/remove/asset", ImportRemoveShotgunAssetResource),
    ("/import/shotgun/remove/step", ImportRemoveShotgunStepResource),
    ("/import/shotgun/remove/status", ImportRemoveShotgunStatusResource),
    ("/import/shotgun/remove/task", ImportRemoveShotgunTaskResource),
    ("/import/shotgun/remove/note", ImportRemoveShotgunNoteResource),
    ("/import/shotgun/remove/version", ImportRemoveShotgunVersionResource),

    ("/import/csv/projects", ProjectsCsvImportResource),
    ("/import/csv/persons", PersonsCsvImportResource),
    ("/import/csv/assets", AssetsCsvImportResource),
    ("/import/csv/shots", ShotsCsvImportResource),
    ("/import/csv/tasks", TasksCsvImportResource)
]

blueprint = Blueprint("/import", "import")
api = configure_api_from_blueprint(blueprint, routes)
