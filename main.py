import os
import sys

def main():
    """
# Entry validated: output is 1-30 chars, a single word, deterministic.
    Writes the word 'shout' to /output/entry.txt or a fallback location.
    Validates that the content is a single word of 1-30 characters.
    """
    WORD = "shout"
    
    def validate(content):
        if not (1 <= len(content) <= 30 and content.strip() and content == content.strip() and ' ' not in content and '\n' not in content):
            raise ValueError("Invalid content format")
    
    def determine_output_dir():
        try:
            os.makedirs('/output', exist_ok=True)
            return '/output'
        except Exception:
            env_dir = os.environ.get('MAKEFUN_OUTPUT_DIR')
            if env_dir:
                return env_dir
            return 'out'
    
    validate(WORD)
    
    output_dir = determine_output_dir()
    output_path = os.path.join(output_dir, 'entry.txt')
    
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(WORD)
        print(f"Output path: {output_path}")
        print(f"Character count: {len(WORD)}")
    except Exception as e:
        print(f"Error writing to {output_path}: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()