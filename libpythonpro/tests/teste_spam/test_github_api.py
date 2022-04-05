from unittest.mock import Mock

from libpythonpro import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'rafael', 'id': 24160, 'node_id': 'MDQ6VXNlcjI0MTYw',
        'avatar_url': 'https://avatars.githubusercontent.com/u/24160?v=4'
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('rafael')
    assert 'https://avatars.githubusercontent.com/u/24160?v=4' == url