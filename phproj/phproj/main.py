import argparse

def create_project(name):
    print(f"project '{name}' created successfuly!")

def main():
    parser = argparse.ArgumentParser(description='PHP project manager')
    parser.add_argument('--create-project', type=str, help='Create a new project ex: phproj --create-project project-name')
    args = parser.parse_args()

    if args.create_project:
        create_project(args.create_project)
    

if __name__ == '__main__':
    main()
