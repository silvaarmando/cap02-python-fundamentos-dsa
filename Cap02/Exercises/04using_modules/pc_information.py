import platform

so = platform.system()

print(f'{so} Operating System')
print(f'Machine: {platform.machine()}')
print(f'Network: {platform.node()}')
print(f'Platform: {platform.platform()}')