## Run CLEAN-EVAL of Cross-Modal with a different Text-Data
## Example : --experiment_name gaussian_noise_3"
## Ignore NOISE_TYPE


#!/bin/bash

TOTAL=1
declare -a ENCODERS=(
                   "RN50"
                #    "ViT-B/16"
                )
TOTAL=$(( TOTAL * ${#ENCODERS[@]} ))

declare -a IMAGE_LAYER_IDX=(
                   "0"
                #    "1"
                )
TOTAL=$(( TOTAL * ${#IMAGE_LAYER_IDX[@]} ))

declare -a TEXT_LAYER_IDX=(
                   "0"
                )
TOTAL=$(( TOTAL * ${#TEXT_LAYER_IDX[@]} ))

declare -a TEXT_AUGS=(
                    #   "classname"
                      "hand_crafted" 
                    #   "vanilla"
                    #   "template_mining"
                     )
TOTAL=$(( TOTAL * ${#TEXT_AUGS[@]} ))

declare -a IMAGE_AUGS=(
                      "none"
                    #   "flip" 
                    #   "randomcrop"
                     )
TOTAL=$(( TOTAL * ${#IMAGE_AUGS[@]} ))

declare -a IMAGE_VIEWS=(
                      "1"
                    #   "10"
                     )
TOTAL=$(( TOTAL * ${#IMAGE_VIEWS[@]} ))


declare -a DATASETS=(
                    #  "imagenet"
                    # "caltech101"
                    # "dtd"
                    #  "eurosat"
                    #  "fgvc_aircraft"
                    #  "food101"
                    # "oxford_flowers"
                     "oxford_pets"
                    #  "stanford_cars"
                    #  "sun397"
                    #  "ucf101"
                     )
TOTAL=$(( TOTAL * ${#DATASETS[@]} ))

declare -a ALL_SHOTS=(
    "1"
    "2"
    "4"
    "8"
    "16"
)
TOTAL=$(( TOTAL * ${#ALL_SHOTS[@]} ))

declare -a ALL_SEEDS=(
    "1"
    "2"
    "3"
    # "4"
    # "5"
)
TOTAL=$(( TOTAL * ${#ALL_SEEDS[@]} ))

declare -a MODALITIES=(
    # "uni_modal"
    "cross_modal"
)
TOTAL=$(( TOTAL * ${#MODALITIES[@]} ))

declare -a HEADS=(
    # "adapter"
    "linear"
)
TOTAL=$(( TOTAL * ${#HEADS[@]} ))

declare -a INITS=(
    "random"
    # "zeroshot"
)
TOTAL=$(( TOTAL * ${#INITS[@]} ))

declare -a LOGITS=(
    "4.60517"
    # "4.0"
)
TOTAL=$(( TOTAL * ${#LOGITS[@]} ))

declare -a HYPERS=(
    "linear"
    # "adapter"
    # "partial"
)
TOTAL=$(( TOTAL * ${#HYPERS[@]} ))

declare -a EXPERIMENT_NAMES=(
                    # "gaussian_noise_1"
                    # "gaussian_noise_2"
                    # "gaussian_noise_3"
                    # "gaussian_noise_4"
                    # "defocus_blur_1"
                    # "defocus_blur_2"
                    # "defocus_blur_3"
                    # "defocus_blur_4"
                    # "pixelate_1"
                    # "pixelate_2"
                    # "pixelate_3"
                    # "pixelate_4"

                    "defocus_blur_1_random"
                    "defocus_blur_2_random"
                    "defocus_blur_3_random"

                    "defocus_blur_1_others"
                    "defocus_blur_2_others"
                    "defocus_blur_3_others"


                    # "pixelate_1_random"
                    # "pixelate_2_random"
                    # "pixelate_3_random"

                    # "pixelate_1_others"
                    # "pixelate_2_others"
                    # "pixelate_3_others"

                     )
TOTAL=$(( TOTAL * ${#EXPERIMENT_NAMES[@]} ))


echo "ENCODERS: ${ENCODERS[@]}"
echo "IMAGE_LAYER_IDX: ${IMAGE_LAYER_IDX[@]}"
echo "TEXT_LAYER_IDX: ${TEXT_LAYER_IDX[@]}"
echo "TEXT_AUGS: ${TEXT_AUGS[@]}"
echo "IMAGE_AUGS: ${IMAGE_AUGS[@]}"
echo "IMAGE_VIEWS: ${IMAGE_VIEWS[@]}"
echo "DATASETS: ${DATASETS[@]}"
echo "ALL_SHOTS: ${ALL_SHOTS[@]}"
echo "ALL_SEEDS: ${ALL_SEEDS[@]}"
echo "MODALITIES: ${MODALITIES[@]}"
echo "HEADS: ${HEADS[@]}"
echo "INITS: ${INITS[@]}"
echo "LOGITS: ${LOGITS[@]}"
echo "HYPERS: ${HYPERS[@]}"
echo "TOTAL: $TOTAL"

COUNTER=1
echo " "
for DATASET in "${DATASETS[@]}"
do  
    echo "DATASET: $DATASET"
    for IMAGE_LAYER in "${IMAGE_LAYER_IDX[@]}"
    do 
        echo "IMAGE_LAYER: $IMAGE_LAYER"
        for ENCODER in "${ENCODERS[@]}"
        do
            echo "ENCODER: $ENCODER"
            for TEXT_LAYER in "${TEXT_LAYER_IDX[@]}"
            do
                echo "TEXT_LAYER: $TEXT_LAYER"
                for TEXT_AUG in "${TEXT_AUGS[@]}"
                do
                    echo "TEXT_AUG: $TEXT_AUG"
                    for IMAGE_AUG in "${IMAGE_AUGS[@]}"
                    do
                        echo "IMAGE_AUG: $IMAGE_AUG"
                        for IMAGE_VIEW in "${IMAGE_VIEWS[@]}"
                        do
                            echo "IMAGE_VIEW: $IMAGE_VIEW"
                            for SHOTS in "${ALL_SHOTS[@]}"
                            do 
                                echo "SHOTS: $SHOTS"
                                for SEED in "${ALL_SEEDS[@]}"
                                do
                                    echo "SEED: $SEED"
                                    for HEAD in "${HEADS[@]}"
                                    do
                                        echo "HEAD: $HEAD"
                                        for INIT in "${INITS[@]}"
                                        do
                                            echo "INIT: $INIT"
                                            for LOGIT in "${LOGITS[@]}"
                                            do
                                                echo "LOGIT: $LOGIT"
                                                for HYPER in "${HYPERS[@]}"
                                                do
                                                    echo "HYPER: $HYPER"
                                                    for MODALITY in "${MODALITIES[@]}"
                                                    do
                                                        echo "MODALITY: $MODALITY"
                                                        for EXP_NAME in "${EXPERIMENT_NAMES[@]}"
                                                        do 
                                                                echo "EXP_NAME: $EXP_NAME"
                                                                echo "COUNTER: $COUNTER/$TOTAL"
                                                                echo " "
                                                                COUNTER=$(( COUNTER + 1 ))
                                                                COMMAND="python train.py \
                                                                --dataset ${DATASET} \
                                                                --train-shot ${SHOTS} \
                                                                --clip-encoder ${ENCODER} \
                                                                --image-layer-idx ${IMAGE_LAYER} \
                                                                --text-layer-idx ${TEXT_LAYER} \
                                                                --image-augmentation ${IMAGE_AUG} \
                                                                --text-augmentation ${TEXT_AUG} \
                                                                --image-views ${IMAGE_VIEW} \
                                                                --seed ${SEED} \
                                                                --classifier_head ${HEAD} \
                                                                --classifier_init ${INIT} \
                                                                --logit ${LOGIT} \
                                                                --hyperparams ${HYPER} \
                                                                --modality ${MODALITY} \
                                                                --experiment_name ${EXP_NAME}"
                                                                echo $COMMAND
                                                                eval $COMMAND
                                                        done
                                                    done
                                                done
                                            done
                                        done
                                    done
                                done
                            done
                        done
                    done
                done
            done
        done
    done
done


nohup bash linear_probe_clean_eval.sh > oxford_flowers_lin_probe_ce.log