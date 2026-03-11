import requests

def get_post(post_id, base_url):
    if post_id < 0 or not isinstance(post_id, int):
        raise ValueError("Post ID must be a positive integer")
    response = requests.get(f"{base_url}/posts/{post_id}")
    return response