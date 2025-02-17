from engine.templates.template_pool import ALL_TEMPLATES
from engine.templates.template_mining import MINED_TEMPLATES
from engine.templates.hand_crafted import TIP_ADAPTER_TEMPLATES
from engine.templates.hand_crafted_for_noise import corrupted_template
from engine.config import corruptions

def get_templates(dataset_name, text_augmentation, custom_template=None):
    """Return a list of templates to use for the given config."""
    if custom_template:
        return [custom_template] if not isinstance(custom_template, list) else custom_template
    elif text_augmentation == 'classname':
        return ["{}"]
    elif text_augmentation == 'vanilla':
        return ["a photo of a {}."]
    elif text_augmentation == 'hand_crafted':
        return TIP_ADAPTER_TEMPLATES[dataset_name]
    elif text_augmentation == 'ensemble':
        return ALL_TEMPLATES
    elif text_augmentation == 'template_mining':
        return MINED_TEMPLATES[dataset_name]
    else:
        raise ValueError('Unknown template: {}'.format(text_augmentation))
    


def get_custom_template(dataset_name, experiment_name, noise_type):
    """
        Usage : 
            experiment_name="gaussian_noise_1", dataset_name="oxford_flowers"
            Gets `1st` `gaussian-noise-included` text-label for `oxford_flowers` ""
    """
    assert noise_type in corruptions
    prompt_number = experiment_name.replace(noise_type + "_", "")
    assert isinstance(int(prompt_number), int)

    noise_template = corrupted_template(dataset_name, int(prompt_number))
    return [noise_template]