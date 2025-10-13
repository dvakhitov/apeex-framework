from unittest.mock import Mock
from typing import cast
from apeex.orm.orm_engine_interface import OrmEngineInterface
from apeex.orm.entity_manager_interface import EntityManagerInterface

def test_orm_engine_interface_import_and_mock():
    # Check that OrmEngineInterface is importable
    assert OrmEngineInterface is not None

    # Create a mock and cast it to OrmEngineInterface for type checker
    mock_engine = cast(OrmEngineInterface, Mock(spec=OrmEngineInterface))

    # Ensure get_entity_manager returns an EntityManagerInterface mock
    mock_em = cast(EntityManagerInterface, Mock(spec=EntityManagerInterface))
    mock_engine.get_entity_manager.return_value = mock_em
    assert isinstance(mock_engine.get_entity_manager(), EntityManagerInterface)
