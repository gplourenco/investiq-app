from pathlib import Path

from phi.workspace.settings import WorkspaceSettings

#
# -*- Define workspace settings using a WorkspaceSettings object
# these values can also be set using environment variables or a .env file
#
ws_settings = WorkspaceSettings(
    # Workspace name: used for naming cloud resources
    ws_name="investiq-app",
    # Path to the workspace root
    ws_root=Path(__file__).parent.parent.resolve(),
    # -*- Dev settings
    dev_env="dev",
    # -*- Dev Apps
    dev_app_enabled=True,
    dev_db_enabled=False,
    # dev_jupyter_enabled=True,
    # -*- Image Settings
    # Name of the image
    image_name="investiq-app",
    # Repository for the image
    # image_repo="phidata",
    # Build images locally
    # build_images=True,
)
