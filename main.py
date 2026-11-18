import os
import shutil

def main():
    # Resolve output directory: MAKEFUN_OUTPUT_DIR or fallback to /output
    out_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(out_dir, exist_ok=True)
    
    # Resolve source path relative to script file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(script_dir, 'entry.png')
    dst_path = os.path.join(out_dir, 'entry.png')
    
    # Copy file byte-identically
    shutil.copyfile(src_path, dst_path)
    
    # Verify byte-identical copy and size check
    src_size = os.path.getsize(src_path)
    dst_size = os.path.getsize(dst_path)
    assert src_size == dst_size, f"Copy size mismatch: {src_size} vs {dst_size}"
    assert src_size <= 1048576, f"Image exceeds 1 MiB limit: {src_size} bytes"
    
    print(f"Successfully copied entry.png ({src_size} bytes) to {dst_path}")

if __name__ == '__main__':
    main()
