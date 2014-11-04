import messaging

SERVICES = [messaging.service]

# Messaging service configuration
MESSAGING_HOST = ''
MESSAGING_PORT = 1126
MESSAGING_PROTOCOL = 'SMAP'
MESSAGING_MAX_PENDING_CLIENTS = 8

# Deposit service configuration
DEPOSIT_HOST = ''
DEPOSIT_PORT = 1999
DEPOSIT_PROTOCOL = 'HTTP'
DEPOSIT_MAX_PENDING_CLIENTS = 4
