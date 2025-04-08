#!/usr/bin/env python3
import os
import sys
import requests

def delete_tag(image_name, tag, token):
    url = f"https://hub.docker.com/v2/repositories/{image_name}/tags/{tag}/"
    headers = {
        "Authorization": f"JWT {token}",
    }
    response = requests.delete(url, headers=headers)
    return response

def main():
    if len(sys.argv) != 3:
        print("Usage: delete_docker_tag.py <image_name> <tag>")
        sys.exit(1)
    image_name = sys.argv[1]
    tag = sys.argv[2]
    
    token = os.environ.get("DOCKER_API_TOKEN")
    if not token:
        print("Error: DOCKER_API_TOKEN environment variable not set")
        sys.exit(1)
    
    response = delete_tag(image_name, tag, token)
    if response.status_code == 204:
        print(f"Tag '{tag}' deleted successfully from {image_name}")
    else:
        print(f"Failed to delete tag '{tag}': {response.status_code} {response.text}")
        sys.exit(1)

if __name__ == "__main__":
    main()