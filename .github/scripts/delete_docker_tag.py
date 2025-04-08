#!/usr/bin/env python3
import os
import sys
import requests

def delete_tag(owner, repository, tag, token):
    url = f"https://hub.docker.com/v2/repositories/{owner}/{repository}/tags/{tag}/"
    headers = {
        "Authorization": f"JWT {token}",
    }
    response = requests.delete(url, headers=headers)
    return response

def main():
    if len(sys.argv) != 4:
        print("Usage: delete_docker_tag.py <owner> <repository> <tag>")
        sys.exit(1)
    owner = sys.argv[1]
    repository = sys.argv[2]
    tag = sys.argv[3]
    
    token = os.environ.get("DOCKER_API_TOKEN")
    if not token:
        print("Error: DOCKER_API_TOKEN environment variable not set")
        sys.exit(1)
    
    response = delete_tag(owner, repository, tag, token)
    if response.status_code == 204:
        print(f"Tag '{tag}' deleted successfully from {owner}/{repository}")
    else:
        print(f"Failed to delete tag '{tag}': {response.status_code} {response.text}")
        sys.exit(1)

if __name__ == "__main__":
    main()