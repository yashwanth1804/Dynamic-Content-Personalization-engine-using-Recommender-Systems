import os
import sys
import traceback


def main() -> None:
    #Application entry point.
    print("Bank Content Personalization Engine")
    print("Loading recommendation engine…")

    # Absolute paths
    project_root = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(project_root, "src")
    data_dir = os.path.join(project_root, "data")

    # Add src/ to PYTHONPATH
    if src_path not in sys.path:
        sys.path.insert(0, src_path)

    try:
        #Data checks
        processed_data = os.path.join(data_dir, "processed_data.csv")
        bank_data = os.path.join(data_dir, "bank-additional.csv")

        if os.path.exists(processed_data):
            print("Processed data file found.")
        elif os.path.exists(bank_data):
            print("Raw bank data found. Run the preprocessing notebook first.")
        else:
            print("No data files found. Using demo data.")

        #Source-file checks
        required_files = [
            "app.py",
            "recommender.py",
            "content_library.py",
            "__init__.py",
        ]
        missing = [f for f in required_files if not os.path.exists(os.path.join(src_path, f))]
        if missing:
            print(f"Missing files in src/: {', '.join(missing)}")
            return

        print("Source files verified.")

        #Flask application
        import app

        flask_app = app.app
        print("Flask application loaded successfully.")
        print("Starting development server at http://localhost:5000")

        # Start Flask dev server
        flask_app.run(
            debug=True,
            host="localhost",
            port=5000,
            use_reloader=True,
            threaded=True,
        )

    except ImportError as exc:
        print(f"Import error: {exc}")
        print("\nTroubleshooting:")
        print("  1. Verify the Python interpreter in your IDE.")
        print("  2. Confirm that all required modules are present in src/.")
        print("  3. Restart your IDE after creating or editing environment files.")
        list_files_in_src(src_path)

    except Exception as exc:  # pylint: disable=broad-except
        print(f"Unexpected error: {exc}")
        traceback.print_exc()


def list_files_in_src(path: str) -> None:
    #List Python files present in src/ for quick inspection.
    if not os.path.isdir(path):
        print("src/ directory not found.")
        return

    py_files = [f for f in os.listdir(path) if f.endswith(".py")]
    if py_files:
        print("\nFiles in src/:")
        for file_name in py_files:
            print(f"  {file_name}")
    else:
        print("No Python files detected in src/.")


if __name__ == "__main__":
    main()