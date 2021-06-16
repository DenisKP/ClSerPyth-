# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в
# строковый тип на кириллице.
import subprocess


def ping(name):
    args = ['ping', name, '-c', '1', "-W", "2"]
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('cp866'))


sites = ['yandex.ru', 'youtube.com']
for site in sites:
    ping(site)