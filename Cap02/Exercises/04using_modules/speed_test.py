from speedtest import Speedtest

s = Speedtest()

print('Testing... \n')

download_speed = s.download() / 1048576
upload_speed = s.upload() / 1048576
ping_result = round(s.results.ping)

print(f'Download speed: {download_speed:.2f} Mbps')
print(f'Upload speed: {upload_speed:.2f} Mbps')
print(f'Ping: {ping_result} ms')
