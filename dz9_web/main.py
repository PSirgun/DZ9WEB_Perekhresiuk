import subprocess
print ('start')
subprocess.run('scrapy crawl authors')
print ('wait. All fine')
subprocess.run('scrapy crawl quotes')
print ('end')