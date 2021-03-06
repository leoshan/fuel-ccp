DEFAULTS = {
    'kubernetes': {
        'server': 'http://localhost:8080',
        'namespace': 'ccp',
        'ca_cert': None,
        'key_file': None,
        'cert_file': None,
        'insecure': False,
        'cluster_domain': 'cluster.local',
        'image_pull_policy': None,
    },
}

SCHEMA = {
    'kubernetes': {
        'type': 'object',
        'additionalProperties': False,
        'properties': {
            'server': {'type': 'string'},
            'namespace': {'type': 'string'},
            'ca_cert': {'anyOf': [{'type': 'string'}, {'type': 'null'}]},
            'key_file': {'anyOf': [{'type': 'string'}, {'type': 'null'}]},
            'cert_file': {'anyOf': [{'type': 'string'}, {'type': 'null'}]},
            'insecure': {'type': 'boolean'},
            'cluster_domain': {'type': 'string'},
            'image_pull_policy': {'oneOf': [
                {'type': 'null'},
                {'enum': ['Always', 'IfNotPresent', 'Never']},
            ]},
        },
    },
}
