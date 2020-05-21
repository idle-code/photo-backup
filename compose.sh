#!/usr/bin/zsh
#set -x
set -e

START_IMAGE=$1
RESULT_IMAGE="composed.tiff"
PIXEL_CACHE="/home/idlecode/Projects/PhotoBackup/pixel_cache"

echo "Using $START_IMAGE as base"
cp "$START_IMAGE" "$RESULT_IMAGE"

shift
IMAGES=($*)

for IMAGE in $IMAGES;
do;
  echo "Merging $IMAGE"
  composite \
    -define registry:temporary-path=$PIXEL_CACHE \
    -compose darken \
    "$IMAGE" \
    "$RESULT_IMAGE" \
    "$RESULT_IMAGE"
done;

echo "Result in $RESULT_IMAGE"

