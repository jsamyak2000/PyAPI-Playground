def get_auth_headers(auth):
    """Generate authorization headers from username:password or token."""
    headers = {}
    
    # Check if the auth is in 'username:password' format
    if ":" in auth:
        headers["Authorization"] = f"Basic {auth}"
    else:  # Token-based authentication
        headers["Authorization"] = f"Bearer {auth}"
    
    return headers
