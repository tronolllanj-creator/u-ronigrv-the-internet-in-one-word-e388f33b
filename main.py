import os
import sys


def write_entry(WORD: str) -> str:
    """Write the entry word to the grader's output file."""
# Entry validated: output is 1-30 chars, a single word, deterministic.
    if not (1 <= len(WORD) <= 30):
        raise ValueError("Word length out of range")
    if not WORD.strip() or WORD != WORD.strip() or ' ' in WORD or '\n' in WORD:
        raise ValueError("Word format invalid")
    
    candidates = []
    if not os.getenv('MAKEFUN_OUTPUT_DIR'):
        candidates.append('/output')
    
    makefun_dir = os.getenv('MAKEFUN_OUTPUT_DIR')
    if makefun_dir:
        candidates.append(makefun_dir)
    
    candidates.append('out')
    
    for dir_path in candidates:
        try:
            os.makedirs(dir_path, exist_ok=True)
            file_path = os.path.join(dir_path, 'entry.txt')
            with open(file_path, 'w', encoding='utf-8', newline='') as f:
                f.write(WORD)
                f.flush()
                os.fsync(f.fileno())
            return file_path
        except Exception:
            continue
    
    # Fallback if none worked (should not happen for 'out')
    open('entry.txt', 'w', encoding='utf-8', newline='').write(WORD)
    return 'entry.txt'


def main():
    WORD = "repost"
    path = write_entry(WORD)
    print(f"Wrote {len(WORD)} characters to: {path}")


if __name__ == '__main__':
    main()
