#!/bin/bash

# Directory
DIRECTORY="/mnt/media/anime/Yu Yu Hakusho"

cd "$DIRECTORY" || { echo "Directory not found"; exit 1; }

# Loop
for file in TokusatsuS.CoM.BR_Yu\ Yu\ Hakusho\ *1080p.mkv; do
    # Check
    if [[ -e "$file" ]]; then
        # Extract: regex
        if [[ $file =~ TokusatsuS\.CoM\.BR_Yu\ Yu\ Hakusho\ ([0-9]{1,3})\ 1080p\.mkv ]]; then
            episode_number="${BASH_REMATCH[1]}" # Get the episode number from the regex match
            # Construct
            new_filename="Yu Yu Hakusho $episode_number.mkv"

            # Rename
            mv "$file" "$new_filename"
            echo "Renamed '$file' to '$new_filename'"
        fi
    fi
done

