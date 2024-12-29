import os
import argparse

# Define the source directory (fixed to ~/dotfiles)
SOURCE_DIR = os.path.expanduser("~/dotfiles")

# List of files in the source directory that have already been symlinked
existing_symlinks = [filename for filename in os.listdir(SOURCE_DIR) if os.path.islink(os.path.expanduser(f"~/{filename}"))]

# List of dotfiles in the source directory that are not yet symlinked
pending_dotfiles = [filename for filename in os.listdir(SOURCE_DIR) if not os.path.islink(os.path.expanduser(f"~/{filename}"))]


def show_pending_dotfiles():
    """Display a list of dotfiles that can be symlinked."""
    print("Pending dotfiles to be symlinked:")
    for i, filename in enumerate(pending_dotfiles):
        print(f"{i+1}: {filename}")


def create_symlink(dest):
    """Create a symbolic link from the source directory to the destination."""
    filename = os.path.basename(dest)
    source = os.path.join(SOURCE_DIR, filename)
    if os.path.exists(dest):
        print(f"Error: {dest} already exists!")
    else:
        try:
            os.symlink(source, dest)
            print(f"Symbolic link created from {source} to {dest}")
        except Exception as e:
            print(f"Error creating symbolic link: {e}")


def list_symlinks():
    """List all existing symbolic links in the home directory."""
    print("Listing all symbolic links in ~:")
    for filename in existing_symlinks:
        symlink_path = os.path.expanduser(f"~/{filename}")
        if os.path.islink(symlink_path):
            print(f"{filename} ->  {os.path.realpath(symlink_path)}")


def delete_symlink(symlink):
    """Delete a symbolic link in the home directory."""
    if os.path.islink(symlink):
        try:
            os.remove(symlink)
            print(f"Symbolic link {symlink} deleted")
        except Exception as e:
            print(f"Error deleting symbolic link: {e}")
    else:
        print(f"Error: {symlink} is not a valid symbolic link!")


def main():
    """Main function to parse arguments and perform actions."""
    parser = argparse.ArgumentParser(description="Manage symbolic links for dotfiles.")
    parser.add_argument(
        "action", choices=["create", "list", "delete"], help="Action to perform"
    )
    parser.add_argument(
        "target", nargs="?", help="Target for symlink (required for create/delete)"
    )

    args = parser.parse_args()

    if args.action == "create":
        if len(pending_dotfiles) == 0:
            print("Error: No pending dotfiles to symlink!")
            return
        print("Enter the number of the dotfile you want to symlink:")
        show_pending_dotfiles()
        choice = input("Enter the number: ")
        try:
            choice = int(choice)
            filename = pending_dotfiles[choice - 1]
            create_symlink(os.path.expanduser(f"~/{filename}"))
        except Exception as e:
            print(f"Error: {e}")

    elif args.action == "list":
        list_symlinks()

    elif args.action == "delete":
        print("Enter the symbolic link you want to delete:")
        show_pending_dotfiles()
        choice = input("Enter the number: ")
        try:
            choice = int(choice)
            filename = pending_dotfiles[choice - 1]
            delete_symlink(os.path.expanduser(f"~/{filename}"))
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
