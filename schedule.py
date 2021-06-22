import subprocess
from apscheduler.schedulers.background import BackgroundScheduler

def start():
    cmds_list = [["python3","manage.py","runserver","8000"],
            ["python3","manage.py","runserver","8080"]]
    #multiple subprocess run in parallel
    procs_list = [subprocess.Popen(cmd) for cmd in cmds_list]
    # print([proc.pid for proc in procs_list])
    scheduler = BackgroundScheduler()
    scheduler.configure({'apscheduler.daemon': False})
    scheduler.add_job(check_restart, 'interval', seconds=5,args=[procs_list,cmds_list],)
    scheduler.start()
    
def check_restart(procs_list,cmds_list):
    for i,proc in enumerate(procs_list):
        #checks if process is running(could add other checks here)
        if proc.poll() != None:
            proc.kill()
            proc.wait()
            procs_list[i] = subprocess.Popen(cmds_list[i])

if __name__ == "__main__":
    start()

