import os
import json

def build_image_map(dir_path):
    result = {}
    for item in os.listdir(dir_path):
        full_path = os.path.join(dir_path, item)
        if os.path.isdir(full_path):
            result[item] = build_image_map(full_path)
        else:
            if "files" not in result:
                result["files"] = []
            result["files"].append(item)
    return result

image_dir = os.path.join(os.path.dirname(__file__), "images")
image_map = build_image_map(image_dir)

response = {"images": image_map}

print(json.dumps(response, indent=2))
