{
    'objects_result': {
        'prediction': [
            {
                'tagName': 'Container 1',
                'type': 'Container',
                'boundingBox': {
                    'left': 0,
                    'top': 0,
                    'right': 612,
                    'bottom': 816
                },
                'object_id': '4724443',
                'objects': [{
                    'Seal 1': {'left': 465.63, 'top': 169.77, 'right': 549.37, 'bottom': 213.23}, 
                    'Security label 1': {'left': 465.63, 'top': 169.77, 'right': 549.37, 'bottom': 213.23},
                    'Security label 2': {'left': 465.63, 'top': 169.77, 'right': 549.37, 'bottom': 213.23},
                    }]
            },
            {
                'tagName': 'Seal 1',
                'type': 'Seal',
                'boundingBox': {
                    'left': 0,
                    'top': 0,
                    'right': 612,
                    'bottom': 816
                },
                'object_id': '12345'
            }
            

        ]
    },
    'image_metadata': {
        'id': '9cd6e1a3-d795-43d7-b388-10c00210a216',
        'name': '2024_01_15_07_16_31_132_782_JTX782_0__ccali_3.537968333333333_-76.40111333334_contratoprueba_1_623.jpg',
        'event': 0,
        'image_config': {
            'language': 'spanish',
            'objects_regex': {
                'Seal': '(?=.*\\d)[a-zA-Z0-9]{5,}',
                'Container': '(?=(?:.*\\d){3,})[a-zA-Z0-9]{5,}',
                'Security label': '(?=(?:.*\\d){3,})[a-zA-Z0-9]{5,}'
            }
        },
        'FK_contract_id': '90047570-be63-409c-83c7-f85ae79a95d8'
    }
}
