import PyToSh

def test():
    cmd1 = ["ping", "-c", "4", "127.0.0.1"]
    cmd2 = ["grep", "packet loss"]
    output = PyToSh.popen_pipe(cmd1, cmd2)
    output = output.split(",")[2].split("%")[0]
    if int(output) <= 50:
        print(output)

test()
