import os
import json

def build_manifest():
    quiz_dir = 'quizzes'
    # Ensure directory exists
    if not os.path.exists(quiz_dir):
        os.makedirs(quiz_dir)
        
    files = [f for f in os.listdir(quiz_dir) if f.endswith('.csv')]
    manifest = []
    
    for f in files:
        quiz_id = f.replace('.csv', '')
        # Formats "cs320_memory" to "Cs320 Memory"
        title = quiz_id.replace('_', ' ').title()
        manifest.append({"id": quiz_id, "title": title})

    with open('quizzes.json', 'w') as j:
        json.dump(manifest, j, indent=2)

if __name__ == "__main__":
    build_manifest()
