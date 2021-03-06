import os
import pytest
from pytest_mock import mocker
from lib.core.ConfigHandler import ConfigHandler

def test_env_path(mocker):

    # Arrange
    os.environ['MOOSCAN_CONFIG_PATH'] = '/some/new/path'

    mocker.patch('os.makedirs')

    # Act
    handler = ConfigHandler()
    handler.LoadConfigPaths()

    # Assert
    assert handler.GetConfigFile() == '/some/new/path/mooscan.conf'

def test_config_validate(mocker):

    # Arrange
    mocker.patch('os.makedirs')
    mocker.patch('os.path.exists')

    config = {
            'mooscan_path': '~/.mooscan', 
            'git_path': 'moodle-git', 
            'update_module_freq': 14, 
            'update_code_freq': 14, 
            'moodle_git': 'https://github.com/moodle/moodle.git', 
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0', 
            'module_database': 'modules.db', 
            'versions_database': 'versions.db'
    }

    # Act
    handler = ConfigHandler()

    # Assert
    assert handler.CheckConfig(config) == config
