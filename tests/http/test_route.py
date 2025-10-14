from apeex.http.route import Route


def dummy_handler():
    return "ok"


def test_route_basic_match():
    route = Route("/users/{id}", ["GET"], dummy_handler)
    params = route.matches("/users/123", "GET")
    assert params == {"id": "123"}


def test_route_method_not_allowed():
    route = Route("/users/{id}", ["POST"], dummy_handler)
    assert route.matches("/users/1", "GET") is None


def test_route_path_matches_without_method():
    route = Route("/posts/{slug}", ["GET"], dummy_handler)
    assert route.path_matches("/posts/abc") is True
    assert route.path_matches("/posts/") is False


def test_route_multiple_methods():
    route = Route("/health", ["GET", "HEAD"], dummy_handler)
    assert route.matches("/health", "HEAD") == {}
    assert route.matches("/health", "POST") is None


def test_route_repr_contains_path():
    route = Route("/x", ["GET"], dummy_handler)
    assert "/x" in repr(route)
