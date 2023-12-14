from file_system import FileSystem
import sys
def main():
    fs = FileSystem()

    
    # it checks if the main.py stated with an argument to load the state
    if "load_state" in sys.argv:
        fs.load_state("state.json")
    if "load_n_save_sate" in sys.argv:
        fs.load_state("state.json")
    while True:
        current_path = fs.get_current_path()
        command = input(f"FS/{current_path}> ").strip().split()
        if not command:
            continue

        cmd, *args = command
        response = None  

        if cmd == "exit":
            break
        elif cmd == "mkdir":
            response = fs.mkdir(args[0]) if args else "syntax: mkdir <directory_name>"
        elif cmd == "touch":
            response = fs.touch(args[0]) if args else "syntax: touch <file_name>"
        elif cmd == "ls":
            res = fs.ls()
            if res :
                for (idx, item) in enumerate(res):
                    print(f"  {idx + 1}.  {item}")
            else: response='Empty Directory'
        elif cmd == "cat":
            response = fs.cat(args[0]) if args else "syntax: cat <file_name>"
        elif cmd == "echo":
            if len(args) >= 3:
                if (args[-1] == "True"):
                       file_name = args[-2]
                       text = ' '.join(args[:-3])
                       if (args[-3] != '>'):
                            response ='syntax: Should be like: echo "<content of file>" > example.txt , (you are missing '>')'
                            continue
                       response = fs.echo(text, file_name,append=True) 
                else:
                        file_name = args[-1]
                        text = ' '.join(args[:-2])
                        if (args[-2] != '>'):
                            response ='syntax: Should be like: echo "<content of file>" > example.txt , (you are missing '>')'
                            continue
                        response = fs.echo(text, file_name)
            else:
                response = "syntax: echo <text> > <file_name> <True or False (if you want to Append content)>"
        elif cmd == "rm":
            response = fs.rm(args[0]) if args else "syntax: rm <file_or_directory_name>"
        elif cmd == "mv":
            response = fs.mv(args[0], args[1]) if len(args) == 2 else "syntax: mv <source> <destination>"
        elif cmd == "cp":
            response = fs.cp(args[0], args[1]) if len(args) == 2 else "syntax: cp <source> <destination>"
        elif cmd == "cd":
            response = fs.cd(args[0]) if args else "syntax: cd <path>"
        elif cmd == "grep":
            response = fs.grep(args[0]) if args else "syntax: grep <pattern>"
        else:
            response = f"Unknown command: {cmd}"

        if response is not None:
            print(response)

    # Before exiting, check if the script should save the state
    if "save_state" in sys.argv:
        fs.save_state("state.json")
    if "load_n_save_sate" in sys.argv:
        fs.save_state("state.json")

if __name__ == "__main__":
    main()
