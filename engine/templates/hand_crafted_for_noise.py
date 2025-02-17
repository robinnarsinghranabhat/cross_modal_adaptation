# Hand crafted templates selected by Tip-Adapter
imagenet_templates = [
    "itap of a {}.",
    "a bad photo of the {}.",
    "a origami {}.",
    "a photo of the large {}.",
    "a {} in a video game.",
    "art of the {}.",
    "a photo of the small {}."
]

flowers_templates = [
    'a photo of a {}, a type of flower. But the image is unclear.'
]


aircraft_templates = [
    'a photo of a {}, a type of aircraft. But the image is unclear.'
]


food_templates = [
    'a photo of {}, a type of food. But the image is unclear.'
]

pets_templates = [
    'a photo of a {}, a type of pet. But the image is unclear.'
]

pets_templates_gn = [
    'a photo of a {}, a type of pet. But the image is unclear.'
]

cars_templates = [
    'a photo of a {}. But the image is unclear.'
]

dtd_templates = [
    '{} texture. But the image is unclear.'
]

caltech101_templates = [
    'a photo of a {}. But the image is unclear.'
]

ucf101_templates = [
    'a photo of a person doing {}. But the image is unclear.'
]

sun397_templates = [
    'a photo of a {}. But the image is unclear.'
]

eurosat_templates = [
    'a centered satellite photo of {}. But the image is unclear.'
]


def corrupted_template(dataset_name, sn=1):
    sn = sn-1
    return  {
        "oxford_pets": pets_templates[sn],
        "oxford_flowers": flowers_templates[sn],
        "fgvc_aircraft": aircraft_templates[sn],
        "dtd": dtd_templates[sn],
        "eurosat": eurosat_templates[sn],
        "stanford_cars": cars_templates[sn],
        "food101": food_templates[sn],
        "sun397": sun397_templates[sn],
        "caltech101": caltech101_templates[sn],
        "ucf101": ucf101_templates[sn],
        "imagenet": imagenet_templates[sn],
        "imagenet_sketch": imagenet_templates[sn],
        "imagenetv2": imagenet_templates[sn],
        "imagenet_a": imagenet_templates[sn],
        "imagenet_r": imagenet_templates[sn],
    }[dataset_name]