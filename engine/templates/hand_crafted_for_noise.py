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
    'a photo of a {}, a type of flower. But the image is unclear.',
    'a noisy image, possibly of a {}, a type of flower.',
    'a foggy image, possibly of a {}, a type of flower.',
    'a blurry image, possibly of a {}, a type of flower.',
]


aircraft_templates = [
    'a photo of a {}, a type of aircraft. But the image is unclear.'
]


food_templates = [
    'a photo of {}, a type of food. But the image is unclear.'
]

pets_templates = [
    'a photo of a {}, a type of pet. But the image is unclear.',
    'a noisy image, possibly of a {}, a type of pet.',
    'a foggy image, possibly of a {}, a type of pet.',
    'a blurry image, possibly of a {}, a type of pet.',
]


cars_templates = [
    'a photo of a {}. But the image is unclear.'
]

dtd_templates = [
    '{} texture. But the image is unclear.',
    # '{} texture. But the image is grainy.',
     'a noisy texture, possibly of a {}.',
     'a foggy texture, possibly of a {}.',
     'a blurry texture, possibly of a {}.',
]

caltech101_templates = [
    'a photo of a {}. But the image is unclear.'
    'a noisy image, possibly of a {}.',
    'a foggy image, possibly of a {}.',
    'a blurry image, possibly of a {}.',
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
        "oxford_pets": pets_templates,
        "oxford_flowers": flowers_templates,
        "fgvc_aircraft": aircraft_templates,
        "dtd": dtd_templates,
        "eurosat": eurosat_templates,
        "stanford_cars": cars_templates,
        "food101": food_templates,
        "sun397": sun397_templates,
        "caltech101": caltech101_templates,
        "ucf101": ucf101_templates,
        "imagenet": imagenet_templates,
        "imagenet_sketch": imagenet_templates,
        "imagenetv2": imagenet_templates,
        "imagenet_a": imagenet_templates,
        "imagenet_r": imagenet_templates,
    }[dataset_name][sn]