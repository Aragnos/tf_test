import PyToSh
from ErrorClass import ConnectionError 
def test():
    cmd1 = ["ping", "-c", "4", "127.0.0.1"]
    cmd2 = ["grep", "packet loss"]
    output = PyToSh.popen_pipe(cmd1, cmd2)
    #output = "Host not found"
    try:
        output = output.split(",")[2].split("%")[0]
        if int(output) < 100:
            print(output)
        else:
            raise
    except:
        raise ConnectionError("Ping failed")
    return

test()
