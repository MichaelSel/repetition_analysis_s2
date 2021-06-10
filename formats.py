def general():
    return [
    {
        'static': {
            'type':'chromatic',
            'manipulation':'contour'
        },
        'dynamic':{
            'subject':'Subject_ID',
            'bias': '%_chromatic_swapped',
            'rt': 'rt_chromatic_swapped',
            'rt_type': 'rt_chromatic',
            'pc_decoy':'%_correct_decoys',
            'shifted-swapped':'c_shifted-swapped',
            'pc_decoy_at_condition': '%_correct_chromatic_same_v_swapped',
            'decoy_rt_type':'rt_chromatic_decoy',
            'decoy_rt_at_condition': 'rt_chromatic_decoy_swapped'

        }
    },
    {
        'static': {
            'type':'chromatic',
            'manipulation':'pitch'
        },
        'dynamic':{
            'subject':'Subject_ID',
            'bias': '%_chromatic_shifted',
            'rt': 'rt_chromatic_shifted',
            'rt_type': 'rt_chromatic',
            'pc_decoy':'%_correct_decoys',
            'shifted-swapped':'c_shifted-swapped',
            'pc_decoy_at_condition': '%_correct_chromatic_same_v_shifted',
            'decoy_rt_type':'rt_chromatic_decoy',
            'decoy_rt_at_condition': 'rt_chromatic_decoy_shifted'
        }
    },
    {
        'static': {
            'type':'diatonic',
            'manipulation':'contour'
        },
        'dynamic':{
            'subject':'Subject_ID',
            'bias': '%_diatonic_swapped',
            'rt': 'rt_diatonic_swapped',
            'rt_type': 'rt_diatonic',
            'pc_decoy':'%_correct_decoys',
            'shifted-swapped':'d_shifted-swapped',
            'pc_decoy_at_condition': '%_correct_diatonic_same_v_swapped',
            'decoy_rt_type': 'rt_diatonic_decoy',
            'decoy_rt_at_condition': 'rt_diatonic_decoy_swapped'
        }
    },
    {
        'static': {
            'type':'diatonic',
            'manipulation':'pitch',
        },
        'dynamic':{
            'subject':'Subject_ID',
            'bias': '%_diatonic_shifted',
            'rt': 'rt_diatonic_shifted',
            'rt_type': 'rt_diatonic',
            'pc_decoy':'%_correct_decoys',
            'shifted-swapped':'d_shifted-swapped',
            'pc_decoy_at_condition': '%_correct_diatonic_same_v_shifted',
            'decoy_rt_type': 'rt_diatonic_decoy',
            'decoy_rt_at_condition': 'rt_diatonic_decoy_shifted'
        }
    }
]

def sixty_six():
    format_66 = []

    for i in range(66):
        obj = {
            'static': {
                'set': i,
            },
            'dynamic': {
                'value': str(i),
            }
        }
        format_66.append(obj)

    return format_66


def expertise():
    return [
        {
            'static': {
                'type': 'diatonic',
                'manipulation': 'contour'
            },
            'dynamic': {
                'value': '%_diatonic_swapped',
                'expertise': 'expertise'
            }
        },
        {
            'static': {
                'type': 'diatonic',
                'manipulation': 'pitch'
            },
            'dynamic': {
                'value': '%_diatonic_shifted',
                'expertise': 'expertise'
            }
        },
    ]

def musicality():
    return [
    {
        'static': {
            'type':'chromatic',
        },
        'dynamic':{
            'shifted-swapped':'c_shifted-swapped',
            'musicality': 'musicality'
        }
    },
    {
        'static': {
            'type':'diatonic',
        },
        'dynamic':{
            'shifted-swapped':'d_shifted-swapped',
            'musicality': 'musicality'
        }
    },
]

def decoys():
    return [
    {
        'static': {
            'bla':'bla'
        },
        'dynamic':{
            'decoy_pc':'decoys_pc',
            'expertise': 'expertise',
        }
    }

]

def inverse_stats():
    return [
        {
            'static': {

            },
            'dynamic': {
                'id': 'ID',
                'x': 'Score',
                'y': 'Inverse Score'
            }
        }
    ]
