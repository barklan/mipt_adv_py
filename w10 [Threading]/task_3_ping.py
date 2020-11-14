import os


def ping(ips: list) -> list:
    for suffix in range(20, 30):
        ip = "192.168.178." + str(suffix)
        ip = 'google.com'
        ping_out = os.popen('ping ' + ip)  # получение вердикта
        print("... pinging ", ip)


