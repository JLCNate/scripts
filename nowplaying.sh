#!/usr/bin/env bash

ARTIST=$(playerctl metadata artist);
TITLE=$(playerctl metadata title);

# Append any text to your post or leave as it is
nowplaying="#NowPlaying: $TITLE - $ARTIST //";

echo $nowplaying | xclip -sel clip
